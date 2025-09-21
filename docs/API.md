# API Documentation

## C++ API

### Calculator Class

The `Calculator` class provides mathematical operations.

#### Constructor
```cpp
Calculator();
```

#### Basic Operations
```cpp
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
```

#### Advanced Operations
```cpp
double power(double base, double exponent);
double squareRoot(double number);
double factorial(int n);
```

#### Memory Functions
```cpp
void setMemory(double value);
double getMemory() const;
void clearMemory();
```

### DataProcessor Class

The `DataProcessor` class handles data analysis and manipulation.

#### Constructor
```cpp
DataProcessor();
```

#### Basic Statistics
```cpp
double calculateSum(const std::vector<int>& data);
double calculateAverage(const std::vector<int>& data);
int findMax(const std::vector<int>& data);
int findMin(const std::vector<int>& data);
```

#### Advanced Statistics
```cpp
double calculateStandardDeviation(const std::vector<int>& data);
double calculateVariance(const std::vector<int>& data);
std::vector<int> sortData(const std::vector<int>& data);
```

#### Data Manipulation
```cpp
std::vector<int> filterEven(const std::vector<int>& data);
std::vector<int> filterOdd(const std::vector<int>& data);
std::vector<int> removeDuplicates(const std::vector<int>& data);
```

### Utils Class

The `Utils` class provides utility functions.

#### String Manipulation
```cpp
static std::string toUpperCase(const std::string& str);
static std::string toLowerCase(const std::string& str);
static std::string reverse(const std::string& str);
static std::string trim(const std::string& str);
```

#### Number Utilities
```cpp
static bool isEven(int number);
static bool isOdd(int number);
static bool isPrime(int number);
static int gcd(int a, int b);
static int lcm(int a, int b);
```

## Python API

### DataAnalyzer Class

The `DataAnalyzer` class provides data analysis capabilities.

#### Constructor
```python
DataAnalyzer()
```

#### Data Management
```python
def add_data_point(self, value: float, timestamp: str, category: str, metadata: Dict[str, Any] = None)
```

#### Statistics
```python
def calculate_basic_stats(self) -> Dict[str, float]
def get_outliers(self, threshold: float = 2.0) -> List[DataPoint]
```

#### Data Filtering
```python
def filter_by_category(self, category: str) -> List[DataPoint]
```

#### Export Functions
```python
def export_to_json(self, filename: str) -> bool
def export_to_csv(self, filename: str) -> bool
```

### DataPoint Class

Represents a single data point.

#### Constructor
```python
DataPoint(value: float, timestamp: str, category: str, metadata: Dict[str, Any] = None)
```

#### Properties
- `value`: The numeric value
- `timestamp`: ISO format timestamp
- `category`: Data category
- `metadata`: Additional metadata dictionary

## Error Handling

### C++ Exceptions

- `std::invalid_argument`: Thrown for invalid inputs (e.g., division by zero)
- `std::runtime_error`: Thrown for runtime errors

### Python Exceptions

- `ValueError`: Thrown for invalid data values
- `FileNotFoundError`: Thrown when files cannot be found
- `IOError`: Thrown for file I/O errors

## Examples

See the `examples/` directory for complete usage examples.
