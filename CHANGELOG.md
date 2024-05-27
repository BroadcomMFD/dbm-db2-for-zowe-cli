# Change Log

This document lists changes made to the DBM-Db2 plug-in for Zowe CLI.

The format of this changelog is based on [Keep a Changelog] and adheres to [Semantic Versioning].



## [Unreleased]



## [1.28.3] - 2024-05-27

Architectural Runway.



## [1.28.2] - 2024-03-01

### Fixed

- `--target-db2`, `--source-db2` parameters required even if specified in the DBM-Db2 Options Profile.



## [1.28.1] - 2024-02-19

Architectural Runway.



## [1.28.0] - 2024-02-14

This release includes minor security improvements. Update is recommended.

### Added

- The secondary profile `dbm-db2-options` with the following parameters:
  - authid
  - changeSet
  - changeSetValues
  - deleteWorkDatasets
  - description
  - id
  - jobCards
  - matchSet
  - matchSetValues
  - modification
  - overwriteOutputFiles
  - ruleSet
  - sqlid
  - sourceDb2
  - targetDb2
  - terminationCharacter
  - type
  - verify
  - workDatasetPrefix
  
- The `dbm-db2-options-profile` CLI parameter for all commands.

### Changed

- CLI options are grouped in the following order:
  - positionals
  - required
  - options
  - profile options
  - dbm-db2 connection options
  - base connection options
  - global options
  - examples

- The `options` section in the error file now supports new parameters:
  - changeSet
  - changeSetValues
  - description
  - id
  - matchSet
  - matchSetValues
  - modification
  - ruleSet
  - type
  - verify

- The title of the `dbm-db2-profile` changes to "DBM-Db2 Connection Profile".



## [1.27.1] - 2023-10-12

This release includes minor security improvements. Update is recommended.

### Fixed

- Error file containing non-printable YAML characters.
- `--target-db2` and `--source-db2` parameters not supporting data sharing group names.
- `--match-set-file` format description having outdated length specification limits.



## [1.27.0] - 2023-09-12

This release includes minor security improvements. Update is recommended.

### Added

- The following parameters added for each command:
  - environment-list
  - job-cards
  - overwrite-output-files
  - protocol
  - work-dataset-prefix


- The `termination-character` parameter added for the following commands:
  - compare ddl
  - deploy ddl
  - generate ddl
  - prepare migration


- `authid` and `sqlid` parameters added for the following commands:
  - check ddl
  - compare ddl
  - deploy ddl
  - generate ddl
  - prepare migration

### Changed

- DBM-Db2 profile is no longer required for execution.


- Removed `environmentList` property with local value from the error file.\
  It still contains the `environment` property which reflects the actual value that is used during execution.


- Renamed property `dbmProfileParameters` -> `options`.


- Output file paths hardening to ensure writing in the end of execution:
  - Switched to using forward slash only during reporting.
  - Added validation that slash is not used on Unix-like systems.
  - Added validation of read/write access before execution.

### Fixed

- Password value displayed in `arguments` section of an error file upon provided as CLI parameter.



## [1.26.0] - 2023-05-24

### Added

- Data for the `--response-format-json | --rfj` output.
  - The `data` property contains additional information, so that you do not need to parse the message to retrieve it.
  </br></br>
  - The `data.files` property may contain the following properties based on the output files available for a command executed:
    - ddlFile
    - summaryFile
    - impactFile
    - compareScript
    - recoveryScript
    - migrateScript
    - errorFile
  </br></br>
  - The `data.attributes` property may contain the following properties:
    - restartToken - Available for `execute` commands that failed.
    - hasObjectChanges - Available for the `compare ddl` command. `false` when there are 0 creates, alters, and drops - otherwise `true`.
  </br></br>
  - The data structure is persistent across commands. If there is no data, the field remains empty:
    ```
    ...
    "data": {
      "files": {},
      "attributes": {}
    },
    ```

### Fixed

- `--rfj` parameter not supported when provided without a value



## [1.25.0] - 2023-02-10

### Added

- Support for the impact report in the `compare ddl` command.
- The `--output-recovery-script` alias for the `execute compare-script` command.
  - Complements the existing `--output-recovery-file` parameter.
  - References in terminal and command help now also use the term "script".



## [1.24.2] - 2022-12-12

### Changed

- Improved API error message reporting.
  - Removed redundant endpoint references.
  - Distinction between the client-side and server-side issues.
  - Added error reason information.


- Error file now reports all steps.
  - Steps that are skipped due to the failure of a preceding step contain a warning message:\
        `[WARNING] No content received.`


- Dependency versions updated and locked per NPM best practices:
  - (Peer dependency) @zowe/imperative `^5.3.8` -> `^5.7.0`
  - (Dependency) @zowe/core-for-zowe-sdk `~7.4.2` -> `7.8.0`



## [1.24.0] - 2022-11-18

### Added

- Command arguments to the error file.

### Changed

- Updated the warning message on status-token mismatch as follows:\
`[Warning] Unable to process the DBM Data Service REST API status-token. Update dbm-db2 plugin to the matching major version of DBM Data Service.`



## [1.23.13] - 2022-11-14

### Added

- New information to the error file:
  - Execution information
  - Connection details
  - Profile parameters

### Changed

- Terminal output format.
  - Aligned between commands.
  - Redundant data removed.

### Fixed

- Authentication types other than "Basic" are not supported.



## [1.23.7] - 2022-09-13

### Changed

- Error file converted to YAML format.



## [1.23.4] - 2022-09-02

### Added

- Zowe CLI base profile support.
- Zowe CLI team configuration support.

### Changed

- Achieved Zowe CLI V2 conformance.

### Fixed

- Base connection options provided with command are ignored.



## [1.21.5] - 2022-05-27

### Added

- `zowe dbm` commands:
  - check ddl
  - compare ddl
  - deploy ddl
  - execute compare-script
  - execute migration-script
  - execute script
  - generate ddl
  - prepare migration



[1.28.3]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.28.3
[1.28.2]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.28.2
[1.28.1]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.28.1
[1.28.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.28.0
[1.27.1]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.27.1
[1.27.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.27.0
[1.26.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.26.0
[1.25.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.25.0
[1.24.2]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.24.2
[1.24.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.24.0
[1.23.13]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.13
[1.23.7]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.7
[1.23.4]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.4
[1.21.5]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.21.5
[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
