Building the RPM on Fedora 25
===============

1. Create a tar.gz file from minishift binary 

```
  $ export cdk_version=3.1.0
  $ tar czvf cdk-minishift-${cdk_version}.tar.gz minishift

  #copy the tar ball 
  $ cp cdk-minishift-${cdk_version}.tar.gz ~/rpmbuild/SOURCES/

  $ rpmbuild -bb cdk-minishift.spec
```
