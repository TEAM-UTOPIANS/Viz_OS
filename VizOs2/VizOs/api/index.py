from flask import Flask, jsonify
import sys
import os

# Add project root to path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Create Flask app
app = Flask(__name__)

# Try to import backend
try:
    from backend.app import app as backend_app
    app = backend_app
except Exception as e:
    # Fallback error handler
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def handler(path):
        import traceback
        return jsonify({
            'error': 'Import failed',
            'message': str(e),
            'traceback': traceback.format_exc()
        }), 500

# Export handler for Vercel - MUST be defined
handler = app
