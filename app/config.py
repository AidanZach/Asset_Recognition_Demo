import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    OCR_API_KEY = os.environ.get('OCR_API_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
