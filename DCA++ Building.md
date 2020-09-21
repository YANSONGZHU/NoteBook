# DCA++ Building

## Prerequisites

Building DCA++ requires a set of tools and libraries:

- C++ compiler (tested: clang >= 3.5, gcc >= 4.9)
- [CMake](https://cmake.org) >= 3.3
- [HDF5](https://support.hdfgroup.org/HDF5) with the C++ interface (tested: 1.8.13 and 1.10)
- [FFTW3](http://www.fftw.org) **or** an FFT library with the FFTW3 interface (e.g. Intel MKL)
- [BLAS](http://www.netlib.org/blas/) and [LAPACK](http://www.netlib.org/lapack/)
- OPENMPI

```bash
$ sudo pacman -S gcc cmake hdf5 fftw blas lapack openmpi
```

## Building steps

1. Clone the [DCA++ repository](https://github.com/CompFUSE/DCA) to obtain the latest version of the master branch:

```bash
 $ git clone https://github.com/CompFUSE/DCA.git dca_source
```

2. Create a clean build directory and change to it:

```bash
 $ mkdir build && cd build
```

3. Use CMake to configure the build and generate the build files:

```bash
cmake ../dca_source \
	 -DCMAKE_CXX_COMPILER=mpicxx \
	 -DCMAKE_C_COMPILER=mpicc \
	 -DFFTW_INCLUDE_DIR=/usr/include \
	 -DFFTW_LIBRARY=/usr/lib/libfftw3.so \
	 -DDCA_WITH_TESTS_FAST=ON \
	 -DTEST_RUNNER=mpirun \
```

4. Compile the applications and tests, if enabled:

```bash
 $ make
```

On multi-core machines, you can use the `-j` option of the `make` command to parallelize the compilation and reduce the compilation time:

```bash
 $ make -j <number-of-cores>
```

5. If tests have been compiled, you can run them with:

```bash
 $ make test
```