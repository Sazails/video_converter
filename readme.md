# Video Converter

## Overview

This program converts a selected `.mkv` video file to `.mp4` format using either NVIDIA GPU decoding and encoding or AMD encoder/decoder. It utilizes the `moviepy` library for video processing and multiprocessing to optimize performance.

## Usage

The program prompts the user to select a `.mkv` file using a file explorer, and then converts the selected file to `.mp4` format. If the conversion fails using NVIDIA GPU decoding and encoding, it falls back to using AMD encoder/decoder.

## Output

The program provides verbose information during the conversion process and prints the input and output file paths upon completion.
