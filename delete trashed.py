import os

directory = '~/.server/komga/all'

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the filename contains ".trashed"
    if '.trashed' in filename:
        # If it does, delete the file
        os.remove(os.path.join(directory, filename))
