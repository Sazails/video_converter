import os
from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip
import multiprocessing

# Function to convert .mkv to .mp4 using NVIDIA GPU decoding and encoding
def convert_to_mp4(input_path):
    # Get the input file name and directory
    input_dir, input_filename = os.path.split(input_path)
    input_name, _ = os.path.splitext(input_filename)

    # Set the output file path
    output_path = os.path.join(input_dir, f"{input_name}.mp4")

    # Print verbose information
    print(f"Converting {input_path} to {output_path}")

    # Get the total available threads
    total_threads = multiprocessing.cpu_count()
    threads = total_threads // 2
    print(f"Using {threads} threads.")

    # Convert the video file using the appropriate GPU decoding and encoding
    try:
        video = VideoFileClip(input_path)
        video.write_videofile(output_path, codec="nvenc", verbose=True, threads=threads)
    except Exception as e:
        print(f"Error using NVIDIA GPU decoding and encoding: {e}")
        try:
            video = VideoFileClip(input_path)
            video.write_videofile(output_path, codec="amd", verbose=True, threads=threads)
        except Exception as e:
            print(f"Error using AMD encoder/decoder: {e}")
            video = VideoFileClip(input_path)
            video.write_videofile(output_path, verbose=True, threads=threads)

    # Print verbose information
    print("Conversion completed!")
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")

# Open file explorer to select the input file
Tk().withdraw()
input_path = filedialog.askopenfilename(title="Select .mkv video file")

# Check if a file was selected
if input_path:
    # Convert the selected file to .mp4
    convert_to_mp4(input_path)
else:
    print("No file selected.")
