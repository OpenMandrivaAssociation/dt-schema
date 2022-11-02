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

%description
Tools for validating DeviceTree files

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/dt*
%{py_puresitedir}/dtschema
%{py_puresitedir}/dtschema*.*-info
