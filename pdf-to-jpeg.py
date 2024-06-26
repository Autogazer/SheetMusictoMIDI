from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_jpeg(pdf_path, output_path):
    # Convert PDF to list of PIL Image objects
    images = convert_from_path(pdf_path)
    
    for i, image in enumerate(images):
        # Save each image as JPEG
        image.save(f"{output_path}_page_{i+1}.jpeg", "JPEG")

# Example usage

pdf_path = os.getcwd() + "/pdfs/pedal_power_mondo_manual.pdf"  # Replace with your PDF file path

output_path = os.getcwd() + "/jpegs/"    # Replace with your desired output path

pdf_to_jpeg(pdf_path, output_path)