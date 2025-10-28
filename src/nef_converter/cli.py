"""
Command Line Interface for NEF Converter

Provides argument parsing and CLI functionality.
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional, cast

from .converter import NEFConverter


def select_directory() -> Optional[str]:
    """Open a GUI dialog to select a directory."""
    try:
        from tkinter import Tk
        from tkinter.filedialog import askdirectory

        root = Tk()
        root.withdraw()  # Hide the main window
        directory: Optional[str] = cast(
            Optional[str], askdirectory(title="Select a directory")
        )
        root.destroy()
        return directory if directory else None
    except ImportError:
        print("Error: tkinter is not available.")
        return None


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="Convert Nikon NEF raw files to JPEG format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Open directory selector GUI
  %(prog)s -d /path/to/nef/files    # Convert files in directory
  %(prog)s -d . -q 90 -o output/    # Custom quality and output
        """,
    )

    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        help="Directory containing NEF files to convert",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output directory (default: creates export_* in input directory)",
    )

    parser.add_argument(
        "-q",
        "--quality",
        type=int,
        default=95,
        metavar="1-100",
        help="JPEG quality (1-100, default: 95)",
    )

    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Disable GUI directory selector",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    parser.add_argument("--version", action="version", version="%(prog)s 2.0.0")

    return parser


def validate_args(args: argparse.Namespace) -> bool:
    """Validate command line arguments."""
    if args.quality < 1 or args.quality > 100:
        print("Error: Quality must be between 1 and 100")
        return False

    if args.directory:
        directory = Path(args.directory)
        if not directory.exists():
            print(f"Error: Directory does not exist: {args.directory}")
            return False
        if not directory.is_dir():
            print(f"Error: Path is not a directory: {args.directory}")
            return False

    return True


def get_input_directory(args: argparse.Namespace) -> Optional[str]:
    """Get input directory from args or GUI."""
    if args.directory:
        return args.directory

    if args.no_gui:
        print("Error: No directory specified and GUI disabled")
        return None

    directory = select_directory()
    if directory is None:
        return None
    return directory


def cli_main() -> None:
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Validate arguments
    if not validate_args(args):
        sys.exit(1)

    # Get input directory
    input_directory = get_input_directory(args)
    if not input_directory:
        sys.exit(1)

    try:
        # Initialize converter
        converter = NEFConverter(quality=args.quality)

        # Convert files
        successful, total = converter.convert_batch(input_directory)

        # Show results
        print()
        print("✅ Conversion completed!")
        print(f"📊 Successfully converted: {successful}/{total} files")

        if successful == 0:
            print("❌ No files were converted. Please check the logs.")
            sys.exit(1)
        elif successful < total:
            print("⚠️ Some files failed to convert. Check the logs for details.")
            sys.exit(1)
        else:
            print("🎉 All files converted successfully!")

    except KeyboardInterrupt:
        print("\n❌ Conversion cancelled by user")
        sys.exit(130)  # SIGINT exit code
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"\n❌ An error occurred: {e}")
        sys.exit(1)
