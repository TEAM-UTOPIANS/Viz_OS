"""
Scheduler Service
Business logic for CPU scheduling algorithms
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from algorithms import FCFS, SJF, Priority, RoundRobin

def fcfs(processes):
    """
    Execute FCFS scheduling algorithm
    
    Args:
        processes: List of process dictionaries
        
    Returns:
        Dictionary containing gantt_chart, metrics, and process_details
    """
    # Validate processes
    validated_processes = _validate_processes(processes)
    
    # Call algorithm
    result = FCFS.execute(validated_processes)
    
    # Format result
    return {
        'gantt_chart': result['gantt_chart'],
        'metrics': result['metrics'],
        'process_details': result['process_details']
    }

def sjf(processes):
    """Execute SJF scheduling algorithm"""
    validated_processes = _validate_processes(processes)
    result = SJF.execute(validated_processes)
    
    return {
        'gantt_chart': result['gantt_chart'],
        'metrics': result['metrics'],
        'process_details': result['process_details']
    }

def priority(processes, preemptive=False):
    """Execute Priority scheduling algorithm"""
    validated_processes = _validate_processes(processes, require_priority=True)
    result = Priority.execute(validated_processes, preemptive)
    
    return {
        'gantt_chart': result['gantt_chart'],
        'metrics': result['metrics'],
        'process_details': result['process_details']
    }

def roundrobin(processes, quantum):
    """Execute Round Robin scheduling algorithm"""
    validated_processes = _validate_processes(processes)
    result = RoundRobin.execute(validated_processes, quantum)
    
    return {
        'gantt_chart': result['gantt_chart'],
        'metrics': result['metrics'],
        'process_details': result['process_details']
    }

def _validate_processes(processes, require_priority=False):
    """
    Validate and normalize process data
    
    Args:
        processes: List of process dictionaries
        require_priority: Whether priority field is required
        
    Returns:
        Validated list of processes
        
    Raises:
        ValueError: If validation fails
    """
    if not isinstance(processes, list) or len(processes) == 0:
        raise ValueError("Processes must be a non-empty list")
    
    validated = []
    for i, proc in enumerate(processes):
        if not isinstance(proc, dict):
            raise ValueError(f"Process {i} must be a dictionary")
        
        # Required fields
        if 'id' not in proc:
            raise ValueError(f"Process {i} missing 'id' field")
        if 'arrival_time' not in proc:
            raise ValueError(f"Process {i} missing 'arrival_time' field")
        if 'burst_time' not in proc:
            raise ValueError(f"Process {i} missing 'burst_time' field")
        
        # Validate values
        if proc['burst_time'] <= 0:
            raise ValueError(f"Process {i} burst_time must be positive")
        if proc['arrival_time'] < 0:
            raise ValueError(f"Process {i} arrival_time must be non-negative")
        
        # Priority validation
        if require_priority:
            if 'priority' not in proc:
                raise ValueError(f"Process {i} missing 'priority' field")
        
        validated.append({
            'id': str(proc['id']),
            'arrival_time': int(proc['arrival_time']),
            'burst_time': int(proc['burst_time']),
            'priority': int(proc.get('priority', 0))
        })
    
    return validated

