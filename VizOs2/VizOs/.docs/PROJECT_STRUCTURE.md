# Viz-OS Project Structure

This document provides a comprehensive overview of the Viz-OS project structure.

## 📁 Complete Directory Structure

```
Viz-OS/
│
├── src/                          # Source code
│   ├── backend/                  # Backend application
│   │   ├── controllers/          # Request handlers
│   │   │   ├── __init__.py
│   │   │   ├── scheduling_controller.py
│   │   │   ├── memory_controller.py
│   │   │   └── deadlock_controller.py
│   │   ├── routes/               # API route definitions
│   │   │   ├── __init__.py
│   │   │   └── api_routes.py
│   │   ├── services/             # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── scheduler_service.py
│   │   │   ├── memory_service.py
│   │   │   └── validation_service.py
│   │   ├── utils/                # Utility functions
│   │   │   ├── __init__.py
│   │   │   ├── response_formatter.py
│   │   │   └── error_handler.py
│   │   └── app.py                # Flask application entry point
│   │
│   ├── frontend/                 # Frontend application
│   │   ├── public/               # Static assets
│   │   └── src/
│   │       ├── components/       # Reusable UI components
│   │       │   ├── GanttChart.js
│   │       │   └── ProcessTable.js
│   │       ├── pages/            # Page components
│   │       │   └── SchedulingPage.js
│   │       ├── hooks/            # Custom React hooks (if using React)
│   │       ├── assets/           # Images, fonts, etc.
│   │       ├── styles/           # CSS files
│   │       │   └── main.css
│   │       └── main.jsx          # Frontend entry point
│   │
│   └── algorithms/               # Algorithm implementations
│       ├── __init__.py
│       ├── FCFS.py               # First Come First Serve
│       ├── SJF.py                # Shortest Job First
│       ├── Priority.py           # Priority Scheduling
│       ├── RoundRobin.py         # Round Robin
│       ├── SCAN.py               # SCAN disk scheduling
│       ├── SSTF.py               # Shortest Seek Time First
│       ├── LOOK.py               # LOOK disk scheduling
│       └── C_LOOK.py             # C-LOOK disk scheduling
│
├── docs/                         # Documentation
│   ├── architecture.md           # System architecture
│   ├── algorithms_explained.md   # Algorithm explanations
│   └── screenshots/              # Project screenshots
│
├── tests/                        # Test files
│   ├── backend_tests/            # Backend unit tests
│   │   ├── __init__.py
│   │   ├── test_algorithms.py
│   │   └── test_services.py
│   └── frontend_tests/           # Frontend tests
│       └── test_components.js
│
├── README.md                     # Main project documentation
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
└── PROJECT_STRUCTURE.md          # This file
```

## 🏗️ Architecture Overview

### Backend Structure

```
backend/
├── app.py              # Flask app initialization and configuration
├── controllers/        # Handle HTTP requests, validate input, call services
├── routes/             # Define API endpoints and route handlers
├── services/           # Business logic, orchestrate algorithm calls
└── utils/              # Helper functions (response formatting, error handling)
```

**Flow**: Request → Route → Controller → Service → Algorithm → Response

### Frontend Structure

```
frontend/
├── public/             # Static files served directly
├── src/
│   ├── components/     # Reusable UI components (GanttChart, ProcessTable)
│   ├── pages/          # Page-level components (SchedulingPage)
│   ├── styles/         # CSS stylesheets
│   └── main.jsx        # Application entry point
```

### Algorithms Structure

```
algorithms/
├── FCFS.py            # CPU Scheduling
├── SJF.py             # CPU Scheduling
├── Priority.py        # CPU Scheduling
├── RoundRobin.py      # CPU Scheduling
├── SCAN.py            # Disk Scheduling
├── SSTF.py            # Disk Scheduling
├── LOOK.py            # Disk Scheduling
└── C_LOOK.py          # Disk Scheduling
```

Each algorithm file exports an `execute()` function that:
- Takes input parameters
- Performs computation
- Returns structured results

## 📝 File Naming Conventions

- **Python files**: `snake_case.py`
- **JavaScript files**: `PascalCase.js` (components), `camelCase.js` (utilities)
- **CSS files**: `kebab-case.css` or `camelCase.css`
- **Test files**: `test_*.py` or `*.test.js`

## 🔄 Data Flow

1. **User Input** → Frontend form
2. **API Request** → HTTP POST to backend
3. **Route Handler** → Validates route, calls controller
4. **Controller** → Validates data, calls service
5. **Service** → Business logic, calls algorithm
6. **Algorithm** → Pure computation, returns results
7. **Response** → JSON formatted data
8. **Visualization** → Frontend renders charts/tables

## 🧪 Testing Structure

- **Backend Tests**: Unit tests for algorithms and services
- **Frontend Tests**: Component and integration tests
- **Test Location**: Mirror source structure in `tests/` directory

## 📚 Documentation Structure

- **README.md**: Project overview, installation, usage
- **CONTRIBUTING.md**: Contribution guidelines
- **docs/architecture.md**: System design and architecture
- **docs/algorithms_explained.md**: Algorithm explanations
- **PROJECT_STRUCTURE.md**: This file

## 🚀 Getting Started

1. **Clone repository**
   ```bash
   git clone https://github.com/TEAM-UTOPIANS/Viz_OS.git
   cd Viz_OS
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run backend**
   ```bash
   python src/backend/app.py
   ```

4. **Open frontend**
   - Navigate to `http://localhost:5000/`
   - Or serve `src/frontend/` with a web server

## 📦 Key Dependencies

### Backend
- Flask 2.3.3
- Flask-CORS 4.0.0

### Frontend
- Vanilla JavaScript (no framework required)
- Canvas API for visualizations

## 🔧 Development Workflow

1. **Feature Development**
   - Create feature branch
   - Implement in appropriate directory
   - Add tests
   - Update documentation

2. **Algorithm Addition**
   - Add algorithm file to `src/algorithms/`
   - Implement `execute()` function
   - Add service method in `src/backend/services/`
   - Add controller method in `src/backend/controllers/`
   - Add route in `src/backend/routes/`
   - Create frontend component if needed

3. **Testing**
   - Write unit tests
   - Test manually
   - Ensure all tests pass

4. **Documentation**
   - Update README if needed
   - Add algorithm explanation
   - Update architecture docs if structure changes

---

**Last Updated**: 2025-01-27

