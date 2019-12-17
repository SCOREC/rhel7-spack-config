## summary

The yaml files in this directory are for installing stacks of common packages
built with GCC and LLVM compilers on the SCOREC RedHat7 workstations.  The
packages are compiled with flags that support optimized execution on the various
generations of Intel and AMD CPUs.

Note, this readme was written after installing all the packages.  There are
likely some mistakes.

## contents

compilers.yaml - compiler locations and flags
config.yaml - spack install directories and options
modules.yaml - module name and hierarchy
packages.yaml - pre-installed packages, architecture target
README.md - this file
setupSpack.sh - setup the env for using spack
spack.yaml - list of packages to install

## setup

```
git clone git@github.com:spack/spack.git spackDev
cd !$
git checkout v0.13.2
# add the simmetrix-simmodsuite package from the develop branch
git cherry-pick 5ddf5e2
# create the environment
spack env create dev
spack env activate dev
# copy the yaml files into the dev
cp /path/to/the/dir/with/the/yaml/files/* var/spack/environments/dev/.
# copy the compiler yaml file into the spack etc dir
cp /path/to/the/dir/with/the/yaml/files/compilers.yaml etc/spack/.
# comment out the gcc 6.5.0, 7.4.0 and llvm sections of compilers.yaml 
# as they have not yet been installed - not sure if this is completely necessary
```

## install GCC 6.5.0

The base GCC 4.8.5 compiler provided with RedHat7 cannot compile LLVM 9.0.0. GCC
6.5.0 can so we will install it as the base compiler from which GCC 7.4.0 and
LLVM 9.0.0 will be installed.

```
spack install gcc@6.5.0
# uncomment and edit the gcc 6.5.0 section in compilers.yaml
```

## install compilers and packages

`spack.yaml` contains all the packages that will eventually be installed.  Given that we
are using compiler flags to maintain portability of the binaries between
multiple generations of AMD and Intel CPUs, we need to break installation of the
listed packages into two steps.  In the first step we will install the GCC 7.4.0
and LLVM 9.0.0 compilers and some core packages (cmake, vim, tmux, etc.) using
GCC 6.5.0.  In the second step we add the new compilers to `compilers.yaml` with
the portability flags.

```
# comment out the last five lines of spack.yaml 
# (starting with the line '- openmpi %gcc@7.4.0 + cuda')
spack install # wait a few hours
# uncomment the last five lines in spack.yaml
spack install # wait a few hours
```

## sanity check

If all goes well then in a new terminal the following commands should provide
access to the two stacks of modules; gcc7.4.0 w/ mpich and llvm9.0.0 w/ mpich.

```
module use /opt/scorec/spack/dev/lmod/linux-rhel7-x86_64/Core
module load gcc mpich
module av
module purge
module load llvm mpich
module av
```

Fin.
