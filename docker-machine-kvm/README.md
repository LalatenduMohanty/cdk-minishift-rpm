Building the RPM on Fedora 25
===============

1. Create a tar.gz file from minishift binary 

```
  $ tar czvf docker-machine-kvm-0.0.7.tar.gz docker-machine-driver-kvm

  #copy the tar ball 
  $ cp docker-machine-kvm-0.0.7.tar.gz ~/rpmbuild/SOURCES/

  $ rpmbuild -ba docker-machine-kvm.spec
```
