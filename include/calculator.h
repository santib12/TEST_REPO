#ifndef CALCULATOR_H
#define CALCULATOR_H

class Calculator {
public:
    Calculator();
    ~Calculator();
    
    // Basic arithmetic operations
    double add(double a, double b);
    double subtract(double a, double b);
    double multiply(double a, double b);
    double divide(double a, double b);
    
    // Advanced operations
    double power(double base, double exponent);
    double squareRoot(double number);
    double factorial(int n);
    
    // Memory functions
    void setMemory(double value);
    double getMemory() const;
    void clearMemory();
    
private:
    double memory;
    bool isValidNumber(double number) const;
};

#endif // CALCULATOR_H