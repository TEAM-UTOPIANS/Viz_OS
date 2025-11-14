"""
Validation Service
Utility functions for validating request data
"""

def validate_processes(processes):
    """
    Validate process data
    
    Args:
        processes: List of process dictionaries
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(processes, list):
        return False, "Processes must be a list"
    
    if len(processes) == 0:
        return False, "At least one process is required"
    
    for i, proc in enumerate(processes):
        if not isinstance(proc, dict):
            return False, f"Process {i} must be a dictionary"
        
        required_fields = ['id', 'arrival_time', 'burst_time']
        for field in required_fields:
            if field not in proc:
                return False, f"Process {i} missing required field: {field}"
        
        if proc['burst_time'] <= 0:
            return False, f"Process {i} burst_time must be positive"
        
        if proc['arrival_time'] < 0:
            return False, f"Process {i} arrival_time must be non-negative"
    
    return True, None

