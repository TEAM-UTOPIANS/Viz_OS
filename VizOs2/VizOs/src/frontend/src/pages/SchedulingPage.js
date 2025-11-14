/**
 * Scheduling Page Component
 * Main page for CPU scheduling algorithm visualization
 */

class SchedulingPage {
  constructor() {
    this.apiBaseUrl = 'http://localhost:5000/api';
    this.currentAlgorithm = 'fcfs';
    this.ganttChart = null;
    this.processTable = null;
  }
  
  /**
   * Initialize the page
   */
  init() {
    this.setupEventListeners();
    this.initializeComponents();
  }
  
  /**
   * Setup event listeners
   */
  setupEventListeners() {
    // Algorithm selection
    const algorithmSelect = document.getElementById('algorithm-select');
    if (algorithmSelect) {
      algorithmSelect.addEventListener('change', (e) => {
        this.currentAlgorithm = e.target.value;
        this.updateAlgorithmUI();
      });
    }
    
    // Submit button
    const submitBtn = document.getElementById('submit-btn');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        this.executeAlgorithm();
      });
    }
    
    // Add process button
    const addProcessBtn = document.getElementById('add-process-btn');
    if (addProcessBtn) {
      addProcessBtn.addEventListener('click', () => {
        this.addProcessRow();
      });
    }
  }
  
  /**
   * Initialize components
   */
  initializeComponents() {
    // Initialize Gantt Chart
    if (document.getElementById('gantt-chart-container')) {
      this.ganttChart = new GanttChart('gantt-chart-container', {
        width: 800,
        height: 200
      });
    }
    
    // Initialize Process Table
    if (document.getElementById('process-table-container')) {
      this.processTable = new ProcessTable('process-table-container');
    }
  }
  
  /**
   * Update UI based on selected algorithm
   */
  updateAlgorithmUI() {
    // Show/hide quantum input for Round Robin
    const quantumInput = document.getElementById('quantum-input');
    if (quantumInput) {
      quantumInput.style.display = 
        this.currentAlgorithm === 'roundrobin' ? 'block' : 'none';
    }
    
    // Show/hide priority input for Priority scheduling
    const priorityInput = document.getElementById('priority-input');
    if (priorityInput) {
      priorityInput.style.display = 
        this.currentAlgorithm === 'priority' ? 'block' : 'none';
    }
  }
  
  /**
   * Collect process data from form
   */
  collectProcessData() {
    const processRows = document.querySelectorAll('.process-row');
    const processes = [];
    
    processRows.forEach((row, index) => {
      const id = row.querySelector('.process-id').value || `P${index + 1}`;
      const arrivalTime = parseInt(row.querySelector('.arrival-time').value) || 0;
      const burstTime = parseInt(row.querySelector('.burst-time').value) || 1;
      const priority = parseInt(row.querySelector('.priority')?.value) || 0;
      
      const process = {
        id: id,
        arrival_time: arrivalTime,
        burst_time: burstTime
      };
      
      if (this.currentAlgorithm === 'priority') {
        process.priority = priority;
      }
      
      processes.push(process);
    });
    
    return processes;
  }
  
  /**
   * Execute the selected algorithm
   */
  async executeAlgorithm() {
    try {
      const processes = this.collectProcessData();
      
      if (processes.length === 0) {
        alert('Please add at least one process');
        return;
      }
      
      // Show loading state
      this.showLoading(true);
      
      // Prepare request body
      const requestBody = { processes };
      
      // Add quantum for Round Robin
      if (this.currentAlgorithm === 'roundrobin') {
        const quantum = parseInt(document.getElementById('quantum').value) || 2;
        requestBody.quantum = quantum;
      }
      
      // Make API request
      const response = await fetch(
        `${this.apiBaseUrl}/scheduling/${this.currentAlgorithm}`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        }
      );
      
      const data = await response.json();
      
      if (data.success) {
        this.displayResults(data.data);
      } else {
        this.showError(data.error?.message || 'An error occurred');
      }
      
    } catch (error) {
      console.error('Error executing algorithm:', error);
      this.showError('Failed to execute algorithm. Please check if the backend server is running.');
    } finally {
      this.showLoading(false);
    }
  }
  
  /**
   * Display algorithm results
   */
  displayResults(data) {
    // Display Gantt Chart
    if (this.ganttChart && data.gantt_chart) {
      this.ganttChart.render(data.gantt_chart);
    }
    
    // Display Process Table
    if (this.processTable && data.process_details) {
      this.processTable.render(data.process_details);
      if (data.metrics) {
        this.processTable.renderMetrics(data.metrics);
      }
    }
  }
  
  /**
   * Add a new process row to the form
   */
  addProcessRow() {
    const container = document.getElementById('processes-container');
    if (!container) return;
    
    const row = document.createElement('div');
    row.className = 'process-row';
    row.innerHTML = `
      <input type="text" class="process-id" placeholder="P1" />
      <input type="number" class="arrival-time" placeholder="Arrival" min="0" />
      <input type="number" class="burst-time" placeholder="Burst" min="1" />
      <input type="number" class="priority" placeholder="Priority" style="display: none;" />
      <button class="remove-process-btn">Remove</button>
    `;
    
    // Add remove functionality
    row.querySelector('.remove-process-btn').addEventListener('click', () => {
      row.remove();
    });
    
    container.appendChild(row);
  }
  
  /**
   * Show/hide loading state
   */
  showLoading(show) {
    const loadingDiv = document.getElementById('loading');
    if (loadingDiv) {
      loadingDiv.style.display = show ? 'block' : 'none';
    }
  }
  
  /**
   * Show error message
   */
  showError(message) {
    alert(message); // Replace with better error display
  }
}

// Initialize page when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  const page = new SchedulingPage();
  page.init();
});

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = SchedulingPage;
}

