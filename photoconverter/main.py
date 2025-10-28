"""
NEF to JPG Converter
A modern Python tool for converting Nikon NEF raw files to JPEG format.
"""

import glob
import logging
import os
import subprocess
import sys
import uuid
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory
from typing import List, Optional, Tuple

import imageio
import rawpy
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Platform-specific file browser
if sys.platform == "win32":
    FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR', 'C:\\Windows'), 'explorer.exe')
elif sys.platform == "darwin":
    FILEBROWSER_PATH = "open"
else:
    FILEBROWSER_PATH = "xdg-open"


class NEFConverter:
    """Modern NEF to JPG converter with improved error handling and progress tracking."""
    
    def __init__(self, quality: int = 95, output_format: str = 'JPEG') -> None:
        """
        Initialize the NEF converter.
        
        Args:
            quality: JPEG quality (1-100)
            output_format: Output format (default: JPEG)
        """
        self.quality = quality
        self.output_format = output_format
        logger.info(f"Initialized NEF Converter with quality={quality}, format={output_format}")
    
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
        nef_files = []
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
                imageio.imwrite(
                    str(output_path), 
                    rgb, 
                    quality=self.quality
                )
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
                
            logger.info(f"Conversion complete: {successful}/{len(nef_files)} files converted")
            
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
                subprocess.run([FILEBROWSER_PATH, str(directory)], check=False)
            else:
                subprocess.run([FILEBROWSER_PATH, str(directory)], check=False)
        except Exception as e:
            logger.warning(f"Could not open directory {directory}: {e}")


def select_directory() -> Optional[str]:
    """
    Open a directory selection dialog.
    
    Returns:
        Selected directory path or None if cancelled
    """
    root = Tk()
    root.withdraw()  # Hide the main window
    
    directory = askdirectory(
        title='Select your Folder with .NEF Files to convert them'
    )
    
    root.destroy()
    return directory if directory else None


def main() -> None:
    """Main entry point for the NEF to JPG converter."""
    print('=' * 50)
    print('🔄 NEF-to-JPG Converter V2.0')
    print('=' * 50)
    print()
    
    try:
        # Select directory
        directory = select_directory()
        
        if not directory:
            logger.info('No directory selected. Exiting...')
            return
        
        # Initialize converter
        converter = NEFConverter(quality=95)
        
        # Convert files
        successful, total = converter.convert_batch(directory)
        
        # Show results
        print()
        print(f'✅ Conversion completed!')
        print(f'📊 Successfully converted: {successful}/{total} files')
        
        if successful == 0:
            print('❌ No files were converted. Please check the logs.')
        elif successful < total:
            print('⚠️ Some files failed to convert. Check the logs for details.')
        else:
            print('🎉 All files converted successfully!')
            
    except KeyboardInterrupt:
        logger.info('Conversion cancelled by user')
        print('\n❌ Conversion cancelled by user')
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        print(f'\n❌ An error occurred: {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
