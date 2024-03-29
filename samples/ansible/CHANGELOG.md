# Change Log

This document lists changes made to the Ansible sample for DBM-Db2 plug-in for Zowe CLI.

The format of this changelog is based on [Keep a Changelog] and adheres to [Semantic Versioning].



## [Unreleased]



## 1.0.2 - 2024-02-23

### Changed

- Readme changed to contain dependency installation commands instead of keeping PIP requirements files.



## 1.0.1 - 2024-01-08

This release includes minor security improvements. Update is recommended.

### Security

- Updated dependencies to resolve vulnerability CVE-2023-49083



## 1.0.0 - 2023-11-10

### Added

- DBM-Db2 Ansible collection usage sample.\
  \
  Scenario: Compares schema changes to a target Db2 subsystem. Promotes changes if they comply with site requirements
(rules).\
  \
  The sample comprises of the following assets:
  - Ansible playbook
  - Ansible configuration
  - Reusable tasks
  - Inventory
  - Work files



[Keep a Changelog]: https://keepachangelog.com/en/1.1.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
