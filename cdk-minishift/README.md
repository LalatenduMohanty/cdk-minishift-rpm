Building the RPM on Fedora 25
===============

1. Create a tar.gz file from minishift binary 

```
  $ tar czvf cdk-minishift-3.0.0.tar.gz minishift

  #copy the tar ball 
  $ cp cdk-minishift-3.0.0.tar.gz ~/rpmbuild/SOURCES/

  $ rpmbuild -ba cdk-minishift.spec
```
