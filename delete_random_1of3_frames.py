import os
import random

def remove_random_third_of_files(folder_path, file_extensions=(".png")):
    # List all files in the directory
    files_in_directory = [file for file in os.listdir(folder_path) 
                          if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith(file_extensions)]

    # Calculate the number of files to delete (1/3 of total)
    count_to_remove = len(files_in_directory) // 3

    # Randomly select files to delete
    files_to_remove = random.sample(files_in_directory, count_to_remove)

    # Delete the selected files
    for file_name in files_to_remove:
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"Deleted file: {file_path}")

    print(f"Deleted {count_to_remove} files from '{folder_path}'.")

if __name__ == "__main__":
    # Define the path to the directory containing extracted files
    folder_path = "/Users/almazbaghirova/Desktop/Hiwi/VideoCut/cut_videos/0708_001_PM3_GCP1_AD_DJI_0404"  
    remove_random_third_of_files(folder_path)


# import os
# import random

# def remove_random_third_of_files_in_subfolders(parent_folder_path, file_extensions=(".png")):
#     # Loop through each subdirectory in the parent folder
#     for subfolder_name in os.listdir(parent_folder_path):
#         subfolder_path = os.path.join(parent_folder_path, subfolder_name)

#         # Ensure that we are working with a directory
#         if os.path.isdir(subfolder_path):
#             # List all files in the current subdirectory
#             files_in_directory = [file for file in os.listdir(subfolder_path) 
#                                   if os.path.isfile(os.path.join(subfolder_path, file)) and file.lower().endswith(file_extensions)]

#             # Calculate the number of files to delete (1/3 of total)
#             count_to_remove = len(files_in_directory) // 3

#             # Randomly select files to delete
#             files_to_remove = random.sample(files_in_directory, count_to_remove)

#             # Delete the selected files
#             for file_name in files_to_remove:
#                 file_path = os.path.join(subfolder_path, file_name)
#                 os.remove(file_path)
#                 print(f"Deleted file: {file_path}")

#             print(f"Deleted {count_to_remove} files from '{subfolder_path}'.")

# if __name__ == "__main__":
#     # Define the path to the parent directory containing all subdirectories
#     parent_folder_path = "/Users/almazbaghirova/Desktop/Hiwi/VideoCut/cut_videos"  
#     remove_random_third_of_files_in_subfolders(parent_folder_path)
