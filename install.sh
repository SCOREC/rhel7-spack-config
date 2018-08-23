#!/bin/bash 

spack install vim@8.1.0001%gcc@rhel7_4.8.5
spack install emacs@26.1%gcc@rhel7_4.8.5
spack install git@2.18.0%gcc@rhel7_4.8.5
spack install tmux@2.7%gcc@rhel7_4.8.5

spack install cmake%gcc@rhel7_4.8.5

spack install gcc@4.8.5%gcc@rhel7_4.8.5
spack install gcc@7.3.0%gcc@rhel7_4.8.5

for compiler in gcc@4.8.5 gcc@7.3.0; do 
  echo $compiler
  spack install mpich@3.2.1%${compiler}
  spack install parmetis%${compiler}
  spack install zoltan%${compiler} +parmetis
  spack install omega-h%${compiler}
  spack install pumi@develop%${compiler} +zoltan ^zoltan +parmetis
done

compiler=gcc@7.3.0
#uint/real-c hdf5 with fortran
spack install petsc%${compiler} ^hdf5 +fortran
#uint/real-c
spack install petsc%${compiler}  
#ulong/real-c
spack install petsc%${compiler} +int64

#uint/complex-c
spack install petsc%${compiler} +complex
#ulong/complex-c
spack install petsc%${compiler} +complex +int64

#uint/complex-cxx
spack install petsc%${compiler} clanguage=C++ +complex
#ulong/complex-cxx
spack install petsc%${compiler} clanguage=C++ +complex +int64
