"""
Algorithm Tests
Unit tests for algorithm implementations
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

from src.algorithms import FCFS, SJF, RoundRobin

class TestFCFS(unittest.TestCase):
    """Test cases for FCFS algorithm"""
    
    def test_fcfs_basic(self):
        """Test basic FCFS scheduling"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 3},
            {'id': 'P3', 'arrival_time': 2, 'burst_time': 8}
        ]
        
        result = FCFS.execute(processes)
        
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)
        self.assertIn('process_details', result)
        self.assertEqual(len(result['gantt_chart']), 3)
        self.assertEqual(len(result['process_details']), 3)
    
    def test_fcfs_single_process(self):
        """Test FCFS with single process"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5}
        ]
        
        result = FCFS.execute(processes)
        
        self.assertEqual(result['process_details'][0]['waiting_time'], 0)
        self.assertEqual(result['process_details'][0]['turnaround_time'], 5)

class TestSJF(unittest.TestCase):
    """Test cases for SJF algorithm"""
    
    def test_sjf_basic(self):
        """Test basic SJF scheduling"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 8},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 4},
            {'id': 'P3', 'arrival_time': 2, 'burst_time': 2}
        ]
        
        result = SJF.execute(processes)
        
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)
        # P3 should execute before P2 (shorter burst time)
        self.assertEqual(result['gantt_chart'][0]['process'], 'P1')

class TestRoundRobin(unittest.TestCase):
    """Test cases for Round Robin algorithm"""
    
    def test_roundrobin_basic(self):
        """Test basic Round Robin scheduling"""
        processes = [
            {'id': 'P1', 'arrival_time': 0, 'burst_time': 5},
            {'id': 'P2', 'arrival_time': 1, 'burst_time': 3}
        ]
        
        result = RoundRobin.execute(processes, quantum=2)
        
        self.assertIn('gantt_chart', result)
        self.assertIn('metrics', result)
        # Should have multiple segments due to quantum
        self.assertGreater(len(result['gantt_chart']), 2)

if __name__ == '__main__':
    unittest.main()

