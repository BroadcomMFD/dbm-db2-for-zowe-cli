# Change Log

This document lists changes made to the DBM-Db2 plug-in for Zowe CLI.

The format of this changelog is based on [Keep a Changelog] and adheres to [Semantic Versioning].



## [Unreleased]



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



[1.25.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.25.0
[1.24.2]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.24.2
[1.24.0]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.24.0
[1.23.13]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.13
[1.23.7]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.7
[1.23.4]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.23.4
[1.21.5]: https://www.npmjs.com/package/@broadcom/dbm-db2-for-zowe-cli/v/1.21.5
[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
