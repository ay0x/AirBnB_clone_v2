#!/usr/bin/python3
"""
Fabric script based on the file 3-deploy_web_static.py that
deletes out-of-date archives, using the function do_clean
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['100.27.4.97', '100.26.254.126']


def do_clean(number=0):
    """Deletes out-of-date archives
    """
    try:
        number = int(number)
        number = 1 if number < 1 else number + 1

        # Delete local archives
        local("ls -1t versions/ | tail -n +{} | xargs -I {} rm versions/{}"
              .format(number, '{}'))

        # Delete remote archives on both web servers
        run("ls -1t /data/web_static/releases | tail -n +{} | "
            "xargs -I {} rm -rf /data/web_static/releases/{}"
            .format(number, '{}'))

        return True

    except Exception as e:
        return False
