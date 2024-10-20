#!/bin/bash
set -e

/bin/bash -c "python3 /home/$user/src/petro_quick/manage.py makemigrations"
/bin/bash -c "python3 /home/$user/src/petro_quick/manage.py migrate"
/bin/bash -c "python3 /home/$user/src/petro_quick/manage.py create_superuser"

sudo -E supervisord -n -c /etc/supervisord.conf