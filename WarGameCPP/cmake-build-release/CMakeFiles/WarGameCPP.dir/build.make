# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\JetBrains\CLion 2018.2\bin\cmake\win\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\JetBrains\CLion 2018.2\bin\cmake\win\bin\cmake.exe" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Projects\WarGameCPP

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Projects\WarGameCPP\cmake-build-release

# Include any dependencies generated for this target.
include CMakeFiles/WarGameCPP.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/WarGameCPP.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/WarGameCPP.dir/flags.make

CMakeFiles/WarGameCPP.dir/main.cpp.obj: CMakeFiles/WarGameCPP.dir/flags.make
CMakeFiles/WarGameCPP.dir/main.cpp.obj: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Projects\WarGameCPP\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/WarGameCPP.dir/main.cpp.obj"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\WarGameCPP.dir\main.cpp.obj -c D:\Projects\WarGameCPP\main.cpp

CMakeFiles/WarGameCPP.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/WarGameCPP.dir/main.cpp.i"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Projects\WarGameCPP\main.cpp > CMakeFiles\WarGameCPP.dir\main.cpp.i

CMakeFiles/WarGameCPP.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/WarGameCPP.dir/main.cpp.s"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Projects\WarGameCPP\main.cpp -o CMakeFiles\WarGameCPP.dir\main.cpp.s

CMakeFiles/WarGameCPP.dir/war.cpp.obj: CMakeFiles/WarGameCPP.dir/flags.make
CMakeFiles/WarGameCPP.dir/war.cpp.obj: ../war.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Projects\WarGameCPP\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/WarGameCPP.dir/war.cpp.obj"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles\WarGameCPP.dir\war.cpp.obj -c D:\Projects\WarGameCPP\war.cpp

CMakeFiles/WarGameCPP.dir/war.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/WarGameCPP.dir/war.cpp.i"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Projects\WarGameCPP\war.cpp > CMakeFiles\WarGameCPP.dir\war.cpp.i

CMakeFiles/WarGameCPP.dir/war.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/WarGameCPP.dir/war.cpp.s"
	C:\PROGRA~2\MINGW-~1\I686-8~1.0-P\mingw32\bin\G__~1.EXE $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Projects\WarGameCPP\war.cpp -o CMakeFiles\WarGameCPP.dir\war.cpp.s

# Object files for target WarGameCPP
WarGameCPP_OBJECTS = \
"CMakeFiles/WarGameCPP.dir/main.cpp.obj" \
"CMakeFiles/WarGameCPP.dir/war.cpp.obj"

# External object files for target WarGameCPP
WarGameCPP_EXTERNAL_OBJECTS =

WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/main.cpp.obj
WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/war.cpp.obj
WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/build.make
WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/linklibs.rsp
WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/objects1.rsp
WarGameCPP.exe: CMakeFiles/WarGameCPP.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Projects\WarGameCPP\cmake-build-release\CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable WarGameCPP.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\WarGameCPP.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/WarGameCPP.dir/build: WarGameCPP.exe

.PHONY : CMakeFiles/WarGameCPP.dir/build

CMakeFiles/WarGameCPP.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\WarGameCPP.dir\cmake_clean.cmake
.PHONY : CMakeFiles/WarGameCPP.dir/clean

CMakeFiles/WarGameCPP.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Projects\WarGameCPP D:\Projects\WarGameCPP D:\Projects\WarGameCPP\cmake-build-release D:\Projects\WarGameCPP\cmake-build-release D:\Projects\WarGameCPP\cmake-build-release\CMakeFiles\WarGameCPP.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/WarGameCPP.dir/depend

