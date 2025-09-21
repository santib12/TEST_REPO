# Testing Codebase

A comprehensive testing codebase designed for testing pull request functionality and development workflows. This project provides a realistic multi-language codebase with C++ and Python components, perfect for testing Git workflows, pull requests, and CI/CD pipelines.

## Project Structure

```
TEST_REPO/
├── src/                    # C++ source files
│   ├── main.cpp           # Main application entry point
│   ├── calculator.cpp     # Calculator implementation
│   ├── data_processor.cpp # Data processing functions
│   └── utils.cpp          # Utility functions
├── include/               # C++ header files
│   ├── calculator.h       # Calculator interface
│   ├── data_processor.h   # Data processor interface
│   └── utils.h            # Utility functions interface
├── tests/                 # Test files
│   ├── data_analyzer.py   # Python data analysis module
│   └── test_runner.py     # Python test runner
├── docs/                  # Documentation
│   ├── README.md          # Main documentation
│   ├── API.md             # API documentation
│   └── EXAMPLES.md        # Usage examples
├── config/                # Configuration files
│   ├── CMakeLists.txt     # CMake configuration
│   ├── Makefile           # Make configuration
│   └── .gitignore         # Git ignore rules
├── data/                  # Data files (generated)
├── examples/              # Example files (placeholder)
├── scripts/               # Build scripts (placeholder)
└── requirements.txt       # Python dependencies
```

## Features

### C++ Components

- **Calculator**: Basic and advanced mathematical operations including arithmetic, power, square root, and factorial
- **DataProcessor**: Statistical analysis and data manipulation with filtering, sorting, and string processing
- **Utils**: String manipulation, number utilities, file operations, and array utilities

### Python Components

- **DataAnalyzer**: Advanced data analysis with statistics, outlier detection, and data export
- **TestRunner**: Comprehensive test suite for all components with unit tests

## Quick Start

### Building the C++ Application

```bash
# Using Make (recommended)
cd config
make all
make run

# Using CMake
mkdir build && cd build
cmake ../config
make
./bin/testing_codebase
```

### Running Python Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
cd tests
python test_runner.py

# Run data analyzer
python data_analyzer.py
```

## Development Workflow

This codebase is designed to test various Git and development workflows:

1. **Feature Branches**: Create branches for new features
2. **Pull Requests**: Test PR creation and merging
3. **Code Reviews**: Practice code review processes
4. **CI/CD**: Test automated builds and tests
5. **Documentation**: Maintain project documentation

## Testing Pull Requests

To test pull request functionality:

1. Create a new branch: `git checkout -b feature/new-feature`
2. Make changes to the codebase
3. Commit changes: `git add . && git commit -m "Add new feature"`
4. Push branch: `git push origin feature/new-feature`
5. Create pull request through your Git platform
6. Review and merge the pull request

## Available Commands

### Build Commands
```bash
cd config
make all          # Build the project
make debug        # Build with debug flags
make release      # Build with release flags
make clean        # Clean build files
```

### Test Commands
```bash
cd config
make test         # Run all tests
make test-python  # Run Python tests only
```

### Utility Commands
```bash
cd config
make format       # Format code
make lint         # Lint code
make help         # Show all available commands
```

## Project Components

### Calculator Class
- Basic arithmetic operations (add, subtract, multiply, divide)
- Advanced operations (power, square root, factorial)
- Memory functions for storing values

### DataProcessor Class
- Statistical calculations (mean, median, standard deviation)
- Data filtering and sorting
- String processing and word counting

### Utils Class
- String manipulation utilities
- Number utilities (prime checking, GCD, LCM)
- File I/O operations
- Array utilities

### Python DataAnalyzer
- Data point management with timestamps and metadata
- Statistical analysis and outlier detection
- Export to JSON and CSV formats
- Category-based filtering

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass: `make test`
6. Commit your changes: `git commit -m 'Add amazing feature'`
7. Push to the branch: `git push origin feature/amazing-feature`
8. Submit a pull request

## Testing Strategy

This codebase includes multiple testing approaches:

- **Unit Tests**: Individual component testing
- **Integration Tests**: Cross-component functionality
- **Data Tests**: Statistical analysis validation
- **Error Handling**: Exception and edge case testing

## File Organization

- **Source Code**: Organized by language and functionality
- **Headers**: Clean separation of interface and implementation
- **Tests**: Comprehensive test coverage
- **Documentation**: Detailed API and usage documentation
- **Configuration**: Build system and dependency management

## License

This project is for testing purposes only. Use it to practice Git workflows, pull request processes, and development best practices.

## Support

For questions about using this codebase for testing purposes, please refer to the documentation in the `docs/` directory or create an issue in the repository.
