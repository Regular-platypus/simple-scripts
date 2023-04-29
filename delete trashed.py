#delete trashed files on my server
import os

directory = '~/.server/komga/all'

for filename in os.listdir(directory):
    if '.trashed' in filename:
        os.remove(os.path.join(directory, filename))
