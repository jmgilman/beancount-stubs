# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2022-02-01

### Added

- Added stub for `beancount.query.query`

### Changed

- `RealAccount.txn_postings` changed from `list[Posting]` to `list[TxnPosting]`
- Return type for fetching from a `RealAccount` was set
- Fixed signature for `query_execute.execute_query`

## [0.1.1] - 2022-01-28

### Changed

- Adds definitions for NamedTuple initializations
- Fixes incorrect fields on some types

## [0.1.0] - 2022-01-28

### Added

- Initial release

[unreleased]: https://github.com/jmgilman/beancount-stubs/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.2
[0.1.1]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.1
[0.1.0]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.0
