## summary

The yaml files in this directory are for installing stacks of common packages
built with GCC and LLVM compilers on the SCOREC RedHat7 workstations.  The
packages are compiled with flags that support optimized execution on the various
generations of Intel and AMD CPUs.

This environment is locked to Spack version v0.13.2.

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
git clone git@github.com:spack/spack.git spack_v0.13.2
cd !$
git checkout v0.13.2
# add the simmetrix-simmodsuite package from the develop branch
git cherry-pick 5ddf5e2
# create the environment
spack env create v0132
spack env activate v0132
# copy the yaml files into the dev
cp /path/to/the/dir/with/the/yaml/files/* var/spack/environments/v0132/.
# copy the compiler yaml file into the spack etc dir
cp /path/to/the/dir/with/the/yaml/files/compilers.yaml etc/spack/.
# comment out the gcc 6.5.0, 7.4.0 and llvm sections of compilers.yaml 
# as they have not yet been installed - not sure if this is completely necessary
```

Create a sub-directory named `XX.Y-YYMMDD` and download the corresponding
Simmetrix SimModSuite tarballs and zip files into the `spack_v0.13.2` directory.

## install GCC 6.5.0

The base GCC 4.8.5 compiler provided with RedHat7 cannot compile LLVM 8.0.0. GCC
6.5.0 can so we will install it as the base compiler from which GCC 7.4.0 and
LLVM 8.0.0 will be installed.

```
spack install gcc@6.5.0
# uncomment and edit the gcc 6.5.0 section in compilers.yaml
```

## install compilers and packages

`spack.yaml` contains all the packages that will eventually be installed.  Given that we
are using compiler flags to maintain portability of the binaries between
multiple generations of AMD and Intel CPUs, we need to break installation of the
listed packages into two steps.  In the first step we will install the GCC 7.4.0
and LLVM 8.0.0 compilers and some core packages (cmake, vim, tmux, etc.) using
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
access to the gcc7.4.0 w/ mpich stack of modules.

```
module use /opt/scorec/spack/v0132/lmod/linux-rhel7-x86_64/Core
module load gcc mpich
module av
```

Fin.

## install new simmodsuite

Starting from scratch in the v0132 environment:

```
source /opt/scorec/spack/rhel7-spack-config/setupSpack.sh
spack env activate v0132
```

download and create checksum

```
cd /opt/scorec/spack/spackDev/simmetrix
mkdir <version-string>
cd !$
/opt/scorec/spack/rhel7-spack-config/downloadSimModSuite.sh <user> <pass> <version-string> 64 <dev=on|off>
/opt/scorec/spack/rhel7-spack-config/getSimModSuiteChecksums.py <version-string> ./
```

add the new version and checksums to the package file for simmodsuite

```
spack edit simmetrix-simmodsuite
#paste block for new version
```

add the following block to 

```
/opt/scorec/spack/spackDev/var/spack/environments/v0132/spack.yaml
```

under the `definitions` section 

```
  - pumiSim15-200714:
    - pumi@develop %gcc@7.4.0 +shared simmodsuite=full ~simmodsuite_version_check
      +zoltan ^zoltan+parmetis ^simmetrix-simmodsuite@15.0-200714
```

and the following line under specs:

```
 - $pumiSim15-200714 
```

to create a new pumi install using the new simmodsuite.

Install:

```
spack concretize -f  
#check the output of concretize to ensure only pumi and simmodsuite are installed
spack install
```

Update docs

```
/opt/scorec/spack/rhel7-spack-config/fixSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install
/opt/scorec/spack/rhel7-spack-config/updateSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install <version-string> <make_latest=0|1>
```
