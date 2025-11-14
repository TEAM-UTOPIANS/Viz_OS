"""
API Routes
Defines all API endpoints for the Viz-OS application
"""

from flask import Blueprint, jsonify, request
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from src.backend.controllers import scheduling_controller, memory_controller, deadlock_controller

# Create blueprint
bp = Blueprint('api', __name__)

@bp.route('/', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'success': True,
        'name': 'Viz-OS API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/api/health',
            'scheduling': {
                'fcfs': '/api/scheduling/fcfs',
                'sjf': '/api/scheduling/sjf',
                'priority': '/api/scheduling/priority',
                'roundrobin': '/api/scheduling/roundrobin'
            },
            'memory': {
                'page_replacement': '/api/page-replacement',
                'memory_allocation': '/api/memory-allocation'
            },
            'deadlock': {
                'bankers': '/api/bankers',
                'detection': '/api/deadlock'
            }
        }
    })

@bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'message': 'Viz-OS API is running'
    })

# Scheduling routes
@bp.route('/scheduling/fcfs', methods=['POST'])
def fcfs():
    """FCFS scheduling endpoint"""
    return scheduling_controller.fcfs(request)

@bp.route('/scheduling/sjf', methods=['POST'])
def sjf():
    """SJF scheduling endpoint"""
    return scheduling_controller.sjf(request)

@bp.route('/scheduling/priority', methods=['POST'])
def priority():
    """Priority scheduling endpoint"""
    return scheduling_controller.priority(request)

@bp.route('/scheduling/roundrobin', methods=['POST'])
def roundrobin():
    """Round Robin scheduling endpoint"""
    return scheduling_controller.roundrobin(request)

# Memory management routes
@bp.route('/page-replacement', methods=['POST'])
def page_replacement():
    """Page replacement endpoint"""
    return memory_controller.page_replacement(request)

@bp.route('/memory-allocation', methods=['POST'])
def memory_allocation():
    """Memory allocation endpoint"""
    return memory_controller.memory_allocation(request)

# Deadlock management routes
@bp.route('/bankers', methods=['POST'])
def bankers():
    """Banker's algorithm endpoint"""
    return deadlock_controller.bankers(request)

@bp.route('/deadlock', methods=['POST'])
def deadlock():
    """Deadlock detection endpoint"""
    return deadlock_controller.detect_deadlock(request)

