# 🚀 Viz-OS - Interactive Operating System Algorithm Visualization Tool

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.3.3-red.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**A comprehensive full-stack web application for visualizing and simulating various operating system algorithms**

[Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Algorithms Included](#-algorithms-included)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contributors](#-contributors)

---

## 🎯 Overview

**Viz-OS** is an educational web application designed to help students and developers understand operating system concepts through interactive visualizations. The tool provides real-time simulations of CPU scheduling, memory management, deadlock detection, and page replacement algorithms with beautiful, intuitive visualizations.

### Why Viz-OS?

- 🎓 **Educational**: Learn OS concepts through hands-on visualization
- 🎨 **Interactive**: Real-time algorithm simulation with step-by-step execution
- 📊 **Comprehensive**: Multiple algorithms with performance metrics
- 🚀 **Modern**: Built with modern web technologies
- 🔧 **Extensible**: Clean architecture for easy algorithm additions

---

## ✨ Features

### CPU Scheduling Algorithms
- ✅ **FCFS (First Come First Serve)** - Non-preemptive scheduling
- ✅ **SJF (Shortest Job First)** - Optimal for minimizing waiting time
- ✅ **Priority Scheduling** - Priority-based process execution
- ✅ **Round Robin** - Time-sliced preemptive scheduling

### Memory Management
- ✅ **Page Replacement** - FIFO and LRU algorithms
- ✅ **Memory Allocation** - Best Fit, First Fit, and Worst Fit strategies

### Deadlock Management
- ✅ **Banker's Algorithm** - Deadlock avoidance with safe sequence detection
- ✅ **Deadlock Detection** - Cycle detection in wait-for graphs

### Visualization Features
- 📈 **Gantt Charts** - Visual representation of process scheduling
- 🕸️ **Resource Allocation Graphs (RAG)** - Interactive graph visualization
- 📊 **Performance Metrics** - Average waiting time, turnaround time, CPU utilization
- 🎯 **Step-by-Step Execution** - Detailed algorithm execution traces

---

## 🛠️ Tech Stack

### Backend
- **Python 3.7+** - Core programming language
- **Flask 2.3.3** - Web framework and API server
- **Flask-CORS 4.0.0** - Cross-origin resource sharing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern design
- **Vanilla JavaScript** - Interactive functionality
- **Canvas API** - Chart rendering
- **SVG** - Graph visualizations

### Development Tools
- **Git** - Version control
- **Vercel** - Deployment platform (optional)

---

## 📁 Project Structure

```
Viz-OS/
│
├── src/
│   ├── backend/
│   │   ├── controllers/      # Request handlers
│   │   ├── routes/           # API route definitions
│   │   ├── services/         # Business logic
│   │   ├── utils/            # Utility functions
│   │   └── app.py            # Flask application entry point
│   │
│   ├── frontend/
│   │   ├── public/           # Static assets
│   │   └── src/
│   │       ├── components/   # Reusable UI components
│   │       ├── pages/        # Page components
│   │       ├── hooks/         # Custom React hooks (if using React)
│   │       ├── assets/       # Images, fonts, etc.
│   │       ├── styles/       # CSS files
│   │       └── main.jsx      # Frontend entry point
│   │
│   └── algorithms/
│       ├── FCFS.py           # First Come First Serve
│       ├── SCAN.py            # SCAN disk scheduling
│       ├── SSTF.py            # Shortest Seek Time First
│       └── RoundRobin.py     # Round Robin scheduling
│
├── docs/
│   ├── architecture.md       # System architecture documentation
│   ├── algorithms_explained.md  # Algorithm explanations
│   └── screenshots/          # Project screenshots
│
├── tests/
│   ├── backend_tests/        # Backend unit tests
│   └── frontend_tests/       # Frontend tests
│
├── README.md                 # This file
├── LICENSE                   # MIT License
├── .gitignore               # Git ignore rules
└── requirements.txt         # Python dependencies
```

---

## 🔬 Algorithms Included

### CPU Scheduling

| Algorithm | Type | Preemptive | Description |
|-----------|------|------------|-------------|
| **FCFS** | Non-preemptive | ❌ | Processes executed in arrival order |
| **SJF** | Non-preemptive | ❌ | Shortest job executed first |
| **Priority** | Both | ✅/❌ | Processes executed by priority |
| **Round Robin** | Preemptive | ✅ | Time-sliced execution with quantum |

### Disk Scheduling

| Algorithm | Description |
|-----------|-------------|
| **SCAN** | Elevator algorithm - moves in one direction |
| **SSTF** | Shortest Seek Time First |
| **LOOK** | SCAN variant that reverses at last request |
| **C-LOOK** | LOOK variant that returns to first request |

### Memory Management

| Algorithm | Type | Description |
|-----------|------|-------------|
| **FIFO** | Page Replacement | First-in-first-out page replacement |
| **LRU** | Page Replacement | Least recently used page replacement |
| **Best Fit** | Memory Allocation | Allocates smallest suitable block |
| **First Fit** | Memory Allocation | Allocates first suitable block |
| **Worst Fit** | Memory Allocation | Allocates largest available block |

---

## 🚀 Installation

### Prerequisites

- **Python 3.7 or higher**
- **pip** (Python package manager)
- **Modern web browser** (Chrome, Firefox, Edge, Safari)

### Step 1: Clone the Repository

```bash
git clone https://github.com/TEAM-UTOPIANS/Viz_OS.git
cd Viz_OS
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python --version  # Should be 3.7+
pip list          # Should show Flask and Flask-CORS
```

---

## 💻 Usage

### Running the Backend Server

```bash
# From project root
python src/backend/app.py

# Or using module syntax
python -m src.backend.app
```

The server will start on `http://localhost:5000`

**Expected Output:**
```
Starting VizOS - Interactive OS Simulation Tool
==================================================
Application: http://localhost:5000/
API Documentation: http://localhost:5000/api
Health Check: http://localhost:5000/api/health
==================================================
Press Ctrl+C to stop the server
```

### Running the Frontend

#### Option 1: Using Flask (Recommended)
The Flask server automatically serves the frontend. Just open:
```
http://localhost:5000/
```

#### Option 2: Using Python HTTP Server
```bash
cd src/frontend
python -m http.server 8000
```
Then open `http://localhost:8000`

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api` | GET | API information |
| `/api/health` | GET | Health check |
| `/api/scheduling/fcfs` | POST | FCFS scheduling |
| `/api/scheduling/sjf` | POST | SJF scheduling |
| `/api/scheduling/priority` | POST | Priority scheduling |
| `/api/scheduling/roundrobin` | POST | Round Robin scheduling |
| `/api/bankers` | POST | Banker's algorithm |
| `/api/deadlock` | POST | Deadlock detection |
| `/api/page-replacement` | POST | Page replacement |
| `/api/memory-allocation` | POST | Memory allocation |

### Example API Request

```bash
curl -X POST http://localhost:5000/api/scheduling/fcfs \
  -H "Content-Type: application/json" \
  -d '{
    "processes": [
      {"id": "P1", "arrival_time": 0, "burst_time": 5},
      {"id": "P2", "arrival_time": 1, "burst_time": 3},
      {"id": "P3", "arrival_time": 2, "burst_time": 8}
    ]
  }'
```

---

## 📚 Documentation

Comprehensive documentation is available in the `/docs` directory:

- **[Architecture Documentation](docs/architecture.md)** - System design and architecture
- **[Algorithms Explained](docs/algorithms_explained.md)** - Detailed algorithm explanations

---

## 📸 Screenshots

> **Note**: Add screenshots to `docs/screenshots/` directory

### Dashboard
![Dashboard](docs/screenshots/dashboard.png)

### CPU Scheduling Visualization
![CPU Scheduling](docs/screenshots/cpu-scheduling.png)

### Banker's Algorithm
![Banker's Algorithm](docs/screenshots/bankers.png)

---

## 🔮 Future Improvements

### Planned Features
- [ ] **Additional Algorithms**
  - [ ] C-SCAN disk scheduling
  - [ ] Optimal page replacement
  - [ ] Multi-level queue scheduling
  
- [ ] **Enhanced Visualizations**
  - [ ] 3D graph visualizations
  - [ ] Animation controls (play/pause/step)
  - [ ] Export visualizations as images
  
- [ ] **Performance Improvements**
  - [ ] Algorithm comparison mode
  - [ ] Batch processing
  - [ ] Performance benchmarking
  
- [ ] **User Experience**
  - [ ] Dark/light theme toggle
  - [ ] Responsive mobile design
  - [ ] Tutorial mode for beginners
  
- [ ] **Technical Enhancements**
  - [ ] React frontend migration
  - [ ] Unit test coverage
  - [ ] CI/CD pipeline
  - [ ] Docker containerization

### Contribution Ideas
- Add new scheduling algorithms
- Improve UI/UX design
- Write comprehensive tests
- Create video tutorials
- Translate documentation

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

### Contribution Guidelines

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   
   **Commit Message Format:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes
   - `refactor:` - Code refactoring
   - `test:` - Adding tests
   - `chore:` - Maintenance tasks

5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Contributors

<div align="center">

**TEAM-UTOPIANS**

Made with ❤️ by the Viz-OS team

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/TEAM-UTOPIANS)

</div>

---

## 🙏 Acknowledgments

- Operating System concepts from various academic resources
- Flask community for excellent documentation
- Open source contributors and maintainers

---

<div align="center">

**⭐ If you find this project helpful, please give it a star! ⭐**

[Report Bug](https://github.com/TEAM-UTOPIANS/Viz_OS/issues) • [Request Feature](https://github.com/TEAM-UTOPIANS/Viz_OS/issues) • [Documentation](docs/)

</div>
