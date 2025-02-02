import unittest
from app import app  

class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a test client before running tests"""
        cls.client = app.test_client()

    def test_homepage(self):
        """Test if the homepage loads correctly"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome", response.data)  # Modify according to your homepage content

    def test_about_page(self):
        """Test if the about page loads correctly"""
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Us", response.data)  # Modify according to your about page content

    def test_404_page(self):
        """Test if a non-existing page returns a 404 status"""
        response = self.client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()

