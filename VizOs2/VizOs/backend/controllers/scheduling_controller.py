"""
Scheduling Controller
Handles HTTP requests for CPU scheduling algorithms
"""

from flask import jsonify
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from backend.services import scheduler_service
from backend.utils import response_formatter, error_handler

def fcfs(request):
    """
    Handle FCFS scheduling request
    
    Expected request body:
    {
        "processes": [
            {"id": "P1", "arrival_time": 0, "burst_time": 5},
            ...
        ]
    }
    """
    try:
        data = request.get_json()
        
        # Validate request
        if not data or 'processes' not in data:
            return error_handler.validation_error("Missing 'processes' field")
        
        processes = data['processes']
        
        # Call service
        result = scheduler_service.fcfs(processes)
        
        # Format and return response
        return response_formatter.success(result, "FCFS scheduling completed successfully")
    
    except Exception as e:
        return error_handler.server_error(str(e))

def sjf(request):
    """Handle SJF scheduling request"""
    try:
        data = request.get_json()
        
        if not data or 'processes' not in data:
            return error_handler.validation_error("Missing 'processes' field")
        
        processes = data['processes']
        result = scheduler_service.sjf(processes)
        
        return response_formatter.success(result, "SJF scheduling completed successfully")
    
    except Exception as e:
        return error_handler.server_error(str(e))

def priority(request):
    """Handle Priority scheduling request"""
    try:
        data = request.get_json()
        
        if not data or 'processes' not in data:
            return error_handler.validation_error("Missing 'processes' field")
        
        processes = data['processes']
        preemptive = data.get('preemptive', False)
        
        result = scheduler_service.priority(processes, preemptive)
        
        return response_formatter.success(result, "Priority scheduling completed successfully")
    
    except Exception as e:
        return error_handler.server_error(str(e))

def roundrobin(request):
    """Handle Round Robin scheduling request"""
    try:
        data = request.get_json()
        
        if not data or 'processes' not in data:
            return error_handler.validation_error("Missing 'processes' field")
        
        if 'quantum' not in data:
            return error_handler.validation_error("Missing 'quantum' field")
        
        processes = data['processes']
        quantum = data['quantum']
        
        if quantum <= 0:
            return error_handler.validation_error("Quantum must be positive")
        
        result = scheduler_service.roundrobin(processes, quantum)
        
        return response_formatter.success(result, "Round Robin scheduling completed successfully")
    
    except Exception as e:
        return error_handler.server_error(str(e))

