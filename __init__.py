import logging
import azure.functions as func
from PIL import Image
import io

def main(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}, Size: {myblob.length} bytes")

    try:
        # Read blob image data
        img_data = myblob.read()
        image = Image.open(io.BytesIO(img_data))

        # Perform your resizing or processing here
        image = image.resize((100, 100))  # example resize

        # Save or upload the processed image to blob storage
        # (you need to implement the upload code or use output binding)
        
        logging.info("Image processed successfully.")
    except Exception as e:
        logging.error(f"Error processing image: {e}")

