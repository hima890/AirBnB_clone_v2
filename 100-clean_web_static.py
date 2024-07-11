from fabric.api import *
import os

# Define your web server IP addresses
env.hosts = ['35.175.102.190', '3.89.146.68']
# Define the username used for SSH access
env.user = 'ubuntu'
# Define the path to your SSH private key file
env.key_filename = '/home/ahmed/.ssh/school'


def do_clean(number=0):
    """
    Deletes out-of-date archives, keeping only the specified number
    of the most recent archives.

    Args:
    number (int): The number of archives to keep, including the most recent.
                  If 0 or 1, keep only the most recent archive. If 2,
                  keep the most recent and second most recent, etc.

    Returns:
    bool: True if the cleanup was successful, False otherwise.
    """
    number = int(number)
    if number <= 0:
        number = 1

    try:
        # Local cleanup
        local_archives = sorted(os.listdir("versions"))
        archives_to_delete = local_archives[:-number]
        for archive in archives_to_delete:
            os.remove(os.path.join("versions", archive))

        # Remote cleanup
        for host in env.hosts:
            result = run('ls -1t /data/web_static/releases', hide=True)
            remote_archives = result.stdout.strip().split()
            remote_archives = [
                name for name in remote_archives if "web_static_" in name
                ]
            archives_to_delete = remote_archives[:-number]
            for archive in archives_to_delete:
                run(f'rm -rf /data/web_static/releases/{archive}')

        print("Cleanup successful.")
        return True

    except Exception as e:
        print(f"Cleanup failed: {e}")
        return False
