"""
Viz-OS Backend Application
Main Flask application entry point
"""

from flask import Flask, send_from_directory
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__, 
            static_folder='../frontend',
            static_url_path='')

# Enable CORS
CORS(app)

# Configuration
app.config['JSON_SORT_KEYS'] = False
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'

# Import routes
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from src.backend.routes import api_routes

# Register blueprints
app.register_blueprint(api_routes.bp, url_prefix='/api')

@app.route('/')
def index():
    """Serve the main frontend page"""
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('../frontend', path)

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return {'success': False, 'error': 'Endpoint not found'}, 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return {'success': False, 'error': 'Internal server error'}, 500

if __name__ == '__main__':
    print("=" * 50)
    print("Starting VizOS - Interactive OS Simulation Tool")
    print("=" * 50)
    print(f"Application: http://localhost:5000/")
    print(f"API Documentation: http://localhost:5000/api")
    print(f"Health Check: http://localhost:5000/api/health")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=True)

