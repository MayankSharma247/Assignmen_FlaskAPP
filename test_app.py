import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Enhanced Flask App", response.data)

    def test_greet(self):
        response = self.client.get("/greet/John")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, John!", response.data)

    def test_api_data(self):
        response = self.client.get("/api/data")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask App", response.data)

if __name__ == "__main__":
    unittest.main()

