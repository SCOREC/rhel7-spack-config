#!/bin/bash

spack install vim@8.1.0001%gcc@rhel7_4.8.5 +python
spack install emacs@26.1%gcc@rhel7_4.8.5
spack install git@2.18.0%gcc@rhel7_4.8.5
spack install tmux@2.7%gcc@rhel7_4.8.5
spack install gdb@8.1%gcc@rhel7_4.8.5

spack install cmake%gcc@rhel7_4.8.5

spack install llvm%gcc@rhel7_4.8.5 +clang -lldb
chmod -x /opt/scorec/spack/install/linux-rhel7-x86_64/gcc-rhel7_4.8.5/llvm-6.0.1-2haksygco2dmqxd2ucqb2b53derwcuko/bin/clang
chmod -x /opt/scorec/spack/install/linux-rhel7-x86_64/gcc-rhel7_4.8.5/llvm-6.0.1-2haksygco2dmqxd2ucqb2b53derwcuko/bin/clang-6.0

spack install gcc@4.8.5%gcc@rhel7_4.8.5
spack install gcc@7.3.0%gcc@rhel7_4.8.5

for compiler in gcc@4.8.5 gcc@7.3.0; do
  echo $compiler
  spack install mpich@3.2.1%${compiler}
  spack install parmetis%${compiler}
  spack install zoltan%${compiler} +parmetis
  spack install omega-h%${compiler}
  spack install pumi@develop%${compiler} +zoltan ^zoltan +parmetis
  spack install netcdf%${compiler}
  spack install adios%${compiler} +fortran
  spack install gsl%${compiler}
  spack install fftw%${compiler}
done

compiler=gcc@7.3.0
#uint/real-c hdf5 with fortran
spack install --keep-stage --test=ALL petsc%${compiler} ^hdf5 +fortran
#uint/real-c
spack install --keep-stage --test=ALL petsc%${compiler}
#ulong/real-c
spack install --keep-stage --test=ALL petsc%${compiler} +int64

#uint/complex-c
spack install --keep-stage --test=ALL petsc%${compiler} +complex +mumps
#ulong/complex-c
spack install --keep-stage --test=ALL petsc%${compiler} +complex +int64 +mumps

#uint/complex-cxx
spack install --keep-stage --test=ALL petsc%${compiler} clanguage=C++ +complex +mumps
#ulong/complex-cxx
spack install --keep-stage --test=ALL petsc%${compiler} clanguage=C++ +complex +int64 +mumps
