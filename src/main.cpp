#include <iostream>
#include <vector>
#include <string>
#include "../include/calculator.h"
#include "../include/data_processor.h"
#include "../include/utils.h"

int main() {
    std::cout << "=== Testing Codebase ===" << std::endl;
    
    // Test Calculator
    Calculator calc;
    std::cout << "Calculator Test:" << std::endl;
    std::cout << "5 + 3 = " << calc.add(5, 3) << std::endl;
    std::cout << "10 - 4 = " << calc.subtract(10, 4) << std::endl;
    std::cout << "6 * 7 = " << calc.multiply(6, 7) << std::endl;
    std::cout << "15 / 3 = " << calc.divide(15, 3) << std::endl;
    
    // Test Data Processor
    DataProcessor processor;
    std::vector<int> numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    
    std::cout << "\nData Processing Test:" << std::endl;
    std::cout << "Sum: " << processor.calculateSum(numbers) << std::endl;
    std::cout << "Average: " << processor.calculateAverage(numbers) << std::endl;
    std::cout << "Max: " << processor.findMax(numbers) << std::endl;
    std::cout << "Min: " << processor.findMin(numbers) << std::endl;
    
    // Test Utils
    std::cout << "\nUtility Functions Test:" << std::endl;
    std::string testString = "Hello World";
    std::cout << "Original: " << testString << std::endl;
    std::cout << "Uppercase: " << Utils::toUpperCase(testString) << std::endl;
    std::cout << "Lowercase: " << Utils::toLowerCase(testString) << std::endl;
    std::cout << "Reversed: " << Utils::reverse(testString) << std::endl;
    
    return 0;
}