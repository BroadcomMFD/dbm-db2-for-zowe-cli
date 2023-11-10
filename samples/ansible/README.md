# DBM-Db2: Ansible Collection Usage Sample
This folder contains the sample playbook that explains how to use the DBM-Db2 Ansible collection. The sample comprises
of the following assets:
- Ansible playbook
- Ansible configuration
- Reusable tasks
- Inventory
- Work files


## Scenario
Compares schema changes to a target Db2 subsystem. Promotes changes if they comply with site requirements (rules).


## Prerequisites
- RC/Migrator and RC/Compare Version 20.0 (configured, current on maintenance, and running)


- DBM Data Service (configured and running)\
  This task assumes that you have completed the post-installation configuration tasks for the Batch Processor, the DBM
  Data Service, the Xmanager, Xnet, and RC/Migrator. DBM Data Service customization includes customizing the DevOps
  templates.


- Python >=3.11.0


## Usage
1. Install [required Python packages](requirements.txt).
2. Install [required Ansible collections](requirements.yml).

3. Configure the sample inventory and playbook:
    - Configure group variable `dev_table_schema` ([inventory/group_vars/dev.yml]).\
      This value is used to verify that new tables conform to your site standards.
   
    - Specify connection details in host variables ([inventory/host_vars/instance001.yml]).
    - Replace the `db2_subsystem` value with the target Db2 subsystem of your choice in the playbook
([schema_promotion.yml](schema_promotion.yml)).

 4. Issue command: `cd samples/ansible`
 5. Issue command: `ansible-playbook schema_promotion.yml -i inventory/dev.yml`


## Inventory Configuration
The inventory folder contains the group file [dev.yml](inventory/dev.yml). This file contains hosts that are used for
application development and their corresponding DBM DS instance names.

You can define variables for each host in the group variables file ([inventory/group_vars/dev.yml]). This sample uses a
table schema name (`dev_table_schema`) to validate new tables.

You can define variables for a specific host in the host variables file ([inventory/host_vars/instance001.yml]).
Modify this file with connection details and DBM-Db2 Ansible collection parameter values. These values apply to all
tasks that use modules from this collection.


## Workflow

> **_NOTE:_**\
\
To protect you from undesired changes and creating an object on your first execution, one of the tables in the input DDL
file ([files/ddl.sql](files/ddl.sql)) contains a “DEV2” schema that is bound to fail validation. When you understand how
rules can protect you, replace “DEV2” with “DEV” and proceed with updating your Db2 subsystem.

To define the playbook, specify the collection namespaces (`collections`) to search for modules, and default parameter
values (`module_defaults`) for these modules. Specify a Db2 subsystem (`target_db2`) for the sample playbook. All input
and output files use the `files` folder in the same sample directory.

DBM-Db2 collection-based tasks are organized in blocks to invoke reusable tasks that process errors. These tasks can
open an error file, print JCL job details, and end playbook execution.

The sample playbook compares the DDL to a target Db2 subsystem and verifies the JSON response to ensure that DDL changes
were identified. If the DDL compare was successful, you can promote the schema. If the DDL compare fails, the playbook
prints JCL job details from the error file.

An impact report is checked for DROP statements and any new tables that violate the schema definition in the group
variables file. These checks use simple JMESPath queries to filter and compare JSON document fields, and serve as
site-specific **rules** that must be adhered to prior to promoting DDL changes.

When all checks are passed, an update script is executed and schema changes are applied to a target Db2 subsystem. A
recovery file is created. We highly recommend that you save this file before the next execution, or use a dynamic file
name.


## Learn More
For more information about the DBM-Db2 Ansible collection module parameters, see the [DBM-Db2 collection syntax].

For more information about the JSON Response Format, see [wiki].


[DBM-Db2 collection syntax]: https://broadcommfd.github.io/broadcom-ansible-collections/generated/broadcom/dbm_db2/index.html
[wiki]: https://github.com/BroadcomMFD/dbm-db2-for-zowe-cli/wiki
[inventory/group_vars/dev.yml]: inventory/group_vars/dev.yml
[inventory/host_vars/instance001.yml]: inventory/host_vars/instance001.yml
