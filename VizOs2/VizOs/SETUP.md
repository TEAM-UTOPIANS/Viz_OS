# Viz-OS Setup Guide

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Modern web browser

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/TEAM-UTOPIANS/Viz_OS.git
   cd Viz_OS
   ```

2. **Create virtual environment** (Recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**
   ```bash
   python src/backend/app.py
   ```

5. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000/`
   - API documentation: `http://localhost:5000/api`

## 📁 Project Structure

```
Viz-OS/
├── src/
│   ├── backend/          # Flask backend
│   ├── frontend/         # Frontend application
│   └── algorithms/       # Algorithm implementations
├── docs/                 # Documentation
├── tests/                # Test files
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔧 Development Setup

### Running Tests

```bash
# Run backend tests
python -m pytest tests/backend_tests/

# Or use unittest
python -m unittest discover tests/backend_tests/
```

### Code Style

- **Python**: Follow PEP 8
- **JavaScript**: Use consistent indentation (2 spaces)

### Adding New Algorithms

1. Create algorithm file in `src/algorithms/`
2. Implement `execute()` function
3. Add service method in `src/backend/services/`
4. Add controller method in `src/backend/controllers/`
5. Add route in `src/backend/routes/api_routes.py`
6. Create frontend component if needed
7. Add tests
8. Update documentation

## 🌐 API Endpoints

### Base URL: `http://localhost:5000/api`

- `GET /api` - API information
- `GET /api/health` - Health check
- `POST /api/scheduling/fcfs` - FCFS scheduling
- `POST /api/scheduling/sjf` - SJF scheduling
- `POST /api/scheduling/priority` - Priority scheduling
- `POST /api/scheduling/roundrobin` - Round Robin scheduling
- `POST /api/page-replacement` - Page replacement
- `POST /api/memory-allocation` - Memory allocation
- `POST /api/bankers` - Banker's algorithm
- `POST /api/deadlock` - Deadlock detection

## 🐛 Troubleshooting

### Import Errors

If you encounter import errors, ensure you're running from the project root:

```bash
# From project root
python src/backend/app.py
```

### Port Already in Use

If port 5000 is already in use, modify `src/backend/app.py`:

```python
app.run(host='0.0.0.0', port=5001, debug=True)  # Change port
```

### CORS Issues

CORS is already configured in `src/backend/app.py`. If you encounter CORS errors, check:

1. Flask-CORS is installed: `pip install Flask-CORS`
2. CORS is enabled in app.py

## 📚 Additional Resources

- [Architecture Documentation](docs/architecture.md)
- [Algorithm Explanations](docs/algorithms_explained.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Project Structure](PROJECT_STRUCTURE.md)

## 💡 Example Usage

### API Request Example

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

### Python Example

```python
from src.algorithms import FCFS

processes = [
    {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'id': 'P2', 'arrival_time': 1, 'burst_time': 3}
]

result = FCFS.execute(processes)
print(result['metrics'])
```

---

**Need Help?** Open an issue on GitHub or check the documentation.

