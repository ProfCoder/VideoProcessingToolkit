# VideoProcessingToolkit

This repository contains Python scripts designed to process video files by trimming, extracting frames, and deleting frames systematically. The two main Jupyter notebooks, `cut_videos_1of3frames.ipynb` and `delete_1of3_frames.ipynb`, perform these operations efficiently on videos stored within specified folders.

## Table of Contents
- [Overview](#overview)
- [Notebooks](#notebooks)
  - [cut_videos_1of3frames.ipynb](#cut_videos_1of3framesipynb)
  - [delete_1of3_frames.ipynb](#delete_1of3_framesipynb)
- [Setup and Usage](#setup-and-usage)
- [Dependencies](#dependencies)

## Overview
This project focuses on:

- **Trimming Videos**: Cutting videos to specified start and end times.
- **Extracting Frames**: Capturing one-third of frames at random intervals from each video.
- **Deleting Frames**: Systematically removing every third frame in bulk.

## Notebooks

### `cut_videos_1of3frames.ipynb`
This notebook loads video file paths and trimming instructions from an Excel file and performs the following:

- **Trims Videos**: Cuts videos to designated segments based on start and end times.
- **Extracts Frames**: Captures random frames, equal to one-third of the total video duration, and saves them to the specified output folder.
- **Deletes Original Videos**: Optionally deletes original videos after processing.

**Note**: Update the path variables within the notebook to match the directory structure on your machine.

### `delete_1of3_frames.ipynb`
This notebook systematically removes every third frame in each subfolder of the specified parent directory by:

- **Listing and Sorting Frames**: Lists all frames in each folder and sorts them by frame number.
- **Deleting Frames**: Deletes every third frame based on their order in the sorted list.

**Note**: Update paths in code to match your directory structure.

## Setup and Usage
1. Clone this repository to your local machine.
2. Install the necessary dependencies (see below).
3. Open the notebooks in Jupyter or JupyterLab.
4. Update folder paths to match your local directory structure.
5. Run the scripts according to the instructions in each notebook.

## Dependencies
These scripts require the following Python libraries:
- `os` (for file and directory management)
- `re` (for regular expressions, used in filename processing)
- `random` (for random sampling of frames)
- `glob` (for file pattern matching)
- `cv2` (OpenCV, for video and image processing)
- `moviepy` (specifically `VideoFileClip` from `moviepy.video.io` for video trimming and frame extraction)
- `numpy` (for numerical operations)
- `pandas` (for data handling, especially Excel files)
- `tqdm` (for progress bars)

