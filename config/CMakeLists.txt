cmake_minimum_required(VERSION 3.10)
project(TestingCodebase)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Set compiler flags
if(MSVC)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /W4")
else()
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
endif()

# Set build type if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../include)

# Source files
set(SOURCES
    ../src/main.cpp
    ../src/calculator.cpp
    ../src/data_processor.cpp
    ../src/utils.cpp
)

# Header files
set(HEADERS
    ../include/calculator.h
    ../include/data_processor.h
    ../include/utils.h
)

# Create executable
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})

# Set output directory
set_target_properties(${PROJECT_NAME} PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Optional: Add tests if Google Test is available
find_package(GTest QUIET)
if(GTest_FOUND)
    enable_testing()
    
    # Create test executable
    add_executable(test_${PROJECT_NAME}
        ../tests/test_main.cpp
        ../tests/test_calculator.cpp
        ../tests/test_data_processor.cpp
        ../tests/test_utils.cpp
        ../src/calculator.cpp
        ../src/data_processor.cpp
        ../src/utils.cpp
    )
    
    target_link_libraries(test_${PROJECT_NAME} GTest::GTest GTest::Main)
    
    # Add test
    add_test(NAME ${PROJECT_NAME}_tests COMMAND test_${PROJECT_NAME})
endif()

# Installation
install(TARGETS ${PROJECT_NAME}
    RUNTIME DESTINATION bin
)

# Print configuration summary
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS "C++ standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "Compiler: ${CMAKE_CXX_COMPILER_ID}")