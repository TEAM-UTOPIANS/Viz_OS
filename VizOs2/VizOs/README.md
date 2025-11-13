# VizOS - Interactive OS Simulation Tool

A comprehensive full-stack web application for visualizing and simulating various operating system algorithms including CPU scheduling, Banker's algorithm, deadlock detection, page replacement, and memory allocation.

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Modern web browser

### Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the backend server:**
   ```bash
   python backend/app.py
   ```

3. **Open the frontend:**
   - Open `frontend/index.html` in your browser
   - Or use: `python -m http.server 8000` in the frontend directory

## 📚 Features

- **CPU Scheduling**: FCFS, SJF, Priority, Round Robin
- **Deadlock Management**: Banker's Algorithm, Deadlock Detection
- **Memory Management**: Page Replacement, Memory Allocation
- **Interactive Visualizations**: Gantt charts, RAG graphs, performance metrics

## 🌐 Deployment

This project is configured for deployment on Vercel. See `VERCEL_DEPLOYMENT.md` for details.

## 📖 Documentation

For detailed documentation, see `docs/README.md` and `PROJECT_OVERVIEW.md`.

## 🛠️ Project Structure

```
VizOS/
├── api/              # Vercel serverless function
├── backend/          # Flask API server
├── frontend/         # Frontend application
├── docs/             # Documentation
└── requirements.txt  # Python dependencies
```

## 📄 License

MIT License

---

**Happy Learning! 🎉**

