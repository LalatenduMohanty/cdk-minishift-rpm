Building the RPM on RHEL7
===============
- Checkout the code from https://github.com/dhiltgen/docker-machine-kvm for a specific released version as suggested in Minishift documentation
- Replace `FROM centos:7` with `FROM rhel7:latest` in  https://github.com/dhiltgen/docker-machine-kvm/blob/master/Dockerfile.centos7
- Build the binary i.e. `make`
- Rename `docker-machine-driver-kvm-centos7` to `docker-machine-driver-kvm` 
- Create a tar.gz file from minishift binary 

```
  $ tar czvf docker-machine-kvm-0.0.7.tar.gz docker-machine-driver-kvm

  #copy the tar ball 
  $ cp docker-machine-kvm-0.0.7.tar.gz ~/rpmbuild/SOURCES/

  $ rpmbuild -ba docker-machine-kvm.spec
```
