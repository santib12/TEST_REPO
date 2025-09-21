#!/usr/bin/env python3
"""
Test Runner for the Testing Codebase
Provides automated testing functionality for all components
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock
import tempfile
import json

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_analyzer import DataAnalyzer, DataPoint, generate_sample_data

class TestDataAnalyzer(unittest.TestCase):
    """Test cases for DataAnalyzer class"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        self.analyzer = DataAnalyzer()
        self.sample_data = [
            DataPoint(10.5, "2024-01-01T10:00:00Z", "temperature"),
            DataPoint(15.2, "2024-01-01T11:00:00Z", "temperature"),
            DataPoint(12.8, "2024-01-01T12:00:00Z", "temperature"),
            DataPoint(8.3, "2024-01-01T13:00:00Z", "pressure"),
            DataPoint(9.1, "2024-01-01T14:00:00Z", "pressure")
        ]
    
    def test_add_data_point(self):
        """Test adding data points"""
        initial_count = len(self.analyzer.data)
        self.analyzer.add_data_point(25.0, "2024-01-01T15:00:00Z", "humidity")
        self.assertEqual(len(self.analyzer.data), initial_count + 1)
    
    def test_calculate_basic_stats(self):
        """Test basic statistics calculation"""
        for dp in self.sample_data:
            self.analyzer.add_data_point(dp.value, dp.timestamp, dp.category)
        
        stats = self.analyzer.calculate_basic_stats()
        
        self.assertIn('count', stats)
        self.assertIn('mean', stats)
        self.assertIn('min', stats)
        self.assertIn('max', stats)
        self.assertEqual(stats['count'], len(self.sample_data))
    
    def test_filter_by_category(self):
        """Test filtering data by category"""
        for dp in self.sample_data:
            self.analyzer.add_data_point(dp.value, dp.timestamp, dp.category)
        
        temp_data = self.analyzer.filter_by_category("temperature")
        self.assertEqual(len(temp_data), 3)
        
        pressure_data = self.analyzer.filter_by_category("pressure")
        self.assertEqual(len(pressure_data), 2)
    
    def test_get_outliers(self):
        """Test outlier detection"""
        # Add normal data
        for i in range(10):
            self.analyzer.add_data_point(10.0 + i, "2024-01-01T10:00:00Z", "test")
        
        # Add an outlier
        self.analyzer.add_data_point(100.0, "2024-01-01T11:00:00Z", "test")
        
        outliers = self.analyzer.get_outliers(threshold=1.5)
        self.assertGreater(len(outliers), 0)
    
    def test_export_to_json(self):
        """Test JSON export functionality"""
        for dp in self.sample_data:
            self.analyzer.add_data_point(dp.value, dp.timestamp, dp.category)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            result = self.analyzer.export_to_json(temp_file)
            self.assertTrue(result)
            
            # Verify file was created and contains data
            self.assertTrue(os.path.exists(temp_file))
            with open(temp_file, 'r') as f:
                data = json.load(f)
                self.assertIn('data_points', data)
                self.assertEqual(len(data['data_points']), len(self.sample_data))
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)
    
    def test_export_to_csv(self):
        """Test CSV export functionality"""
        for dp in self.sample_data:
            self.analyzer.add_data_point(dp.value, dp.timestamp, dp.category)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
            temp_file = f.name
        
        try:
            result = self.analyzer.export_to_csv(temp_file)
            self.assertTrue(result)
            
            # Verify file was created
            self.assertTrue(os.path.exists(temp_file))
        finally:
            if os.path.exists(temp_file):
                os.unlink(temp_file)

class TestDataPoint(unittest.TestCase):
    """Test cases for DataPoint class"""
    
    def test_data_point_creation(self):
        """Test DataPoint object creation"""
        dp = DataPoint(25.5, "2024-01-01T10:00:00Z", "temperature", {"sensor": "A1"})
        
        self.assertEqual(dp.value, 25.5)
        self.assertEqual(dp.timestamp, "2024-01-01T10:00:00Z")
        self.assertEqual(dp.category, "temperature")
        self.assertEqual(dp.metadata["sensor"], "A1")
    
    def test_data_point_default_metadata(self):
        """Test DataPoint with default metadata"""
        dp = DataPoint(25.5, "2024-01-01T10:00:00Z", "temperature")
        
        self.assertIsNone(dp.metadata)

class TestSampleDataGeneration(unittest.TestCase):
    """Test cases for sample data generation"""
    
    def test_generate_sample_data(self):
        """Test sample data generation"""
        sample_data = generate_sample_data(10)
        
        self.assertEqual(len(sample_data), 10)
        
        for dp in sample_data:
            self.assertIsInstance(dp, DataPoint)
            self.assertIsInstance(dp.value, float)
            self.assertIsInstance(dp.timestamp, str)
            self.assertIsInstance(dp.category, str)

def run_tests():
    """Run all tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestDataAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestDataPoint))
    suite.addTests(loader.loadTestsFromTestCase(TestSampleDataGeneration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()

if __name__ == "__main__":
    print("=== Running Test Suite ===")
    success = run_tests()
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)