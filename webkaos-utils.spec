###############################################################################

Summary:         Helpers for working with webkaos server
Name:            webkaos-utils
Version:         1.3.2
Release:         0%{?dist}
Group:           Applications/System
License:         EKOL
URL:             https://github.com/essentialkaos/webkaos-utils

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        webkaos >= 1.9 openssl

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Helpers for working with webkaos server.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}

ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/wu

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/*

###############################################################################

%changelog
* Thu Apr 06 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.2-0
- Output errors to stderr
- Minor improvements

* Wed Feb 15 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Improved version output

* Thu Nov 17 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Code refactoring

* Sun Oct 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Dark grey color usage for some output
- Improved help output

* Thu Mar 31 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1-0
- Improved HPKP generation

* Tue Dec 08 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0-0
- Initial release
