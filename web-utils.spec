################################################################################

Summary:    Helpers for working with web server
Name:       web-utils
Version:    2.3.2
Release:    0%{?dist}
Group:      Applications/System
License:    Apache License, Version 2.0
URL:        https://kaos.sh/web-utils

Source0:    https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   bash openssl

Provides:   %{name} = %{version}-%{release}

################################################################################

%description
Helpers for working with web server.

################################################################################

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

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/*

################################################################################

%changelog
* Fri Dec 06 2024 Anton Novojilov <andy@essentialkaos.com> - 2.3.2-0
- Improved options parsing

* Sun Jun 09 2024 Anton Novojilov <andy@essentialkaos.com> - 2.3.1-0
- Improved automatic disabling of color output usage

* Thu Nov 30 2023 Anton Novojilov <andy@essentialkaos.com> - 2.3.0-0
- Improved version output
- Code refactoring

* Tue Jan 31 2023 Anton Novojilov <andy@essentialkaos.com> - 2.2.1-0
- Minor fixes

* Sun Jan 09 2022 Anton Novojilov <andy@essentialkaos.com> - 2.2.0-0
- Added command 'crt-info' for viewing information from certificates
- Added 'NO_COLOR' support
- Options parser updated to the latest version
- Code refactoring

* Sat Jan 02 2021 Anton Novojilov <andy@essentialkaos.com> - 2.1.0-0
- Fixed bug with showing CSR info
- Improved UI

* Wed Jun 10 2020 Anton Novojilov <andy@essentialkaos.com> - 2.0.0-0
- Renamed to web-utils
- Added option for key size configuration

* Sun May 31 2020 Anton Novojilov <andy@essentialkaos.com> - 1.8.1-0
- Default RSA key length changed to 2048

* Sat May 30 2020 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-0
- Added possibility to generate CSR files based on information from OpenSSL
  configuration file
- Added command 'csr-config-gen' for generating OpenSSL configuration files
  for CSR generation
- Added command 'htpasswd' for generating records for .htpasswd files
- Show key info in 'csr-info' output
- Code refactoring

* Thu May 28 2020 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- Added command '0rtt-check' for checking 0-RTT support
- Fixed usage info

* Sat Jan 18 2020 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Added option for generating ECC certificate signing request

* Wed Dec 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.5.3-0
- Removed handler for script errors

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 1.5.2-0
- Added handling of SCRIPT_DEBUG environment variable for enabling debug mode
- Added handler for script errors

* Tue Aug 07 2018 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Generating files with more strict permissions

* Mon Aug 06 2018 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- Added output name normalization for csr-gen command

* Wed Mar 14 2018 Anton Novojilov <andy@essentialkaos.com> - 1.4.2-0
- Fixed bug with cleaning temporary data

* Tue Dec 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-0
- Code refactoring

* Wed Oct 18 2017 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Added command 'csr-info' for viewing info from certificate signing request

* Mon Apr 24 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.3-0
- Arguments parser updated to v3 with fixed stderr output redirection for
  showArgWarn and showArgValWarn functions

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
