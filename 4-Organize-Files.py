import os
import shutil

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        # 1. Full path of the item
        item_path = os.path.join(folder_path, filename)

        # 2. Skip if it's a directory (or the script itself)
        if os.path.isdir(item_path):
            continue

        # 3. Determine the extension
        if '.' in filename:
            # For files with an extension (e.g., 'document.pdf' -> 'PDF')
            ext = filename.split('.')[-1]
            if len(ext) > 5: # Added to prevent very long strings from becoming folders
                ext = "OTHER_FILES"
        else:
            # For files without an extension (e.g., 'README')
            ext = "NO_EXTENSION"
        
        # 4. Create the destination folder path
        ext_folder = os.path.join(folder_path, ext.upper())
        
        # 5. Create the folder (exist_ok=True is correct here)
        os.makedirs(ext_folder, exist_ok=True)
        
        # 6. Move the file
        shutil.move(item_path, os.path.join(ext_folder, filename))

# Example usage (uncommented):
# organize_files(r"C:\Users\vinaygandhi\Downloads")
organize_files(r"/path/to/your/folder")
