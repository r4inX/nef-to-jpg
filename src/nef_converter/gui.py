"""
NEF Converter - Graphical User Interface

User-friendly GUI for NEF to JPEG conversion using Gooey.
Note: Requires 'gooey' package. Install with: pip install nef-to-jpg-converter[gui]
"""

import argparse
import logging
import sys
from pathlib import Path

# Check if Gooey is available
try:
    from gooey import Gooey, GooeyParser

    GOOEY_AVAILABLE = True
except ImportError:
    GOOEY_AVAILABLE = False

    # Create dummy decorators for when Gooey is not installed
    def Gooey(*args, **kwargs):
        def decorator(func):
            return func

        return decorator

    GooeyParser = argparse.ArgumentParser

# Handle both direct execution and package import
try:
    from .converter import NEFConverter
except ImportError:
    from nef_converter.converter import NEFConverter

logger = logging.getLogger(__name__)


@Gooey(
    program_name="NEF to JPEG Converter",
    program_description="Convert Nikon NEF raw files to high-quality JPEG images",
    default_size=(800, 900),
    required_cols=1,
    optional_cols=1,
    navigation="SIDEBAR",
    sidebar_title="Options",
    header_bg_color="#2c3e50",
    body_bg_color="#ecf0f1",
    footer_bg_color="#2c3e50",
    menu=[
        {
            "name": "Help",
            "items": [
                {
                    "type": "AboutDialog",
                    "menuTitle": "About",
                    "name": "NEF to JPEG Converter",
                    "description": "Convert Nikon NEF raw files to JPEG format with EXIF preservation and parallel processing",
                    "version": "2.1.0",
                    "copyright": "2025",
                    "website": "https://github.com/r4inX/nef-to-jpg",
                    "developer": "r4inX",
                    "license": "MIT",
                },
                {
                    "type": "Link",
                    "menuTitle": "Documentation",
                    "url": "https://github.com/r4inX/nef-to-jpg#readme",
                },
            ],
        }
    ],
    progress_regex=r"^Converting NEF files:\s+(\d+)%",
    progress_expr="x[0]",
    disable_progress_bar_animation=False,
    timing_options={
        "show_time_remaining": True,
        "hide_time_remaining_on_complete": False,
    },
)
def create_gui() -> None:
    """Create and run the GUI."""
    parser = GooeyParser(
        description="Convert Nikon NEF raw files to JPEG format\n\n"
        "This tool converts your RAW NEF files to high-quality JPEG images "
        "with optional EXIF metadata preservation and multi-core parallel processing."
    )

    # Required arguments group
    required_group = parser.add_argument_group(
        "Required Settings",
        "Main settings for conversion",
    )

    required_group.add_argument(
        "directory",
        metavar="Input Directory",
        help="Select the folder containing your NEF files",
        widget="DirChooser",
    )

    # Optional arguments group
    optional_group = parser.add_argument_group(
        "Optional Settings",
        "Advanced conversion options",
    )

    optional_group.add_argument(
        "-q",
        "--quality",
        metavar="JPEG Quality",
        type=int,
        default=95,
        help="JPEG quality (1-100, higher is better)",
        widget="Slider",
        gooey_options={
            "min": 1,
            "max": 100,
            "increment": 5,
        },
    )

    optional_group.add_argument(
        "--workers",
        metavar="CPU Cores",
        type=int,
        default=None,
        help="Number of CPU cores to use (leave empty for automatic)",
        widget="Dropdown",
        choices=[None, 1, 2, 4, 6, 8, 12, 16],
    )

    optional_group.add_argument(
        "--no-exif",
        metavar="Preserve EXIF",
        action="store_true",
        help="Disable EXIF metadata preservation",
        widget="CheckBox",
    )

    optional_group.add_argument(
        "--no-parallel",
        metavar="Single Core Mode",
        action="store_true",
        help="Disable parallel processing (slower but uses less memory)",
        widget="CheckBox",
    )

    optional_group.add_argument(
        "-v",
        "--verbose",
        metavar="Verbose Logging",
        action="store_true",
        help="Show detailed processing information",
        widget="CheckBox",
    )

    args = parser.parse_args()

    # Configure logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    try:
        # Validate input directory
        directory = Path(args.directory)
        if not directory.exists():
            print(f"❌ Error: Directory does not exist: {args.directory}")
            print("💡 Please select a valid directory with NEF files.")
            sys.exit(1)

        if not directory.is_dir():
            print(f"❌ Error: Path is not a directory: {args.directory}")
            print("💡 Please select a folder, not a file.")
            sys.exit(1)

        # Validate quality
        if args.quality < 1 or args.quality > 100:
            print("❌ Error: Quality must be between 1 and 100")
            print(f"💡 You entered: {args.quality}")
            sys.exit(1)

        # Initialize converter
        print("🔧 Initializing converter...")
        converter = NEFConverter(
            quality=args.quality,
            max_workers=args.workers,
            preserve_exif=not args.no_exif,
        )

        # Convert files
        print(f"📂 Converting files from: {directory}")
        print(f"⚙️  Quality: {args.quality}")
        print(f"⚙️  EXIF Preservation: {'Yes' if not args.no_exif else 'No'}")
        print(f"⚙️  Parallel Processing: {'Yes' if not args.no_parallel else 'No'}")
        print(f"⚙️  Workers: {args.workers if args.workers else 'Auto'}")
        print()

        successful, total, stats = converter.convert_batch(
            str(directory), parallel=not args.no_parallel
        )

        # Show results
        print()
        print("=" * 60)
        print("✅ Conversion completed!")
        print(f"📊 Successfully converted: {successful}/{total} files")

        # Display statistics
        if stats:
            print()
            print("📈 Statistics:")
            print(f"   ⏱️  Total time: {stats['total_time']:.2f}s")
            print(f"   📸 Time per file: {stats['time_per_file']:.2f}s")
            print(f"   ⚡ Speed: {stats['files_per_second']:.2f} files/s")

        print()

        if successful == 0:
            print("❌ No files were converted!")
            print("💡 Tips:")
            print("   • Make sure the directory contains NEF files")
            print("   • Check file permissions")
            print("   • Enable verbose mode for more details")
            sys.exit(1)
        elif successful < total:
            print(f"⚠️  Warning: {total - successful} files failed to convert")
            print("💡 Enable verbose mode (-v) for detailed error messages")
            sys.exit(1)
        else:
            print("🎉 All files converted successfully!")
            print(f"📁 Output location: {directory / 'export_*'}")
            print()
            print("✨ Thank you for using NEF Converter!")

    except KeyboardInterrupt:
        print("\n❌ Conversion cancelled by user")
        sys.exit(130)
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        print(f"\n❌ An error occurred: {e}")
        print()
        print("💡 Troubleshooting tips:")
        print("   • Make sure the directory contains valid NEF files")
        print("   • Check that you have write permissions in the directory")
        print("   • Try reducing the quality setting if running out of memory")
        print("   • Enable verbose mode (-v) for more details")
        print()
        print("📖 Documentation: https://github.com/r4inX/nef-to-jpg#readme")
        sys.exit(1)


def gui_main() -> None:
    """GUI entry point."""
    if not GOOEY_AVAILABLE:
        print("❌ Error: Gooey is not installed!")
        print()
        print("The GUI requires the 'gooey' package.")
        print("Install it with:")
        print()
        print("  pip install nef-to-jpg-converter[gui]")
        print()
        print("Or install gooey directly:")
        print("  pip install gooey")
        print()
        sys.exit(1)

    create_gui()


if __name__ == "__main__":
    gui_main()
