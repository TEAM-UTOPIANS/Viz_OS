"""
SCAN (Elevator) Algorithm
Disk scheduling algorithm that moves in one direction
"""

def execute(requests, initial_head, direction='right', disk_size=200):
    """
    Execute SCAN disk scheduling algorithm
    
    Args:
        requests: List of track numbers to access
        initial_head: Initial head position
        direction: 'left' or 'right'
        disk_size: Total number of tracks
        
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
        # Move right first
        for request in right_requests:
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
        
        # Move to end if needed
        if right_requests:
            total_seek_time += abs(disk_size - 1 - current_head)
            current_head = disk_size - 1
        
        # Move left
        for request in reversed(left_requests):
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
    
    else:  # direction == 'left'
        # Move left first
        for request in reversed(left_requests):
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
        
        # Move to beginning if needed
        if left_requests:
            total_seek_time += abs(0 - current_head)
            current_head = 0
        
        # Move right
        for request in right_requests:
            seek_sequence.append(request)
            total_seek_time += abs(request - current_head)
            current_head = request
    
    return {
        'seek_sequence': seek_sequence,
        'total_seek_time': total_seek_time,
        'average_seek_time': round(total_seek_time / len(seek_sequence), 2) if seek_sequence else 0
    }

