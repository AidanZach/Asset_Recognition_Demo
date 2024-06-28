Setup Instructions
Prerequisites
Python 3.11 or higher
Git
Clone the Repository
git clone https://github.com/AidanZach/Asset_Recognition_Demo.git
cd Asset_Recognition_Demo

Setting Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Run the following commands to create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install Dependencies
Install the required dependencies using pip:

pip install -r requirements.txt

Environment Variables
Create a .env file in the root directory of the project and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key

You can use the .env.example file as a template.

Running the Application
To start the Flask application, run:

flask --app run.py run

Usage
Open your web browser and go to http://127.0.0.1:5000.
Upload an image of an industrial asset nameplate.
View the extracted text and JSON output.
Project Structure
Asset_Recognition_Demo/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── config.py
│ ├── models.py
│ ├── routes.py
│ ├── utils.py
│ ├── ocr/
│ │ ├── init.py
│ │ ├── ocr_service.py
│ │ └── tests/
│ │ ├── init.py
│ │ ├── test_ocr_service.py
│ ├── ai/
│ │ ├── init.py
│ │ ├── ai_service.py
│ │ └── tests/
│ │ ├── init.py
│ │ ├── test_ai_service.py
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── js/
│ │ └── script.js
│ ├── templates/
│ │ └── index.html
├── tests/
│ ├── init.py
│ ├── test_routes.py
│ └── test_integration.py
├── data/
│ └── images/
├── requirements.txt
├── README.md
└── run.py

Notes
Ensure that the data/images/ directory exists before uploading images.
For any issues, please refer to the error logs in the terminal.
