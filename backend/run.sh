#!/bin/bash
lsof -i:8012 | grep -v COMMAND | awk '{ print $2 }' | xargs kill -9
nohup gunicorn -w 4 -b 0.0.0.0:8012 app:app --timeout 0 --reload --threads 16 >> console_main.log &