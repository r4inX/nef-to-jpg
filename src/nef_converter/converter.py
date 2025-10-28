"""
NEF to JPG Converter Module

Core conversion functionality for NEF files.
"""

import logging
import subprocess  # nosec: B404
import sys
import time
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import rawpy
from PIL import Image
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

    def __init__(
        self,
        quality: int = 95,
        output_format: str = "JPEG",
        max_workers: Optional[int] = None,
        preserve_exif: bool = True,
    ) -> None:
        """
        Initialize the NEF converter.

        Args:
            quality: JPEG quality (1-100)
            output_format: Output format (default: JPEG)
            max_workers: Maximum number of parallel workers (None = auto)
            preserve_exif: Preserve EXIF metadata from NEF files
        """
        self.quality = quality
        self.output_format = output_format
        self.max_workers = max_workers
        self.preserve_exif = preserve_exif
        logger.info(
            f"Initialized NEF Converter with "
            f"quality={quality}, format={output_format}, "
            f"workers={max_workers or 'auto'}, preserve_exif={preserve_exif}"
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
        if not directory.exists():
            raise ValueError(
                f"❌ Directory does not exist: {directory}\n"
                f"💡 Tip: Check the path and try again\n"
                f"📖 See: https://github.com/r4inX/nef-to-jpg#usage"
            )

        if not directory.is_dir():
            raise ValueError(
                f"❌ Path is not a directory: {directory}\n"
                f"💡 Tip: Provide a folder path, not a file path"
            )

        # Find both .nef and .NEF files
        nef_files: list[Path] = []
        for pattern in ["*.nef", "*.NEF"]:
            nef_files.extend(directory.glob(pattern))

        if not nef_files:
            raise ValueError(
                f"❌ No NEF files found in: {directory}\n"
                f"💡 Tip: Ensure the directory contains .nef or .NEF files\n"
                f"📂 Supported: .nef, .NEF extensions"
            )

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
            # Extract EXIF data before conversion if needed
            exif_data = None
            if self.preserve_exif:
                exif_data = self._extract_exif_data(nef_path)

            # Convert NEF to RGB array
            with rawpy.imread(str(nef_path)) as raw:
                rgb = raw.postprocess()

            # Convert to PIL Image for better control
            img = Image.fromarray(rgb)

            # Save with EXIF data if available
            if exif_data:
                try:
                    img.save(str(output_path), "JPEG", quality=self.quality, exif=exif_data)
                    logger.debug(f"Saved {output_path.name} with EXIF data")
                except Exception as exif_err:
                    # If EXIF save fails, save without EXIF
                    logger.warning(f"Could not save with EXIF for {nef_path.name}: {exif_err}, saving without EXIF")
                    img.save(str(output_path), "JPEG", quality=self.quality)
            else:
                img.save(str(output_path), "JPEG", quality=self.quality)

            return True
        except FileNotFoundError:
            logger.error(f"File not found: {nef_path}")
            print(f"❌ File not found: {nef_path.name}")
            return False
        except PermissionError:
            logger.error(f"Permission denied: {nef_path}")
            print(
                f"❌ Permission denied: {nef_path.name}\n"
                f"💡 Tip: Check file permissions or close any program using the file"
            )
            return False
        except Exception as e:
            error_msg = str(e).lower()
            logger.error(f"Failed to convert {nef_path}: {e}")

            # Provide helpful error messages based on error type
            if "corrupted" in error_msg or "invalid" in error_msg:
                print(
                    f"❌ File may be corrupted: {nef_path.name}\n"
                    f"💡 Tip: Try opening in Nikon software to verify\n"
                    f"📖 See: https://github.com/r4inX/nef-to-jpg#troubleshooting"
                )
            elif "memory" in error_msg:
                print(
                    f"❌ Out of memory processing: {nef_path.name}\n"
                    f"💡 Tip: Close other applications or use --no-parallel flag"
                )
            else:
                print(
                    f"❌ Failed to convert: {nef_path.name}\n"
                    f"💡 Error: {e}\n"
                    f"📖 See: https://github.com/r4inX/nef-to-jpg#troubleshooting"
                )
            return False

    def _extract_exif_data(self, source_path: Path) -> Optional[bytes]:
        """
        Extract EXIF metadata from source file.

        Args:
            source_path: Source NEF file

        Returns:
            EXIF data as bytes or None if not available
        """
        try:
            with Image.open(str(source_path)) as source_img:
                exif = source_img.getexif()
                if exif:
                    # Convert to bytes for saving
                    return exif.tobytes()
                return None
        except Exception as e:
            logger.warning(f"Could not extract EXIF data from {source_path.name}: {e}")
            return None

    def _copy_exif_data(self, source_path: Path, dest_path: Path) -> None:
        """
        Copy EXIF metadata from source to destination.
        
        DEPRECATED: Now handled directly in convert_nef_to_jpg

        Args:
            source_path: Source NEF file
            dest_path: Destination JPEG file
        """
        # This method is kept for backward compatibility but is no longer used
        pass

    @staticmethod
    def _convert_single_file(args: Tuple[Path, Path, int, bool]) -> Tuple[bool, Path]:
        """
        Static method for parallel processing of single file.

        Args:
            args: Tuple of (nef_path, output_path, quality, preserve_exif)

        Returns:
            Tuple of (success, nef_path)
        """
        nef_path, output_path, quality, preserve_exif = args
        try:
            # Extract EXIF data before conversion if needed
            exif_data = None
            if preserve_exif:
                try:
                    with Image.open(str(nef_path)) as source_img:
                        exif = source_img.getexif()
                        if exif:
                            exif_data = exif.tobytes()
                except Exception as e:
                    logger.warning(f"Could not extract EXIF from {nef_path.name}: {e}")

            # Convert NEF to RGB array
            with rawpy.imread(str(nef_path)) as raw:
                rgb = raw.postprocess()

            # Convert to PIL Image and save
            img = Image.fromarray(rgb)

            # Save with EXIF data if available
            if exif_data:
                try:
                    img.save(str(output_path), "JPEG", quality=quality, exif=exif_data)
                except Exception:
                    # If EXIF save fails, save without EXIF
                    img.save(str(output_path), "JPEG", quality=quality)
            else:
                img.save(str(output_path), "JPEG", quality=quality)

            return True, nef_path
        except Exception as e:
            logger.error(f"Failed to convert {nef_path}: {e}")
            return False, nef_path

    def convert_batch(
        self, input_directory: str, parallel: bool = True
    ) -> Tuple[int, int, Dict[str, float]]:
        """
        Convert all NEF files in a directory to JPG.

        Args:
            input_directory: Directory containing NEF files
            parallel: Use parallel processing (default: True)

        Returns:
            Tuple of (successful_conversions, total_files, statistics)
        """
        start_time = time.time()

        try:
            directory = Path(input_directory)
            nef_files = self.get_nef_files(directory)
            output_dir = self.create_output_directory(directory)

            successful = 0

            if parallel and len(nef_files) > 1:
                # Parallel processing for better performance
                tasks = [
                    (
                        nef_file,
                        output_dir / f"{nef_file.stem}.jpg",
                        self.quality,
                        self.preserve_exif,
                    )
                    for nef_file in nef_files
                ]

                with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                    futures = {
                        executor.submit(self._convert_single_file, task): task[0]
                        for task in tasks
                    }

                    with tqdm(
                        total=len(nef_files), desc="Converting NEF files", unit="file"
                    ) as pbar:
                        for future in as_completed(futures):
                            success, _ = future.result()
                            if success:
                                successful += 1
                            pbar.update(1)
            else:
                # Sequential processing
                for nef_file in tqdm(
                    nef_files, desc="Converting NEF files", unit="file"
                ):
                    output_file = output_dir / f"{nef_file.stem}.jpg"

                    if self.convert_nef_to_jpg(nef_file, output_file):
                        successful += 1

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Calculate statistics
            stats = {
                "total_time": elapsed_time,
                "time_per_file": elapsed_time / len(nef_files) if nef_files else 0,
                "files_per_second": len(nef_files) / elapsed_time if elapsed_time > 0 else 0,
            }

            logger.info(
                f"Conversion complete: {successful}/{len(nef_files)} "
                f"files converted in {elapsed_time:.2f}s"
            )

            # Open output directory
            if successful > 0:
                self._open_directory(output_dir)

            return successful, len(nef_files), stats

        except Exception as e:
            logger.error(f"Batch conversion failed: {e}")
            return 0, 0, {}

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
