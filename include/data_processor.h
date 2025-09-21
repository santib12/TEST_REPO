#ifndef DATA_PROCESSOR_H
#define DATA_PROCESSOR_H

#include <vector>
#include <string>
#include <map>

class DataProcessor {
public:
    DataProcessor();
    ~DataProcessor();
    
    // Basic statistics
    double calculateSum(const std::vector<int>& data);
    double calculateAverage(const std::vector<int>& data);
    int findMax(const std::vector<int>& data);
    int findMin(const std::vector<int>& data);
    
    // Advanced statistics
    double calculateStandardDeviation(const std::vector<int>& data);
    double calculateVariance(const std::vector<int>& data);
    std::vector<int> sortData(const std::vector<int>& data);
    
    // Data manipulation
    std::vector<int> filterEven(const std::vector<int>& data);
    std::vector<int> filterOdd(const std::vector<int>& data);
    std::vector<int> removeDuplicates(const std::vector<int>& data);
    
    // String processing
    std::vector<std::string> splitString(const std::string& str, char delimiter);
    std::string joinStrings(const std::vector<std::string>& strings, const std::string& delimiter);
    std::map<std::string, int> countWords(const std::string& text);
    
private:
    bool isValidData(const std::vector<int>& data) const;
};

#endif // DATA_PROCESSOR_H