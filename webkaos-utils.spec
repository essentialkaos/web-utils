###############################################################################

Summary:         Helpers for working with webkaos server
Name:            webkaos-utils
Version:         1.1
Release:         0%{?dist}
Group:           Applications/System
License:         EKOL
URL:             https://essentialkaos.com
Vendor:          ESSENTIAL KAOS

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
* Thu Mar 31 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1-0
- Improved HPKP generation

* Tue Dec 08 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0-0
- Initial release
