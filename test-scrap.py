import unittest
from unittest.mock import MagicMock
from app.main import scrape
from unittest.mock import patch
class TestScrape(unittest.TestCase):

    def test_scrape(self):
        # Set up a mock response from the get_posts function
        mock_response = [
            {'text': 'post 1', 'time': '2022-02-01T12:00:00', 'video': False, 'likes': 10, 'comments': 5, 'shares': 2},
            {'text': 'post 2', 'time': '2022-02-02T12:00:00', 'video': True, 'likes': 20, 'comments': 3, 'shares': 1},
            {'text': 'post 3', 'time': '2022-02-03T12:00:00', 'video': False, 'likes': 15, 'comments': 2, 'shares': 0}
        ]
        # Set up a mock collection object
        mock_collection = MagicMock()
        mock_collection.insert_one.side_effect = [None, None, None]

        # Call the scrape function with the mock response and collection object
        with patch('app.get_posts', return_value=mock_response):
            with patch('my_module.collection', mock_collection):
                result = scrape()

        # Check that the mock collection object was called with the correct data
        mock_collection.insert_one.assert_any_call({'text': 'post 1', 'time': '2022-02-01T12:00:00', 'video': False, 'likes': 10, 'comments': 5, 'shares': 2})
        mock_collection.insert_one.assert_any_call({'text': 'post 2', 'time': '2022-02-02T12:00:00', 'video': True, 'likes': 20, 'comments': 3, 'shares': 1})
        mock_collection.insert_one.assert_any_call({'text': 'post 3', 'time': '2022-02-03T12:00:00', 'video': False, 'likes': 15, 'comments': 2, 'shares': 0})

        # Check that the function returns the expected message
        self.assertEqual(result, {"message": "Scrapping done!"})
