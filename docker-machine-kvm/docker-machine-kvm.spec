Name:	        docker-machine-kvm	
Version:	0.0.7
Release:	1%{?dist}
Summary:	docker machine driver for kvm
License:        ASL 2.0	
URL:		https://github.com/dhiltgen/docker-machine-kvm/

Source0:	 %{name}-%{version}.tar.gz

#BuildRequires:	
Requires:	kvm
Requires:       libvirt

%description
docker machine driver for KVM

%prep
%setup -n %{name}-%{version} -c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_exec_prefix}/local/bin/
cp %{_builddir}/%{name}-%{version}/docker-machine-driver-kvm %{buildroot}/%{_exec_prefix}/local/bin/
chmod +x %{buildroot}/%{_exec_prefix}/local/bin/docker-machine-driver-kvm

%postun
if [ $1 -eq 0 ] ; then
        rm -rf %{buildroot}/%{_exec_prefix}/local/bin/docker-machine-driver-kvm
fi

#%post

%files
%{_exec_prefix}/local/bin/docker-machine-driver-kvm

#%doc 



%changelog
* Fri May 12 2017 Lalatendu Mohanty<lmohanty@redhat.com>
- Initial commit
