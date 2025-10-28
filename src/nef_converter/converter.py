"""
NEF to JPG Converter Module

Core conversion functionality for NEF files.
"""

import logging
import subprocess  # nosec: B404
import sys
import uuid
from pathlib import Path
from typing import List, Tuple

import imageio
import rawpy
from tqdm import tqdm

# Configure logging
logger = logging.getLogger(__name__)

# Platform-specific file browser
if sys.platform == "win32":
    import os

    FILEBROWSER_PATH = os.path.join(os.getenv("WINDIR", "C:\\Windows"), "explorer.exe")
elif sys.platform == "darwin":
    FILEBROWSER_PATH = "open"
else:
    FILEBROWSER_PATH = "xdg-open"


class NEFConverter:
    """
    Modern NEF to JPG converter with improved error handling and progress
    tracking.
    """

    def __init__(self, quality: int = 95, output_format: str = "JPEG") -> None:
        """
        Initialize the NEF converter.

        Args:
            quality: JPEG quality (1-100)
            output_format: Output format (default: JPEG)
        """
        self.quality = quality
        self.output_format = output_format
        logger.info(
            f"Initialized NEF Converter with "
            f"quality={quality}, format={output_format}"
        )

    def get_nef_files(self, directory: Path) -> List[Path]:
        """
        Find all NEF files in the given directory.

        Args:
            directory: Directory to search for NEF files

        Returns:
            List of NEF file paths

        Raises:
            ValueError: If directory doesn't exist or no NEF files found
        """
        if not directory.exists() or not directory.is_dir():
            raise ValueError(f"Directory does not exist: {directory}")

        # Find both .nef and .NEF files
        nef_files: list[Path] = []
        for pattern in ["*.nef", "*.NEF"]:
            nef_files.extend(directory.glob(pattern))

        if not nef_files:
            raise ValueError(f"No NEF files found in: {directory}")

        logger.info(f"Found {len(nef_files)} NEF files in {directory}")
        return nef_files

    def create_output_directory(self, base_directory: Path) -> Path:
        """
        Create a unique output directory.

        Args:
            base_directory: Base directory for output

        Returns:
            Path to created output directory
        """
        output_dir = base_directory / f"export_{uuid.uuid4().hex[:8]}"
        output_dir.mkdir(exist_ok=True)
        logger.info(f"Created output directory: {output_dir}")
        return output_dir

    def convert_nef_to_jpg(self, nef_path: Path, output_path: Path) -> bool:
        """
        Convert a single NEF file to JPG.

        Args:
            nef_path: Path to input NEF file
            output_path: Path for output JPG file

        Returns:
            True if conversion successful, False otherwise
        """
        try:
            with rawpy.imread(str(nef_path)) as raw:
                rgb = raw.postprocess()
                imageio.imwrite(str(output_path), rgb, quality=self.quality)
            return True
        except Exception as e:
            logger.error(f"Failed to convert {nef_path}: {e}")
            return False

    def convert_batch(self, input_directory: str) -> Tuple[int, int]:
        """
        Convert all NEF files in a directory to JPG.

        Args:
            input_directory: Directory containing NEF files

        Returns:
            Tuple of (successful_conversions, total_files)
        """
        try:
            directory = Path(input_directory)
            nef_files = self.get_nef_files(directory)
            output_dir = self.create_output_directory(directory)

            successful = 0

            # Convert files with progress bar
            for nef_file in tqdm(nef_files, desc="Converting NEF files", unit="file"):
                output_file = output_dir / f"{nef_file.stem}.jpg"

                if self.convert_nef_to_jpg(nef_file, output_file):
                    successful += 1

            logger.info(
                f"Conversion complete: {successful}/{len(nef_files)} "
                f"files converted"
            )

            # Open output directory
            if successful > 0:
                self._open_directory(output_dir)

            return successful, len(nef_files)

        except Exception as e:
            logger.error(f"Batch conversion failed: {e}")
            return 0, 0

    def _open_directory(self, directory: Path) -> None:
        """Open directory in system file manager."""
        try:
            if sys.platform == "win32":
                # nosec: B603 - subprocess is safe here with hardcoded paths
                subprocess.run([FILEBROWSER_PATH, str(directory)], check=False)
            else:
                # nosec: B603 - subprocess is safe here with hardcoded paths
                subprocess.run([FILEBROWSER_PATH, str(directory)], check=False)
        except Exception as e:
            logger.warning(f"Could not open directory {directory}: {e}")
