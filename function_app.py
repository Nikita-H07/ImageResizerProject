import azure.functions as func
from PIL import Image
import io
import logging

# You can change the resize dimensions here
RESIZE_WIDTH = 200
RESIZE_HEIGHT = 200

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", 
                  path="input-container/{name}",   # Input container name
                  connection="AzureWebJobsStorage")
@app.blob_output(arg_name="outputblob", 
                 path="output-container/{name}",  # Output container name
                 connection="AzureWebJobsStorage")
def ImageResizeFunction(myblob: func.InputStream, outputblob: func.Out[func.InputStream]):
    logging.info(f"Python blob trigger function processed blob\n"
                 f"Name: {myblob.name}\n"
                 f"Size: {myblob.length} bytes")

    try:
        # Read image data from blob
        image_data = myblob.read()
        image = Image.open(io.BytesIO(image_data))

        # Resize image
        resized_image = image.resize((RESIZE_WIDTH, RESIZE_HEIGHT))

        # Save resized image to bytes buffer
        output_buffer = io.BytesIO()
        resized_image.save(output_buffer, format=image.format)
        output_buffer.seek(0)

        # Write resized image back to output blob
        outputblob.set(output_buffer.read())

        logging.info(f"Resized image saved to output container: output-container/{myblob.name}")

    except Exception as e:
        logging.error(f"Error processing blob {myblob.name}: {e}")
        raise
