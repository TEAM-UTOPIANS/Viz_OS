# Contributing to Viz-OS

Thank you for your interest in contributing to Viz-OS! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/TEAM-UTOPIANS/Viz_OS/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. Check existing feature requests
2. Create a new issue with:
   - Clear feature description
   - Use case and benefits
   - Possible implementation approach

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make your changes**
   - Follow the code style guidelines
   - Add comments for complex logic
   - Update documentation if needed
   - Write tests for new features

4. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing feature"
   ```
   
   **Commit Message Format:**
   - `feat:` - New feature
   - `fix:` - Bug fix
   - `docs:` - Documentation changes
   - `style:` - Code style changes (formatting, etc.)
   - `refactor:` - Code refactoring
   - `test:` - Adding or updating tests
   - `chore:` - Maintenance tasks

5. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Provide a clear description
   - Reference related issues
   - Request review from maintainers

## 📝 Code Style Guidelines

### Python

- Follow **PEP 8** style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Maximum line length: 100 characters

**Example:**
```python
def calculate_average_waiting_time(processes):
    """
    Calculate average waiting time for processes.
    
    Args:
        processes: List of process dictionaries with 'waiting_time' key
        
    Returns:
        float: Average waiting time
    """
    if not processes:
        return 0.0
    
    total_waiting = sum(p['waiting_time'] for p in processes)
    return round(total_waiting / len(processes), 2)
```

### JavaScript

- Use meaningful variable names
- Add comments for complex logic
- Use ES6+ features
- Follow consistent indentation (2 spaces)

**Example:**
```javascript
/**
 * Calculate average waiting time
 * @param {Array} processes - Array of process objects
 * @returns {number} Average waiting time
 */
function calculateAverageWaitingTime(processes) {
  if (!processes || processes.length === 0) {
    return 0;
  }
  
  const totalWaiting = processes.reduce((sum, p) => sum + p.waitingTime, 0);
  return Math.round((totalWaiting / processes.length) * 100) / 100;
}
```

## 🧪 Testing

- Write unit tests for new algorithms
- Test edge cases
- Ensure all tests pass before submitting PR

**Example Test:**
```python
import unittest
from src.algorithms import FCFS

class TestFCFS(unittest.TestCase):
    def test_fcfs_basic(self):
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 3}
        ]
        result = FCFS.execute(processes)
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)
```

## 📚 Documentation

- Update README.md if adding new features
- Add algorithm explanations to `docs/algorithms_explained.md`
- Update architecture docs if changing system design
- Add inline comments for complex logic

## ✅ Pull Request Checklist

Before submitting a PR, ensure:

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] Commit messages follow convention
- [ ] No merge conflicts
- [ ] Code is reviewed by yourself

## 🎯 Areas for Contribution

- **New Algorithms**: Add more OS algorithms
- **UI/UX Improvements**: Enhance visualizations
- **Testing**: Increase test coverage
- **Documentation**: Improve docs and tutorials
- **Performance**: Optimize algorithm implementations
- **Accessibility**: Improve accessibility features

## 📞 Questions?

Feel free to open an issue for questions or discussions!

---

Thank you for contributing to Viz-OS! 🎉

