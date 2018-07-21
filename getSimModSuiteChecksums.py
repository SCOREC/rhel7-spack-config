#!/usr/bin/python

import os, sys
import hashlib

def md5(fname):
  hash_md5 = hashlib.md5()
  with open(fname, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_md5.update(chunk)
    return hash_md5.hexdigest()

if len(sys.argv) != 3:
  print "Usage: {0} <version string> </path/to/tarballs>".format(sys.argv[0])
  sys.exit() 

version = sys.argv[1]
path = sys.argv[2]
dirs = os.listdir( path )

componentToLicense = { 
    'mscore': 'base',
    'fdcore': 'base',
    'gmcore': 'base',
    'msadapt': 'base',
    'aciskrnl': 'acis',
    'psint': 'parasolid',
    'pskrnl': 'parasolid',
    'discrete': 'discrete',
    'gmabstract': 'abstract',
    'gmadv': 'advmodel',
    'gmimport': 'import',
    'gmvoxel': 'voxel',
    'msadv': 'adv',
    'msparalleladapt': 'paralleladapt',
    'msparallelmesh': 'parallelmesh',
    'FieldSim': 'base',
    'GeomSim': 'base',
    'MeshSim': 'base',
    'MeshSimAdapt': 'base',
    'GeomSimAcis': 'acis',
    'GeomSimParasolid': 'parasolid',
    'GeomSimDiscrete': 'discrete',
    'GeomSimAbstract': 'abstract',
    'GeomSimAdvanced': 'advmodel',
    'GeomSimImport': 'import',
    'GeomSimVoxel': 'voxel',
    'GeomSimSolidWorks': 'parasolid',
    'GeomSimProe': 'granite',
    'MeshSimAdvanced': 'adv',
    'ParallelMeshSimAdapt': 'paralleladapt',
    'ParallelMeshSim': 'parallelmesh'
    }


resource = '       \'{name}\': [\'{md5}\', \'{lic}\'],'
components = ''
# components
for file in dirs:
   if ".tgz" in file:
      name = file.split('-')[0]
      d = {
       'name': name,
       'md5': md5(file),
       'lic': componentToLicense[name]
      }
      line = resource.format(**d)
      components = components + '\n' + line

# docs
docs = ''
for file in dirs:
   if ".zip" in file:
      name = file.split('.')[0]
      d = {
       'name': name,
       'md5': md5(file),
       'lic': componentToLicense[name]
      }
      line = resource.format(**d)
      docs = docs + '\n' + line

release = '''
{{
    \'version\': \'{version}\',
    \'components\': {{
        {components}
    }},
    \'docs\': {{
       {docs}
    }}
}}'''

d = {
 'version': version, 
 'components': components,
 'docs': docs
}
print(release.format(**d))
