/**
 * Process Table Component
 * Displays process details in a table format
 */

class ProcessTable {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
  }
  
  /**
   * Render process table
   * @param {Array} processes - Array of process objects
   */
  render(processes) {
    if (!processes || processes.length === 0) {
      this.container.innerHTML = '<p>No process data available</p>';
      return;
    }
    
    const table = document.createElement('table');
    table.className = 'process-table';
    
    // Create header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    
    const headers = ['Process ID', 'Arrival Time', 'Burst Time', 'Waiting Time', 'Turnaround Time', 'Completion Time'];
    headers.forEach(header => {
      const th = document.createElement('th');
      th.textContent = header;
      headerRow.appendChild(th);
    });
    
    thead.appendChild(headerRow);
    table.appendChild(thead);
    
    // Create body
    const tbody = document.createElement('tbody');
    processes.forEach(process => {
      const row = document.createElement('tr');
      
      const cells = [
        process.id,
        process.arrival_time,
        process.burst_time,
        process.waiting_time,
        process.turnaround_time,
        process.completion_time || '-'
      ];
      
      cells.forEach(cell => {
        const td = document.createElement('td');
        td.textContent = cell;
        row.appendChild(td);
      });
      
      tbody.appendChild(row);
    });
    
    table.appendChild(tbody);
    
    // Clear container and append table
    this.container.innerHTML = '';
    this.container.appendChild(table);
  }
  
  /**
   * Render metrics summary
   * @param {Object} metrics - Metrics object
   */
  renderMetrics(metrics) {
    const metricsDiv = document.createElement('div');
    metricsDiv.className = 'metrics-summary';
    
    metricsDiv.innerHTML = `
      <h3>Performance Metrics</h3>
      <div class="metric-item">
        <span class="metric-label">Average Waiting Time:</span>
        <span class="metric-value">${metrics.average_waiting_time}</span>
      </div>
      <div class="metric-item">
        <span class="metric-label">Average Turnaround Time:</span>
        <span class="metric-value">${metrics.average_turnaround_time}</span>
      </div>
      <div class="metric-item">
        <span class="metric-label">CPU Utilization:</span>
        <span class="metric-value">${metrics.cpu_utilization}%</span>
      </div>
      <div class="metric-item">
        <span class="metric-label">Throughput:</span>
        <span class="metric-value">${metrics.throughput}</span>
      </div>
    `;
    
    this.container.appendChild(metricsDiv);
  }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ProcessTable;
}

