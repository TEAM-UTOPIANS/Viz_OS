"""
FCFS (First Come First Serve) Algorithm
Non-preemptive CPU scheduling algorithm
"""

def execute(processes):
    """
    Execute FCFS scheduling algorithm
    
    Args:
        processes: List of process dictionaries with:
            - id: Process identifier
            - arrival_time: Arrival time
            - burst_time: CPU burst time
            
    Returns:
        Dictionary containing:
            - gantt_chart: List of execution segments
            - metrics: Performance metrics
            - process_details: Detailed process information
    """
    # Sort processes by arrival time
    sorted_processes = sorted(processes, key=lambda x: x['arrival_time'])
    
    # Initialize variables
    gantt_chart = []
    process_details = []
    current_time = 0
    
    # Execute processes in order
    for proc in sorted_processes:
        arrival = proc['arrival_time']
        burst = proc['burst_time']
        
        # Wait if process hasn't arrived
        if current_time < arrival:
            current_time = arrival
        
        # Calculate times
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        # Add to Gantt chart
        gantt_chart.append({
            'process': proc['id'],
            'start': current_time,
            'end': current_time + burst
        })
        
        # Update process details
        process_details.append({
            'id': proc['id'],
            'arrival_time': arrival,
            'burst_time': burst,
            'waiting_time': waiting_time,
            'turnaround_time': turnaround_time,
            'completion_time': current_time + burst
        })
        
        # Update current time
        current_time += burst
    
    # Calculate metrics
    total_waiting_time = sum(p['waiting_time'] for p in process_details)
    total_turnaround_time = sum(p['turnaround_time'] for p in process_details)
    n = len(process_details)
    
    metrics = {
        'average_waiting_time': round(total_waiting_time / n, 2),
        'average_turnaround_time': round(total_turnaround_time / n, 2),
        'cpu_utilization': round((sum(p['burst_time'] for p in process_details) / current_time) * 100, 2) if current_time > 0 else 0,
        'throughput': round(n / current_time, 2) if current_time > 0 else 0
    }
    
    return {
        'gantt_chart': gantt_chart,
        'metrics': metrics,
        'process_details': process_details
    }

