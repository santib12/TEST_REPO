#!/usr/bin/env python3
"""
Data Analysis Module for Testing Codebase
Provides various data analysis and processing functions
"""

import json
import csv
import statistics
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import random

@dataclass
class DataPoint:
    """Represents a single data point with value and metadata"""
    value: float
    timestamp: str
    category: str
    metadata: Dict[str, Any] = None

class DataAnalyzer:
    """Main class for data analysis operations"""
    
    def __init__(self):
        self.data: List[DataPoint] = []
        self.statistics: Dict[str, float] = {}
    
    def add_data_point(self, value: float, timestamp: str, category: str, metadata: Dict[str, Any] = None):
        """Add a new data point to the analyzer"""
        data_point = DataPoint(value, timestamp, category, metadata or {})
        self.data.append(data_point)
    
    def calculate_basic_stats(self) -> Dict[str, float]:
        """Calculate basic statistics for the data"""
        if not self.data:
            return {}
        
        values = [dp.value for dp in self.data]
        
        self.statistics = {
            'count': len(values),
            'mean': statistics.mean(values),
            'median': statistics.median(values),
            'mode': statistics.mode(values) if values else 0,
            'std_dev': statistics.stdev(values) if len(values) > 1 else 0,
            'variance': statistics.variance(values) if len(values) > 1 else 0,
            'min': min(values),
            'max': max(values),
            'range': max(values) - min(values)
        }
        
        return self.statistics
    
    def filter_by_category(self, category: str) -> List[DataPoint]:
        """Filter data points by category"""
        return [dp for dp in self.data if dp.category == category]
    
    def get_outliers(self, threshold: float = 2.0) -> List[DataPoint]:
        """Find outliers using standard deviation method"""
        if not self.data:
            return []
        
        values = [dp.value for dp in self.data]
        mean = statistics.mean(values)
        std_dev = statistics.stdev(values) if len(values) > 1 else 0
        
        outliers = []
        for dp in self.data:
            z_score = abs(dp.value - mean) / std_dev if std_dev > 0 else 0
            if z_score > threshold:
                outliers.append(dp)
        
        return outliers
    
    def export_to_json(self, filename: str) -> bool:
        """Export data to JSON file"""
        try:
            data_dict = {
                'data_points': [
                    {
                        'value': dp.value,
                        'timestamp': dp.timestamp,
                        'category': dp.category,
                        'metadata': dp.metadata
                    }
                    for dp in self.data
                ],
                'statistics': self.statistics
            }
            
            with open(filename, 'w') as f:
                json.dump(data_dict, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def export_to_csv(self, filename: str) -> bool:
        """Export data to CSV file"""
        try:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['value', 'timestamp', 'category', 'metadata'])
                
                for dp in self.data:
                    writer.writerow([
                        dp.value,
                        dp.timestamp,
                        dp.category,
                        json.dumps(dp.metadata)
                    ])
            return True
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False

def generate_sample_data(count: int = 100) -> List[DataPoint]:
    """Generate sample data for testing"""
    categories = ['temperature', 'pressure', 'humidity', 'speed', 'voltage']
    data_points = []
    
    for i in range(count):
        category = random.choice(categories)
        value = random.uniform(0, 100)
        timestamp = f"2024-01-{(i % 30) + 1:02d}T{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:00Z"
        metadata = {'sensor_id': f"sensor_{i % 10}", 'location': f"room_{i % 5}"}
        
        data_points.append(DataPoint(value, timestamp, category, metadata))
    
    return data_points

def main():
    """Main function to demonstrate the data analyzer"""
    print("=== Data Analyzer Demo ===")
    
    # Create analyzer instance
    analyzer = DataAnalyzer()
    
    # Generate sample data
    sample_data = generate_sample_data(50)
    for dp in sample_data:
        analyzer.add_data_point(dp.value, dp.timestamp, dp.category, dp.metadata)
    
    # Calculate statistics
    stats = analyzer.calculate_basic_stats()
    print(f"Data Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")
    
    # Find outliers
    outliers = analyzer.get_outliers()
    print(f"\nFound {len(outliers)} outliers")
    
    # Export data
    analyzer.export_to_json('../data/data_analysis.json')
    analyzer.export_to_csv('../data/data_analysis.csv')
    print("\nData exported to JSON and CSV files")

if __name__ == "__main__":
    main()