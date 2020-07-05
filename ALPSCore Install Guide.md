### Personal Computer (HP OMEN 15) Configration

CPU : i5 7300HQ

RAM : 8GB

GPU : 1050Ti

SSD : 40GB SATA SSD

SYSTEM : elementary OS 5.1.4 Hera



## ALPSCore Prerequisites

ALPSCore Mainpage : http://alpscore.org

ALPSCore Install.md : https://github.com/ALPSCore/ALPSCore/blob/master/INSTALL.md

To install ALPSCore, the following is needed :

1. C++ compiler: g++ >= 4.8.1 OR Intel >= 15.0 OR Clang >= 3.2
2. CMake >= 3.1
3. HDF5 library 1.10.6
4. Boost 1.73.0
5. Eigen (can be requested to be downloaded automatically by ALPSCore build)

Optional requirements:

1. An MPI library and headers for compiling multi-cpu versions of the libraries (If using ALPSCore/CT-INT, This is needed)
2. Doxygen for creating low-level documentation

##### C++ compiler & CMake :

```bash
$ sudo apt install g++
$ sudo apt install cmake
```

##### HDF5 library :

HDF Group mainpage : https://www.hdfgroup.org/

download CMake-HDF5 : https://support.hdfgroup.org/ftp/HDF5/releasesGit/hdf5-1.10/hdf5-1.10.6/src/CMake-hdf5-1.10.6.tar.gz

```bash
$ gzip -d CMake-hdf5-1.10.6.tar.gz
$ tar -xf CMake-hdf5-1.10.6.tar
$ cd CMake-hdf5-1.10.6/hdf5-1.10.6
$ sudo ./configure --prefix=/where/to/install/hdf5
$ sudo make
$ sudo make check
$ sudo make install
```

##### Boost library :

boost Mainpage : https://www.boost.org/

download boost 1.73.0 : https://dl.bintray.com/boostorg/release/1.73.0/source/boost_1_73_0.tar.gz

```bash
$ tar -xjf boost_1_73_0.tar.bz2
```



### Manual source installation

------

#### Obtaining the source code

The ALPSCore package can be obtained by Git:

```bash
$ git clone https://github.com/ALPSCore/ALPSCore.git
$ cd ALPSCore
```

#### Complilation

The ALPSCore library uses CMake as its build system.

1. Create a build directory and change to it:

   ```bash
   $ mkdir build
   $ cd build
   ```

2. Next, generate the ALPSCore build.

   ```bash
   $ cmake .. -DALPS_INSTALL_EIGEN=yes -DCMAKE_INSTALL_PREFIX=/where/to/install/ALPSCore -DBOOST_ROOT=/path/to/boost -DBoost_NO_SYSTEM_PATHS=ON -DBoost_NO_BOOST_CMAKE=ON -DHDF5_ROOT=/path/to/HDF5
   ```

3. Once the build tree successfully generated, perform the build:

   ```bash
   $ make
   ```

   on multicore machines with enough memory you can also run

   ```bash
   $ make -j njobs
   ```

   with `njobs` the number of parallel jobs to run the compilation in parallel.

4. Run the tests and install ALPSCore:

   ```bash
   $ make test
   $ make install
   ```

   The ALPScore will be installed in the directory specified in step 2 (`/where/to/install/ALPSCore` in this example).

   

### ALPSCore/CT-INT Installation

------

ALPSCore/CT-INT mainpage: https://github.com/ALPSCore/CT-INT

The CT-INT package can be installed by following steps:

1. Clone Git repository at Github:

   ```bash
   $ git clone https://github.com/ALPSCore/CT-INT.git
   ```

2. Create a build directory and change to it:

   ```bash
   $ mkdir build
   $ cd build
   ```

3. Generate the ALPSCore/CT-INT build:

   ```bash
   $ cmake -DALPSCore_DIR=/path/to/ALPSCore -DCMAKE_INSTALL_PREFIX=/where/to/install/CT-INT ../CT-INT
   ```

4. Perform the build, Run the tests and install ALPSCore/CT-INT:

   ```bash
   $ make
   $ make test
   $ make install
   ```

   

   