#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
#	TODO
# - check I2C
#
# BCOND:
%bcond_without smp	# don't build SMP kernel
%bcond_without up	# don't build UP kernel
%bcond_without source	# don't build kernel-source package
%bcond_without lsm	# don't build LSM/SELinux kernel

## netfilter snap 
%define		_netfilter_snap		20040105
## Program required by kernel to work.
%define		_binutils_ver		2.12
%define		_util-linux_ver		2.10o
%define		_module-init-tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_xfsprogs_ver		2.1.0
%define		_pcmcia-cs_ver		3.1.21
%define		_quota-tools_ver	3.09
%define		_PPP_ver		2.4.0
%define		_isdn4k-utils_ver	3.1pre1
%define		_nfs-utils_ver		1.0.5
%define		_procps_ver		3.1.13
%define		_oprofile_ver		0.5.3


%define		_rel		1
%define		_rc		rc2
%define		_cset		20040106_0706

%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')

%define		no_install_post_strip	1
%define		no_install_post_compress_modules	1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel
Version:	2.6.1
Release:	1.%{_rc}.%{_rel}.cset%{_cset}
Epoch:		1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}-%{_rc}.tar.bz2
# Source0-md5:	0b4e662aaec673604387f59e4c4a7703
Source1:	%{name}-autoconf.h
Source20:	%{name}-ia32.config
Source21:	%{name}-ia32-smp.config
Source30:	%{name}-amd64.config
Source31:	%{name}-amd64-smp.config
Source50:	%{name}-sparc.config
#Source51:	%{name}-sparc-smp.config
#Source60:	%{name}-sparc64.config
Source61:	%{name}-sparc64-smp.config
Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config
Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config

Source99:	%{name}-sound-oss.config
Source100:	%{name}-misc.config

Patch0:		2.6.0-ksyms-add.patch

%if "%{_cset}" != "0"
# http://www.kernel.org/pub/linux/kernel/v2.5/testing/cset/
Patch1:		cset-%{_cset}.txt.gz
%endif

Patch4:		squashfs1.3r2-patch

Patch6:		2.6.0-t3-sysfs_mem-lkml.patch

Patch8:		2.6.0-t4-PPC-ENODEV.patch

Patch14:	2.6.0-t5-documented_unused_pte_bits_i386-lkml.patch
Patch16:	2.6.0-t6-usb-irq.patch

Patch18:	2.6.0-t7-memleak-lkml.patch
Patch19:	2.6.0-t7-memleak2-lkml.patch

Patch22:	2.6.0-t8-clean-mtd-lkml.patch
Patch24:	2.6.0-t8-swap-include-lkml.patch

Patch26:	http://www.uclinux.org/pub/uClinux/uClinux-2.6.x/linux-2.6.0-test10-uc0.patch.gz

Patch28:	2.6.0-t8-VLSI-ix86-lkml.patch

Patch30:	2.6.0-t8-appletalk-SYSCTL-lkml.patch

Patch32:	2.6.0-t8-pci_dma_sync_to_device-lkml.patch

Patch34:	2.6.0-t8-umsdos-lkml.patch

Patch38:	2.6.0-t9-acpi_osl-lkml.patch

Patch40:	2.6.0-t9-forcedeth-lkml.patch

Patch44:	2.6.0-t9-PPC-smp.patch

Patch52:	2.6.0-t10-POSIX_message_queues-1of2-lkml.patch
Patch53:	2.6.0-t10-POSIX_message_queues-2of2-lkml.patch

Patch62:	2.6.0-t11-EPoX-sound-lkml.patch

Patch64:	bootsplash-3.1.3-2.6.0-test9.diff

Patch66:	2.6.0-t11-AIC_and_db4-lkml.patch

# http://bytesex.org/patches/2.6.0-1/patch-2.6.0-kraxel.gz
Patch68:	patch-2.6.0-kraxel.gz

Patch70:	2.6.0-t11-r8169-getstats.patch

Patch72:	2.6.0-t11-ALI-M1563-lkml.patch

Patch80:	linux-tdfxfb-fillrect.patch
Patch81:	linux-fbcon-margins.patch
Patch82:	linux-tdfxfb-interlace+double.patch

Patch84:	linux-sound-oss-devinit-oops.patch

Patch86:	2.6.0-t11-ini9100_dma.patch

Patch88:	2.6.0-sensors-chip-update-1of4-lkml.patch
Patch89:	2.6.0-sensors-chip-update-2of4-lkml.patch
Patch90:	2.6.0-sensors-chip-update-3of4-lkml.patch
Patch91:	2.6.0-sensors-chip-update-4of4-lkml.patch

Patch94:	acpi-20031203-2.6.0.diff.gz

Patch96:	2.6.0-mount-rainier-lkml.patch
Patch97:	2.6.0-mount-rainier-fix-lkml.patch
Patch98:	2.6.0-mount-rainier-fix-EROFS.patch

Patch100:	2.6.0-sysfs-1of4-lkml.patch
Patch101:	2.6.0-sysfs-3of4-lkml.patch
Patch102:	2.6.0-sysfs-4of4-lkml.patch

Patch106:	2.6.0-NF-time-20031226.patch

Patch110:	linux-2.6-xfs-cvs-20040102.patch
Patch111:	linux-2.6-xfs-secure-attr.patch

Patch114:	2.6.1-rc1-NF-u32-%{_netfilter_snap}.patch
Patch116:	2.6.1-rc1-NF-osf-%{_netfilter_snap}.patch

Patch120:	http://www.saout.de/misc/dm-crypt.diff

Patch122:	2.6-pnp.patch

URL:		http://www.kernel.org/
BuildRequires:	module-init-tools
BuildRequires:	perl-base
BuildRequires:	binutils >= 2.14.90.0.7
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
Autoreqprov:	no
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
PreReq:		geninitrd >= 2.57
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	module-info
Provides:	%{name}(netfilter) = %{_netfilter_snap}
Obsoletes:	kernel-modules
Conflicts:	binutils < %{_binutils_ver}
Conflicts:	util-linux < %{_util-linux_ver}
Conflicts:	module-init-tool < %{_module-init-tool_ver}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Conflicts:	quota-tools < %{_quota-tools_ver}
Conflicts:	PPP < %{_PPP_ver}
Conflicts:	isdn4k-utils < %{_isdn4k-utils_ver}
Conflicts:	nfs-utils < %{_nfs-utils_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	oprofile < %{_oprofile_ver}
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc amd64
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeß-Management, Geräte Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un système d'exploitation Linux. Le noyau traite les
fonctions basiques d'un système d'exploitation: allocation mémoire,
allocation de process, entrée/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j±dro Linuksa niezbêdne do prawid³owego dzia³ania
Twojego komputera. Zawiera w sobie sterowniki do sprzêtu znajduj±cego
siê w komputerze, takiego jak sterowniki dysków itp.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl):	J±dro Linuksa w wersji %{version} dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
PreReq:		geninitrd >= 2.26
Provides:	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	module-info
Provides:	%{name}(netfilter) = %{_netfilter_snap}
Conflicts:	binutils < %{_binutils_ver}
Conflicts:	util-linux < %{_util-linux_ver}
Conflicts:	module-init-tool < %{_module-init-tool_ver}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Conflicts:	quota-tools < %{_quota-tools_ver}
Conflicts:	PPP < %{_PPP_ver}
Conflicts:	isdn4k-utils < %{_isdn4k-utils_ver}
Conflicts:	nfs-utils < %{_nfs-utils_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	oprofile < %{_oprofile_ver}
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description smp -l de
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description smp -l fr
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nécessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand même fonctionner pour les système mono-processeur.

%description smp -l pl
Pakiet zawiera j±dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj±ce dwa lub wiêcej procesorów.
Powinno równie¿ dobrze dzia³aæ na maszynach z jednym procesorem.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Summary(pl):	J±dro Linuksa w wersji %{version} dla dyskietek startowych
Group:		Base/Kernel
PreReq:		module-init-tools
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description BOOT -l de
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l pl
Pakiet zawiera j±dro Linuksa dedykowane dyskietkom startowym i powinno
byæ u¿ywane jedynie podczas instalacji systemu. Wiele u¿ytecznych
opcji zosta³o wy³±czonych, aby jak najbardziej zmniejszyæ jego
rozmiar.

%package pcmcia
Summary:	PCMCIA modules
Summary(pl):	Modu³y PCMCIA
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	%{name}-pcmcia = %{pcmcia_version}
Provides:	kernel(pcmcia)
Conflicts:	pcmcia-cs < %{_pcmcia-cs_ver}

%description pcmcia
PCMCIA modules (%{pcmcia_version}).

%description pcmcia -l pl
Modu³y PCMCIA (%{pcmcia_version}).

%package smp-pcmcia
Summary:	PCMCIA modules for SMP kernel
Summary(pl):	Modu³y PCMCIA dla maszyn SMP
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	%{name}-pcmcia = %{pcmcia_version}
Provides:	kernel(pcmcia)
Conflicts:	pcmcia-cs < %{_pcmcia-cs_ver}

%description smp-pcmcia
PCMCIA modules for SMP kernel (%{pcmcia_version}).

%description smp-pcmcia -l pl
Modu³y PCMCIA dla maszyn SMP (%{pcmcia_version}).

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	%{name}-drm = %{drm_xfree_version}

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description drm -l pl
Sterowniki DRM (%{drm_xfree_version}).

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	%{name}-drm = %{drm_xfree_version}

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description smp-drm -l pl
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package sound-oss
Summary:	OSS kernel modules
Summary(pl):	Sterowniki d¼wiêku OSS
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}

%description sound-oss
OSS (Open Sound System) drivers.

%description sound-oss -l pl
Sterowniki d¼wiêku OSS (Open Sound System).

%package smp-sound-oss
Summary:	OSS SMP kernel modules
Summary(pl):	Sterowniki d¼wiêku OSS dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}

%description smp-sound-oss
OSS (Open Sound System) SMP sound drivers.

%description smp-sound-oss -l pl
Sterowniki OSS (Open Sound System) dla maszyn wieloprocesorowych.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	alsa-driver
Obsoletes:	alsa-driver
Obsoletes:	alsa-driver-up

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l pl
Sterowniki d¼wiêku ALSA (Advanced Linux Sound Architecture).

%package smp-sound-alsa
Summary:	ALSA SMP kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	alsa-driver
Obsoletes:	alsa-driver
Obsoletes:	alsa-driver-smp

%description smp-sound-alsa
ALSA (Advanced Linux Sound Architecture) SMP sound drivers.

%description smp-sound-alsa -l pl
Sterowniki d¼wiêku ALSA (Advanced Linux Sound Architecture) dla maszyn
wieloprocesorowych.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra Linuksa
Group:		Base/Kernel
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Provides:	kernel-i2c-devel
Provides:	%{name}-headers(netfilter) = %{_netfilter_snap}
Provides:	%{name}-headers(alsa-drivers)
Obsoletes:	kernel-i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel
or building kernel modules.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbêdne do rekompilacji j±dra
oraz budowania modu³ów j±dra.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuksa
Group:		Base/Kernel
Autoreqprov:	no
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
%ifarch %{ix86}
Requires:	bin86
%endif

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l de
Das Kernel-Source-Paket enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nécessaires pour compiler la plupart des
programmes C, car il dépend de constantes définies dans le code
source. Les sources peuvent être aussi utilisée pour compiler un noyau
personnalisé pour avoir de meilleures performances sur des matériels
particuliers.

%description source -l pl
Pakiet zawiera kod ¼ród³owy j±dra systemu.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja do j±dra Linuksa
Group:		Base/Kernel
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê do j±dra Linuksa pochodz±c± z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{version}-%{_rc}
%patch0 -p1
%if "%{_cset}" != "0"
%patch1 -p1
%endif

%patch4 -p1

%patch6 -p1

%patch8 -p1

%patch14 -p1
%patch16 -p1

%patch18 -p1
%patch19 -p1

%patch22 -p1
%patch24 -p1

%patch26 -p1

%patch28 -p1

%patch30 -p1

%patch32 -p1

%patch34 -p1

%patch38 -p1

%patch40 -p1

%patch44 -p1

%patch52 -p1
%patch53 -p1

%patch62 -p1

%patch64 -p1

%patch66 -p1

%patch68 -p1

%patch70 -p1

%patch72 -p1

%patch80 -p1
%patch81 -p1
%patch82 -p1

%patch84 -p1

%patch94 -p1

%patch96 -p1
%patch97 -p0
%patch98 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1

%patch106 -p1

%patch110 -p1
%patch111 -p1

%patch114 -p1
%patch116 -p1

%patch120 -p1

%patch122 -p1

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    Makefile.orig >Makefile

%build
BuildConfig (){
	%{?_debug:set -x}
	# is this a special kernel we want to build?
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
%ifarch %{ix86}
	if [ "$smp" = "yes" ]; then
		Config="ia32-smp"
	else
		Config="ia32"
	fi
%else
	if [ "$smp" = "yes" ]; then
		Config="%{_target_cpu}-smp"
	else
		Config="%{_target_cpu}"
	fi
%endif
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi
	echo "Building config file for KERNEL $1..."
:> arch/%{base_arch}/defconfig
	cat $RPM_SOURCE_DIR/kernel-$Config.config >> arch/%{base_arch}/defconfig
%ifarch i386
	echo "CONFIG_M386=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch i586
	echo "CONFIG_M586=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch i686
	echo "CONFIG_M686=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch athlon
	echo "CONFIG_MK7=y" >> arch/%{base_arch}/defconfig
%endif

%ifarch i386
	mv -f arch/%{base_arch}/defconfig arch/%{base_arch}/defconfig.orig
	sed -e 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/%{base_arch}/defconfig.orig > arch/%{base_arch}/defconfig
%endif

	cat %{SOURCE100} >> arch/%{base_arch}/defconfig
	cat %{SOURCE99} >> arch/%{base_arch}/defconfig
	ln -sf arch/%{base_arch}/defconfig .config

	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
	%{__make} include/linux/autoconf.h
	if [ "$smp" = "yes" ]; then
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h
	else
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h
	fi
}

BuildKernel() {
	%{?_debug:set -x}
	echo "Building kernel $1 ..."	
	%{__make} mrproper \
		RCS_FIND_IGNORE='-name build-done -prune -o'
	ln -sf arch/%{base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%else
	%{__make} clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%endif
	%{__make} %{?debug:V=1} include/linux/version.h

# make does vmlinux, modules and bzImage at once
%ifarch sparc
	sparc32 %{__make} %{?debug:V=1}
%else
	%{__make} %{?debug:V=1}
%endif
}

PreInstallKernel (){
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
%ifarch %{ix86}
	if [ "$smp" = "yes" ]; then
		Config="ia32-smp"
	else
		Config="ia32"
	fi
%else
	if [ "$smp" = "yes" ]; then
		Config="%{_target_cpu}-smp"
	else
		Config="%{_target_cpu}"
	fi
%endif
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86}
	cp arch/i386/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch amd64
	cp arch/x86_64/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif

%ifarch alpha sparc sparc64
	gzip -cfv vmlinux > vmlinuz
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinuz $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%ifarch sparc sparc64
	elftoaout vmlinux -o vmlinux.aout
	install vmlinuz.aout $KERNEL_INSTALL_DIR/boot/vmlinuz.aout-$KernelVer
%endif
%endif

%ifarch ppc
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
     %{__make} modules_install \
	%{?debug:V=1} \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer $KernelVer || echo

	echo "KERNEL RELEASE $KernelVer DONE"

}

KERNEL_BUILD_DIR=`pwd`

# UP KERNEL
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-UP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig
%{?with_up:BuildKernel}
%{?with_up:PreInstallKernel}

# SMP KERNEL
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-SMP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig smp
%{?with_smp:BuildKernel smp}
%{?with_smp:PreInstallKernel smp}

# BOOT kernel
#%%ifnarch i586 i686 athlon
#%KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/BOOT"
#%rm -rf $KERNEL_INSTALL_DIR
#%%{?with_boot:BuildKernel BOOT}
#%%{?with_boot:PreInstallKernel boot}
#%%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

install -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

KERNEL_BUILD_DIR=`pwd`

%if %{with up} || %{with smp}
cp -a $KERNEL_BUILD_DIR/build-done/kernel-*/* $RPM_BUILD_ROOT
%endif

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf %{_prefix}/src/linux-%{version} \
			$RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done

ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux

find . ! -name "build-done" -maxdepth 1 -exec cp -a "{}" "$RPM_BUILD_ROOT/usr/src/linux-%{version}/" ";"

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

%{__make} mrproper \
	RCS_FIND_IGNORE='-name build-done -prune -o'
find -name "*~" -exec rm -f "{}" ";"
find -name "*.orig" -exec rm -f "{}" ";"
cp $KERNEL_BUILD_DIR/scripts/modpost scripts

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32.config > .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config
%endif

%ifarch i386
echo "CONFIG_M386=y" >> .config
%endif
%ifarch i586
echo "CONFIG_M586=y" >> .config
%endif
%ifarch i686
echo "CONFIG_M686=y" >> .config
%endif
%ifarch athlon
echo "CONFIG_MK7=y" >> .config
%endif

cat %{SOURCE100} >> .config

cp .config config-up

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32-smp.config >> .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}-smp.config .config
%endif

%ifarch i386
echo "CONFIG_M386=y" >> .config
%endif
%ifarch i586
echo "CONFIG_M586=y" >> .config
%endif
%ifarch i686
echo "CONFIG_M686=y" >> .config
%endif
%ifarch athlon
echo "CONFIG_MK7=y" >> .config
%endif

cat %{SOURCE100} >> .config

cp .config config-smp

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux/autoconf.h

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
fi

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
fi

%if %{with up} || %{with smp}
# UP or SMP
install $KERNEL_BUILD_DIR/build-done/kernel-*/usr/src/linux-%{version}/include/linux/* \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
%endif

%ifarch %{ix86}
ln -sf asm-i386 $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/include/asm
%endif

%{__make} include/linux/version.h
%{__make} clean
cp $KERNEL_BUILD_DIR/scripts/modpost scripts

%clean
rm -rf $RPM_BUILD_ROOT

%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
%depmod %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -f %{_prefix}/src/linux-%{version}/config-up ] ; then
	cp -f %{_prefix}/src/linux-%{version}/config-up %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}
%depmod %{version}-%{release}smp

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -f %{_prefix}/src/linux-%{version}/config-smp ] ; then
	cp -f %{_prefix}/src/linux-%{version}/config-smp %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post BOOT
if [ ! -L %{_libdir}/bootdisk/lib/modules/%{version} ] ; then
	mv -f %{_libdir}/bootdisk/lib/modules/%{version} %{_libdir}/bootdisk/lib/modules/%{version}.rpmsave
fi
if [ ! -L %{_libdir}/bootdisk/boot/vmlinuz-%{version} ] ; then
	mv -f %{_libdir}/bootdisk/boot/vmlinuz-%{version} %{_libdir}/bootdisk/boot/vmlinuz-%{version}.rpmsave
fi
rm -f %{_libdir}/bootdisk/lib/modules/%{version}
ln -snf %{version}-%{release}BOOT %{_libdir}/bootdisk/lib/modules/%{version}
rm -f %{_libdir}/bootdisk/boot/vmlinuz-%{version}
ln -snf vmlinuz-%{version}-%{release}BOOT %{_libdir}/bootdisk/boot/vmlinuz-%{version}

%postun
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%post pcmcia
%depmod %{version}-%{release}

%postun pcmcia
%depmod %{version}-%{release}

%post drm
%depmod %{version}-%{release}

%postun drm
%depmod %{version}-%{release}

%post sound-oss
%depmod %{version}-%{release}

%postun sound-oss
%depmod %{version}-%{release}

%post sound-alsa
%depmod %{version}-%{release}

%postun sound-alsa
%depmod %{version}-%{release}

%postun smp
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%post smp-pcmcia
%depmod %{version}-%{release}smp

%postun smp-pcmcia
%depmod %{version}-%{release}smp

%post smp-drm
%depmod %{version}-%{release}smp

%postun smp-drm
%depmod %{version}-%{release}smp

%post smp-sound-oss
%depmod %{version}-%{release}smp

%postun smp-sound-oss
%depmod %{version}-%{release}smp

%post smp-sound-alsa
%depmod %{version}-%{release}smp

%postun smp-sound-alsa
%depmod %{version}-%{release}smp

%postun BOOT
if [ -L %{_libdir}/bootdisk/lib/modules/%{version} ]; then
	if [ "`ls -l %{_libdir}/bootdisk/lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}BOOT" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_libdir}/bootdisk/lib/modules/%{version}
		fi
	fi
fi

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L %{_prefix}/src/linux ]; then
	if [ "`ls -l %{_prefix}/src/linux | awk '{ print $10 }'`" = "linux-%{version}" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_prefix}/src/linux
		fi
	fi
fi

%if %{with up}
%files
%defattr(644,root,root,755)
%ifarch alpha ppc
/boot/vmlinux-%{version}-%{release}
%endif
%ifarch sparc sparc64
/boot/vmlinux-%{version}-%{release}
/boot/vmlinux.aout-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko
#drm stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
#oss sound stuff
%exclude /lib/modules/%{version}-%{release}/kernel/sound/oss
#alsa sound stuff
%exclude /lib/modules/%{version}-%{release}/kernel/sound/core
%exclude /lib/modules/%{version}-%{release}/kernel/sound/drivers
%exclude /lib/modules/%{version}-%{release}/kernel/sound/i2c
%exclude /lib/modules/%{version}-%{release}/kernel/sound/isa
%exclude /lib/modules/%{version}-%{release}/kernel/sound/pci
%exclude /lib/modules/%{version}-%{release}/kernel/sound/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/sound/synth
%exclude /lib/modules/%{version}-%{release}/kernel/sound/usb

/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko
/lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko
/lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko

%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif			# %%{with up}

%if %{with smp}
%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko
#drm stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
#oss sound stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/oss
#alsa sound stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/core
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/drivers
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/i2c
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/isa
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/pci
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/synth
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/usb

/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*

%files -n kernel-smp-pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko
/lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko

%files -n kernel-smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif			# %%{with smp}

%if %{with boot}
%ifnarch i586 i686 athlon 		# narch
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc		# arch
%{_libdir}/bootdisk/boot/vmlinux-%{version}-%{release}BOOT
%endif				#arch
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/build
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*
%endif				# narch
%endif				# %%{with boot}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_prefix}/src/linux-%{version}/config-smp
%{_prefix}/src/linux-%{version}/config-up
%attr(755,root,root)	%{_prefix}/src/linux-%{version}/scripts/modpost
#%{_prefix}/src/linux-%{version}/.config

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
#%%{_prefix}/src/linux-%{version}/netfilter-patch-o-matic

%if %{with source}
%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/sound
%{_prefix}/src/linux-%{version}/security
%{_prefix}/src/linux-%{version}/usr
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%endif

%if %{with up}
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound/oss

%files sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound/core
/lib/modules/%{version}-%{release}/kernel/sound/drivers
/lib/modules/%{version}-%{release}/kernel/sound/i2c
/lib/modules/%{version}-%{release}/kernel/sound/isa
/lib/modules/%{version}-%{release}/kernel/sound/pci
/lib/modules/%{version}-%{release}/kernel/sound/pcmcia
/lib/modules/%{version}-%{release}/kernel/sound/synth
/lib/modules/%{version}-%{release}/kernel/sound/usb
%endif

%if %{with smp}
%files smp-sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound/oss

%files smp-sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound/core
/lib/modules/%{version}-%{release}smp/kernel/sound/drivers
/lib/modules/%{version}-%{release}smp/kernel/sound/i2c
/lib/modules/%{version}-%{release}smp/kernel/sound/isa
/lib/modules/%{version}-%{release}smp/kernel/sound/pci
/lib/modules/%{version}-%{release}smp/kernel/sound/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/sound/synth
/lib/modules/%{version}-%{release}smp/kernel/sound/usb
%endif
