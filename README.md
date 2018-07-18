# rhel7-spack-config
rhel7 spack configuration and scripts

## useful commands

regenerate lmod module tree:

```
spack module refresh --module-type lmod --delete-tree  -y
```

## contents

compilers.yaml - compiler list
config.yaml - global config
install.sh - package installation commands
modules.yaml - hierarchical layout for lua modules
packages.yaml - system installed packages
README.md - this file
setupSpack.sh - env needed for executing spack commands
