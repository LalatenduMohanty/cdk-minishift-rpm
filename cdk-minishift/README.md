Building the RPM on Fedora 25
===============

1. Export cdk_version to env

Example:

```
  $ export cdk_version=3.1.0
```

2. Create a tar.gz file from minishift binary

```
  $ tar czvf cdk-minishift-${cdk_version}.tar.gz minishift

  #copy the tar ball 
  $ cp cdk-minishift-${cdk_version}.tar.gz ~/rpmbuild/SOURCES/

  $ rpmbuild -ba cdk-minishift.spec
```
