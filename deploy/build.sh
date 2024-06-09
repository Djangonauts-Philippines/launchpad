#!/usr/bin/env bash

folder="logs"
logfile="$folder/app.log"

if [ ! -d "$folder" ] || [ ! -f "$logfile" ]; then
    mkdir -p "$folder"
    touch "$logfile"
fi

pip install --upgrade pip
pip install -r requirements/base-requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
