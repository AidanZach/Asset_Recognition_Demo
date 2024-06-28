import openai
import os

# Instantiate the OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpret_text(extracted_text):
    prompt = f"""
    The data extracted from the nameplate is as follows:

    {extracted_text}

    Please output the data in the following JSON format:
    {{
        "manufacturer": "value",
        "model": "value",
        "serial_number": "value",
        "year": "value"
    }}

    If a field is not present in the extracted data, set its value to an empty string. Ensure the JSON is properly formatted and include any additional relevant information you can identify.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a highly intelligent AI tasked with extracting and categorizing information from industrial asset nameplate data. "},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the content of the AI's response
    return response.choices[0].message.content