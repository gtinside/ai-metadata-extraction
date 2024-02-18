import unittest
from unittest.mock import Mock, patch
from util.extraction import ExtractionHelper
from assets.metadata import MayBeMetadata

class TestExtractionHelper(unittest.TestCase):
    @patch('util.extraction.instructor')
    def test_extract_metadata(self, mock_instructor):
        # Arrange
        mock_openai = Mock()
        mock_instructor.patch.return_value = mock_instructor
        mock_instructor.chat.completions.create.return_value = 'Test Metadata'
        extraction_helper = ExtractionHelper(mock_openai)

        # Act
        result = extraction_helper.extract_metadata('Test Text')

        # Assert
        mock_instructor.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            response_model=MayBeMetadata,
            messages=[
                {"role": "user", "content": 'Test Text'},
            ],
        )
        self.assertEqual(result, 'Test Metadata')

if __name__ == '__main__':
    unittest.main()