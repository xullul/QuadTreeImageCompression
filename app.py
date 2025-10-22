import os
import sys
from pathlib import Path
from quad_tree_compression import compress_image_file, reconstruct_image_from_file


def main():
    input_path: Path = Path('input')
    output_path: Path = Path('output')
    input_image = ''
    
    if len(sys.argv) == 2:
        input_image = sys.argv[1]
    else:
        print('no file_name defined, choose default image "plant.jpg"')
        input_image = Path('input/plant.jpg')
    
    output_file = f'{input_image.stem}.qid'
    output_file_path = output_path / output_file
    
    # Compress the image and encode is a binary file (any file extension can be chosen)
    compress_image_file(input_image, output_path / output_file, iterations=20_000)

    # Reconstruct the image from the binary file. (Returns a PIL.Image object)
    image = reconstruct_image_from_file(output_file_path)
    image.show()


if __name__ == '__main__':
    main()