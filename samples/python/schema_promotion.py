"""
Copyright (c) 2023 Broadcom. All rights reserved. The term
"Broadcom" refers to Broadcom Inc. and/or its subsidiaries.

This software and all information contained therein is confidential and proprietary and
shall not be duplicated, used, disclosed or disseminated in any way without the express
written permission of Broadcom. All authorized reproductions must be marked with this
language.

TO THE EXTENT PERMITTED BY APPLICABLE LAW, BROADCOM PROVIDES THIS
SOFTWARE "AS IS" WITHOUT WARRANTY OF ANY KIND, INCLUDING WITHOUT
LIMITATION, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE OR NONINFRINGEMENT. IN NO EVENT WILL BROADCOM BE
LIABLE TO THE END USER OR ANY THIRD PARTY FOR ANY LOSS OR DAMAGE, DIRECT OR
INDIRECT, FROM THE USE OF THIS MATERIAL, INCLUDING WITHOUT LIMITATION, LOST
PROFITS, BUSINESS INTERRUPTION, GOODWILL, OR LOST DATA, EVEN IF BROADCOM IS
EXPRESSLY ADVISED OF SUCH LOSS OR DAMAGE.
"""

import json
import os
from typing import Tuple, Any, Literal

import jmespath
import yaml

from classes.zowe import Zowe


"""
Sample schema promotion scenario script.
Uses Zowe wrapper class for getting response data dictionary.


Prerequisites:
- Zowe CLI V2 is installed.
    https://docs.zowe.org/stable/user-guide/cli-installcli/#install-zowe-cli-from-npm

- DBM-Db2 Plug-in for Zowe CLI (>=1.26.0) is installed.
    https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli

- Zowe DBM-Db2 profile configured in Zowe Team configuration.
    https://docs.zowe.org/stable/user-guide/cli-using-using-team-profiles


Steps:
- Calls `compare ddl`.
- Checks:
    - Script has object changes.
    - Script has no drop statements.
    - Newly created tables have specific schema name.
- Calls `execute compare-script` if all checks passed.


Usage:
1. Configure the `subsystem` environment variable, or replace the default subsystem value in the `__main__` function.
2. Configure the `schema` environment variable, or replace the default schema value in the `__main__` function.
3. Run schema_promotion.py

Note: To provide an overview of how validation works, the input DDL file (files/ddl.sql) intentionally contains the
"DEV2" schema that is bound to fail the checks based on rules.

4. Update the schema by replacing the "DEV2" value with "DEV" in the input DDL file.
5. Re-run schema_promotion.py

[Warning] Step #5 creates two tables defined in the input DDL file.
"""


nl = '\n'  # newline character


def get_files_dir() -> str:
    """
    Returns normalized relative path for the `files` folder.
    """

    script_dir = os.path.dirname(os.path.realpath(__file__))
    cwd = os.getcwd()

    def __get_dir(name: str) -> str:
        return os.path.normpath(os.path.relpath(os.path.join(script_dir, name), cwd))

    return __get_dir('files')


def compare_ddl(ddl_path: str) -> dict:
    """
    Runs `compare ddl` command with some predefined parameters.

    :param ddl_path: DDL file name path.
    :return: Response dictionary.
    """

    return Zowe.dbm(f'''compare ddl {ddl_path} --td {ssid} \
    --error-file {folder}/error.log                        \
    --output-compare-script {folder}/compare.txt           \
    --output-summary-file {folder}/summary.txt             \
    --output-impact-file {folder}/impact.json              \
    ''')


def check_results(response: dict) -> Tuple[Any, Any]:
    """
    Verifies command execution was successful.

    :param response: Response dictionary that is returned by the command execution.
    :return: File and attribute dictionaries.
    """

    files = response.get('data').get('files')
    attr = response.get('data').get('attributes')

    if not response.get('success'):
        job_info = ''
        if files:
            content = read_output_file(files, 'errorFile', 'yaml')
            job_info = f'{content.get("jobName")}({content.get("jobId")}) - {content.get("jobRetCode")}\n'

        raise Exception(f'{job_info}\n{response.get("stderr")}')

    return files, attr


def read_output_file(output_files: dict, file_id: str, data_format: Literal['json', 'yaml']) -> dict:
    """
    Reads output file in JSON/YAML format and returns content as a dictionary.

    :param output_files: File dictionary (`data.files`) from the response.
    :param file_id: File identifier.
    :param data_format: `json` or `yaml` format to use for content parsing.
    """

    path = output_files.get(file_id)
    if not path:
        raise Exception(f'Output file "{file_id}" not found in the response.')

    with open(path, 'r') as file:
        if data_format == 'json':
            content = json.load(file)
        else:
            content = yaml.safe_load(file)

    return content


def check_object_changes(data_attributes: dict) -> None:
    """
    Ends execution if no object changes were identified during comparison.

    :param data_attributes: Attributes dictionary (`data.attributes`) from the response.
    """

    if not data_attributes.get('hasObjectChanges'):
        raise Exception('No object changes identified.')


def check_rules(output_files: dict, schema: str) -> None:
    """
    Evaluates the impact report:\n
    - Verifies there are no DROPs.
    - Verifies all new tables have specific schema.

    :param output_files: File dictionary (`data.files`) from the response.
    :param schema: Required schema for the new tables.
    """

    content = read_output_file(output_files, 'impactFile', 'json')

    # check no DROPs
    assert jmespath.search('strategyOperationsStatisticsSummary.totals.drops', content) == 0, 'Drops detected.'

    # check tables schema
    tables = jmespath.search(
        f"strategyObjectListsDetail.tables[?join('', operations) == 'create'] | [?creator != '{schema}']",
        content
    )
    assert len(tables) == 0, f"New tables have forbidden schema definitions:\n{nl.join(str(t) for t in tables)}"


def execute_compare_script(output_files: dict) -> dict:
    """
    Runs `execute compare-script` command with some predefined parameters.

    :param output_files: File dictionary (`data.files`) from the response.
    :return: Response dictionary.
    """

    return Zowe.dbm(f'''execute compare-script {output_files.get('compareScript')} \
    --error-file {folder}/error.log                                                \
    --output-recovery-script {folder}/recovery.txt                                 \
    ''')


if __name__ == '__main__':
    # Global variables
    ssid = os.getenv('subsystem', 'v13a')       # provide an environment variable or hard-code the subsystem
    schema = os.getenv('schema', 'DEV')         # provide an environment variable or hard-code the expected table schema
    folder = get_files_dir()

    # Compare DDL
    res = compare_ddl(f'{folder}/ddl.sql')      # tip: replace "DEV2" schema with "DEV" in the DDL file to update the Db2 subsystem
    files, attr = check_results(res)
    print('Compare DDL completed successfully.')

    # Checks
    check_object_changes(attr)
    check_rules(files, schema)
    print('All checks passed.')

    # Execute compare-script
    res = execute_compare_script(files)
    files, attr = check_results(res)
    print('Execute compare-script completed successfully.')
