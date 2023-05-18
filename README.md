# DBM-Db2: Sample Scripts
This repository contains sample scripts for use cases that involve DBM-Db2 plug-in for Zowe CLI.

## Response Format JSON
Use the `--rfj` parameter to enable JSON output during command execution.

The following example shows the typical output of the command execution with JSON output enabled:
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

The `data` property contains additional information, so that you do not need to parse the message to retrieve it.

The `data.files` property may contain the following properties based on the output files available for a command 
executed:
- ddlFile
- summaryFile
- impactFile
- compareScript
- recoveryScript
- migrateScript
- errorFile

The `data.attributes` property may contain the following properties:
- restartToken - Available for `execute` commands that failed.
- hasObjectChanges - Available for the `compare ddl` command. `false` when there are 0 creates, alters, and drops - 
otherwise `true`.

The `data` structure is persistent across commands. If there is no data, the field remains empty:
```
...
"files": {},
"attributes": {}
```


### Processing in Python

Requirements: Python >=3.11.0

1. JSON output always includes `data`, `files`, and `attributes` levels, so no verification is required.

2. Parse JSON response and get files dictionary:
    ```python
    res = json.loads(response)
    files = res.get("data").get("files")
    ```

3. Get the file you need based on the command executed and outcome (success/failure):
    ```python
    files.get('errorFile') # -> string relative path | None
    ```

For more information about processing JSON response in python, see [Python samples].



[Python samples]: samples/python/
