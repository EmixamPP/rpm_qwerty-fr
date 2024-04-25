# <p align=center>qwerty-fr_rpm</p>

RPM package of qwerty-fr <https://github.com/qwerty-fr/qwerty-fr>, a qwerty keyboard layout with French accents.

QWERTY-fr is a keyboard layout that combines the best of multiple worlds:
    - Full compatibility with QWERTY, no keys are moved.
    - Extra keys to type French, Italian, and German (plus many other languages) effortlessly and fast.

## Install the package
### Fedora
1. `sudo dnf copr enable emixampp/qwerty-fr`
2. `sudo dnf --refresh install qwerty-fr`

### Fedora Silverblue
1. Download the repo file corresponding to your Fedora version on the [Copr page](https://copr.fedorainfracloud.org/coprs/emixampp/qwerty-fr/)
2. `sudo rpm-ostree install qwerty-fr`
3. Reboot

### Other RPM based distro
1. Go on the [Copr builds page](https://copr.fedorainfracloud.org/coprs/emixampp/qwerty-fr/build/) and click and the latest build, then on any chroot name.
2. Click on the `qwerty-fr-x.x.x-x.fcxx.noarch.rpm` file to download it
3. `sudo rpm -iv qwerty-fr-*.noarch.rpm`
