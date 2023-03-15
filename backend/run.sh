#!/bin/bash
gunicorn -w 8 -b 0.0.0.0:8012 app:app --timeout 0 --reload --threads 16