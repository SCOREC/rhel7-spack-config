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

# install pumi with simmodsuite and shared libs using existing zoltan and cmake
# (the hashes at the specify those installs)
#spack install pumi@develop%gcc@7.3.0 +shared ~fortran +zoltan simmodsuite=full ^/uetnhbx ^/i5ahqcy

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

# install kokkos and techos with the OpenMP backend via trilinos (techos is
#  needed by omega_h).
triConfig="+shared+kokkos+openmp+teuchos~alloptpkgs~amesos~amesos2~anasazi~aztec~belos~boost~cgns~complex~dtk~epetra~epetraext~exodus~explicit_template_instantiation~float~fortran~fortrilinos~gtest~hdf5~hypre~ifpack~ifpack2~intrepid~intrepid2~isorropia~metis~minitensor~ml~muelu~mumps~nox~phalanx~piro~pnetcdf~python~rol~rythmos~sacado~shards~stk~suite-sparse~superlu~superlu-dist~teko~tempus~tpetra~x11~xsdkflags~zlib~zoltan~zoltan2"
spack install trilinos@develop%gcc@7.3.0 $triConfig ^/niuhmad
# trilinos_enable_debug=on
spack install trilinos@develop%gcc@7.3.0 +debug$triConfig ^/niuhmad

# install omega_h with the trilinos just installed (hash at the end)
spack install omega-h%gcc@7.3.0 +trilinos ^/2zim243 #~debug
spack install omega-h%gcc@7.3.0 +trilinos ^/ackkufk #+debug
