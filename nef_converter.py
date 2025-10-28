#!/usr/bin/env python
"""
Entry point script for the new NEF converter structure.
This script allows running the converter from the project root.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from nef_converter.main import main

if __name__ == "__main__":
    main()