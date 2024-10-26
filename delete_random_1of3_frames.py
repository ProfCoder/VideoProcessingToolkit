import os
import random

def delete_random_1of3_frames(folder_path, frame_extensions=(".png")):
    """
    Deletes 1/3 of frames in the specified folder at random.

    Parameters:
    - folder_path (str): Path to the folder containing frames to be deleted.
    """

    # List all files in the folder (assuming frames are individual files like .png or .jpg)
    frames = [f for f in os.listdir(folder_path) 
              if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(frame_extensions)]

    # Calculate number of frames to delete (1/3 of total frames)
    num_frames_to_delete = len(frames) // 3

    # Randomly select frames to delete
    frames_to_delete = random.sample(frames, num_frames_to_delete)

    # Delete the selected frames
    for frame in frames_to_delete:
        frame_path = os.path.join(folder_path, frame)
        os.remove(frame_path)
        print(f"Deleted frame: {frame_path}")

    print(f"Deleted {num_frames_to_delete} frames from '{folder_path}'.")

# Example usage
if __name__ == "__main__":
    # Define the path to the folder containing extracted frames
    folder_path = "/Users/almazbaghirova/Desktop/Hiwi/VideoCut/cut_videos/0708_001_PM3_GCP1_AD_DJI_0404"  
    delete_random_1of3_frames(folder_path)
