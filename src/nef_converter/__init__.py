"""
NEF Converter Package

A modern Python package for converting Nikon NEF raw files to JPEG format.
"""

__version__ = "2.0.0"
__author__ = "r4inX"
__email__ = "your-email@example.com"

# Import main components
try:
    from .converter import NEFConverter
    from .main import main
    __all__ = ["NEFConverter", "main"]
except ImportError:
    # Handle cases where dependencies aren't installed yet
    __all__ = []