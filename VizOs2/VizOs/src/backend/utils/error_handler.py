"""
Error Handler
Utility functions for handling errors
"""

from src.backend.utils.response_formatter import error

def validation_error(message, details=None):
    """Return validation error response"""
    return error('VALIDATION_ERROR', message, details)

def server_error(message):
    """Return server error response"""
    return error('SERVER_ERROR', message), 500

def algorithm_error(message):
    """Return algorithm error response"""
    return error('ALGORITHM_ERROR', message), 422

