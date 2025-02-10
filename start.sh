#!/bin/bash
echo "Starting application..."
echo "PORT: $PORT"
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120 --log-level debug app:app