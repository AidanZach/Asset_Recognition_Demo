from flask import Blueprint, request, jsonify, render_template
from .ocr.ocr_service import extract_text
from .ai.ai_service import interpret_text

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['image']
    file_path = f"./data/images/{file.filename}"
    file.save(file_path)
    
    extracted_text = extract_text(file_path)
    parsed_data = interpret_text(extracted_text)
    
    response = {
        "extracted_text": extracted_text,
        "parsed_data": parsed_data
    }
    return jsonify(response)
