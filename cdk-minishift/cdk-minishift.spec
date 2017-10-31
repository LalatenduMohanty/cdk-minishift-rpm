Name:           cdk-minishift
Version:        3.2.0
Release:	1%{?dist}
Summary:	Red Hat CDK Minishift binary 

License:        ASL 2.0	
URL:		https://developers.redhat.com
Source0:	 %{name}-%{version}.tar.gz

%define BIN_FILE minishift

#BuildRequires:	
Requires:       libvirt

%description
RPM for installing minishift binary which is part of Red Hat Container Development Kit

%prep
%setup -n %{name}-%{version} -c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
cp %{_builddir}/%{name}-%{version}/%{BIN_FILE} %{buildroot}/%{_bindir}/
chmod +x %{buildroot}/%{_bindir}/%{BIN_FILE}


%files
%{_bindir}/%{BIN_FILE}


%changelog
* Tue Oct 31 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Bumping the release for cdk-minishift v3.2.0

* Thu Sep 14 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Bumping the release for cdk-minishift v3.1.1

* Wed Aug 09 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Installing the minishift binary to /usr/bin
- Bumping the release for cdk-minishift v3.1.0

* Tue Jun 20 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Bumping the release for cdk-minishift

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Removing dependancy on qemu (i.e. qemu-kvm)

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- adding dependancy on qemu (i.e. qemu-kvm)

* Wed May 17 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Adding excutable access to minishift binary

* Wed Apr 26 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Initial commit
