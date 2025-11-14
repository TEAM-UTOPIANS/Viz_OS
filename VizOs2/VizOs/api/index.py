"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Import Flask FIRST to ensure it's always available
from flask import Flask, jsonify

# Get the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Try to import the backend app
app = None
try:
    from backend.app import app
    print("Successfully imported Flask app from backend.app")
except Exception as e:
    # If import fails, create a minimal Flask app with error handler
    import traceback
    app = Flask(__name__)
    
    error_details = {
        'error': 'Backend import failed',
        'message': str(e),
        'type': type(e).__name__,
        'project_root': project_root,
        'current_dir': current_dir,
        'traceback': traceback.format_exc()
    }
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def error_handler(path):
        return jsonify({
            **error_details,
            'requested_path': path
        }), 500
    
    print(f"Failed to import backend app: {e}")

# CRITICAL: Vercel requires 'handler' to be defined
# This MUST be the Flask app (WSGI application)
handler = app
