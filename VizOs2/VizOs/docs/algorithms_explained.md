# Operating System Algorithms Explained

This document provides detailed explanations of all algorithms implemented in Viz-OS, including their working principles, formulas, and visual representations.

---

## 📋 Table of Contents

1. [CPU Scheduling Algorithms](#cpu-scheduling-algorithms)
   - [FCFS (First Come First Serve)](#fcfs-first-come-first-serve)
   - [SJF (Shortest Job First)](#sjf-shortest-job-first)
   - [Priority Scheduling](#priority-scheduling)
   - [Round Robin](#round-robin)

2. [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
   - [SCAN (Elevator Algorithm)](#scan-elevator-algorithm)
   - [SSTF (Shortest Seek Time First)](#sstf-shortest-seek-time-first)
   - [LOOK](#look)
   - [C-LOOK](#c-look)

3. [Memory Management Algorithms](#memory-management-algorithms)
   - [Page Replacement](#page-replacement)
   - [Memory Allocation](#memory-allocation)

---

## 🖥️ CPU Scheduling Algorithms

### FCFS (First Come First Serve)

**Type**: Non-preemptive  
**Complexity**: O(n)  
**Fairness**: Fair (FIFO order)

#### Description

FCFS is the simplest CPU scheduling algorithm. Processes are executed in the order they arrive in the ready queue. It's a non-preemptive algorithm, meaning once a process starts executing, it runs until completion.

#### Algorithm Steps

```
1. Sort processes by arrival time
2. Execute processes in order
3. Calculate waiting time and turnaround time
```

#### Formula

- **Waiting Time (WT)**: `WT[i] = Completion Time[i] - Arrival Time[i] - Burst Time[i]`
- **Turnaround Time (TAT)**: `TAT[i] = Completion Time[i] - Arrival Time[i]`
- **Average Waiting Time**: `AWT = Σ(WT[i]) / n`
- **Average Turnaround Time**: `ATAT = Σ(TAT[i]) / n`

#### Example

**Input**:
```
Process | Arrival Time | Burst Time
--------|--------------|------------
P1      | 0            | 5
P2      | 1            | 3
P3      | 2            | 8
```

**Gantt Chart**:
```
| P1 | P2 |    P3    |
0    5    8         16
```

**Results**:
```
Process | WT | TAT
--------|----|----
P1      | 0  | 5
P2      | 4  | 7
P3      | 6  | 14
Average | 3.33 | 8.67
```

#### Advantages
- ✅ Simple to implement
- ✅ No starvation
- ✅ Fair (FIFO)

#### Disadvantages
- ❌ Poor average waiting time
- ❌ Not suitable for time-sharing systems
- ❌ Convoy effect (short processes wait behind long ones)

---

### SJF (Shortest Job First)

**Type**: Non-preemptive (can be preemptive as SRTF)  
**Complexity**: O(n²) or O(n log n) with sorting  
**Fairness**: Unfair (favors short jobs)

#### Description

SJF selects the process with the smallest burst time for execution. It can be non-preemptive (executes until completion) or preemptive (Shortest Remaining Time First - SRTF).

#### Algorithm Steps

```
1. Sort processes by arrival time
2. For each time unit:
   a. Add arrived processes to ready queue
   b. Select process with shortest burst time
   c. Execute until completion
3. Calculate metrics
```

#### Formula

Same as FCFS, but execution order differs.

#### Example

**Input**:
```
Process | Arrival Time | Burst Time
--------|--------------|------------
P1      | 0            | 8
P2      | 1            | 4
P3      | 2            | 2
P4      | 3            | 1
```

**Gantt Chart (Non-preemptive)**:
```
| P1 | P2 | P3 | P4 |    P1    |
0    1    3    5    6         14
```

**Results**:
```
Process | WT | TAT
--------|----|----
P1      | 6  | 14
P2      | 0  | 4
P3      | 1  | 3
P4      | 2  | 3
Average | 2.25 | 6.0
```

#### Advantages
- ✅ Optimal average waiting time (non-preemptive)
- ✅ Minimizes average turnaround time

#### Disadvantages
- ❌ Starvation of long processes
- ❌ Difficult to predict burst time
- ❌ Not suitable for interactive systems

---

### Priority Scheduling

**Type**: Preemptive or Non-preemptive  
**Complexity**: O(n log n)  
**Fairness**: Depends on priority assignment

#### Description

Each process is assigned a priority. The process with the highest priority (lowest number in some systems) is executed first. Can be preemptive or non-preemptive.

#### Algorithm Steps

```
1. Sort processes by arrival time
2. For each time unit:
   a. Add arrived processes to ready queue
   b. Select process with highest priority
   c. Execute (preempt if preemptive)
3. Calculate metrics
```

#### Priority Assignment

- **Lower number = Higher priority** (common)
- **Higher number = Higher priority** (alternative)

#### Example

**Input**:
```
Process | Arrival Time | Burst Time | Priority
--------|--------------|------------|----------
P1      | 0            | 4          | 2
P2      | 1            | 3          | 1
P3      | 2            | 1          | 3
P4      | 3            | 5          | 4
```

**Gantt Chart (Non-preemptive)**:
```
| P1 | P2 | P3 |    P4    |
0    4    7    8         13
```

#### Advantages
- ✅ Flexible priority system
- ✅ Important processes can be prioritized

#### Disadvantages
- ❌ Starvation of low-priority processes
- ❌ Priority inversion problem
- ❌ Aging needed to prevent starvation

---

### Round Robin

**Type**: Preemptive  
**Complexity**: O(n)  
**Fairness**: Very fair

#### Description

Each process is assigned a fixed time slice (quantum). Processes execute in a circular queue. If a process doesn't complete within its quantum, it's preempted and moved to the end of the queue.

#### Algorithm Steps

```
1. Create ready queue
2. For each time quantum:
   a. Select process from front of queue
   b. Execute for quantum time (or until completion)
   c. If not completed, add to end of queue
   d. Add newly arrived processes
3. Calculate metrics
```

#### Formula

- **Context Switch Overhead**: Considered in real systems
- **Quantum Size**: Critical for performance
  - Too small: High context switching overhead
  - Too large: Approaches FCFS

#### Example

**Input**:
```
Process | Arrival Time | Burst Time
--------|--------------|------------
P1      | 0            | 5
P2      | 1            | 3
P3      | 2            | 8
Quantum = 2
```

**Gantt Chart**:
```
|P1|P2|P1|P3|P2|P1|P3|P3|P3|P3|
0 2 4 6 8 10 12 14 16 18 20
```

**Results**:
```
Process | WT | TAT
--------|----|----
P1      | 7  | 12
P2      | 3  | 6
P3      | 10 | 18
Average | 6.67 | 12.0
```

#### Advantages
- ✅ No starvation
- ✅ Fair scheduling
- ✅ Suitable for time-sharing systems
- ✅ Responsive

#### Disadvantages
- ❌ Performance depends on quantum size
- ❌ Context switching overhead
- ❌ Not optimal for batch systems

---

## 💾 Disk Scheduling Algorithms

### SCAN (Elevator Algorithm)

**Type**: Bi-directional  
**Complexity**: O(n log n)  
**Description**: Moves in one direction, serves all requests, then reverses

#### Algorithm Steps

```
1. Sort requests by track number
2. Start from initial head position
3. Move in one direction (e.g., towards higher tracks)
4. Serve all requests in that direction
5. When reaching end, reverse direction
6. Serve remaining requests
```

#### Example

**Input**:
```
Initial Head Position: 50
Requests: [176, 79, 34, 60, 92, 11, 41, 114]
Direction: Right (towards higher tracks)
```

**Execution**:
```
50 → 60 → 79 → 92 → 114 → 176 → 41 → 34 → 11
```

**Total Seek Time**: Calculate based on track differences

#### Advantages
- ✅ No starvation
- ✅ Better than FCFS
- ✅ Predictable performance

#### Disadvantages
- ❌ Long wait for requests at opposite end
- ❌ Unnecessary movement to end

---

### SSTF (Shortest Seek Time First)

**Type**: Greedy  
**Complexity**: O(n²)  
**Description**: Always serves the request closest to current head position

#### Algorithm Steps

```
1. Start from initial head position
2. Find request with minimum seek time
3. Move head to that request
4. Repeat until all requests served
```

#### Example

**Input**:
```
Initial Head Position: 50
Requests: [176, 79, 34, 60, 92, 11, 41, 114]
```

**Execution**:
```
50 → 60 → 79 → 92 → 114 → 176 → 41 → 34 → 11
```

#### Advantages
- ✅ Better average response time than FCFS
- ✅ Reduces total seek time

#### Disadvantages
- ❌ Starvation possible
- ❌ Not optimal for all cases

---

### LOOK

**Type**: Bi-directional  
**Complexity**: O(n log n)  
**Description**: Like SCAN but reverses at last request instead of end

#### Algorithm Steps

```
1. Sort requests
2. Move in one direction
3. Serve all requests
4. Reverse at last request (not at end)
5. Serve remaining requests
```

#### Advantages
- ✅ Better than SCAN (no unnecessary movement)
- ✅ No starvation

---

### C-LOOK

**Type**: Circular  
**Complexity**: O(n log n)  
**Description**: Like LOOK but jumps to first request after last

#### Algorithm Steps

```
1. Sort requests
2. Move in one direction
3. Serve all requests
4. Jump to first request (circular)
5. Continue in same direction
```

#### Advantages
- ✅ Most efficient SCAN variant
- ✅ Minimal head movement

---

## 🧠 Memory Management Algorithms

### Page Replacement

#### FIFO (First In First Out)

**Description**: Replace the oldest page in memory

**Algorithm**:
```
1. Maintain queue of pages in memory
2. On page fault:
   a. Remove page from front (oldest)
   b. Add new page to back
```

**Example**:
```
Frames: 3
Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

Page Faults: 9
```

#### LRU (Least Recently Used)

**Description**: Replace the page that hasn't been used for the longest time

**Algorithm**:
```
1. Track access time for each page
2. On page fault:
   a. Find page with oldest access time
   b. Replace it
3. Update access time on each reference
```

**Example**:
```
Frames: 3
Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2

Page Faults: 7 (better than FIFO)
```

---

### Memory Allocation

#### First Fit

**Description**: Allocate first block that is large enough

**Algorithm**:
```
1. Search from beginning
2. Allocate first block ≥ required size
3. Split block if larger than needed
```

#### Best Fit

**Description**: Allocate smallest block that is large enough

**Algorithm**:
```
1. Search all blocks
2. Find smallest block ≥ required size
3. Allocate and split if needed
```

#### Worst Fit

**Description**: Allocate largest available block

**Algorithm**:
```
1. Search all blocks
2. Find largest block ≥ required size
3. Allocate and split
```

---

## 📊 Performance Metrics

### CPU Scheduling Metrics

- **Throughput**: Number of processes completed per unit time
- **CPU Utilization**: Percentage of time CPU is busy
- **Turnaround Time**: Time from submission to completion
- **Waiting Time**: Time spent waiting in ready queue
- **Response Time**: Time from submission to first response

### Disk Scheduling Metrics

- **Seek Time**: Time to move head to track
- **Rotational Latency**: Time for disk to rotate to sector
- **Transfer Time**: Time to read/write data
- **Total Access Time**: Seek + Latency + Transfer

### Memory Management Metrics

- **Page Fault Rate**: Number of page faults per reference
- **Hit Ratio**: Percentage of successful memory accesses
- **Memory Utilization**: Percentage of memory in use
- **Fragmentation**: Internal and external fragmentation

---

## 🔬 Algorithm Complexity Comparison

| Algorithm | Time Complexity | Space Complexity | Optimal |
|-----------|----------------|------------------|---------|
| FCFS | O(n) | O(n) | ❌ |
| SJF (Non-preemptive) | O(n²) | O(n) | ✅ (for avg WT) |
| Priority | O(n log n) | O(n) | ❌ |
| Round Robin | O(n) | O(n) | ❌ |
| SCAN | O(n log n) | O(n) | ❌ |
| SSTF | O(n²) | O(n) | ❌ |
| LRU | O(n) | O(frames) | ❌ |

---

## 📚 References

1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley.

2. Tanenbaum, A. S., & Bos, H. (2014). *Modern Operating Systems* (4th ed.). Pearson.

3. Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.

---

**Last Updated**: 2025-01-27

