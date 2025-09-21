# Usage Examples

## C++ Examples

### Basic Calculator Usage

```cpp
#include "calculator.h"
#include <iostream>

int main() {
    Calculator calc;
    
    // Basic operations
    std::cout << "5 + 3 = " << calc.add(5, 3) << std::endl;
    std::cout << "10 - 4 = " << calc.subtract(10, 4) << std::endl;
    std::cout << "6 * 7 = " << calc.multiply(6, 7) << std::endl;
    std::cout << "15 / 3 = " << calc.divide(15, 3) << std::endl;
    
    // Advanced operations
    std::cout << "2^8 = " << calc.power(2, 8) << std::endl;
    std::cout << "√64 = " << calc.squareRoot(64) << std::endl;
    std::cout << "5! = " << calc.factorial(5) << std::endl;
    
    return 0;
}
```

### Data Processing Example

```cpp
#include "data_processor.h"
#include <iostream>
#include <vector>

int main() {
    DataProcessor processor;
    std::vector<int> data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    // Calculate statistics
    std::cout << "Sum: " << processor.calculateSum(data) << std::endl;
    std::cout << "Average: " << processor.calculateAverage(data) << std::endl;
    std::cout << "Max: " << processor.findMax(data) << std::endl;
    std::cout << "Min: " << processor.findMin(data) << std::endl;
    
    // Filter data
    auto evenNumbers = processor.filterEven(data);
    std::cout << "Even numbers: ";
    for (int num : evenNumbers) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    return 0;
}
```

## Python Examples

### Data Analysis Example

```python
from data_analyzer import DataAnalyzer, DataPoint, generate_sample_data

# Create analyzer
analyzer = DataAnalyzer()

# Add sample data
sample_data = generate_sample_data(100)
for dp in sample_data:
    analyzer.add_data_point(dp.value, dp.timestamp, dp.category, dp.metadata)

# Calculate statistics
stats = analyzer.calculate_basic_stats()
print("Statistics:")
for key, value in stats.items():
    print(f"  {key}: {value:.2f}")

# Find outliers
outliers = analyzer.get_outliers()
print(f"Found {len(outliers)} outliers")

# Export data
analyzer.export_to_json('analysis_results.json')
analyzer.export_to_csv('analysis_results.csv')
```

### Custom Data Analysis

```python
from data_analyzer import DataAnalyzer, DataPoint

# Create analyzer
analyzer = DataAnalyzer()

# Add custom data
analyzer.add_data_point(25.5, "2024-01-01T10:00:00Z", "temperature", {"sensor": "A1"})
analyzer.add_data_point(26.1, "2024-01-01T11:00:00Z", "temperature", {"sensor": "A1"})
analyzer.add_data_point(24.8, "2024-01-01T12:00:00Z", "temperature", {"sensor": "A2"})

# Filter by category
temp_data = analyzer.filter_by_category("temperature")
print(f"Temperature readings: {len(temp_data)}")

# Calculate statistics
stats = analyzer.calculate_basic_stats()
print(f"Average temperature: {stats['mean']:.2f}°C")
```

## Build Examples

### Using Make

```bash
# Build the project
cd config
make all

# Run the program
make run

# Run tests
make test

# Clean build files
make clean
```

### Using CMake

```bash
# Create build directory
mkdir build && cd build

# Configure with CMake
cmake ../config

# Build
make

# Run
./bin/testing_codebase
```

### Python Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
cd tests
python test_runner.py

# Run data analyzer
python data_analyzer.py
```

## Testing Examples

### Running All Tests

```bash
# C++ tests (if Google Test is available)
cd config
make test

# Python tests
cd tests
python test_runner.py
```

### Individual Test Execution

```python
# Run specific test class
python -m unittest tests.test_runner.TestDataAnalyzer

# Run with verbose output
python -m unittest tests.test_runner -v
```
