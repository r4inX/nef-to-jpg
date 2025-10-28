# 🔄 NEF to JPG Converter

[![CI/CD Pipeline](https://github.com/r4inX/nef-to-jpg/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/r4inX/nef-to-jpg/actions)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern Python tool for converting Nikon NEF raw files to JPEG format with parallel processing, EXIF preservation, GUI support, and comprehensive command-line interface.

## ✨ Features

### 🖥️ **Dual Interface Support**
- **GUI Mode**: Beautiful Gooey-based desktop application (optional)
  - Drag & drop folder selection
  - JPEG quality slider
  - CPU core selection
  - EXIF preservation toggle
  - Real-time progress tracking
- **CLI Mode**: Powerful command-line interface with advanced options
- **Batch Processing**: Convert entire directories of NEF files

### ⚡ **Performance Features**
- **Parallel Processing**: Multi-core CPU utilization for 2-4x faster conversion
- **Smart Resource Management**: Automatic optimal worker allocation
- **Conversion Statistics**: Time per file, total time, and files/s metrics
- **Watch Mode**: Auto-convert new files as they appear in a directory

### � **EXIF Preservation**
- **Metadata Copying**: Automatically preserves camera settings, GPS, copyright, timestamps
- **Optional Disable**: Use `--no-exif` flag to skip metadata copying
- **Robust Handling**: Graceful fallback for files with problematic EXIF data

### �🚀 **Modern Architecture**
- **Type-safe**: Full type hints for better code reliability
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Progress tracking**: Real-time progress bars with `tqdm`
- **Error handling**: Comprehensive error reporting and logging with helpful tips

### 📊 **Quality & Reliability**
- **High-quality conversion**: Configurable JPEG quality (1-100)
- **Memory efficient**: Handles large files without memory issues
- **Smart file handling**: Auto-detects .nef and .NEF extensions
- **Fast processing**: Optimized for large batches

## 🚀 Quick Start

### Installation

```bash
# Basic installation (CLI only)
pip install git+https://github.com/r4inX/nef-to-jpg.git

# With GUI support (recommended for desktop use)
pip install "git+https://github.com/r4inX/nef-to-jpg.git#egg=nef-to-jpg-converter[gui]"

# For development
git clone https://github.com/r4inX/nef-to-jpg.git
cd nef-to-jpg
pip install -e ".[gui,dev]"
```

### Usage

#### GUI Mode (requires [gui] extra)

The GUI provides an easy-to-use desktop interface powered by Gooey:

```bash
# Launch graphical interface
nef-gui

# Or
python -m nef_converter.gui
```

Features:
- 📁 **Drag & drop folder selection**
- 🎚️ **Quality slider** (1-100)
- 💻 **CPU core selection** for parallel processing
- 📸 **EXIF toggle** to preserve metadata
- 📊 **Real-time progress** tracking

#### Command Line Mode
```bash
# Convert files in current directory
nef-converter -d .

# Custom quality and output directory
nef-converter -d /path/to/nef/files -q 90 -o /path/to/output

# Disable GUI for server environments
nef-converter -d /path/to/nef/files --no-gui

# Watch mode - auto-convert new files
nef-converter --watch -d /path/to/watch

# Parallel processing (2-4x faster)
nef-converter -d . --workers 8

# Disable EXIF preservation
nef-converter -d . --no-exif
```

### Advanced Options

```bash
usage: nef-converter [-h] [-d DIRECTORY] [-o OUTPUT] [-q 1-100] [--no-parallel] 
                     [--workers WORKERS] [--no-exif] [--watch] [--no-gui] [-v] [--version]

Convert Nikon NEF raw files to JPEG format

options:
  -h, --help            show this help message and exit
  -d, --directory DIRECTORY
                        Directory containing NEF files to convert
  -o, --output OUTPUT   Output directory (default: creates export_* in input directory)
  -q, --quality 1-100   JPEG quality (1-100, default: 95)
  --no-parallel         Disable parallel processing
  --workers WORKERS     Number of parallel workers (default: auto)
  --no-exif             Do not preserve EXIF metadata
  --watch               Watch directory for new NEF files and convert automatically
  --no-gui              Disable GUI directory selector
  -v, --verbose         Enable verbose logging
  --version             show program's version number and exit
```

## 🚀 New in v2.1.0

- 🖥️ **GUI Mode**: Beautiful Gooey-based desktop application (optional dependency)
- ⚡ **Parallel Processing**: 2-4x faster with multi-core CPU support
- 📸 **EXIF Preservation**: Automatically copy metadata from NEF to JPEG
- 👁️ **Watch Mode**: Auto-convert new files as they appear
- 📊 **Statistics Display**: See time per file, total time, and files/s metrics
- 🎯 **Better Errors**: Helpful tips, troubleshooting links, and suppressed harmless warnings
- 📦 **Standalone Apps**: Windows/macOS/Linux executables (no Python needed)

## 📋 Requirements

- **Python 3.9+**
- **Core Dependencies**: `rawpy`, `numpy`, `pillow`, `tqdm`, `watchdog`
- **Optional GUI**: `gooey` (install with `pip install nef-to-jpg-converter[gui]`)
- **Optional**: `tkinter` for basic file dialogs (usually included with Python)

## 🏗️ Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/r4inX/nef-to-jpg.git
cd nef-to-jpg

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_converter.py
```

### Code Quality

```bash
# Format code
black src tests

# Sort imports
isort src tests

# Lint code
flake8 src tests

# Type checking
mypy src
```

## 📸 Example Usage

### Batch Conversion Examples

```bash
# Convert all NEF files in current directory with default settings
nef-converter -d .

# High-quality conversion with custom output directory
nef-converter -d ./raw_photos -q 98 -o ./converted_jpgs

# Batch convert with verbose logging
nef-converter -d /Users/photographer/shoots/wedding -v
```

### Performance

Modern performance improvements over the original version:

| File Count | Original Version | V2.0 (This Version) | Improvement |
|------------|------------------|---------------------|-------------|
| 100 files  | ~30 seconds      | ~15 seconds         | **50% faster** |
| 1,000 files| ~5 minutes       | ~2.5 minutes        | **50% faster** |
| 2,000 files| ~10 minutes      | ~5 minutes          | **50% faster** |

## 🔧 Technical Details

### Architecture

```
src/nef_converter/
├── __init__.py         # Package initialization
├── main.py            # GUI entry point
├── cli.py             # Command-line interface
└── converter.py       # Core conversion logic
```

### Key Improvements from V1

- **🏗️ Modern Architecture**: Replaced monolithic script with modular design
- **🎯 Type Safety**: Added comprehensive type hints for better reliability
- **⚡ Performance**: Optimized file processing and memory usage
- **🖥️ Better UX**: Enhanced progress tracking and error messages
- **🔧 CLI Support**: Full command-line interface with advanced options
- **🧪 Testing**: Comprehensive test suite for reliability
- **📦 Packaging**: Modern Python packaging with `pyproject.toml`

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Ensure tests pass: `pytest`
5. Format code: `black src tests && isort src tests`
6. Commit changes: `git commit -m "Add amazing feature"`
7. Push to branch: `git push origin feature/amazing-feature`
8. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Original concept and implementation inspiration
- [rawpy](https://github.com/letmaik/rawpy) library for NEF file support
- [imageio](https://github.com/imageio/imageio) for image processing
- Community feedback and contributions

## 📊 Project Status

- ✅ **Core Features**: Complete
- ✅ **GUI Mode**: Complete (v2.1.0)
- ✅ **CLI Interface**: Complete  
- ✅ **Parallel Processing**: Complete (v2.1.0)
- ✅ **EXIF Preservation**: Complete (v2.1.0)
- ✅ **Watch Mode**: Complete (v2.1.0)
- ✅ **Modern Architecture**: Complete
- ✅ **Type Safety**: Complete

## 🗺️ Roadmap

See our detailed [ROADMAP.md](ROADMAP.md) for planned features and improvements!

### 🚀 Upcoming Features

#### v2.2.0 - Enhanced User Experience (Q1 2026)
- 🎨 **GUI Improvements**: Drag & drop files, preview images, dark mode, conversion history
- � **CLI Enhancements**: Recursive mode, file filtering, dry run, JSON output
- 📊 **Statistics & Reporting**: HTML/PDF reports, file size comparison, CSV export

#### v2.3.0 - Professional Features (Q2 2026)
- 📸 **Advanced Processing**: Auto-rotate, white balance, sharpening, watermarking
- 🖼️ **Format Support**: PNG, TIFF, WebP, HEIC + Canon/Sony RAW formats
- 🎨 **Color Management**: ICC profiles, color space conversion, 16-bit output

#### v2.4.0 - Web & Integration (Q3 2026)
- 🌍 **Web Interface**: Browser-based UI with REST API
- 🔌 **Cloud Integration**: Dropbox, Google Drive, OneDrive support
- 📦 **Automation**: Hot folders, scheduling, webhook notifications

#### v2.5.0 - DevOps & Deployment (Q4 2026)
- � **Containerization**: Docker, Kubernetes, serverless functions
- 📊 **Monitoring**: Prometheus metrics, Grafana dashboards

#### v3.0.0 - Enterprise & Advanced (2027)
- 🏢 **Enterprise**: Multi-user, licensing, audit logging, distributed processing
- 🤖 **AI Features**: Scene detection, auto-tagging, face detection, smart cropping
- 📱 **Native Apps**: Windows Store, Mac App Store, iOS, Android

### � Top Community Requests

Want to help shape the future? Vote on features or suggest new ones in our [Discussions](https://github.com/r4inX/nef-to-jpg/discussions)!

**Quick Wins** (Easy to implement):
- System tray icon with quick actions
- Context menu integration (right-click in Explorer)
- Sound notification on completion
- Remember last used settings
- Color-coded CLI output

**Most Requested**:
- Batch rename files during conversion
- Preserve folder structure in output
- Multiple output formats simultaneously
- GPU acceleration for faster processing
- Before/After comparison slider

See [ROADMAP.md](ROADMAP.md) for the complete list of 100+ planned features!

---

**Made with ❤️ for photographers and developers**

If this tool helped you, please consider giving it a star ⭐ on GitHub! 
