import os

# Get port from environment variable
port = os.environ.get("PORT", 10000)

# Bind to the port
bind = f"0.0.0.0:{port}"

# Worker configuration - reduce workers to save memory
workers = 1
threads = 2
worker_class = 'gthread'

# Memory optimization
max_requests = 1000
max_requests_jitter = 50
worker_tmp_dir = '/dev/shm'  # Use shared memory

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Timeout configuration
timeout = 120