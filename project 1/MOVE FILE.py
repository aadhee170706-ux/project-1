import os
import shutil

source_folder = r"D:\Aadheeswer\Aadheeswer\D-1\Source"
destination_folder = r"D:\Aadheeswer\Aadheeswer\D-2\JPG_Files"

os.makedirs(destination_folder, exist_ok=True)

for file_name in os.listdir(source_folder):
    
    if file_name.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, file_name)
        dst_path = os.path.join(destination_folder, file_name)

        shutil.move(src_path, dst_path)
        print(f"Moved: {file_name}")

print("Done!")
