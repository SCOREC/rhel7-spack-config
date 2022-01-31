## summary

The yaml files in this directory are for installing stacks of common packages
built with GCC and LLVM compilers on the SCOREC RedHat7 workstations.  The
packages are compiled with flags that support optimized execution on the various
generations of Intel and AMD CPUs.  Note, some older generations of CPUs are
not supported

This environment is locked to Spack version v0.15.4

## contents

modules.yaml - module name and hierarchy

README.md - this file

setupSpack.sh - setup the env for using spack

spack.yaml - list of packages to install, config, and existing packages

## setup

```
git clone git@github.com:spack/spack.git spack_v0.15.4
cd !$
git checkout v0.15.4
# create the environment
spack env create v0154_2
spack env activate v0154_2
# copy the yaml files into the environment
cp /path/to/the/dir/with/the/yaml/files/* var/spack/environments/v0154_2/.
```

Comment out the gcc 6.5.0 and 10.1.0 sections of compilers.yaml 
as they have not yet been installed; I'm not sure if this is completely necessary.

Create a sub-directory named `XX.Y-YYMMDD` and download the corresponding
Simmetrix SimModSuite tarballs and zip files into the `spack_v0.15.4` directory.

```
version=XX.Y-YYMMDD
mkdir $version
cd $_
/path/to/this/repo/downloadSimModSuite*.sh <args...>
cd -
#Generate checksums for the new version if needed
../rhel7-spack-config/getSimModSuiteChecksums.py $version $version/
#paste the resulting checksums into the 'simmetrix-simmodsuite' package file
spack edit simmetrix-simmodsuite
```

## install GCC 6.5.0

GCC 6.5.0 can so we will install it as the base compiler from which GCC 10.1.0
will be installed.  This is the 'core' compiler in the lua module heirarchy that
spack creates.

```
spack install gcc@6.5.0
```

Now that gcc 6.5 is installed, uncomment and edit the gcc 6.5.0 section in
compilers.yaml.

## install compilers and packages

In the first step we will install the GCC 10.1.0
and some core packages (cmake, vim, tmux, etc.) using
GCC 6.5.0.

Comment out the last four lines  
(starting with the line '- mpich %gcc@10.1.0')
of the `specs:` section of `spack.yaml`.

```
spack install # wait a few hours
```

Uncomment the last four lines in `spack.yaml` to
install the remaining packages depending on gcc 10.1.0.

```
cd /directory/with/simmodsuite/tarballs
spack install # wait a few hours
```

## sanity check

If all goes well then in a new terminal the following commands should provide
access to the gcc10.1.0 w/ mpich stack of modules.

```
module use /opt/scorec/spack/v0154_2/lmod/linux-rhel7-x86_64/Core
module load gcc mpich
module av
```

Fin.

## install new simmodsuite

Starting from scratch in the v0154_2 environment:

```
source /opt/scorec/spack/spack0.15.4/setupSpack.sh
spack env activate v0154_2
```

download and create checksum

```
cd /opt/scorec/spack/simmetrix
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
$SPACK_ROOT/var/spack/environments/v0154_2/spack.yaml
```

under the `definitions` section 

```
  - pumiSim##:
    - pumi@develop %gcc@7.4.0 +shared simmodsuite=full ~simmodsuite_version_check
      +zoltan ^zoltan+parmetis ^simmetrix-simmodsuite@15.0-200714
```

and the following line under specs:

```
 - $pumiSim##
```

, where `##` is the major version number, to create a new pumi install using the new simmodsuite.

Install:

```
spack concretize -f  
#check the output of concretize to ensure only pumi and simmodsuite are installed
spack install
```

Update docs

```
/opt/scorec/spack/rhel7-spack-config/fixSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install/html
/opt/scorec/spack/rhel7-spack-config/updateSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install <version-string> <make_latest=0|1>
```

## Troubleshooting

### printing from a package file

Python print statements `print('aksjdlkjd')` added to a package file will appear when running `spack -d install -v`.

### build-stage problems

If the spack install fails to copy SimModSuite files from the build-stage to the spack `prefix`
directory check that the build-stage is not corrupted somehow.

For example, the build-stage was corrupted after a `spack install` was run with a bad version
string for the newly added Simmetrix SimModSuite version.  Manually deleting
the problematic build-stage (`spack clean -a` was not sufficient) resolved the
issue.  Specifically, running `spack -d install -v` produced the following
error:

```
==> [2022-01-26-14:08:49.860826] MeshSimAdvanced: Executing phase: 'install'
==> [2022-01-26-14:08:52.081648] Error: FileNotFoundError: [Errno 2] No such file or directory: '/space/cwsmith/spack/v0154_2/build_stage/spack-stage-simmetrix-simmodsuite-17.0-220124dev-fgm5s4i7icj324t46tqgb6b2djgo6zog/spack-src/pskrnl/17.0-220124dev/'
```

and manually removing the
`/space/cwsmith/spack/v0154_2/build_stage/resource-pskrnl-fgm5s4i7icj324t46tqgb6b2djgo6zog`
directory after setting write permissions on the `schema` sub-directories fixed
the problem.
