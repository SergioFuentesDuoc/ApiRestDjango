#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python -m pip install django-cors-headers
python manage.py collectstatic --no-input
python manage.py migrate