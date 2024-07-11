#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
import os


from datetime import datetime
import os
import subprocess


def do_pack():
    """
    Packs the contents of the 'web_static' folder into a compressed
    archive (.tgz file).

    This function creates a timestamped archive of the 'web_static'
    folder, storing it in the 'versions' directory. The archive
    name follows the format:
    'web_static_<year><month><day><hour><minute><second>.tgz'.
    If the 'versions' directory does not exist, it will be created.

    Returns:
    str: The absolute path of the created archive if successful,
    otherwise None.
    """
    source_folder = 'web_static'
    target_folder = 'versions'
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    archive_path = os.path.join(target_folder, archive_name)
    command = f'tar -czvf {archive_path} {source_folder}'

    try:
        subprocess.check_call(command, shell=True)
        return os.path.abspath(archive_path)
    except subprocess.CalledProcessError as e:
        print(f"Error packing archive: {e}")
        return None


if __name__ == '__main__':
    archive_path = do_pack()
    if archive_path:
        print(f"Archive created successfully: {archive_path}")
    else:
        print("Failed to create archive.")
