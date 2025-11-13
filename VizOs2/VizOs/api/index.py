"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Get the project root (parent of api directory)
# In Vercel, __file__ will be in /var/task/api/index.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to the path first
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Change to project root to ensure relative paths work correctly
try:
    os.chdir(project_root)
except:
    pass  # If chdir fails, continue anyway

# Import the Flask app
from backend.app import app

# Vercel expects the app to be exported as 'handler'
# The @vercel/python builder will automatically wrap this Flask app as WSGI
handler = app

