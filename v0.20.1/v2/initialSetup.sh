#!/bin/bash
spack add gcc@7.4.0 +binutils %gcc@4.8.5_rhel7 # Step 1
spack concretize -f
spack install
spack compiler add $(spack location -i gcc@7.4.0)
spack add gcc@11.2.0 %gcc@7.4.0
spack concretize -f
spack install
spack compiler add $(spack location -i gcc@11.2.0)
