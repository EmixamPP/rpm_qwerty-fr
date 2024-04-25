%global debug_package %{nil}

Name:       qwerty-fr
Version:    0.7.3
Release:    1%{?dist}
Summary:    Qwerty keyboard layout with French accents.

License:    MIT
URL:        https://github.com/qwerty-fr/qwerty-fr
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:  noarch

%description
QWERTY-fr is a keyboard layout that combines the best of multiple worlds:
  - Full compatibility with QWERTY, no keys are moved.
  - Extra keys to type French, Italian, and German (plus many other languages) effortlessly and fast.

%prep
%autosetup

%install
install -Dm 644 linux/us_qwerty-fr -t %{buildroot}%{_datarootdir}/X11/xkb/symbols/

gzip linux/man/qwerty-fr.7
install -Dm 644 linux/man/qwerty-fr.7.gz -t %{buildroot}%{_mandir}/man7/

%files
%{_datarootdir}/X11/xkb/symbols/us_qwerty-fr
%{_mandir}/man7/qwerty-fr.7.gz
%license linux/copyright
%doc README.md linux/keymap.txt

%changelog
* Thu Apr 25 2024 Maxime Dirksen <dev@emixam.be> - 0.7.3
- Version 0.7.3 of qwerty-fr
