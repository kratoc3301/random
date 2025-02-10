import os
import re

# Get the location of the targets
path = "/media/panagiotis/HDD/BU/Videos/Ταινιες"

# Get a list of the folders
folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

# Clean the folder names
cleaned_names = []
for folder in folders:
    # Remove everything inside () or [] including the brackets themselves and any spaces
    folder = re.sub(r"[\[\(].*?[\]\)]", "", folder)
    folder = re.sub(r"\s+", " ", folder).strip()
    cleaned_names.append(folder)

# Rename each folder
for folder, cleaned_name in zip(folders, cleaned_names):
    path_old = os.path.join(path, folder)  # Original folder path
    path_new = os.path.join(path, cleaned_name)  # New folder path

    os.rename(path_old, path_new)
    print(f"Cleaned: {path_old} -> {path_new}")
