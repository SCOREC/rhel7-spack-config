#!/bin/bash -ex

EXPECTED_ARGS=5

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` <simmetrix username> <simmetrix password> " \
       "<release string ex) 7.1-110613 > <word size=[32|64]> <dev=[yes|no]>"
  exit 1
fi

username=$1
password=$2
release=$3
wordSz=$4
dev=$5
isbeta=0
if [[ "$release" = *"beta" ]]; then
  isbeta=1
  echo "is beta"
fi

if [ "$wordSz" != "32" ] && [ "$wordSz" != "64" ]; then
  echo "Error: word size must be 32 or 64"
  exit 1
fi

if [ "$dev" != "yes" ] && [ "$dev" != "no" ]; then
  echo "Error: dev must be yes or no"
  exit 1
fi

# in vi add newlines
# %s/<\/a>/<\/a>\r/g
# to source.php( source code of support download site ) then run the command 
# grep documentation.*zip ~/Downloads/source.php | sed 's/.*documentation\/\([A-Za-z]*.zip\).*/\1/g'
# to extract the zip file names

documentation=(
GeomSimAcis.zip
GeomSimDiscrete.zip
GeomSimDiscreteModeling.zip
FieldSim.zip
GeomSimAbstract.zip
GeomSimAdvanced.zip
GeomSim.zip
GeomSimImport.zip
GeomSimVoxel.zip
MeshSimAdapt.zip
MeshSimAdvanced.zip
MeshSim.zip
ParallelMeshSimAdapt.zip
ParallelMeshSim.zip
GeomSimParasolid.zip
)

simUrl=http://www.simmetrix.com/support_area/
if [ "$dev" == "yes" ]; then
  simUrl=${simUrl}/DM
else
  simUrl=${simUrl}/M
fi

up="--user=${username} --password=${password}"

set +e
for doc in ${documentation[@]}; do 
  wget ${up} ${simUrl}/${release}/documentation/${doc}
done
set -e

# run the command
# grep linux64.tgz ~/Downloads/source.php | sed 's/.*release\/\([a-z]*-linux64.tgz\).*/\1/g'
# to extract the tarball names

components=( gmcore-linux${wordSz}.tgz gmimport-linux${wordSz}.tgz 
gmvoxel-linux${wordSz}.tgz aciskrnl-linux${wordSz}.tgz 
discrete-linux${wordSz}.tgz fdcore-linux${wordSz}.tgz
gmabstract-linux${wordSz}.tgz gmadv-linux${wordSz}.tgz 
msadapt-linux${wordSz}.tgz msadv-linux${wordSz}.tgz
mscore-linux${wordSz}.tgz msparalleladapt-linux${wordSz}.tgz 
msparallelmesh-linux${wordSz}.tgz psint-linux${wordSz}.tgz pskrnl-linux${wordSz}.tgz )

set +e
for comp in ${components[@]}; do 
  wget ${up} ${simUrl}/${release}/release/${comp}
done
set -e

# the dev releases tend not to have release notes
if [[ "$dev" == "no" && ! $isbeta ]]; then
  wget ${up} ${simUrl}/${release}/documentation/ReleaseNotes.zip
fi