#include "../include/data_processor.h"
#include <algorithm>
#include <numeric>
#include <cmath>
#include <sstream>
#include <unordered_set>

DataProcessor::DataProcessor() {}

DataProcessor::~DataProcessor() {}

double DataProcessor::calculateSum(const std::vector<int>& data) {
    if (!isValidData(data)) {
        return 0.0;
    }
    return std::accumulate(data.begin(), data.end(), 0.0);
}

double DataProcessor::calculateAverage(const std::vector<int>& data) {
    if (!isValidData(data)) {
        return 0.0;
    }
    return calculateSum(data) / data.size();
}

int DataProcessor::findMax(const std::vector<int>& data) {
    if (!isValidData(data)) {
        return 0;
    }
    return *std::max_element(data.begin(), data.end());
}

int DataProcessor::findMin(const std::vector<int>& data) {
    if (!isValidData(data)) {
        return 0;
    }
    return *std::min_element(data.begin(), data.end());
}

double DataProcessor::calculateStandardDeviation(const std::vector<int>& data) {
    if (!isValidData(data) || data.size() < 2) {
        return 0.0;
    }
    
    double mean = calculateAverage(data);
    double sumSquaredDiffs = 0.0;
    
    for (int value : data) {
        double diff = value - mean;
        sumSquaredDiffs += diff * diff;
    }
    
    return std::sqrt(sumSquaredDiffs / (data.size() - 1));
}

double DataProcessor::calculateVariance(const std::vector<int>& data) {
    if (!isValidData(data) || data.size() < 2) {
        return 0.0;
    }
    
    double mean = calculateAverage(data);
    double sumSquaredDiffs = 0.0;
    
    for (int value : data) {
        double diff = value - mean;
        sumSquaredDiffs += diff * diff;
    }
    
    return sumSquaredDiffs / (data.size() - 1);
}

std::vector<int> DataProcessor::sortData(const std::vector<int>& data) {
    std::vector<int> sortedData = data;
    std::sort(sortedData.begin(), sortedData.end());
    return sortedData;
}

std::vector<int> DataProcessor::filterEven(const std::vector<int>& data) {
    std::vector<int> evenNumbers;
    for (int value : data) {
        if (value % 2 == 0) {
            evenNumbers.push_back(value);
        }
    }
    return evenNumbers;
}

std::vector<int> DataProcessor::filterOdd(const std::vector<int>& data) {
    std::vector<int> oddNumbers;
    for (int value : data) {
        if (value % 2 != 0) {
            oddNumbers.push_back(value);
        }
    }
    return oddNumbers;
}

std::vector<int> DataProcessor::removeDuplicates(const std::vector<int>& data) {
    std::unordered_set<int> uniqueSet(data.begin(), data.end());
    return std::vector<int>(uniqueSet.begin(), uniqueSet.end());
}

std::vector<std::string> DataProcessor::splitString(const std::string& str, char delimiter) {
    std::vector<std::string> tokens;
    std::stringstream ss(str);
    std::string token;
    
    while (std::getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }
    
    return tokens;
}

std::string DataProcessor::joinStrings(const std::vector<std::string>& strings, const std::string& delimiter) {
    if (strings.empty()) {
        return "";
    }
    
    std::string result = strings[0];
    for (size_t i = 1; i < strings.size(); ++i) {
        result += delimiter + strings[i];
    }
    
    return result;
}

std::map<std::string, int> DataProcessor::countWords(const std::string& text) {
    std::map<std::string, int> wordCount;
    std::stringstream ss(text);
    std::string word;
    
    while (ss >> word) {
        // Convert to lowercase for case-insensitive counting
        std::transform(word.begin(), word.end(), word.begin(), ::tolower);
        wordCount[word]++;
    }
    
    return wordCount;
}

bool DataProcessor::isValidData(const std::vector<int>& data) const {
    return !data.empty();
}