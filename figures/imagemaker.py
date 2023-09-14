from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f"The original image size is {width} wide x {height} tall")

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f"The resized image size is {width} wide x {height} tall")
    resized_image.show()
    resized_image.save(output_image_path)

# specify your image path here
image_path = "figures/sun/1024283.jpg"

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