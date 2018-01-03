%global git 1
%global commit 9e8aedcb3ac1974a97315580e1226a9dab2e5ae3
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mangareader
Version:        0.3.0
Release:        20171219git%{shortcommit}%{?dist}
Summary:        Library for the BOUndary Turbulence simulation framework

License:        GPLv3
URL:            https://github.com/dschwoerer/%{name}
Source0:        https://github.com/dschwoerer/%{name}/archive/%{commit}/%{name}-%{version}.tar.gz

Requires: python3-pillow-tk
Requires: python3-natsort
Requires: python3-numpy

BuildArch: noarch

%description
mangareader is a image viewer, well suited for reading mangas.

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/bin/
install mangareader  ${RPM_BUILD_ROOT}/usr/bin/

%files
%{_bindir}/mangareader
%license LICENSE

%changelog
* Wed Jan 03 2018 David Schwörer <schword2mail.dcu.ie> - git
- Initial RPM release.
