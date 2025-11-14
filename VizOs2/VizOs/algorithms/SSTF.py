"""
SSTF (Shortest Seek Time First) Algorithm
Disk scheduling algorithm that serves closest request
"""

def execute(requests, initial_head):
    """
    Execute SSTF disk scheduling algorithm
    
    Args:
        requests: List of track numbers to access
        initial_head: Initial head position
        
    Returns:
        Dictionary containing seek_sequence and total_seek_time
    """
    # Create a copy of requests
    remaining_requests = list(set(requests))
    seek_sequence = []
    current_head = initial_head
    total_seek_time = 0
    
    # Process all requests
    while remaining_requests:
        # Find closest request
        closest_request = min(remaining_requests, key=lambda x: abs(x - current_head))
        
        # Add to sequence
        seek_sequence.append(closest_request)
        total_seek_time += abs(closest_request - current_head)
        current_head = closest_request
        
        # Remove from remaining
        remaining_requests.remove(closest_request)
    
    return {
        'seek_sequence': seek_sequence,
        'total_seek_time': total_seek_time,
        'average_seek_time': round(total_seek_time / len(seek_sequence), 2) if seek_sequence else 0
    }

