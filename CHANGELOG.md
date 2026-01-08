# Changelog

All notable changes to ChromaTerm2 will be documented in this file.

## [2.0.1] - 2026-01-07

### Fixed
- Fixed buffer overflow error in `window_resize_handler` on some systems ([#2](https://github.com/rgcr/ChromaTerm2/issues/2))
  - Changed `fcntl.ioctl` buffer from string literal `'0000'` to proper `struct.pack('HHHH', 0, 0, 0, 0)`

---

## [2.0.0]

### Added
- New maintainer: rgcr
- Modern Python packaging with `pyproject.toml`
- Proper credit to original author (hSaria) in README and code

### Changed
- **BREAKING**: Package name changed from `chromaterm` to `chromaterm2`
- **BREAKING**: New package version scheme starting at 2.0.0
- Refactored codebase for better maintainability and scalability:
  - Split `__init__.py` into separate modules
  - Moved core classes to `chromaterm/core.py`
  - Moved CLI logic to `chromaterm/cli.py`
  - Simplified `__init__.py` to imports only
  - Removed `__main__.py` file
- Updated all internal imports to use relative imports
- Updated dependencies to use modern versions (PyYAML>=5.1, psutil)
- Updated Python version support (>=3.9, tested up to 3.13)
- Improved project metadata and package information

### Fixed
- Fixed PCRE2 named group handling (`test_rule_set_color_named_group`)
- Fixed PCRE2 `GroupIndex.get()` method implementation
- Fixed test compatibility with both Python RE and PCRE2 engines
- Updated entry point to use new module structure

### Technical Details
- All tests now pass (170/170)
- Maintained backward compatibility for end users (`ct` command unchanged)
- Updated from setup.py-only to modern pyproject.toml configuration

### Migration Notes
- **For new installations**: Use `pip install chromaterm2` instead of `pip install chromaterm`
- **For existing users**: The `ct` command works exactly the same
- **Functionality**: All original features preserved, with improvements and bug fixes

---

## About ChromaTerm2

ChromaTerm2 is a maintained and refactored fork of the original ChromaTerm project by hSaria.
The original project is archived at: https://github.com/hSaria/ChromaTerm

### Why ChromaTerm2?
- **Active maintenance**: I'll try to keep it up-to-date and fix bugs as well
- **Modern codebase**: Refactored for better maintainability
- **Python 3.6+ support**: Compatible with modern Python versions
- **Community driven**: Open to contributions and feedback

Repository: https://github.com/rgcr/ChromaTerm2
