export SPACK_ROOT=/opt/scorec/spack/spack0.18.1
export PATH=$SPACK_ROOT/bin:$PATH
source $SPACK_ROOT/share/spack/setup-env.sh
envDir=$SPACK_ROOT/v0181_2
export SPACK_DISABLE_LOCAL_CONFIG=true #disable use of user and system config files
export SPACK_USER_CACHE_PATH=$envDir
spack env list
spack env activate $envDir
