"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Get the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import Flask app
try:
    from backend.app import app
except Exception as e:
    # If import fails, create a minimal error handler
    from flask import Flask, jsonify
    app = Flask(__name__)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def error(path):
        return jsonify({
            'error': 'Import failed',
            'message': str(e),
            'type': type(e).__name__,
            'project_root': project_root,
            'current_dir': current_dir,
            'sys_path': sys.path
        }), 500

# Export the Flask app as the handler
# Vercel Python runtime will automatically wrap this as a serverless function
handler = app

