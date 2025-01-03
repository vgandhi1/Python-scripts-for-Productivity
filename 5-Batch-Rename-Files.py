import os

def rename_files(folder_path, prefix):
    for count, filename in enumerate(os.listdir(folder_path)):
        ext = filename.split('.')[-1]
        new_name = f"{prefix}_{count}.{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))

rename_files(r"/path/to/your/folder", "Document")
