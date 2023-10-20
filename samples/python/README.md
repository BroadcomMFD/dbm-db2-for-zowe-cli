# DBM-Db2: Python Sample
This folder contains the sample script that explains how to use the DBM for Db2 Plug-in for Zowe CLI with Python. The
sample comprises of the following assets:
- Schema promotion script
- Python classes
- Work files


## Scenario
Compares schema changes to a target Db2 subsystem. Promotes changes if they comply with site requirements (rules).


## Prerequisites
- RC/Migrator and RC/Compare Version 20.0 (configured, current on maintenance, and running)


- DBM Data Service (configured and running)\
    This task assumes that you have completed the post-installation configuration tasks for the Batch Processor, the DBM
    Data Service, the Xmanager, Xnet, and RC/Migrator. DBM Data Service customization includes customizing the DevOps
    templates.


- Python (>=3.11.0)
- Zowe CLI V2
- DBM-Db2 Plug-in for Zowe CLI (>=1.26.0)
- Zowe DBM-Db2 profile in the Zowe Team configuration\
    For more information, see [Team configurations] on Zowe Docs.


## Usage
1. Install [required Python packages](requirements.txt).
2. Configure environment variables:
    - `subsystem`: Specify the target Db2 subsystem.
    - `schema`: Specify the schema name for new tables in your environment.\
      This value is used to verify that new tables conform to your site standards.
    
    Alternatively, replace the default values in the sample script (schema_promotion.py) as follows:\
    `ssid = os.getenv('subsystem', 'v13a')` => `ssid = os.getenv('subsystem', 'YOUR_DB2_SUBSYSTEM')`


3. Issue command: `cd samples/python`
4. Issue command: `python schema_promotion.py`


## Workflow

> **_NOTE:_**\
\
To protect you from undesired changes and creating an object on your first execution, one of the tables in the input DDL
file ([files/ddl.sql](files/ddl.sql)) contains a “DEV2” schema that is bound to fail validation. When you understand how
rules can protect you, replace “DEV2” with “DEV” and proceed with updating your Db2 subsystem.

The sample script consists of the `__main__` function that is the skeleton of the workflow, and task-based functions
that are invoked during the execution.

Define required environment variables, or hard-code the values in the main function. All input and output files use the
`files` folder in the same sample directory.

The wrapper class `Zowe` allows you to specify commands much the same as in the terminal:\
`zowe dbm compare ddl ...` => `Zowe.dbm('compare ddl ...')`\
`zowe files list ds ...` => `Zowe.files('list ds ...')`

This class returns output in JSON format, and currently supports the `DBM` and `files` plug-ins.  

The sample script compares the DDL to a target Db2 subsystem and verifies the JSON response to ensure that DDL changes
were identified. If the DDL compare was successful, you can promote the schema. If the DDL compare fails, the script
prints JCL job details from the error file.

An impact report is checked for DROP statements and any new tables that violate the schema definition. These checks use
simple JMESPath queries to filter and compare JSON document fields, and serve as site-specific **rules** that must be
adhered to prior to promoting DDL changes.

When all checks are passed, an update script is executed and schema changes are implemented on a target Db2 subsystem. A
recovery file is created. We highly recommend that you save this file before the next execution, or use a dynamic file
name.


## Learn More
For more information about the JSON response format, see [wiki].


[Team configurations]: https://docs.zowe.org/stable/user-guide/cli-using-using-team-profiles
[wiki]: https://github.com/BroadcomMFD/dbm-db2-for-zowe-cli/wiki
