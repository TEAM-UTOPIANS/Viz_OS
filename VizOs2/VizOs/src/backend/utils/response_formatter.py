"""
Response Formatter
Utility functions for formatting API responses
"""

from flask import jsonify

def success(data, message="Operation completed successfully"):
    """
    Format successful response
    
    Args:
        data: Response data
        message: Success message
        
    Returns:
        JSON response with success format
    """
    return jsonify({
        'success': True,
        'data': data,
        'message': message
    }), 200

def error(error_code, message, details=None):
    """
    Format error response
    
    Args:
        error_code: Error code
        message: Error message
        details: Additional error details
        
    Returns:
        JSON response with error format
    """
    response = {
        'success': False,
        'error': {
            'code': error_code,
            'message': message
        }
    }
    
    if details:
        response['error']['details'] = details
    
    return jsonify(response), 400

