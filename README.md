# CS127
My assignments for CS127. These will not be usable software in any way, but they should work!

### Building

#### Easy
To build any single project, just go into the directory and run the main file with python or compile all cpp files with g++ in C++11 mode. 

#### "Complicated"
If you know how to build with cmake, do that. Otherwise, run the following:

```
mkdir build
cd build
cmake ..
make
```

You can then go into any subfolder and run the appropriate python or exe files.

### Running tests

Once built with cmake, run `make tests` to run all tests.

### Format C++

If you have clang-format installed running `make format` will format all c++ code correctly according to the repo's clang-format file.

### Ninja

If you like the ninja build system run the following commands

```
mkdir build
cd build
cmake .. -GNinja
ninja
ninja test
```
