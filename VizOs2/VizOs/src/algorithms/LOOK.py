"""
LOOK Algorithm
Disk scheduling algorithm - SCAN variant that reverses at last request
"""

def execute(requests, initial_head, direction='right'):
    """
    Execute LOOK disk scheduling algorithm
    
    Args:
        requests: List of track numbers to access
        initial_head: Initial head position
        direction: 'left' or 'right'
        
    Returns:
        Dictionary containing seek_sequence and total_seek_time
    """
    # Sort requests
    sorted_requests = sorted(set(requests))
    
    # Separate requests based on direction
    left_requests = [r for r in sorted_requests if r < initial_head]
    right_requests = [r for r in sorted_requests if r >= initial_head]
    
    seek_sequence = []
    current_head = initial_head
    total_seek_time = 0
    
    if direction == 'right':
        # Move right to last request
        for request in right_requests:
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
        
        # Reverse direction (no need to go to end)
        # Move left to first request
        for request in reversed(left_requests):
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
    
    else:  # direction == 'left'
        # Move left to first request
        for request in reversed(left_requests):
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
        
        # Reverse direction (no need to go to beginning)
        # Move right to last request
        for request in right_requests:
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
    
    return {
        'seek_sequence': seek_sequence,
        'total_seek_time': total_seek_time,
        'average_seek_time': round(total_seek_time / len(seek_sequence), 2) if seek_sequence else 0
    }

