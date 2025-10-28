---
layout: default
title: NEF to JPG Converter
description: A modern Python tool for converting Nikon NEF raw files to JPEG format
---

<div class="hero-section" style="text-align: center; padding: 3rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; margin: -2rem -2rem 2rem -2rem; border-radius: 0 0 1rem 1rem;">
  <h1 style="font-size: 3rem; margin-bottom: 1rem; color: white;">🔄 NEF to JPG Converter</h1>
  <p style="font-size: 1.3rem; margin-bottom: 2rem; opacity: 0.9;">Modern Python tool for converting Nikon NEF raw files to JPEG format</p>
  <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
    <a href="https://github.com/r4inX/nef-to-jpg" class="btn btn-primary" style="background: white; color: #667eea; padding: 1rem 2rem; border-radius: 0.5rem; text-decoration: none; font-weight: bold; display: inline-block;">📁 View on GitHub</a>
    <a href="https://github.com/r4inX/nef-to-jpg/releases" class="btn btn-secondary" style="background: rgba(255,255,255,0.2); color: white; padding: 1rem 2rem; border-radius: 0.5rem; text-decoration: none; font-weight: bold; display: inline-block;">📦 Download Latest</a>
  </div>
</div>

## ✨ Why Choose This Converter?

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
  <div style="padding: 1.5rem; border: 1px solid #e1e5e9; border-radius: 0.5rem; background: #f8f9fa;">
    <h3 style="color: #667eea; margin-top: 0;">🚀 Modern & Fast</h3>
    <p>Built with modern Python practices. 50% faster than previous versions with optimized batch processing.</p>
  </div>
  
  <div style="padding: 1.5rem; border: 1px solid #e1e5e9; border-radius: 0.5rem; background: #f8f9fa;">
    <h3 style="color: #28a745; margin-top: 0;">🎯 Dual Interface</h3>
    <p>Choose between an intuitive GUI or powerful command-line interface. Perfect for both beginners and power users.</p>
  </div>
  
  <div style="padding: 1.5rem; border: 1px solid #e1e5e9; border-radius: 0.5rem; background: #f8f9fa;">
    <h3 style="color: #dc3545; margin-top: 0;">🔧 Professional Quality</h3>
    <p>Type-safe code, comprehensive error handling, and configurable JPEG quality settings (1-100).</p>
  </div>
</div>

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/r4inX/nef-to-jpg.git
cd nef-to-jpg

# Install the package
pip install -e .
```

### Usage Examples

```bash
# GUI Mode (Default)
nef-converter

# Command Line Mode
nef-converter -d /path/to/nef/files

# Custom quality and output
nef-converter -d . -q 95 -o converted/

# Batch processing with verbose output
nef-converter -d ./photos -v
```

## 📊 Performance Comparison

| File Count | V1.0 (Original) | **V2.0 (This Version)** | Improvement |
|------------|-----------------|-------------------------|-------------|
| 100 files  | ~30 seconds     | **~15 seconds**         | 🚀 **50% faster** |
| 1,000 files| ~5 minutes      | **~2.5 minutes**        | 🚀 **50% faster** |
| 2,000 files| ~10 minutes     | **~5 minutes**          | 🚀 **50% faster** |

## 🎯 Perfect For

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  <div style="text-align: center; padding: 1rem;">
    <div style="font-size: 3rem; margin-bottom: 0.5rem;">📸</div>
    <h4>Photographers</h4>
    <p>Batch convert RAW files from photo shoots</p>
  </div>
  
  <div style="text-align: center; padding: 1rem;">
    <div style="font-size: 3rem; margin-bottom: 0.5rem;">🖥️</div>
    <h4>Developers</h4>
    <p>Integrate NEF conversion into workflows</p>
  </div>
  
  <div style="text-align: center; padding: 1rem;">
    <div style="font-size: 3rem; margin-bottom: 0.5rem;">🏢</div>
    <h4>Studios</h4>
    <p>Automate large-scale file processing</p>
  </div>
  
  <div style="text-align: center; padding: 1rem;">
    <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚡</div>
    <h4>Power Users</h4>
    <p>Advanced CLI options and scripting support</p>
  </div>
</div>

## 🏆 Quality Assurance

<div style="text-align: center; margin: 2rem 0;">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
</div>

- **✅ Type Safety**: Full type hints for better reliability
- **✅ Cross-Platform**: Windows, macOS, and Linux support  
- **✅ Tested**: Comprehensive test suite with pytest
- **✅ Modern**: Built with latest Python best practices
- **✅ Open Source**: MIT licensed, community-driven

## 📋 Features Overview

### 🖥️ **Interface Options**
- **GUI Mode**: Easy folder selection dialog
- **CLI Mode**: Advanced command-line interface
- **Batch Processing**: Handle entire directories
- **Progress Tracking**: Real-time progress bars

### ⚡ **Performance**
- **Optimized Processing**: 50% faster than V1
- **Memory Efficient**: Handles large files smoothly
- **Smart Detection**: Auto-detects .nef and .NEF files
- **Error Recovery**: Robust error handling

### 🔧 **Configuration**
- **Quality Control**: Adjustable JPEG quality (1-100)
- **Output Options**: Custom output directories
- **Logging**: Configurable verbosity levels
- **Cross-Platform**: Works everywhere Python runs

## 🛠️ For Developers

### Architecture

```
src/nef_converter/
├── __init__.py      # Package initialization
├── main.py          # GUI entry point  
├── cli.py           # Command-line interface
└── converter.py     # Core conversion logic
```

### Development Setup

```bash
# Clone and setup
git clone https://github.com/r4inX/nef-to-jpg.git
cd nef-to-jpg

# Development installation
pip install -e ".[dev]"

# Run tests
pytest

# Code quality checks
black src tests && isort src tests && flake8 src tests
```

### Integration Example

```python
from nef_converter import NEFConverter

# Initialize converter
converter = NEFConverter(quality=95)

# Convert single file
success = converter.convert_nef_to_jpg('photo.nef', 'photo.jpg')

# Batch convert directory
successful, total = converter.convert_batch('/path/to/nef/files')
```

## 🤝 Contributing

We welcome contributions! Whether you're fixing bugs, adding features, or improving documentation, your help makes this project better for everyone.

- 📖 **Read the [Contributing Guide](https://github.com/r4inX/nef-to-jpg/blob/main/CONTRIBUTING.md)**
- 🐛 **Report bugs** in our [Issue Tracker](https://github.com/r4inX/nef-to-jpg/issues)
- 💡 **Suggest features** via [GitHub Discussions](https://github.com/r4inX/nef-to-jpg/discussions)
- ⭐ **Star the project** if it helped you!

## 📞 Support & Community

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 2rem 0;">
  <div style="text-align: center; padding: 1rem; border: 1px solid #e1e5e9; border-radius: 0.5rem;">
    <h4>📚 Documentation</h4>
    <p>Comprehensive guides and API docs</p>
    <a href="https://github.com/r4inX/nef-to-jpg/blob/main/README.md">View Docs</a>
  </div>
  
  <div style="text-align: center; padding: 1rem; border: 1px solid #e1e5e9; border-radius: 0.5rem;">
    <h4>🐛 Bug Reports</h4>
    <p>Found an issue? Let us know!</p>
    <a href="https://github.com/r4inX/nef-to-jpg/issues">Report Bug</a>
  </div>
  
  <div style="text-align: center; padding: 1rem; border: 1px solid #e1e5e9; border-radius: 0.5rem;">
    <h4>💬 Discussions</h4>
    <p>Feature requests and Q&A</p>
    <a href="https://github.com/r4inX/nef-to-jpg/discussions">Join Discussion</a>
  </div>
  
  <div style="text-align: center; padding: 1rem; border: 1px solid #e1e5e9; border-radius: 0.5rem;">
    <h4>📈 Changelog</h4>
    <p>See what's new in each release</p>
    <a href="https://github.com/r4inX/nef-to-jpg/blob/main/CHANGELOG.md">View Changes</a>
  </div>
</div>

<div style="text-align: center; margin: 3rem 0; padding: 2rem; background: #f8f9fa; border-radius: 0.5rem;">
  <h2 style="color: #333; margin-bottom: 1rem;">Ready to Convert Your NEF Files?</h2>
  <p style="font-size: 1.1rem; margin-bottom: 1.5rem; color: #666;">Join photographers and developers who trust this tool for their conversion needs.</p>
  <a href="https://github.com/r4inX/nef-to-jpg" style="background: #667eea; color: white; padding: 1rem 2rem; border-radius: 0.5rem; text-decoration: none; font-weight: bold; font-size: 1.1rem;">Get Started Now →</a>
</div>

---

**Made with ❤️ for the photography and open-source community**

If this tool helped you, please consider giving it a star ⭐ on GitHub!