import PIL as pil
from PIL import Image, ImageEnhance
import numpy as np

# original 480 × 360
RESOLUTION = (1920, 1080)
SOURCE_IMAGES_DIR = "frames"
OUTPUT_IMAGES_DIR = "processed_frames"
MAX_THREADS = 1

def process_frame(file_path, output_path):
    # Load the frame
    frame = Image.open(file_path)
    # Resize the frame to 224x224 pixels
    frame = frame.resize(RESOLUTION, resample=Image.BOX)
    # Convert the frame to a NumPy array
    frame = np.array(frame)
    # to 2 colors black and white
    for pixel in frame:
        for i in range(len(pixel)):
            avg = sum(pixel[i]) / len(pixel[i])
            if avg > 127:
                pixel[i] = [255, 255, 255]
            else:
                pixel[i] = [0, 0, 0]

    # save the frame
    frame = Image.fromarray(frame)
    frame.save(output_path)

import threading
import os
import time

from alive_progress import alive_bar

with alive_bar(len(os.listdir(SOURCE_IMAGES_DIR))) as bar:
    for image in os.listdir(SOURCE_IMAGES_DIR):
        while threading.active_count() > MAX_THREADS + 1:
            time.sleep(0.05)
            #print(f"threads: {threading.active_count()}")
        else:
            threading.Thread(target=process_frame, args=(f"{SOURCE_IMAGES_DIR}/{image}", f"{OUTPUT_IMAGES_DIR}/{image}")).start()
            bar()


while threading.active_count() > 1:
    time.sleep(0.05)
    pass

# frame = process_frame("frames/frame-105.png")
# # show
# Image.fromarray(frame).show()
