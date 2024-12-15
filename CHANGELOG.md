# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.5 - 2024-12-15

### Fixed

- Add missing hint of `Iterable[TxnPosting]` for `txn_postings` to `compute_postings_balance`

## 0.1.4 - 2024-07-28

### Added

- Added stubs for `beancount.ingest.{cache,importer,regression_pytest}`

### Changed

- Replaced poetry with rye for the build system
- Switched to namespace packages to play better with pyright
- `Posting.units` is `Optional` now
- Better `_replace` signatures for all core datatypes
- Relaxed selected types for `realization.pyi`
- Allow `FrozenSet` to be passed as `tags` or `meta`

## [0.1.3] - 2022-02-01

### Changed

- Fixed incorrect return type on `query.run_query`
- Fixed incorrect type on `RealAccount.txn_postings`

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

[0.1.5]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.5
[0.1.4]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.4
[0.1.3]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.3
[0.1.2]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.2
[0.1.1]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.1
[0.1.0]: https://github.com/jmgilman/beancount-stubs/releases/tag/v0.1.0
