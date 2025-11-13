"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Get the project root (parent of api directory)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Change to project root to ensure relative paths work correctly
os.chdir(project_root)

# Add the project root to the path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import the Flask app
from backend.app import app

# Vercel expects the app to be exported as 'handler'
# The @vercel/python builder will automatically wrap this Flask app
handler = app

