## summary

The yaml files in this directory are for installing stacks of common packages
built with GCC and LLVM compilers on the SCOREC RedHat7 workstations.  The
packages are compiled with flags that support optimized execution on the various
generations of Intel and AMD CPUs.  Note, some older generations of CPUs are
not supported

This environment is locked to Spack version v0.18.1

## contents

modules.yaml - module name and hierarchy

README.md - this file

setupSpack.sh - setup the env for using spack

spack.yaml - list of packages to install, config, and existing packages

## setup

```
git clone -b v0.18.1 git@github.com:spack/spack.git spack0.18.1
export SPACK_ROOT=/opt/scorec/spack/spack0.18.1
export PATH=$SPACK_ROOT/bin:$PATH
source $SPACK_ROOT/share/spack/setup-env.sh
# create the environment
cd spack0.18.1
mkdir v0181_0 
cd $_
spack env create -d .
spack env activate .
# copy the yaml files into the environment
cp /path/to/the/dir/with/the/yaml/files/* .
```

Comment out the gcc 6.5.0 and 10.1.0 sections of spack.yaml 
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

## install GCC 11.2.0

## install compilers and packages

In the first step we will install the GCC 11.2.0

Comment out the compilers in `spack.yaml` except the base gcc@4.8.5_rhel7 compiler

```
spack install gcc@11.2.0
```

## sanity check

If all goes well then in a new terminal the following commands should provide
access to the gcc11.2.0 w/ mpich stack of modules.

```
module use /opt/scorec/spack/v0154_2/lmod/linux-rhel7-x86_64/Core
module load gcc mpich
module av
```

Fin.

## install new simmodsuite

Starting from scratch in the environment:

```
source /opt/scorec/spack/spack0.##.#/setupSpack.sh
```

download and create checksum

```
cd /opt/scorec/spack/simmetrix
/opt/scorec/spack/rhel7-spack-config/downloadSimModSuite.sh <user> <pass> <version-string> 64 <dev=yes|no>
cd <version-string>
/opt/scorec/spack/rhel7-spack-config/getSimModSuiteChecksums.py <version-string> ./
```

add the new version and checksums to the package file for simmodsuite

```
spack edit simmetrix-simmodsuite
#paste block for new version
```

Run the following command to open the spack config yaml file for this
environment:

```
spack config edit
```

add the following block to 
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
spack find -l simmetrix-simmodsuite #find the hash for the new install
spack location -i /<hash> #get the path to the install
/opt/scorec/spack/rhel7-spack-config/fixSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install/html
/opt/scorec/spack/rhel7-spack-config/updateSimmodsuiteDocs.sh /path/to/latest/simmodsuite/install <version-string> <make_latest=0|1>
```

## Troubleshooting

### errors about packages that don't exist

During an attempted install of `pumi` with spack `v0.18.0` errors about package `armpl-gcc` not existing were hit.  It turned out that the `~/.spack` directory was the cause.  Removing the directory fixed the error.

The user home directory config/cache dir can be avoided as described here:

https://spack.readthedocs.io/en/latest/configuration.html?highlight=SPACK_USER_CONFIG_PATH#overriding-local-configuration

### printing from a package file

Python print statements `print('aksjdlkjd')` added to a package file will appear when running `spack -d install -v`.

### permission error

During the simmetrix simmodsuite install the following error was appearing:

```
363 ==> [2022-08-12-16:12:11.860125] Error: Failed to install MeshSimAdvanced
due to PermissionError: [Errno 1] Operation not permitted:
'/opt/scorec/spack/v0154_2/install/linux-rhel7-x86_64/gcc-10.1.0/simmetrix-simmodsuite-18.0-220810dev-ghwwdxua4e6rdtvjtctkx4osmanhhfce'
364 ==> [2022-08-12-16:12:11.860158] Flagging MeshSimAdvanced as failed: [Errno
1] Operation not permitted:
'/opt/scorec/spack/v0154_2/install/linux-rhel7-x86_64/gcc-10.1.0/simmetrix-simmodsuite-18.0-220810dev-ghwwdxua4e6rdtvjtctkx4osmanhhfce' 
```

This install was done through the pumi package as a dependency.  Directly
installing simmodsuite (`spack --debug install simmetrix-simmmodsuite`) gave me
a usable stack trace to the os.chmod python call that was failing.

For some reason (recent system update?) the os.chmod(...) command was failing
from spack and disabling the use of the sgidbit via:

```
spack config add "config:allow_sgid:false"
```

allowed it to proceed as described here:

https://github.com/spack/spack/issues/28407#issuecomment-1012558772



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
