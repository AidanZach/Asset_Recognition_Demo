from paddleocr import PaddleOCR

def extract_text(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # Initialize the PaddleOCR model
    result = ocr.ocr(image_path, cls=True)  # Perform OCR on the image

    # Extract the text from the OCR result
    text = "\n".join([line[1][0] for line in result[0]])
    return text
