cmake_minimum_required(VERSION 3.16)
project(HYBRID_IMU_GNSS_POSITIONING)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_REQUIRED ON)

set(SOURCES
    src/main.cpp  
)

include_directories(include)

add_executable(
  nav_system ${SOURCES}
  )

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_CXX_FLAGS_DEBUG "-g")


