"""
Watch Mode for NEF Converter

Monitors a directory for new NEF files and converts them automatically.
"""

import logging
import time
from pathlib import Path
from typing import Set

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from .converter import NEFConverter

logger = logging.getLogger(__name__)


class NEFWatchHandler(FileSystemEventHandler):
    """Handler for monitoring NEF file creation events."""

    def __init__(self, converter: NEFConverter, output_dir: Path) -> None:
        """
        Initialize the watch handler.

        Args:
            converter: NEFConverter instance to use for conversions
            output_dir: Directory to save converted files
        """
        self.converter = converter
        self.output_dir = output_dir
        self.processed_files: Set[str] = set()
        super().__init__()

    def on_created(self, event: FileSystemEvent) -> None:
        """
        Handle file creation events.

        Args:
            event: File system event
        """
        if event.is_directory:
            return

        file_path = Path(event.src_path)

        # Check if it's a NEF file
        if file_path.suffix.lower() not in [".nef"]:
            return

        # Avoid processing same file multiple times
        if str(file_path) in self.processed_files:
            return

        logger.info(f"New NEF file detected: {file_path.name}")

        # Wait a moment to ensure file is fully written
        time.sleep(1)

        try:
            output_path = self.output_dir / f"{file_path.stem}.jpg"
            success = self.converter.convert_nef_to_jpg(file_path, output_path)

            if success:
                self.processed_files.add(str(file_path))
                print(f"✅ Converted: {file_path.name} → {output_path.name}")
            else:
                print(f"❌ Failed to convert: {file_path.name}")

        except Exception as e:
            logger.error(f"Error converting {file_path}: {e}")
            print(f"❌ Error converting {file_path.name}: {e}")


def watch_directory(
    directory: str, converter: NEFConverter, output_dir: Path
) -> None:
    """
    Watch a directory for new NEF files and convert them automatically.

    Args:
        directory: Directory to watch
        converter: NEFConverter instance
        output_dir: Output directory for converted files
    """
    watch_path = Path(directory)

    if not watch_path.exists() or not watch_path.is_dir():
        raise ValueError(f"Invalid watch directory: {directory}")

    event_handler = NEFWatchHandler(converter, output_dir)
    observer = Observer()
    observer.schedule(event_handler, str(watch_path), recursive=False)

    observer.start()
    print(f"👁️  Watching: {watch_path}")
    print(f"📁 Output: {output_dir}")
    print("🔄 Waiting for new NEF files... (Press Ctrl+C to stop)")
    print()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping watch mode...")
        observer.stop()

    observer.join()
    print("✅ Watch mode stopped")
