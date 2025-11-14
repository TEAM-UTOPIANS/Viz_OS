"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Import Flask first to ensure it's available
from flask import Flask, jsonify

# Get the project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Initialize Flask app first (always available)
app = Flask(__name__)

# Try to import and use the backend app
try:
    from backend.app import app as backend_app
    # Copy routes from backend app to our app
    for rule in backend_app.url_map.iter_rules():
        app.add_url_rule(
            rule.rule,
            endpoint=rule.endpoint,
            view_func=backend_app.view_functions[rule.endpoint],
            methods=rule.methods
        )
    print("Successfully imported and registered backend routes")
except Exception as e:
    # If import fails, create error routes
    import traceback
    error_msg = str(e)
    error_type = type(e).__name__
    error_traceback = traceback.format_exc()
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def error_handler(path):
        return jsonify({
            'error': 'Backend import failed',
            'message': error_msg,
            'type': error_type,
            'path': path,
            'project_root': project_root,
            'current_dir': current_dir,
            'sys_path': sys.path[:5],  # First 5 entries only
            'traceback': error_traceback
        }), 500
    
    print(f"Failed to import backend app: {error_msg}")

# Vercel Python runtime expects the handler to be the Flask app
# This MUST be defined for Vercel to recognize the function
handler = app
