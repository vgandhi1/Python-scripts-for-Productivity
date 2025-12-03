import os
import shutil

# ====== CONFIG =======
ROOT = ""   # change this
KEEP_FORMAT = "heic"            # "heic" or "jpeg"
DUP_DIR = os.path.join(ROOT, "duplicates")
# ======================

os.makedirs(DUP_DIR, exist_ok=True)

# Normalize known extensions
JPEG_EXTS = {".jpg", ".jpeg"}
HEIC_EXTS = {".heic"}

files_map = {}

# Scan folder
for file in os.listdir(ROOT):
    full = os.path.join(ROOT, file)
    if not os.path.isfile(full):
        continue
    
    name, ext = os.path.splitext(file.lower())
    
    if ext in JPEG_EXTS or ext in HEIC_EXTS:
        if name not in files_map:
            files_map[name] = []
        files_map[name].append(file)

# Detect duplicates and move
for base, variants in files_map.items():
    if len(variants) < 2:
        continue  # no duplicates

    has_jpeg = any(v.lower().endswith(tuple(JPEG_EXTS)) for v in variants)
    has_heic = any(v.lower().endswith(tuple(HEIC_EXTS)) for v in variants)

    # Only process jpeg+heic pairs
    if not (has_jpeg and has_heic):
        continue

    print(f"Duplicate set found: {variants}")

    # Determine which to keep
    keep_file = None
    remove_file = None

    if KEEP_FORMAT == "heic":
        keep_file = next(v for v in variants if v.lower().endswith(".heic"))
        remove_file = next(v for v in variants if v.lower().endswith(tuple(JPEG_EXTS)))
    else:
        keep_file = next(v for v in variants if v.lower().endswith(tuple(JPEG_EXTS)))
        remove_file = next(v for v in variants if v.lower().endswith(".heic"))

    print(f"Keeping:   {keep_file}")
    print(f"Removing:  {remove_file}")

    # Move duplicate to duplicates/
    shutil.move(
        os.path.join(ROOT, remove_file),
        os.path.join(DUP_DIR, remove_file)
    )

print("\nDone! Check the 'duplicates' folder.")

