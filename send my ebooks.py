#send my ebooks to my komga server
import os
import paramiko

# SSH connection parameters
hostname = '192.168.29.100'
username = ''
password = ''
port = 22

source_dir = '~/downloads'


dest_dir = '~/.server/komga/all'

# Connect via SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=hostname, username=username, password=password, port=port)

# List files 
files_to_move = [f for f in os.listdir(source_dir) if f.endswith(('.epub', '.pdf'))]

# Move files
for filename in files_to_move:
    foldername = os.path.splitext(filename)[0]  
    sftp_client = ssh_client.open_sftp()
    sftp_client.mkdir(os.path.join(dest_dir, foldername))  # Create folder
    sftp_client.put(os.path.join(source_dir, filename), os.path.join(dest_dir, foldername, filename))  # Transfer file to folder 
    sftp_client.close()

# Close SSH connection
ssh_client.close()