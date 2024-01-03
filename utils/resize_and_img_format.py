from PIL import Image
import os
import sys


def resize_images(input_dir, output_dir, new_size):
    # loop through all files in the directory
    for file_name in os.listdir(input_dir):
        # check if the file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            # open the image file and resize it
            with Image.open(os.path.join(input_dir, file_name)) as img:
                img = img.resize(new_size)
                # save the resized image with a new file name
                new_file_name = "resized_" + file_name
                if img.mode == 'P':
                    img = img.convert('RGB')
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(os.path.join(output_dir, new_file_name))


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print(
            "Usage: python script.py <input_directory> <output_directory> <width> <height>")
        sys.exit(1)

    # Parse command-line arguments
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    new_size = (width, height)

    # Check if the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Resize images
    resize_images(input_dir, output_dir, new_size)
    print("Images resized successfully.")
