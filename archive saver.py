#python script to move files with extention zip,rar,7zip and delete rest
import os
import shutil

folder_path = input("Enter the path to the folder you want to scan: ")

archive_path = os.path.join(folder_path, "archive")

if not os.path.exists(archive_path):
    os.makedirs(archive_path)

files = os.listdir(folder_path)

for file in files:
    if file.endswith(("zip", "rar", "7z")):
        
        file_path = os.path.join(folder_path, file)
        
        shutil.move(file_path, archive_path)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
