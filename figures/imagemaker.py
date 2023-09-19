from PIL import Image
import os

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    print(f"The original image size is {original_image.size[0]} wide x {original_image.size[1]} tall")

    resized_image = original_image.resize(size)
    print(f"The resized image size is {resized_image.size[0]} wide x {resized_image.size[1]} tall")
    resized_image.save(output_image_path)

def grayscale_image(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    gray_scale = color_image.convert('L')
    gray_scale.save(output_image_path)

# specify your image path here
name = "map"
extension = "jpg"
image_path = f"figures/{name}/{name}.{extension}"

# list of widths
widths = [1000, 500, 100]

for width in widths:
    output_path = f"{''.join(image_path.split('.')[:-1])}_{width}.jpeg"
    # open the image file
    with Image.open(image_path) as img:
        # fetch image dimensions
        w, h = img.size
        # calculate the height for the given width to maintain aspect ratio
        height = int(h * width / w)
        # call the resize function
        resize_image(image_path, output_path, (width, height))

output_path = f"{''.join(image_path.split('.')[:-1])}_grayscale.jpeg"
grayscale_image(image_path, output_path)

os.remove(image_path)