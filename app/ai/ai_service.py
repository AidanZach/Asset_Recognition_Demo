import openai
import os
import base64
import requests
import json

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def interpret_image(image_path):
    try:
        base64_image = encode_image(image_path)

        prompt = """
        Extract and categorize all information from the industrial asset nameplate in the image. Provide the data in the following JSON format:
        {
            "manufacturer": "value",
            "model_string": "value",
            "serial_number": "value",
            "year": "value",
            "additional_info": {
                "field_name": "value",
                ...
            },
            "asset_type_description": "value"
        }
        If a field is not present in the extracted data, set its value to an empty string. Ensure the JSON is properly formatted and include any additional relevant information you can identify. Internally use critical step-by-step reasoning to determine the asset type description. ONLY OUTPUT THE JSON FORMATTED INFORMATION.
        """

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a highly intelligent AI tasked with extracting and categorizing information from industrial asset nameplate data."
                },
                {"role": "user", "content": prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Here is the image for analysis:"},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ],
            "max_tokens": 500
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_json = response.json()

        # Extract JSON content from the model's response
        model_response = response_json.get("choices", [])[0].get("message", {}).get("content", "")
        json_start = model_response.find('{')
        json_end = model_response.rfind('}') + 1
        json_content = model_response[json_start:json_end]

        return json.loads(json_content)
    except Exception as e:
        print(f"Error in interpret_image: {str(e)}")
        return {"error": str(e)}