from flask import Blueprint, request, jsonify, render_template
from .ai.ai_service import interpret_image

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_image():
    try:
        file = request.files['image']
        print(f"Received file: {file.filename}")
        file_path = f"./data/images/{file.filename}"
        file.save(file_path)
        print(f"Saved file to: {file_path}")
        
        result = interpret_image(file_path)
        print(f"Interpretation result: {result}")
        
        response = {
            "parsed_data": result
        }
        return jsonify(response)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500
