"""
Main entry point for NEF Converter

This module provides the command-line interface and GUI functionality.
"""

import logging
import sys
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory
from typing import Optional

from .converter import NEFConverter

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def select_directory() -> Optional[str]:
    """
    Open a directory selection dialog.

    Returns:
        Selected directory path or None if cancelled
    """
    root = Tk()
    root.withdraw()  # Hide the main window

    directory = askdirectory(title="Select your Folder with .NEF Files to convert them")

    root.destroy()
    return directory if directory else None


def main() -> None:
    """Main entry point for the NEF to JPG converter."""
    print("=" * 50)
    print("🔄 NEF-to-JPG Converter V2.0")
    print("=" * 50)
    print()

    try:
        # Select directory
        directory = select_directory()

        if not directory:
            logger.info("No directory selected. Exiting...")
            return

        # Initialize converter
        converter = NEFConverter(quality=95)

        # Convert files
        successful, total = converter.convert_batch(directory)

        # Show results
        print()
        print(f"✅ Conversion completed!")
        print(f"📊 Successfully converted: {successful}/{total} files")

        if successful == 0:
            print("❌ No files were converted. Please check the logs.")
        elif successful < total:
            print("⚠️ Some files failed to convert. Check the logs for details.")
        else:
            print("🎉 All files converted successfully!")

    except KeyboardInterrupt:
        logger.info("Conversion cancelled by user")
        print("\n❌ Conversion cancelled by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
