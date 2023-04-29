import os
import shutil

# ask the user for the path to the directory containing the files
path = input("Enter the path to the directory containing the files to be sorted: ")

# create a new directory to hold the sorted files
sorted_dir = os.path.join(path, "sorted_files")
if not os.path.exists(sorted_dir):
    os.mkdir(sorted_dir)

# loop through all files in the directory
for filename in os.listdir(path):
    # get the full path to the file
    filepath = os.path.join(path, filename)
    
    # check if it's a file and not a directory
    if os.path.isfile(filepath):
        # get the first 10 characters of the filename
        first_10_chars = filename[:10]
        
        # remove anything after "(" or "[" in the name of the folder
        foldername = filename.split("(")[0].split("[")[0].strip()
        
        # create a new directory for this type of file if it doesn't exist
        file_dir = os.path.join(sorted_dir, foldername)
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)
        
        # move the file into the appropriate directory
        new_filepath = os.path.join(file_dir, filename)
        shutil.move(filepath, new_filepath)

# show a message when the sorting is done
print("Sorting is done! The sorted files can be found in the 'sorted_files' directory.")
