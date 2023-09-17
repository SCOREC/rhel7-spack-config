export SPACK_ROOT=/opt/scorec/spack/spack0.20.1
export PATH=$SPACK_ROOT/bin:$PATH
source $SPACK_ROOT/share/spack/setup-env.sh
envDir=$SPACK_ROOT/v0201_2
export SPACK_DISABLE_LOCAL_CONFIG=true #disable use of user and system config files
export SPACK_USER_CACHE_PATH=$envDir
spack env create -d $envDir
spack env activate $envDir
spack env status
