"""
Copyright (c) 2023 Broadcom. All rights reserved. The term
“Broadcom” refers to Broadcom Inc. and/or its subsidiaries.

This software and all information contained therein is confidential and proprietary and
shall not be duplicated, used, disclosed or disseminated in any way without the express
written permission of Broadcom. All authorized reproductions must be marked with this
    language.

TO THE EXTENT PERMITTED BY APPLICABLE LAW, BROADCOM PROVIDES THIS
SOFTWARE “AS IS” WITHOUT WARRANTY OF ANY KIND, INCLUDING WITHOUT
LIMITATION, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE OR NONINFRINGEMENT. IN NO EVENT WILL BROADCOM BE
LIABLE TO THE END USER OR ANY THIRD PARTY FOR ANY LOSS OR DAMAGE, DIRECT OR
INDIRECT, FROM THE USE OF THIS MATERIAL, INCLUDING WITHOUT LIMITATION, LOST
PROFITS, BUSINESS INTERRUPTION, GOODWILL, OR LOST DATA, EVEN IF BROADCOM IS
EXPRESSLY ADVISED OF SUCH LOSS OR DAMAGE.
"""


import json
import subprocess


class Zowe:
    """
    Wrapper class to execute provided Zowe CLI commands and return JSON response as a dictionary\n
    - automatically adds `zowe {command}` prefix
    - automatically adds `--rfj` option
    """

    @staticmethod
    def dbm(command: str) -> dict:
        return Zowe.__process_command(command, 'dbm')

    @staticmethod
    def files(command: str) -> dict:
        return Zowe.__process_command(command, 'files')

    @staticmethod
    def __process_command(command: str, plugin: str) -> dict:
        cmd = f'zowe {plugin} {command} --rfj'
        return json.loads(Zowe.__execute_command(cmd))

    @staticmethod
    def __execute_command(command: str, raise_exc=False):
        failed = False

        try:
            res = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            failed = True
            res = e.output

        if raise_exc and failed:
            raise Exception(res)
        return res
