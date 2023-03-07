# DBM-Db2: sample scripts
This repository contains sample scripts for use cases involving DBM-Db2 plug-in for Zowe CLI.

## Response format JSON
Use the `--rfj` parameter to enable JSON output during command execution.

Typical output looks like:
```json
{
  "success": false,
  "exitCode": 1,
  "message": "Execution failed. Failure details saved to error.log\nRestart token: 840413D5D132CB8A7149C85940B7FBA4",
  "stdout": "",
  "stderr": "\u001b[31mCommand Error:\u001b[39m\n\u001b[31m\u001b[39mExecution failed. Failure details saved to error.log\nRestart token: 840413D5D132CB8A7149C85940B7FBA4\n",
  "data": {
    "files": {
      "errorFile": "error.log"
    },
    "attributes": {
      "restartToken": "840413D5D132CB8A7149C85940B7FBA4"
    }
  },
  "error": {
    "msg": "Execution failed. Failure details saved to error.log\nRestart token: 840413D5D132CB8A7149C85940B7FBA4"
  }
}
```

The `data` property is populated with additional information so that you don't need to parse the `message` to retrieve
it.

The `data.files` property can contain the following properties based on the output files available for a command 
executed:
- ddlFile
- summaryFile
- impactFile
- compareScript
- recoveryScript
- migrateScript
- errorFile

The `data.attributes` property can contain the following properties:
- restartToken - Available for `execute` commands that failed.
- hasObjectChanges - Available for `compare ddl` command. `true` when there are 0 creates, alters and drops - otherwise 
`false`.

The `data` structure is persistent across commands, and if there is no data for a field - it will be left empty:
```
...
"files": {},
"attributes": {}
```


### Processing in Python
1. Consider `data`, `files` and `attributes` levels are always there (persistent structure), so there is no need to
verify them not missing.

2. Parse JSON response and get files dictionary:
    ```python
    res = json.loads(response)
    files = res.get("data").get("files")
    ```

3. Get the file you need based on the command executed and outcome (success/failure):
    ```python
    files.get('errorFile') # -> string relative path | None
    ```

For more details about processing JSON response in python, see [Python samples].



[Python samples]: samples/python/schema_promotion.py
