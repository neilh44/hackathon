# gunicorn_config.py
import os

# Get port from environment variable
port = os.environ.get("PORT", 10000)

# Bind to the port
bind = f"0.0.0.0:{port}"

# Worker configuration
workers = 1
threads = 2
worker_class = 'gthread'

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Timeout configuration
timeout = 120