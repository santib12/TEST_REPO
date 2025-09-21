#ifndef UTILS_H
#define UTILS_H

#include <string>
#include <vector>

class Utils {
public:
    // String manipulation
    static std::string toUpperCase(const std::string& str);
    static std::string toLowerCase(const std::string& str);
    static std::string reverse(const std::string& str);
    static std::string trim(const std::string& str);
    
    // Number utilities
    static bool isEven(int number);
    static bool isOdd(int number);
    static bool isPrime(int number);
    static int gcd(int a, int b);
    static int lcm(int a, int b);
    
    // Array utilities
    static std::vector<int> generateRandomNumbers(int count, int min, int max);
    static void printVector(const std::vector<int>& vec);
    static std::vector<int> reverseVector(const std::vector<int>& vec);
    
    // File utilities
    static bool fileExists(const std::string& filename);
    static std::string readFile(const std::string& filename);
    static bool writeFile(const std::string& filename, const std::string& content);
    
private:
    Utils() {} // Static class, prevent instantiation
};

#endif // UTILS_H