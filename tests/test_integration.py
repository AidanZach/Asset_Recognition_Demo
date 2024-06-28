import unittest
from app import create_app
from app.ocr.ocr_service import extract_text
from app.ai.ai_service import interpret_text

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_end_to_end(self):
        with open('data/images/test_image.png', 'rb') as img:
            response = self.client.post('/upload', content_type='multipart/form-data', data={'image': img})
            self.assertEqual(response.status_code, 200)
            json_data = response.get_json()
            self.assertIn('extracted_text', json_data)
            self.assertIn('parsed_data', json_data)

if __name__ == '__main__':
    unittest.main()
