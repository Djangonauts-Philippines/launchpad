#!/bin/bash

gunicorn tesseract.wsgi:application --log-file -
