# cmake_minimum_required(VERSION <specify CMake version here>)
project(WarGameCPP)

set(CMAKE_CXX_STANDARD 17)

add_executable(WarGameCPP main.cpp war.cpp war.h)