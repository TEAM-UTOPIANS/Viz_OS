/**
 * Gantt Chart Component
 * Renders Gantt chart visualization for CPU scheduling algorithms
 */

class GanttChart {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    this.canvas = document.createElement('canvas');
    this.container.appendChild(this.canvas);
    this.ctx = this.canvas.getContext('2d');
    
    this.options = {
      width: options.width || 800,
      height: options.height || 200,
      padding: options.padding || 20,
      barHeight: options.barHeight || 40,
      colors: options.colors || this._generateColors(),
      ...options
    };
    
    this.canvas.width = this.options.width;
    this.canvas.height = this.options.height;
  }
  
  /**
   * Render Gantt chart from data
   * @param {Array} ganttData - Array of {process, start, end} objects
   */
  render(ganttData) {
    if (!ganttData || ganttData.length === 0) {
      this._drawEmpty();
      return;
    }
    
    // Clear canvas
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    // Calculate scale
    const maxTime = Math.max(...ganttData.map(d => d.end));
    const scale = (this.canvas.width - 2 * this.options.padding) / maxTime;
    
    // Draw timeline
    this._drawTimeline(maxTime, scale);
    
    // Draw bars
    ganttData.forEach((segment, index) => {
      this._drawBar(segment, index, scale);
    });
  }
  
  /**
   * Draw a single bar in the Gantt chart
   */
  _drawBar(segment, index, scale) {
    const x = this.options.padding + segment.start * scale;
    const y = this.options.padding + index * (this.options.barHeight + 10);
    const width = (segment.end - segment.start) * scale;
    
    // Get color for process
    const color = this._getColor(segment.process);
    
    // Draw bar
    this.ctx.fillStyle = color;
    this.ctx.fillRect(x, y, width, this.options.barHeight);
    
    // Draw border
    this.ctx.strokeStyle = '#333';
    this.ctx.lineWidth = 1;
    this.ctx.strokeRect(x, y, width, this.options.barHeight);
    
    // Draw process label
    this.ctx.fillStyle = '#fff';
    this.ctx.font = '14px Arial';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(
      segment.process,
      x + width / 2,
      y + this.options.barHeight / 2
    );
    
    // Draw time labels
    this.ctx.fillStyle = '#333';
    this.ctx.font = '10px Arial';
    this.ctx.textAlign = 'left';
    this.ctx.fillText(segment.start.toString(), x, y - 5);
    this.ctx.textAlign = 'right';
    this.ctx.fillText(segment.end.toString(), x + width, y - 5);
  }
  
  /**
   * Draw timeline axis
   */
  _drawTimeline(maxTime, scale) {
    this.ctx.strokeStyle = '#333';
    this.ctx.lineWidth = 2;
    
    const y = this.options.padding;
    const startX = this.options.padding;
    const endX = this.canvas.width - this.options.padding;
    
    // Draw horizontal line
    this.ctx.beginPath();
    this.ctx.moveTo(startX, y);
    this.ctx.lineTo(endX, y);
    this.ctx.stroke();
    
    // Draw tick marks
    const tickInterval = Math.ceil(maxTime / 10);
    for (let i = 0; i <= maxTime; i += tickInterval) {
      const x = startX + i * scale;
      this.ctx.beginPath();
      this.ctx.moveTo(x, y);
      this.ctx.lineTo(x, y + 5);
      this.ctx.stroke();
      
      this.ctx.fillStyle = '#333';
      this.ctx.font = '10px Arial';
      this.ctx.textAlign = 'center';
      this.ctx.fillText(i.toString(), x, y + 20);
    }
  }
  
  /**
   * Draw empty state
   */
  _drawEmpty() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    this.ctx.fillStyle = '#999';
    this.ctx.font = '16px Arial';
    this.ctx.textAlign = 'center';
    this.ctx.textBaseline = 'middle';
    this.ctx.fillText(
      'No data to display',
      this.canvas.width / 2,
      this.canvas.height / 2
    );
  }
  
  /**
   * Get color for a process
   */
  _getColor(processId) {
    const colors = this.options.colors;
    const index = processId.charCodeAt(1) % colors.length;
    return colors[index];
  }
  
  /**
   * Generate default colors
   */
  _generateColors() {
    return [
      '#3498db', '#e74c3c', '#2ecc71', '#f39c12',
      '#9b59b6', '#1abc9c', '#e67e22', '#34495e'
    ];
  }
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = GanttChart;
}

