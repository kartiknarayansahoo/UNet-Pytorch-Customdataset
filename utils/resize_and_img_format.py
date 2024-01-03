from PIL import Image
import os
import sys
from tqdm import tqdm


def resize_images(input_dir, output_dir, new_size):
    # Get the total number of files for the progress bar
    total_files = len([f for f in os.listdir(input_dir)
                      if f.endswith((".jpg", ".jpeg", ".png"))])

    # loop through all files in the directory with tqdm
    for file_name in tqdm(os.listdir(input_dir), total=total_files, desc="Resizing images"):
        # check if the file is an image
        if file_name.endswith((".jpg", ".jpeg", ".png")):
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
    if len(sys.argv) != 5:
        print("Usage: python resize_and_img_format.py <input_directory> <output_directory> <width> <height>")
        sys.exit(1)

    # Parse command-line arguments
    script_path = sys.argv[0]
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    new_size = (width, height)

    # Check if the script path is valid
    if not os.path.exists(script_path):
        print(f"Error: Script path '{script_path}' does not exist.")
        sys.exit(1)

    # Check if the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)

    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Resize images with progress bar
    resize_images(input_dir, output_dir, new_size)
    print("Images resized successfully.")
