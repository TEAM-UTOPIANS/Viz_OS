"""
Service Tests
Unit tests for service layer
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.backend.services import scheduler_service

class TestSchedulerService(unittest.TestCase):
    """Test cases for scheduler service"""
    
    def test_fcfs_service(self):
        """Test FCFS service"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 3}
        ]
        
        result = scheduler_service.fcfs(processes)
        
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)
        self.assertIn('process_details', result)
    
    def test_roundrobin_service(self):
        """Test Round Robin service"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 3}
        ]
        
        result = scheduler_service.roundrobin(processes, quantum=2)
        
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)

if __name__ == '__main__':
    unittest.main()

