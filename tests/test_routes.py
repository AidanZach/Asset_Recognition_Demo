import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload Asset Nameplate', response.data)

    def test_upload_image(self):
        with open('data/images/test_image.png', 'rb') as img:
            response = self.client.post('/upload', content_type='multipart/form-data', data={'image': img})
            self.assertEqual(response.status_code, 200)
            self.assertIn('extracted_text', response.json)
            self.assertIn('parsed_data', response.json)

if __name__ == '__main__':
    unittest.main()
