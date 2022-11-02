Name: dt-schema
Version: 2022.08.1
Release: 1
Source0: https://github.com/devicetree-org/dt-schema/archive/refs/tags/v%{version}.tar.gz
Summary: Tools for validating DeviceTree files
URL: https://github.com/devicetree-org/dt-schema
License: BSD
Group: Development/Tools
BuildArch: noarch
BuildRequires: python
BuildRequires: python%{pyver}dist(setuptools)
BuildRequires: python%{pyver}dist(setuptools-scm)
BuildRequires: python%{pyver}dist(pip)
BuildRequires: git-core

%description
Tools for validating DeviceTree files

%prep
%autosetup -p1

# Trick setuptools-scm into accepting the tarball
git init
git config user.name "OpenMandriva Builder"
git config user.email builder@openmandriva.org
git add .
git commit -m "Import"
git tag %{version}

echo "__version__='%{version}'" >dtschema/version.py

%build
%py_build

%install
%py_install

%files
%{_bindir}/dt*
%{py_puresitedir}/dtschema
%{py_puresitedir}/dtschema*.*-info
