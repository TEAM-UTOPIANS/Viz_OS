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
    print(f"Successfully imported Flask app from backend.app")
except Exception as e:
    # If import fails, create a minimal error handler
    import traceback
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
            'sys_path': sys.path,
            'traceback': traceback.format_exc()
        }), 500
    print(f"Failed to import Flask app: {e}")

# Vercel Python runtime expects the handler to be the Flask app
# The Flask app (WSGI application) will be automatically wrapped by Vercel
handler = app
