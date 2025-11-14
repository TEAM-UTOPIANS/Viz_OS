# Viz-OS Architecture Documentation

## 📐 System Architecture Overview

Viz-OS follows a **client-server architecture** with a clear separation between frontend visualization and backend algorithm computation. The system is designed to be modular, scalable, and maintainable.

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Frontend (HTML/CSS/JS)                   │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │  Pages   │  │Components│  │  Assets  │          │   │
│  │  └──────────┘  └──────────┘  └──────────┘          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            │
                    HTTP/REST API
                            │
┌─────────────────────────────────────────────────────────────┐
│                        SERVER LAYER                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Flask Backend (Python)                   │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │ Routes   │  │Services  │  │Controllers│          │   │
│  │  └──────────┘  └──────────┘  └──────────┘          │   │
│  └──────────────────────────────────────────────────────┘   │
│                            │                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │            Algorithm Layer (Pure Python)              │   │
│  │  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐            │   │
│  │  │ FCFS │  │ SJF  │  │ RR   │  │ ...  │            │   │
│  │  └──────┘  └──────┘  └──────┘  └──────┘            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture Layers

### 1. Frontend Layer

**Location**: `src/frontend/`

**Responsibilities**:
- User interface rendering
- User input collection
- Visualization rendering (Gantt charts, graphs)
- API communication
- State management

**Technology Stack**:
- HTML5 for structure
- CSS3 for styling
- Vanilla JavaScript for interactivity
- Canvas API for chart rendering
- SVG for graph visualizations

**Structure**:
```
src/frontend/
├── public/              # Static assets (images, fonts)
├── src/
│   ├── components/      # Reusable UI components
│   │   ├── GanttChart.js
│   │   ├── ProcessTable.js
│   │   └── MetricsCard.js
│   ├── pages/           # Page components
│   │   ├── SchedulingPage.js
│   │   ├── MemoryPage.js
│   │   └── DeadlockPage.js
│   ├── hooks/           # Custom hooks (if using React)
│   ├── assets/          # Images, icons
│   ├── styles/          # CSS files
│   └── main.jsx         # Entry point
```

---

### 2. Backend Layer

**Location**: `src/backend/`

**Responsibilities**:
- HTTP request handling
- Request validation
- Business logic orchestration
- Response formatting
- Error handling

**Technology Stack**:
- Python 3.7+
- Flask 2.3.3 (Web framework)
- Flask-CORS 4.0.0 (CORS handling)

**Structure**:
```
src/backend/
├── app.py               # Flask application entry point
├── controllers/         # Request handlers
│   ├── scheduling_controller.py
│   ├── memory_controller.py
│   └── deadlock_controller.py
├── routes/              # API route definitions
│   ├── scheduling_routes.py
│   ├── memory_routes.py
│   └── api_routes.py
├── services/            # Business logic
│   ├── scheduler_service.py
│   ├── memory_service.py
│   └── validation_service.py
└── utils/               # Utility functions
    ├── response_formatter.py
    ├── error_handler.py
    └── logger.py
```

---

### 3. Algorithm Layer

**Location**: `src/algorithms/`

**Responsibilities**:
- Pure algorithm implementation
- Algorithm computation
- Result generation
- No dependencies on web framework

**Structure**:
```
src/algorithms/
├── __init__.py
├── FCFS.py              # First Come First Serve
├── SJF.py               # Shortest Job First
├── Priority.py          # Priority Scheduling
├── RoundRobin.py        # Round Robin
├── SCAN.py              # SCAN disk scheduling
├── SSTF.py              # Shortest Seek Time First
├── LOOK.py              # LOOK disk scheduling
└── C_LOOK.py            # C-LOOK disk scheduling
```

---

## 🔄 Request Flow

### Typical API Request Flow

```
1. User Input (Frontend)
   │
   ├─> 2. HTTP POST Request
   │      POST /api/scheduling/fcfs
   │      Body: { processes: [...] }
   │
   ├─> 3. Route Handler (routes/scheduling_routes.py)
   │      - Validates route
   │      - Calls controller
   │
   ├─> 4. Controller (controllers/scheduling_controller.py)
   │      - Validates request data
   │      - Calls service
   │      - Formats response
   │
   ├─> 5. Service (services/scheduler_service.py)
   │      - Business logic
   │      - Calls algorithm
   │      - Processes results
   │
   ├─> 6. Algorithm (algorithms/FCFS.py)
   │      - Pure computation
   │      - Returns results
   │
   └─> 7. Response (JSON)
         {
           "success": true,
           "data": {
             "gantt_chart": [...],
             "metrics": {...}
           }
         }
```

---

## 🔌 API Design

### RESTful API Endpoints

#### Base URL: `http://localhost:5000/api`

#### CPU Scheduling Endpoints

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/scheduling/fcfs` | POST | FCFS scheduling | `{ processes: [...] }` |
| `/scheduling/sjf` | POST | SJF scheduling | `{ processes: [...] }` |
| `/scheduling/priority` | POST | Priority scheduling | `{ processes: [...] }` |
| `/scheduling/roundrobin` | POST | Round Robin | `{ processes: [...], quantum: int }` |

#### Memory Management Endpoints

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/page-replacement` | POST | Page replacement | `{ pages: [...], frames: int }` |
| `/memory-allocation` | POST | Memory allocation | `{ blocks: [...], processes: [...] }` |

#### Deadlock Management Endpoints

| Endpoint | Method | Description | Request Body |
|----------|--------|-------------|--------------|
| `/bankers` | POST | Banker's algorithm | `{ allocation: [...], max: [...], available: [...] }` |
| `/deadlock` | POST | Deadlock detection | `{ allocation: [...], request: [...] }` |

#### Utility Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/` | GET | API information |

---

## 📡 Frontend-Backend Communication

### Request Format

```javascript
// Example: FCFS Scheduling Request
fetch('http://localhost:5000/api/scheduling/fcfs', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    processes: [
      { id: 'P1', arrival_time: 0, burst_time: 5 },
      { id: 'P2', arrival_time: 1, burst_time: 3 },
      { id: 'P3', arrival_time: 2, burst_time: 8 }
    ]
  })
})
.then(response => response.json())
.then(data => {
  // Handle response
  console.log(data);
});
```

### Response Format

```json
{
  "success": true,
  "data": {
    "gantt_chart": [
      { "process": "P1", "start": 0, "end": 5 },
      { "process": "P2", "start": 5, "end": 8 },
      { "process": "P3", "start": 8, "end": 16 }
    ],
    "metrics": {
      "average_waiting_time": 3.33,
      "average_turnaround_time": 8.33,
      "cpu_utilization": 100.0
    },
    "process_details": [
      {
        "id": "P1",
        "arrival_time": 0,
        "burst_time": 5,
        "waiting_time": 0,
        "turnaround_time": 5
      }
    ]
  },
  "message": "FCFS scheduling completed successfully"
}
```

### Error Response Format

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid process data",
    "details": "burst_time must be positive"
  }
}
```

---

## 🗄️ Data Models

### Process Model

```python
{
    "id": str,              # Process identifier (e.g., "P1")
    "arrival_time": int,    # Arrival time (≥ 0)
    "burst_time": int,      # CPU burst time (> 0)
    "priority": int,        # Priority (optional, lower = higher priority)
    "waiting_time": int,    # Calculated waiting time
    "turnaround_time": int  # Calculated turnaround time
}
```

### Gantt Chart Entry

```python
{
    "process": str,         # Process ID
    "start": int,           # Start time
    "end": int              # End time
}
```

### Metrics

```python
{
    "average_waiting_time": float,
    "average_turnaround_time": float,
    "cpu_utilization": float,  # Percentage
    "throughput": float        # Processes per unit time
}
```

---

## 🔒 Error Handling

### Error Types

1. **Validation Errors** (400)
   - Invalid input data
   - Missing required fields
   - Type mismatches

2. **Algorithm Errors** (422)
   - Invalid algorithm parameters
   - Infeasible solutions

3. **Server Errors** (500)
   - Internal server errors
   - Unexpected exceptions

### Error Handling Flow

```
Request → Validation → Algorithm → Response
           ↓ (error)
        Error Handler → Formatted Error Response
```

---

## 🧪 Testing Architecture

### Test Structure

```
tests/
├── backend_tests/
│   ├── test_controllers.py
│   ├── test_services.py
│   ├── test_algorithms.py
│   └── test_routes.py
└── frontend_tests/
    ├── test_components.js
    └── test_utils.js
```

### Testing Strategy

- **Unit Tests**: Test individual functions and classes
- **Integration Tests**: Test API endpoints
- **Algorithm Tests**: Test algorithm correctness
- **Frontend Tests**: Test UI components and interactions

---

## 🚀 Deployment Architecture

### Development

```
Frontend (localhost:8000) ←→ Backend (localhost:5000)
```

### Production (Vercel)

```
User → Vercel Edge Network → Serverless Functions → Response
```

---

## 📊 Performance Considerations

1. **Algorithm Optimization**
   - Efficient data structures
   - O(n log n) or better complexity where possible

2. **API Response Time**
   - Minimal processing in controllers
   - Caching for repeated requests (future)

3. **Frontend Rendering**
   - Efficient canvas rendering
   - Debounced user inputs
   - Lazy loading of components

---

## 🔐 Security Considerations

1. **Input Validation**
   - Validate all user inputs
   - Sanitize data before processing
   - Prevent injection attacks

2. **CORS Configuration**
   - Configured for specific origins
   - Secure headers

3. **Error Messages**
   - Don't expose internal errors
   - Generic error messages for users

---

## 🔮 Future Architecture Enhancements

1. **Database Integration**
   - Store algorithm results
   - User history
   - Saved configurations

2. **WebSocket Support**
   - Real-time algorithm visualization
   - Step-by-step execution streaming

3. **Microservices**
   - Separate services for different algorithm types
   - Independent scaling

4. **Caching Layer**
   - Redis for frequently accessed data
   - Algorithm result caching

---

## 📝 Code Organization Principles

1. **Separation of Concerns**
   - Controllers handle HTTP
   - Services handle business logic
   - Algorithms are pure functions

2. **DRY (Don't Repeat Yourself)**
   - Reusable utility functions
   - Shared components

3. **SOLID Principles**
   - Single Responsibility
   - Open/Closed
   - Dependency Inversion

4. **Clean Code**
   - Meaningful names
   - Small functions
   - Comprehensive comments

---

**Last Updated**: 2025-01-27
