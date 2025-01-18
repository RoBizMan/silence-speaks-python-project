import sys
import os
import unittest
from app import create_app

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.client.get('/echo')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertIn("message", json_data)
        self.assertIn("timestamp", json_data)
        self.assertEqual(
            json_data["message"], "Send a POST request with a message."
        )


if __name__ == '__main__':
    unittest.main()
