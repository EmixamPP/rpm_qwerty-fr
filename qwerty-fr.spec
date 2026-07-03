%global debug_package %{nil}

Name:       qwerty-fr
Version:    0.7.3
Release:    2%{?dist}
Summary:    Qwerty keyboard layout with French accents.

License:    MIT
URL:        https://github.com/qwerty-fr/qwerty-fr
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:    evdev.xml

BuildArch:  noarch

Requires:       libxkbcommon >= 1.13
Requires:       xkeyboard-config

%global xkb_extensions_dir %{_datadir}/xkeyboard-config.d

%description
QWERTY-fr is a keyboard layout that combines the best of multiple worlds:
  - Full compatibility with QWERTY, no keys are moved.
  - Extra keys to type French, Italian, and German (plus many other languages) effortlessly and fast.

%prep
%autosetup

%install
# XKB symbols
install -Dm0644 \
    linux/us_qwerty-fr \
    %{buildroot}%{xkb_extensions_dir}/qwerty-fr/symbols/us_qwerty-fr

# XKB registry fragment
install -Dm0644 \
    %{SOURCE1} \
    %{buildroot}%{xkb_extensions_dir}/qwerty-fr/rules/evdev.xml

# Man page
gzip -9 linux/man/qwerty-fr.7
install -Dm0644 \
    linux/man/qwerty-fr.7.gz \
    %{buildroot}%{_mandir}/man7/qwerty-fr.7.gz

%files
%license linux/copyright
%doc README.md linux/keymap.txt
%{_mandir}/man7/qwerty-fr.7.gz
%dir %{xkb_extensions_dir}/qwerty-fr
%dir %{xkb_extensions_dir}/qwerty-fr/symbols
%dir %{xkb_extensions_dir}/qwerty-fr/rules
%{xkb_extensions_dir}/qwerty-fr/symbols/us_qwerty-fr
%{xkb_extensions_dir}/qwerty-fr/rules/evdev.xml

%changelog
* Fri Jul 03 2026 Harold Mertzweiller <harold@mrtz.fr> - 0.7.3-2
- Require libxkbcommon >= 1.13
- Leverage libxkbcommon 1.13 XKB extensions
* Thu Apr 25 2024 Maxime Dirksen <dev@emixam.be> - 0.7.3
- Version 0.7.3 of qwerty-fr
