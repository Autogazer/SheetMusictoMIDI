from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_tiff(pdf_path, output_path):
    # Convert PDF to list of PIL Image objects
    images = convert_from_path(pdf_path)
    
    for i, image in enumerate(images):
        # Save each image as TIFF
        image.save(f"{output_path}_page_{i+1}.tiff", "TIFF")

# Example usage

pdf_path = os.getcwd() + "/pdfs/test1.pdf"  # Replace with your PDF file path

output_path = os.getcwd() + "/tiffs/"    # Replace with your desired output path

pdf_to_tiff(pdf_path, output_path)