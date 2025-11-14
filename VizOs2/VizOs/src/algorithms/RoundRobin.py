"""
Round Robin Algorithm
Preemptive CPU scheduling algorithm with time quantum
"""

from collections import deque

def execute(processes, quantum):
    """
    Execute Round Robin scheduling algorithm
    
    Args:
        processes: List of process dictionaries
        quantum: Time quantum for each process
        
    Returns:
        Dictionary containing gantt_chart, metrics, and process_details
    """
    # Sort processes by arrival time
    sorted_processes = sorted(processes, key=lambda x: x['arrival_time'])
    
    # Initialize
    gantt_chart = []
    process_details = {p['id']: {
        'id': p['id'],
        'arrival_time': p['arrival_time'],
        'burst_time': p['burst_time'],
        'remaining_time': p['burst_time'],
        'waiting_time': 0,
        'turnaround_time': 0,
        'completion_time': 0
    } for p in sorted_processes}
    
    ready_queue = deque()
    current_time = 0
    process_index = 0
    
    # Main scheduling loop
    while process_index < len(sorted_processes) or ready_queue or any(p['remaining_time'] > 0 for p in process_details.values()):
        # Add arrived processes to ready queue
        while process_index < len(sorted_processes) and sorted_processes[process_index]['arrival_time'] <= current_time:
            proc_id = sorted_processes[process_index]['id']
            ready_queue.append(proc_id)
            process_index += 1
        
        # Get next process from queue
        if ready_queue:
            proc_id = ready_queue.popleft()
            proc = process_details[proc_id]
            
            if proc['remaining_time'] > 0:
                # Execute for quantum or until completion
                execution_time = min(quantum, proc['remaining_time'])
                start_time = current_time
                end_time = current_time + execution_time
                
                # Add to Gantt chart
                gantt_chart.append({
                    'process': proc_id,
                    'start': start_time,
                    'end': end_time
                })
                
                # Update remaining time
                proc['remaining_time'] -= execution_time
                current_time = end_time
                
                # Add arrived processes during execution
                while process_index < len(sorted_processes) and sorted_processes[process_index]['arrival_time'] <= current_time:
                    new_proc_id = sorted_processes[process_index]['id']
                    if new_proc_id not in [p['process'] for p in gantt_chart[-1:]]:
                        ready_queue.append(new_proc_id)
                    process_index += 1
                
                # If process not completed, add back to queue
                if proc['remaining_time'] > 0:
                    ready_queue.append(proc_id)
                else:
                    # Process completed
                    proc['completion_time'] = current_time
                    proc['turnaround_time'] = proc['completion_time'] - proc['arrival_time']
                    proc['waiting_time'] = proc['turnaround_time'] - proc['burst_time']
        else:
            # No process ready, advance time
            if process_index < len(sorted_processes):
                current_time = sorted_processes[process_index]['arrival_time']
            else:
                break
    
    # Calculate metrics
    process_list = list(process_details.values())
    total_waiting_time = sum(p['waiting_time'] for p in process_list)
    total_turnaround_time = sum(p['turnaround_time'] for p in process_list)
    n = len(process_list)
    
    metrics = {
        'average_waiting_time': round(total_waiting_time / n, 2) if n > 0 else 0,
        'average_turnaround_time': round(total_turnaround_time / n, 2) if n > 0 else 0,
        'cpu_utilization': round((sum(p['burst_time'] for p in process_list) / current_time) * 100, 2) if current_time > 0 else 0,
        'throughput': round(n / current_time, 2) if current_time > 0 else 0
    }
    
    return {
        'gantt_chart': gantt_chart,
        'metrics': metrics,
        'process_details': process_list
    }

