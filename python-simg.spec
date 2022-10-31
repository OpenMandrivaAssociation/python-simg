Name:           python-simg
Version:        2018.12.18
Release:        1
Summary:        Python library and tools for handling Android fastboot's sparse image format
License:        MIT
Group:          Development/Python
URL:            https://github.com/dlenski/PySIMG
Source0:        https://github.com/dlenski/PySIMG/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-flit-core
BuildRequires:  python-pip

%description
Python library and tools for handling Android fastboot's sparse image format

%prep
%autosetup -p1 -n PySIMG-master

%build
%py_build

%install
%py_install

# don't conflict with android-tools
mv %{buildroot}%{_bindir}/img2simg %{buildroot}%{_bindir}/img2simg.py

%files
%{_bindir}/*
%{py_puresitedir}/pysimg-*.egg-info
%{py_puresitedir}/pysimg
