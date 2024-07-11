#!/usr/bin/python3
""""
A Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy.
"""
from fabric.api import *
import os

# Define your web server IP addresses
env.hosts = ['35.175.102.190', '3.89.146.68']
# Define the username used for SSH access
env.user = 'ubuntu'
# Define the path to your SSH private key file
env.key_filename = '/home/ahmed/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers, performs deployment steps.

    This function uploads the specified archive to the /tmp/ directory
    of each web server, uncompresses it to /data/web_static/releases/,
    deletes the archive, updates the symbolic link /data/web_static/current
    to the new version, and handles all operations on both web servers.

    Args:
    archive_path (str): The local path to the archive file to deploy.

    Returns:
    bool: True if all operations were successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        print(f"Error: Archive file '{archive_path}' not found.")
        return False

    try:
        # Upload archive to /tmp/ directory on each web server
        remote_archive_path = f'/tmp/{os.path.basename(archive_path)}'
        put(archive_path, remote_archive_path)

        # Extract archive to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path).replace(
            '.tgz',
            ''
        ).replace('.tar.gz', '')
        release_folder = f'/data/web_static/releases/{archive_filename}'
        run(f'mkdir -p {release_folder}')
        run(f'tar -xzf {remote_archive_path} -C {release_folder}')

        # Delete uploaded archive from /tmp/
        run(f'rm {remote_archive_path}')

        # Update symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        run(f'rm -f {current_link}')
        run(f'ln -s {release_folder} {current_link}')

        print("Deployment successful.")
        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
