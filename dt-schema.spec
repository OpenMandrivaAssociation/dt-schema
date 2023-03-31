Name: dt-schema
Version: 2023.01
Release: 2
Source0: https://github.com/devicetree-org/dt-schema/archive/refs/tags/%{name}-%{version}.tar.gz
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

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_install

%files
%{_bindir}/dt*
%{py_puresitedir}/dtschema
%{py_puresitedir}/dtschema*.*-info
