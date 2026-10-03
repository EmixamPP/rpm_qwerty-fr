# <p align=center>qwerty-fr_rpm</p>

RPM package of qwerty-fr <https://github.com/qwerty-fr/qwerty-fr>, a QWERTY keyboard layout with French accents.

QWERTY-fr is a keyboard layout that combines the best of multiple worlds:
    - Full compatibility with QWERTY, no keys are moved.
    - Extra keys to type French, Italian, and German (plus many other languages) effortlessly and fast.

## Install the package
### Fedora
1. Execute `sudo dnf copr enable emixampp/qwerty-fr`
2. Execute `sudo dnf --refresh install qwerty-fr`

### Fedora Silverblue
1. Download the repo file corresponding to your Fedora version on the [Copr page](https://copr.fedorainfracloud.org/coprs/emixampp/qwerty-fr/)
2. Execute `sudo mv emixampp-qwerty-fr-fedora-*.repo /etc/yum.repos.d/`
3. Execute `sudo rpm-ostree install qwerty-fr`
4. Reboot (or add `-A` above if you do not want to reboot).

### Other RPM-based distro
1. Go to the [Copr builds page](https://copr.fedorainfracloud.org/coprs/emixampp/qwerty-fr/build/) and click on the latest build, then on any chroot name.
2. Click on the `qwerty-fr-x.x.x-x.fcxx.noarch.rpm` file to download it.
3. Execute `sudo rpm -iv qwerty-fr-*.noarch.rpm`

## Enable the keyboard layout
### GNOME
1. Execute `gnome-control-center keyboard`
2. Add a new keyboard layout, then search for "Other", and select `English (US, qwerty-fr)`
3. Delete the other layouts or switch to it in the top bar.

## How to type the extra symbols?
Please refer to the official [qwerty-fr README](https://github.com/qwerty-fr/qwerty-fr#-philosophy-overview).
