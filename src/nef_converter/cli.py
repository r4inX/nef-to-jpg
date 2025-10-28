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

logger = logging.getLogger(__name__)


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
        "--no-parallel",
        action="store_true",
        help="Disable parallel processing",
    )

    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of parallel workers (default: auto)",
    )

    parser.add_argument(
        "--no-exif",
        action="store_true",
        help="Do not preserve EXIF metadata",
    )

    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch directory for new NEF files and convert automatically",
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

    parser.add_argument("--version", action="version", version="%(prog)s 2.1.0")

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
        converter = NEFConverter(
            quality=args.quality,
            max_workers=args.workers,
            preserve_exif=not args.no_exif,
        )

        # Watch mode
        if args.watch:
            from .watch import watch_directory

            output_dir = (
                Path(args.output)
                if args.output
                else Path(input_directory) / "watch_output"
            )
            output_dir.mkdir(exist_ok=True)

            try:
                watch_directory(input_directory, converter, output_dir)
            except Exception as e:
                logger.error(f"Watch mode failed: {e}")
                print(f"❌ Watch mode error: {e}")
                print("💡 Tip: Ensure watchdog is installed: pip install watchdog")
                sys.exit(1)
            return

        # Convert files
        successful, total = converter.convert_batch(
            input_directory, parallel=not args.no_parallel
        )

        # Show results
        print()
        print("✅ Conversion completed!")
        print(f"📊 Successfully converted: {successful}/{total} files")

        if successful == 0:
            print("❌ No files were converted. Please check the logs.")
            print("💡 Tip: Use -v flag for detailed error messages")
            sys.exit(1)
        elif successful < total:
            print("⚠️ Some files failed to convert. Check the logs for details.")
            print(f"💡 Tip: {total - successful} files had errors")
            sys.exit(1)
        else:
            print("🎉 All files converted successfully!")

    except KeyboardInterrupt:
        print("\n❌ Conversion cancelled by user")
        sys.exit(130)  # SIGINT exit code
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"\n❌ An error occurred: {e}")
        print("💡 Tip: Use -v flag for detailed error information")
        print("📖 See: https://github.com/r4inX/nef-to-jpg#troubleshooting")
        sys.exit(1)
