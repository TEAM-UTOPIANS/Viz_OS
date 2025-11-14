"""
Priority Scheduling Algorithm
CPU scheduling algorithm based on process priority
"""

def execute(processes, preemptive=False):
    """
    Execute Priority scheduling algorithm
    
    Args:
        processes: List of process dictionaries with priority
        preemptive: Whether to use preemptive scheduling
        
    Returns:
        Dictionary containing gantt_chart, metrics, and process_details
    """
    if preemptive:
        return _execute_preemptive(processes)
    else:
        return _execute_non_preemptive(processes)

def _execute_non_preemptive(processes):
    """Non-preemptive priority scheduling"""
    sorted_processes = sorted(processes, key=lambda x: (x['arrival_time'], x['priority']))
    
    gantt_chart = []
    process_details = []
    current_time = 0
    completed = set()
    
    while len(completed) < len(sorted_processes):
        available = [
            p for p in sorted_processes
            if p['id'] not in completed and p['arrival_time'] <= current_time
        ]
        
        if not available:
            current_time = min(
                p['arrival_time'] for p in sorted_processes
                if p['id'] not in completed
            )
            continue
        
        # Select process with highest priority (lowest number)
        selected = min(available, key=lambda x: x['priority'])
        
        arrival = selected['arrival_time']
        burst = selected['burst_time']
        
        if current_time < arrival:
            current_time = arrival
        
        waiting_time = current_time - arrival
        turnaround_time = waiting_time + burst
        
        gantt_chart.append({
            'process': selected['id'],
            'start': current_time,
            'end': current_time + burst
        })
        
        process_details.append({
            'id': selected['id'],
            'arrival_time': arrival,
            'burst_time': burst,
            'priority': selected['priority'],
            'waiting_time': waiting_time,
            'turnaround_time': turnaround_time,
            'completion_time': current_time + burst
        })
        
        current_time += burst
        completed.add(selected['id'])
    
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

def _execute_preemptive(processes):
    """Preemptive priority scheduling (similar to Round Robin but priority-based)"""
    # Simplified implementation - similar to non-preemptive for now
    # Full preemptive implementation would require time-slicing
    return _execute_non_preemptive(processes)

