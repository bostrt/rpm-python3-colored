%global debug_package %{nil}

Name:		python3-colored
Version:	1.4.0
Release:	0%{?dist}
Summary:	Very simple Python library for color and formatting in terminal.


License:	GPLv3
URL:		https://gitlab.com/dslackw/colored
Source0:	https://gitlab.com/dslackw/colored/-/archive/%{version}/colored-%{version}.tar.gz

BuildRequires:	python3-devel

%description
Very simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups.
The following is a list of 256 colors for Xterm, containing an example
of the displayed color, Xterm Name, Xterm Number and HEX.

%prep
%setup -q -n colored-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc README.rst docs
%license COPYING
%{python3_sitelib}/colored
%{python3_sitelib}/colored-%{version}-py?.?.egg-info

%changelog

