import os
from PIL import Image

input_folder = "images"
output_folder = "resized"

resize_width = 200
resize_height = 200

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            resized_img = img.resize((resize_width, resize_height))
            resized_img.save(output_path)

        print(f"Resized and saved: {output_path}")
