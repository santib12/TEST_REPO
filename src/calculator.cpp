#include "../include/calculator.h"
#include <cmath>
#include <stdexcept>

Calculator::Calculator() : memory(0.0) {}

Calculator::~Calculator() {}

double Calculator::add(double a, double b) {
    return a + b;
}

double Calculator::subtract(double a, double b) {
    return a - b;
}

double Calculator::multiply(double a, double b) {
    return a * b;
}

double Calculator::divide(double a, double b) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero is not allowed");
    }
    return a / b;
}

double Calculator::power(double base, double exponent) {
    return std::pow(base, exponent);
}

double Calculator::squareRoot(double number) {
    if (number < 0) {
        throw std::invalid_argument("Square root of negative number is not allowed");
    }
    return std::sqrt(number);
}

double Calculator::factorial(int n) {
    if (n < 0) {
        throw std::invalid_argument("Factorial of negative number is not allowed");
    }
    if (n == 0 || n == 1) {
        return 1;
    }
    double result = 1;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

void Calculator::setMemory(double value) {
    memory = value;
}

double Calculator::getMemory() const {
    return memory;
}

void Calculator::clearMemory() {
    memory = 0.0;
}

bool Calculator::isValidNumber(double number) const {
    return !std::isnan(number) && !std::isinf(number);
}