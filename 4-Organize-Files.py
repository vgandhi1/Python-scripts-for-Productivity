import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        ext = filename.split('.')[-1]
        ext_folder = os.path.join(folder_path, ext.upper())
        os.makedirs(ext_folder, exist_ok=True)
        shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))

organize_files("/path/to/your/folder")