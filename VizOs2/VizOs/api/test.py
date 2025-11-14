"""
Minimal test handler for Vercel
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handler(path):
    return jsonify({
        'message': 'Test handler works!',
        'path': path
    })

handler = app

