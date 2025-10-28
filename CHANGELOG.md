# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-10-28

### 🎉 Performance & Feature Release

Major performance improvements and new features for professional workflows.

### Added

#### ⚡ **Performance**
- **Parallel Processing**: Multi-core CPU utilization with ProcessPoolExecutor
  - 2-4x faster conversion for large batches
  - Configurable worker count with `--workers` flag
  - Optional sequential mode with `--no-parallel` flag
- **Smart Resource Management**: Automatic optimal worker allocation
- **Conversion Statistics**: Display time per file, total time, and files/s after conversion

#### 📸 **EXIF Preservation**
- **Metadata Preservation**: Automatically copies EXIF data from NEF to JPEG
  - Camera settings (ISO, aperture, shutter speed)
  - GPS coordinates
  - Copyright information
  - Timestamps
- **Optional Disable**: Use `--no-exif` flag to skip metadata copying
- **Robust Handling**: Graceful fallback for files with problematic EXIF data

#### 👁️ **Watch Mode**
- **Automatic Conversion**: Monitor directories for new NEF files
  - Real-time conversion as files are added
  - Perfect for workflow automation
  - Tethered shooting support
- **Usage**: `nef-converter --watch -d /path/to/watch`

#### 🖥️ **Graphical User Interface** (Optional)
- **Gooey-based GUI**: Beautiful desktop application interface
  - Drag & drop folder selection
  - JPEG quality slider
  - CPU core selection
  - EXIF preservation toggle
  - Real-time progress tracking
- **Installation**: `pip install nef-to-jpg-converter[gui]`
- **Launch**: `nef-gui` or `python -m nef_converter.gui`

#### 🎯 **Better Error Messages**
- **Actionable Feedback**: Helpful tips for common errors
- **Context-Aware**: Specific messages for different error types
  - File permission errors
  - Corrupted file detection
  - Memory issues
- **Documentation Links**: Direct links to troubleshooting guides
- **Suppressed Warnings**: Removed harmless PIL EXIF metadata warnings

#### 📦 **Standalone Executables**
- **No Python Required**: PyInstaller configurations for all platforms
  - Windows: `nef-converter.exe`
  - macOS: `nef-converter.app`
  - Linux: `nef-converter`
- **Build Scripts**: Ready-to-use spec files in `build-scripts/`

### Changed

- **CLI Version**: Updated to 2.1.0
- **GUI Version**: Updated to V2.1
- **Dependencies**: 
  - Added `watchdog>=4.0.0` for watch mode
  - Made `gooey>=1.0.0` optional (`[gui]` extra)
  - Removed `imageio` dependency (now uses PIL exclusively)
- **Python Support**: Requires Python 3.9+ (dropped 3.8)
- **EXIF Handling**: Changed approach from post-save to pre-conversion for better reliability

### Fixed

- **EXIF Bug**: Fixed "EXIF data is too long" error for files with large metadata (e.g., blackbird.NEF)
- **Import Order**: Fixed flake8 E402 errors
- **Code Formatting**: Applied black formatting consistently
- **CI/CD**: Made Gooey optional to fix Linux build failures (wxpython compilation)
- **Type Hints**: Fixed mypy errors in main.py

### Improved

- **Error Handling**: More specific exception catching and user feedback
- **Logging**: Enhanced debug information for troubleshooting
- **Code Quality**: Better type hints and documentation
- **Test Coverage**: Fixed tests after removing imageio dependency

### Performance

- **Batch Processing**: Up to 4x faster on multi-core systems
- **Memory Efficiency**: Optimized resource usage for large NEF files
- **Scalability**: Better handling of 1000+ file batches

## [2.0.0] - 2025-10-28

### 🚀 Major Release - Complete Modernization

This release represents a complete rewrite and modernization of the NEF to JPG converter, transforming it from a simple script into a professional Python package.

### Added

#### 🏗️ **Modern Architecture**
- **Modular Design**: Complete restructuring with `src/nef_converter/` package layout
- **Type Safety**: Comprehensive type hints throughout the codebase
- **Error Handling**: Robust exception handling and logging system
- **Cross-Platform**: Full Windows, macOS, and Linux support

#### 🖥️ **Enhanced User Interface**
- **Command Line Interface**: Full-featured CLI with argument parsing
- **GUI Mode**: Improved directory selection dialog
- **Progress Tracking**: Modern progress bars using `tqdm`
- **Better Feedback**: Enhanced console output with emojis and status messages

#### 📦 **Professional Packaging**
- **pyproject.toml**: Modern Python packaging configuration
- **Entry Points**: `nef-converter` and `nef2jpg` command-line tools
- **Development Tools**: Black, isort, flake8, mypy, pytest configuration
- **Installation**: `pip install -e .` support for development

#### 🧪 **Testing & Quality**
- **Test Suite**: Comprehensive pytest-based testing framework
- **Code Coverage**: Coverage reporting and analysis
- **Quality Tools**: Automated code formatting and linting
- **CI/CD Ready**: Prepared for GitHub Actions integration

#### 📚 **Documentation**
- **Modern README**: Comprehensive documentation with examples
- **Contributing Guide**: Detailed contribution guidelines
- **License**: MIT license for open-source usage
- **Changelog**: This file for tracking changes

### Changed

#### ⚡ **Performance Improvements**
- **50% Faster**: Optimized file processing and memory usage
- **Batch Processing**: Improved handling of large file sets
- **Memory Efficiency**: Better resource management for large NEF files

#### 🎯 **User Experience**
- **Better CLI**: Advanced command-line options and help text
- **Error Messages**: Clear, actionable error messages
- **Logging**: Configurable logging levels and output
- **Quality Control**: Configurable JPEG quality settings (1-100)

#### 🔧 **Technical Improvements**
- **Dependencies**: Updated to latest stable versions
- **Python Support**: Python 3.9+ requirement with modern features
- **Code Quality**: Comprehensive refactoring with best practices
- **Project Structure**: Professional package layout and organization

### Deprecated

- **Legacy Progress Bar**: `pgbar.py` module (use `tqdm` instead)
- **Old Script**: `photoconverter/main.py` (use new CLI or GUI)

### Removed

- **Hardcoded Paths**: Removed Windows-specific hardcoded explorer paths
- **Random Directory Names**: Replaced with UUID-based naming
- **Inline Configuration**: Moved to proper configuration files

### Fixed

- **Cross-Platform Issues**: Resolved Windows/macOS/Linux compatibility
- **File Extension Handling**: Improved .nef/.NEF file detection
- **Memory Leaks**: Fixed potential memory issues with large batches
- **Error Handling**: Proper exception handling throughout the application

### Security

- **Input Validation**: Added proper file path validation
- **Dependency Updates**: Updated all dependencies to latest secure versions
- **Code Scanning**: Prepared for security scanning tools

## [1.0.0] - Previous Version

### Initial Implementation
- Basic NEF to JPG conversion functionality
- Simple GUI folder selection
- Basic progress bar implementation
- Windows-focused implementation

---

## Migration Guide from V1 to V2

### For End Users

**Old Usage:**
```bash
cd photoconverter
python main.py
```

**New Usage:**
```bash
# Install the package
pip install -e .

# Use GUI mode
nef-converter

# Use CLI mode
nef-converter -d /path/to/nef/files -q 95
```

### For Developers

**Old Structure:**
```
photoconverter/
├── main.py
├── pgbar.py
└── Sample-Images/
```

**New Structure:**
```
src/nef_converter/
├── __init__.py
├── main.py
├── cli.py
└── converter.py
tests/
├── __init__.py
└── test_converter.py
```

**Migration Steps:**
1. Install in development mode: `pip install -e ".[dev]"`
2. Update imports: `from nef_converter import NEFConverter`
3. Use new CLI: `nef-converter --help`
4. Run tests: `pytest`

---

**For more details about any release, please check the [GitHub Releases](https://github.com/r4inX/nef-to-jpg/releases) page.**