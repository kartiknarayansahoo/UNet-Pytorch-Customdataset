from PIL import Image
import os
import sys
import numpy as np
from tqdm import tqdm


def binarize_images(input_dir, output_dir):
    # Get the total number of files for the progress bar
    total_files = len([f for f in os.listdir(input_dir)
                      if f.endswith((".jpg", ".jpeg", ".png"))])

    # loop through all files in the directory with tqdm
    for file_name in tqdm(os.listdir(input_dir), total=total_files, desc="Binarizing images"):
        # check if the file is an image
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            # open the image file and binarize it
            with Image.open(os.path.join(input_dir, file_name)) as img:
                # Convert Image to Numpy as array
                img_array = np.array(img)
                # print(img_array.shape)
                # Put threshold to make it binary
                binarr = img_array
                binarr[binarr >= 128] = 255
                binarr[binarr < 128] = 0
                # Convert numpy array back to image
                binimg = Image.fromarray(binarr.astype(np.uint8))
                new_file_name = file_name
                binimg.save(os.path.join(output_dir, new_file_name))


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python convert_to_binary.py <input_directory> <output_directory>")
        sys.exit(1)

    # Parse command-line arguments
    script_path = sys.argv[0]
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

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

    # Binarize images with progress bar
    binarize_images(input_dir, output_dir)
    print("Images binarized successfully.")
