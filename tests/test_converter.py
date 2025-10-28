"""
Tests for NEF Converter

Basic test structure for the NEF converter functionality.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.nef_converter.converter import NEFConverter


class TestNEFConverter:
    """Test cases for the NEFConverter class."""

    def test_init(self):
        """Test converter initialization."""
        converter = NEFConverter(quality=90)
        assert converter.quality == 90
        assert converter.output_format == "JPEG"

    def test_init_with_custom_format(self):
        """Test converter initialization with custom format."""
        converter = NEFConverter(quality=85, output_format="PNG")
        assert converter.quality == 85
        assert converter.output_format == "PNG"

    def test_get_nef_files_nonexistent_directory(self):
        """Test error handling for nonexistent directory."""
        converter = NEFConverter()
        nonexistent_path = Path("/nonexistent/directory")

        with pytest.raises(ValueError, match="Directory does not exist"):
            converter.get_nef_files(nonexistent_path)

    @patch("src.nef_converter.converter.Image")
    @patch("src.nef_converter.converter.rawpy")
    def test_convert_nef_to_jpg_success(self, mock_rawpy, mock_image):
        """Test successful NEF to JPG conversion."""
        # Setup mocks
        mock_raw = MagicMock()
        mock_rgb_data = MagicMock()
        mock_raw.postprocess.return_value = mock_rgb_data
        mock_rawpy.imread.return_value.__enter__.return_value = mock_raw

        mock_img = MagicMock()
        mock_image.fromarray.return_value = mock_img

        converter = NEFConverter(quality=95, preserve_exif=False)
        result = converter.convert_nef_to_jpg(Path("test.nef"), Path("test.jpg"))

        assert result is True
        mock_rawpy.imread.assert_called_once_with("test.nef")
        mock_raw.postprocess.assert_called_once()
        mock_image.fromarray.assert_called_once()
        mock_img.save.assert_called_once()

    @patch("src.nef_converter.converter.rawpy")
    def test_convert_nef_to_jpg_failure(self, mock_rawpy):
        """Test failed NEF to JPG conversion."""
        # Setup mock to raise exception
        mock_rawpy.imread.side_effect = Exception("Mock error")

        converter = NEFConverter()
        result = converter.convert_nef_to_jpg(Path("test.nef"), Path("test.jpg"))

        assert result is False


if __name__ == "__main__":
    pytest.main([__file__])
