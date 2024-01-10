#!/usr/bin/python3
"""This module provides a function that generates
a `.tgz` archive from the contents of the web_static
folder of my AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    folder.

    Returns:
        str: Archive path if successfully generated, None otherwise.
    """
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Get the current date and time
    now = datetime.utcnow()
    formatted_date = now.strftime("%Y%m%d%H%M%S")

    # Set the archive path
    archive_path = "versions/web_static_{}.tgz".format(formatted_date)

    # Compress the contents of the web_static folder into a .tgz archive
    result = local("tar -czvf {} web_static".format(archive_path))

    # Check if the compression was successful
    if result.succeeded:
        # Get the size of the archive
        archive_size = os.path.getsize(archive_path)

        # Print the archive path and size
        print("web_static packed: {} -> {}Bytes".format(archive_path,
                                                        archive_size))
        return archive_path
    else:
        return None

# Example usage
do_pack()
