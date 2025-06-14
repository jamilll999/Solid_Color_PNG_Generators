import png
import numpy as np
import multiprocessing as mp
import random
import os

# set the width and height of PNGS
width, height = 30000, 10000  
chunk_size = 100  # generate 100 rows per chunk
num_chunks = height // chunk_size  

# output folder path
output_folder = "generated_pngs"

# creat out folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

def generate_chunk(args):
    #genereate chunk_size rows pure color pixel data
    color, _ = args  
    row = np.tile(color, width)  # create a color value for each pixel
    row = row.astype(np.uint8).tobytes()  # transform the format
    return [row] * chunk_size  

def generate_color_image(color, file_name):
    #generate a specified solid-color PNG file
    with open(file_name, "wb") as f:
        writer = png.Writer(width, height, greyscale=False)
        with mp.Pool(mp.cpu_count()) as pool:
            
            rows = pool.imap(generate_chunk, [(color, i) for i in range(num_chunks)])  
            writer.write(f, (row for chunk in rows for row in chunk)) 

def generate_random_color():
    #generate a random color
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

if __name__ == "__main__":
    # generate 100 random color png files
    for i in range(100):
        color = generate_random_color()  
        file_name = os.path.join(output_folder, f"pure_color_{i+1}.png") 
        generate_color_image(color, file_name)  
        print("Generated and saved %d solid color PNG file(s)" % (i+1))

    print(f"100 solid color PNG files have been generated and saved to the folder: {output_folder}")
