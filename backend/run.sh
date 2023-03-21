#!/bin/bash
gunicorn -w 4 -b 0.0.0.0:8012 app:app --timeout 0 --reload --threads 16