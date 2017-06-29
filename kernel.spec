#
# LATEST VERSION CHECKER:
# # curl -s https://www.kernel.org/finger_banner
#
# TODO:
# - benchmark NO_HZ & HZ=1000 vs HZ=300 on i686
# - IPv4 source address selection for multihomed vservers is completely broken
#	meaning routing table is ignored except for default
#
# HOWTO update configuration files:
# - run build
# - add new options to proper config (kernel-multiarch.config, kernel-x86.config, kernel-powerpc.config etc)
# - sort configuration files using:
#   ./kernel-config-sort.pl ~/rpm/BUILD/kernel-%{version}/linux-%{version}/ -a x86 kernel-x86.config
#   ./kernel-config-sort.pl ~/rpm/BUILD/kernel-%{version}/linux-%{version} kernel-multiarch.config
#
# Conditional build:
%bcond_without	source		# don't build kernel-source package
%bcond_without	doc			# don't build kernel-doc package
%bcond_without	pcmcia		# don't build pcmcia
%bcond_without	firmware	# don't build firmware into main package

%bcond_with	verbose		# verbose build (V=1)

%bcond_with	fbcondecor	# build fbcondecor (disable FB_TILEBLITTING and affected fb modules)
%bcond_without	pae		# build PAE (HIGHMEM64G) support on 32bit i686 athlon pentium3 pentium4
%bcond_with	nfsroot		# build with root on NFS support

%bcond_without	imq		# imq support
%bcond_without	ipv6		# ipv6 support

%bcond_without	aufs		# aufs4 support

%bcond_with	vserver		# support for VServer

%bcond_with	rt		# real-time kernel (CONFIG_PREEMPT_RT) for low latencies

%bcond_with	vanilla		# don't include any patches
%bcond_with	rescuecd	# build kernel for our rescue
%bcond_with	myown		# build with your own config (kernel-myown.config)

%{?debug:%define with_verbose 1}

%define		have_drm	1
%define		have_ide	1
%define		have_oss	1
%define		have_sound	1
%define		have_pcmcia	1

%if %{with rescuecd}
%unglobal	with_vserver
%define		have_drm	0
%define		have_sound	0
%endif

%if %{with myown}
%define		have_drm	0
%define		have_ide	0
%define		have_oss	0
%define		have_sound	0
%define		have_pcmcia	0
%endif

%ifarch sparc sparc64
%unglobal	with_pcmcia
%define		have_drm	0
%define		have_oss	0
%endif

%if %{without pcmcia}
%define		have_pcmcia	0
%endif

%define		rel		1
%define		basever		4.9
%define		postver		.35

# define this to '-%{basever}' for longterm branch
%define		versuffix	-%{basever}

# __alt_kernel is list of features, empty string if none set
# _alt kernel is defined as: %{nil}%{?alt_kernel:-%{?alt_kernel}} (defined in rpm.macros)
# alt_kernel should be defined if __alt_kernel has non-empty value (for %{?alt_kernel:foo} constructs)
%define		__alt_kernel	%{nil}

%if "%{__alt_kernel}" != ""
%define		alt_kernel	%{__alt_kernel}
%endif

# these override whatever name was picked from bconds
%if %{with myown} && "%{_alt_kernel}" == ""
%define		alt_kernel	myown
%endif
%if %{with rescuecd}
%define		alt_kernel	rescuecd
%endif
%if %{with vanilla}
%define		alt_kernel	vanilla
%endif
%if %{without pae}
%define		alt_kernel	nopae
%endif
%if %{with rt}
%define		alt_kernel	rt
%endif

# kernel release (used in filesystem and eventually in uname -r)
# modules will be looked from /lib/modules/%{kernel_release}
# localversion is just that without version for "> localversion"
%define		localversion	%{rel}
%define		kernel_release	%{version}%{?alt_kernel:.%{alt_kernel}}-%{localversion}

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de.UTF-8):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(et.UTF-8):	Linuxi kernel (ehk operatsioonisüsteemi tuum)
Summary(fr.UTF-8):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl.UTF-8):	Jądro Linuksa
Name:		kernel%{versuffix}%{_alt_kernel}
Version:	%{basever}%{postver}
Release:	%{rel}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
Source0:	https://www.kernel.org/pub/linux/kernel/v4.x/linux-%{basever}.tar.xz
# Source0-md5:	0a68ef3615c64bd5ee54a3320e46667d
%if "%{postver}" != ".0"
Patch0:		https://www.kernel.org/pub/linux/kernel/v4.x/patch-%{version}.xz
# Patch0-md5:	763409bff0cb4bd6646e27cf4c4bb42e
%endif
Source1:	kernel.sysconfig

Source3:	kernel-autoconf.h
Source4:	kernel-config.h
Source6:	kernel-config.awk
Source7:	kernel-module-build.pl
Source8:	kernel-track-config-change.awk
# not used by kernel.spec, but it's good to have it in SOURCES
Source9:	kernel-config-sort.pl
Source10:	kernel.make

Source20:	kernel-multiarch.config
Source21:	kernel-x86.config
Source22:	kernel-sparc.config
Source23:	kernel-alpha.config
Source24:	kernel-powerpc.config
Source25:	kernel-ia64.config

Source41:	kernel-patches.config
Source43:	kernel-vserver.config
Source44:	kernel-rt.config

Source55:	kernel-imq.config

Source58:	kernel-inittmpfs.config

# http://dev.gentoo.org/~spock/projects/fbcondecor/archive/fbcondecor-0.9.4-2.6.25-rc6.patch
Patch3:		kernel-fbcondecor.patch
Patch6:		linux-wistron-nx.patch

# netfilter related stuff mostly based on patch-o-matic-ng
# snapshot 20070806 with some fixes. Some modules
# were ported to nf_conntrack.

Patch10:	kernel-pom-ng-IPV4OPTSSTRIP.patch

# http://ftp.linux-vserver.org/pub/people/dhozac/p/k/delta-owner-xid-feat02.diff
Patch37:	kernel-owner-xid.patch

# based on kernel-2.6.25-layer7-2.20.patch from
# http://switch.dl.sourceforge.net/sourceforge/l7-filter/netfilter-layer7-v2.20.tar.gz
Patch40:	kernel-layer7.patch

### End netfilter

# http://www.linuximq.net
Patch50:	kernel-imq.patch

# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	kernel-atm-vbr.patch
Patch56:	kernel-atmdd.patch

# http://synce.svn.sourceforge.net/svnroot/synce/trunk/patches/linux-2.6.22-rndis_host-wm5.patch
Patch59:	kernel-rndis_host-wm5.patch

# adds some ids for hostap suported cards and monitor_enable from/for aircrack-ng
# http://patches.aircrack-ng.org/hostap-kernel-2.6.18.patch
Patch85:	kernel-hostap.patch

%define	vserver_patch 3.18.5-vs2.3.7.3
# http://vserver.13thfloor.at/Experimental/patch-3.18.5-vs2.3.7.3.diff
# note there are additional patches from above url:
# - *fix* are real fixes (we want these)
# - *feat* are new features/tests (we don't want these)
Patch100:	kernel-vserver-2.3.patch
Patch101:	kernel-vserver-fixes.patch

# git://github.com/sfjro/aufs4-standalone.git, read README
# Patch creation:
# git clone git://github.com/sfjro/aufs4-standalone.git
# cd aufs4-standalone
# git checkout -b aufs4.9 origin/aufs4.9
# cat aufs4-kbuild.patch aufs4-base.patch aufs4-mmap.patch aufs4-standalone.patch > ~/rpm/packages/kernel/kernel-aufs4.patch
# rm -rf linux && mkdir linux
# cp -a Documentation fs include linux
# diff -urN /usr/share/empty linux | filterdiff -x linux/include/uapi/linux/Kbuild >> ~/rpm/packages/kernel/kernel-aufs4.patch
# cat aufs4-loopback.patch >> ~/rpm/packages/kernel/kernel-aufs4.patch
#
Patch145:	kernel-aufs4.patch
Patch146:	kernel-aufs4+vserver.patch

# Show normal colors in menuconfig with ncurses ABI 6
Patch250:	kernel-fix_256colors_menuconfig.patch

# https://rt.wiki.kernel.org/
# https://www.kernel.org/pub/linux/kernel/projects/rt/4.9/patch-4.9.27-rt18.patch.xz
Patch500:	kernel-rt.patch

Patch2000:	kernel-small_fixes.patch
Patch2001:	kernel-pwc-uncompress.patch
Patch2003:	kernel-regressions.patch
Patch2004:	kernel-libata-ahci-pm.patch

# git://git.kernel.org/pub/scm/linux/kernel/git/jj/linux-apparmor
# branch v4.7-aa2.8-out-of-tree
Patch5000:	kernel-apparmor.patch

# for rescuecd
# based on ftp://ftp.leg.uct.ac.za/pub/linux/rip/tmpfs_root-2.6.30.diff.gz
Patch7000:	kernel-inittmpfs.patch

# Do not remove this line, please. It is easier for me to uncomment two lines, then patch
# kernel.spec every time.
#Patch50000:	kernel-usb_reset.patch

URL:		https://www.kernel.org/
AutoReqProv:	no
BuildRequires:	/sbin/depmod
BuildRequires:	bc
BuildRequires:	binutils >= 3:2.18
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
BuildRequires:	elfutils-devel
BuildRequires:	gcc >= 5:3.2
BuildRequires:	hostname
BuildRequires:	kmod >= 12-2
BuildRequires:	openssl-devel
BuildRequires:	perl-base
BuildRequires:	rpm-build >= 4.5-24
BuildRequires:	rpmbuild(macros) >= 1.707
%ifarch ppc
BuildRequires:	uboot-mkimage
%endif
BuildRequires:	xz >= 1:4.999.7
Requires(post):	coreutils
Requires(post):	geninitrd >= 12749
Requires(post):	kmod >= 12-2
Requires:	/sbin/depmod
Requires:	coreutils
Requires:	geninitrd >= 12749
Requires:	kmod >= 12-2
%if %{with pae}
%ifarch i686 athlon pentium3 pentium4
Requires:	cpuinfo(pae)
%endif
%endif
Suggests:	crda
Suggests:	dracut
Suggests:	keyutils
Suggests:	kernel%{versuffix}-ide = %{epoch}:%{version}-%{release}
%if %{with firmware}
Suggests:	linux-firmware
%else
Requires:	linux-firmware
%endif
Provides:	%{name}(netfilter) = 20070806
Provides:	%{name}(vermagic) = %{kernel_release}
Obsoletes:	kernel%{_alt_kernel}-char-lirc-ene0100
Obsoletes:	kernel%{_alt_kernel}-char-lirc-it87
Obsoletes:	kernel%{_alt_kernel}-char-lirc-ite8709
Obsoletes:	kernel%{_alt_kernel}-char-lirc-mceusb
Obsoletes:	kernel%{_alt_kernel}-char-lirc-streamzap
Obsoletes:	kernel%{_alt_kernel}-isdn-mISDN
Obsoletes:	kernel-firmware
Obsoletes:	kernel-misc-acer_acpi
Obsoletes:	kernel-misc-fuse
Obsoletes:	kernel-misc-uvc
Obsoletes:	kernel-modules
Obsoletes:	kernel-net-ar81
Obsoletes:	kernel-net-hostap
Obsoletes:	kernel-net-ieee80211
Obsoletes:	kernel-net-ipp2p
Obsoletes:	kernel-net-rt61
Obsoletes:	kernel-smp
Conflicts:	e2fsprogs < 1.29
Conflicts:	isdn4k-utils < 3.1pre1
Conflicts:	jfsutils < 1.1.3
Conflicts:	libusb < 1.0.9
Conflicts:	linux-firmware < 20120720
Conflicts:	lvm2 < 2.02.40
Conflicts:	module-init-tools < 3.16
Conflicts:	nfs-utils < 1.0.5
Conflicts:	oprofile < 0.9
Conflicts:	ppp < 1:2.4.0
Conflicts:	procps < 3.2.0
Conflicts:	quota-tools < 3.09
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	rpm < 4.4.2-0.2
Conflicts:	udev < 1:081
Conflicts:	util-linux < 2.10o
Conflicts:	util-vserver < 0.30.216
Conflicts:	xfsprogs < 2.6.0
%if %{without pae}
ExclusiveArch:	i686 pentium3 pentium4 athlon
%else
ExclusiveArch:	i486 i586 i686 pentium3 pentium4 athlon %{x8664} x32 alpha arm ia64 ppc ppc64 sparc sparc64
%endif
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		kmod_compress_cmd	%{__xz}

%ifarch %{ix86} %{x8664} x32
%define		target_arch_dir		x86
%endif
%ifarch ppc ppc64
%define		target_arch_dir		powerpc
%endif
%ifarch sparc sparc64
%define		target_arch_dir		sparc
%endif
%ifnarch %{ix86} %{x8664} x32 ppc ppc64 sparc sparc64
%define		target_arch_dir		%{_target_base_arch}
%endif

%define		defconfig	arch/%{target_arch_dir}/defconfig

# No ELF objects there to strip (skips processing 27k files)
%define		_noautostrip	\\(.*%{_kernelsrcdir}/.*\\|.*/vmlinux.*\\)
%define		_noautochrpath	.*%{_kernelsrcdir}/.*
%define		_enable_debug_packages	0

%ifarch ia64
%define		initrd_dir	/boot/efi
%else
%define		initrd_dir	/boot
%endif

%define		topdir		%{_builddir}/%{name}-%{version}
%define		srcdir		%{topdir}/linux-%{basever}
%define		objdir		%{topdir}/%{targetobj}
%define		targetobj	%{_target_base_arch}-gcc-%(%{__cc} -dumpversion)

%define		_kernelsrcdir	/usr/src/linux%{versuffix}%{_alt_kernel}-%{version}

%if "%{_target_base_arch}" != "%{_host_base_arch}"
	%define CrossOpts ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-
	%define	DepMod /bin/true

	%if "%{_host_base_arch}" == "sparc" && "%{_target_base_arch}" == "sparc64"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_host_base_arch}" == "sparc64" && "%{_target_base_arch}" == "sparc"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_host_base_arch}" == "x86_64" && "%{_target_base_arch}" == "i386"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_target_base_arch}" == "ppc" || "%{_target_base_arch}" == "ppc64"
	%define CrossOpts ARCH=powerpc CROSS_COMPILE=%{_target_cpu}-pld-linux-
	%endif
%else
	%ifarch ppc ppc64
	%define CrossOpts ARCH=powerpc CC="%{__cc}"
	%else
	%define CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%endif
	%define	DepMod /sbin/depmod
%endif
# use 64-bit offsets for fixdeps to work with 64-bit inodes
%define MakeOpts %{CrossOpts} HOSTCC="%{__cc} -D_FILE_OFFSET_BITS=64"

%define __features \
%{?with_vserver:Vserver - enabled}\
%{!?with_vserver:WARNING: VSERVER IS DISABLED IN THIS KERNEL BUILD!}\
%{?with_fbcondecor:Fbsplash/fbcondecor - enabled }\
%{?with_nfsroot:Root on NFS - enabled}\
%{?with_vserver:Linux-VServer - %{vserver_patch}}\
%{?with_rt:CONFIG_PREEMPT_RT - enabled}\

%define Features %(echo "%{__features}" | sed '/^$/d')

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%{Features}

%description -l de.UTF-8
Das Kernel-Paket enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeß-Management, Geräte Ein- und Ausgaben, usw.

%{Features}

%description -l fr.UTF-8
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un système d'exploitation Linux. Le noyau traite les
fonctions basiques d'un système d'exploitation: allocation mémoire,
allocation de process, entrée/sortie de peripheriques, etc.

%{Features}

%description -l pl.UTF-8
Pakiet zawiera jądro Linuksa niezbędne do prawidłowego działania
Twojego komputera. Zawiera w sobie sterowniki do sprzętu znajdującego
się w komputerze, takiego jak sterowniki dysków itp.

%{Features}

%package vmlinux
Summary:	vmlinux - uncompressed kernel image
Summary(de.UTF-8):	vmlinux - dekompressiertes Kernel Bild
Summary(pl.UTF-8):	vmlinux - rozpakowany obraz jądra
Group:		Base/Kernel
Obsoletes:	kernel-smp-vmlinux

%description vmlinux
vmlinux - uncompressed kernel image.

%description vmlinux -l de.UTF-8
vmlinux - dekompressiertes Kernel Bild.

%description vmlinux -l pl.UTF-8
vmlinux - rozpakowany obraz jądra.

%package drm
Summary:	DRM kernel modules
Summary(de.UTF-8):	DRM Kernel Treiber
Summary(pl.UTF-8):	Sterowniki DRM
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-smp-drm
AutoReqProv:	no

%description drm
DRM kernel modules.

%description drm -l de.UTF-8
DRM Kernel Treiber.

%description drm -l pl.UTF-8
Sterowniki DRM.

%package ide
Summary:	IDE kernel modules
Summary(de.UTF-8):	IDE Kernel Treiber
Summary(pl.UTF-8):	Sterowniki IDE
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReqProv:	no

%description ide
IDE kernel modules.

%description ide -l de.UTF-8
IDE Kernel Treiber.

%description ide -l pl.UTF-8
Sterowniki IDE.

%package pcmcia
Summary:	PCMCIA modules
Summary(de.UTF-8):	PCMCIA Module
Summary(pl.UTF-8):	Moduły PCMCIA
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-smp-pcmcia
Conflicts:	pcmcia-cs < 3.1.21
Conflicts:	pcmciautils < 004
AutoReqProv:	no

%description pcmcia
PCMCIA modules.

%description pcmcia -l de.UTF-8
PCMCIA Module.

%description pcmcia -l pl.UTF-8
Moduły PCMCIA.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(de.UTF-8):	ALSA Kernel Module
Summary(pl.UTF-8):	Sterowniki dźwięku ALSA
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-smp-sound-alsa
AutoReqProv:	no

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l de.UTF-8
ALSA (Advanced Linux Sound Architecture) Sound-Treiber.

%description sound-alsa -l pl.UTF-8
Sterowniki dźwięku ALSA (Advanced Linux Sound Architecture).

%package sound-oss
Summary:	OSS kernel modules
Summary(de.UTF-8):	OSS Kernel Module
Summary(pl.UTF-8):	Sterowniki dźwięku OSS
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-smp-sound-oss
AutoReqProv:	no

%description sound-oss
OSS (Open Sound System) drivers.

%description sound-oss -l de.UTF-8
OSS (Open Sound System) Treiber.

%description sound-oss -l pl.UTF-8
Sterowniki dźwięku OSS (Open Sound System).

%package headers
Summary:	Header files for the Linux kernel
Summary(de.UTF-8):	Header Dateien für den Linux-Kernel
Summary(pl.UTF-8):	Pliki nagłówkowe jądra Linuksa
Group:		Development/Building
Provides:	%{name}-headers(netfilter) = 20070806
AutoReqProv:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%description headers -l de.UTF-8
Dies sind die C Header Dateien für den Linux-Kernel, die definierte
Strukturen und Konstante beinhalten, die beim rekompilieren des
Kernels oder bei Kernel Modul kompilationen gebraucht werden.

%description headers -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe jądra, niezbędne do rekompilacji jądra
oraz budowania modułów jądra.

%package module-build
Summary:	Development files for building kernel modules
Summary(de.UTF-8):	Development Dateien die beim Kernel Modul kompilationen gebraucht werden
Summary(pl.UTF-8):	Pliki służące do budowania modułów jądra
Group:		Development/Building
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Requires:	elfutils-devel
Requires:	make
Conflicts:	rpmbuild(macros) < 1.704
AutoReqProv:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%description module-build -l de.UTF-8
Development Dateien des Linux-Kernels die beim kompilieren externer
Kernel Module gebraucht werden.

%description module-build -l pl.UTF-8
Pliki ze drzewa źródeł jądra potrzebne do budowania modułów jądra
Linuksa z zewnętrznych pakietów.

%package source
Summary:	Kernel source tree
Summary(de.UTF-8):	Der Kernel Quelltext
Summary(pl.UTF-8):	Kod źródłowy jądra Linuksa
Group:		Development/Building
Requires:	%{name}-module-build = %{epoch}:%{version}-%{release}
AutoReqProv:	no
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description source
This is the source code for the Linux kernel. You can build a custom
kernel that is better tuned to your particular hardware.

%description source -l de.UTF-8
Das Kernel-Source-Paket enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu kompilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu kompilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr.UTF-8
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nécessaires pour compiler la plupart des
programmes C, car il dépend de constantes définies dans le code
source. Les sources peuvent être aussi utilisée pour compiler un noyau
personnalisé pour avoir de meilleures performances sur des matériels
particuliers.

%description source -l pl.UTF-8
Pakiet zawiera kod źródłowy jądra systemu.

%package doc
Summary:	Kernel documentation
Summary(de.UTF-8):	Kernel Dokumentation
Summary(pl.UTF-8):	Dokumentacja do jądra Linuksa
Group:		Documentation
AutoReqProv:	no
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l de.UTF-8
Dies ist die Kernel Dokumentation wie sie im 'Documentation'
Verzeichniss vorgefunden werden kann.

%description doc -l pl.UTF-8
Pakiet zawiera dokumentację do jądra Linuksa pochodzącą z katalogu
/usr/src/linux/Documentation.

%prep
%setup -qc
ln -s %{SOURCE7} kernel-module-build.pl
ln -s %{SOURCE10} Makefile
cd linux-%{basever}

%if "%{postver}" != ".0"
%patch0 -p1
%endif

%if %{without vanilla}

%if %{with fbcondecor}
%patch3 -p1
%endif
%patch6 -p1

## netfilter
#

# kernel-pom-ng-IPV4OPTSSTRIP.patch
%patch10 -p1

# kernel-owner-xid.patch
%if %{with vserver}
%patch37 -p1
%endif

# kernel-layer7.patch
%patch40 -p1

##
# end of netfilter

%if %{with imq}
%patch50 -p1
%endif

%patch55 -p1
%patch56 -p1

# kernel-rndis_host-wm5.patch
%patch59 -p1

# hostap enhancements from/for aircrack-ng
%patch85 -p1

# vserver
%if %{with vserver}
%patch100 -p1
%patch101 -p1
%endif

%if %{with aufs}
# aufs4
%patch145 -p1
%if %{with vserver}
%patch146 -p1
%endif
%endif

%if %{with rescuecd}
%patch7000 -p1
%endif

%if %{with rt}
%patch500 -p1
rm -f localversion-rt
%endif

# apparmor
%patch5000 -p1

%patch250 -p1

%endif # vanilla

# Small fixes:
%patch2000 -p1
%patch2001 -p1
#%patch2003 -p1
%patch2004 -p1

# Do not remove this, please!
#%%patch50000 -p1

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{?alt_kernel:.%{alt_kernel}}#g' Makefile

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' -o -name '.gitignore' ')' -print0 | xargs -0 -r -l512 rm -f

%build
install -d %{objdir}
cat > %{targetobj}.mk <<'EOF'
# generated by %{name}.spec
KERNELSRC	:= %{srcdir}
KERNELOUTPUT	:= %{objdir}

SRCARCH		:= %{target_arch_dir}
ARCH		:= %{_target_base_arch}
Q		:= %{!?with_verbose:@}
MAKE_OPTS	:= %{MakeOpts}
DEFCONFIG	:= %{defconfig}
EOF

RescueConfig() {
	set -x
		# CONFIG_SOUND is not set
		# CONFIG_AUDIT is not set
		# CONFIG_TR is not set
		# CONFIG_BT is not set
		# CONFIG_VIDEO_DEV is not set
		# CONFIG_DVB_CORE is not set
		# CONFIG_HAMRADIO is not set
		# CONFIG_ARCNET is not set
		# CONFIG_DRM is not set
		# CONFIG_WATCHDOG is not set
		# CONFIG_INPUT_JOYSTICK is not set
		# CONFIG_DEBUG_KERNEL is not set
		# CONFIG_ISDN is not set
		# CONFIG_AGP is not set
		# CONFIG_SECURITY is not set
		# CONFIG_PARIDE is not set
		# CONFIG_CPU_FREQ is not set
		# CONFIG_GAMEPORT is not set
		# CONFIG_KVM is not set
		# CONFIG_PHONE is not set
		# CONFIG_STRICT_DEVMEM is not set
		# CONFIG_IMA is not set
		# CONFIG_MEDIA_SUPPORT is not set
		# CONFIG_UWB is not set
		# CONFIG_PWM is not set
		# CONFIG_COMEDI_NI_LABPC_ISA is not set
		# CONFIG_FB_SYS_FILLRECT is not set
		# CONFIG_FB_SYS_COPYAREA is not set
		# CONFIG_FB_SYS_IMAGEBLIT is not set
		# CONFIG_FB_SYS_FOPS is not set
		# CONFIG_FB_HECUBA is not set
		# CONFIG_FB_SVGALIB is not set
		# CONFIG_FB_CIRRUS is not set
		# CONFIG_FB_PM2 is not set
		# CONFIG_FB_CYBER2000 is not set
		# CONFIG_FB_ARC is not set
		# CONFIG_FB_ASILIANT is not set
		# CONFIG_FB_IMSTT is not set
		# CONFIG_FB_VGA16 is not set
		# CONFIG_FB_UVESA is not set
		# CONFIG_FB_N411 is not set
		# CONFIG_FB_HGA is not set
		# CONFIG_FB_S1D13XXX is not set
		# CONFIG_FB_NVIDIA is not set
		# CONFIG_FB_RIVA is not set
		# CONFIG_FB_I740 is not set
		# CONFIG_FB_LE80578 is not set
		# CONFIG_FB_CARILLO_RANCH is not set
		# CONFIG_FB_MATROX is not set
		# CONFIG_FB_RADEON is not set
		# CONFIG_FB_ATY128 is not set
		# CONFIG_FB_ATY is not set
		# CONFIG_FB_S3 is not set
		# CONFIG_FB_SAVAGE is not set
		# CONFIG_FB_SIS is not set
		# CONFIG_FB_VIA is not set
		# CONFIG_FB_NEOMAGIC is not set
		# CONFIG_FB_KYRO is not set
		# CONFIG_FB_3DFX is not set
		# CONFIG_FB_VOODOO1 is not set
		# CONFIG_FB_VT8623 is not set
		# CONFIG_FB_TRIDENT is not set
		# CONFIG_FB_ARK is not set
		# CONFIG_FB_PM3 is not set
		# CONFIG_FB_CARMINE is not set
		# CONFIG_FB_GEODE is not set
		# CONFIG_FB_TMIO is not set
		# CONFIG_FB_SM501 is not set
		# CONFIG_FB_SMSCUFX is not set
		# CONFIG_FB_UDL is not set
		# CONFIG_FB_GOLDFISH is not set
		# CONFIG_XEN_FBDEV_FRONTEND is not set
		# CONFIG_FB_METRONOME is not set
		# CONFIG_FB_MB862XX is not set
		# CONFIG_FB_BROADSHEET is not set
		# CONFIG_FB_AUO_K190X is not set
		# CONFIG_FB_AUO_K1900 is not set
		# CONFIG_FB_AUO_K1901 is not set
		# CONFIG_FB_HYPERV is not set
		CONFIG_AUFS=y
		CONFIG_AUFS_FS=y
		CONFIG_AUFS_BR_RAMFS=y
		CONFIG_AUFS_RDU=y
		CONFIG_BLK_DEV_LOOP=y
		CONFIG_ISO9660_FS=y
		CONFIG_NLS_UTF8=y
		CONFIG_SQUASHFS=y
		CONFIG_FB=y
		CONFIG_FB_EFI=y
		CONFIG_FRAMEBUFFER_CONSOLE_DETECT_PRIMARY=y
EOCONFIG

	return 0
}

BuildConfig() {
	%{?debug:set -x}
	set -e

	Config="kernel-%{target_arch_dir}.config"
	echo >&2 "Building config file for %{_target_cpu} using $Config et al."

	# prepare local and important options
	cat <<-EOCONFIG > important.config
		LOCALVERSION="-%{localversion}"

%if 0%{?debug:1}
		CONFIG_DEBUG_SLAB=y
		CONFIG_DEBUG_SLAB_LEAK=y
		CONFIG_DEBUG_PREEMPT=y
		CONFIG_RT_DEADLOCK_DETECT=y
%endif

%if %{without ipv6}
		CONFIG_IPV6=n
%endif

%ifarch i686 athlon pentium3 pentium4
	%if %{with pae}
		CONFIG_HIGHMEM4G=n
		CONFIG_HIGHMEM64G=y
		CONFIG_X86_PAE=y
		CONFIG_NUMA=n
	%endif
%endif

%if %{without pcmcia}
		CONFIG_PCMCIA=n
%endif

%if %{with fbcondecor}
		CONFIG_FB_S3=n
		CONFIG_FB_VT8623=n
		CONFIG_FB_ARK=n
		CONFIG_FB_TILEBLITTING=n
		CONFIG_FB_CON_DECOR=y
%endif

%if %{with nfsroot}
		CONFIG_NFS_FS=y
		CONFIG_ROOT_NFS=y
%endif
EOCONFIG

%if %{with rescuecd}
	RescueConfig rescue.config
%endif
	# prepare kernel-style config file from multiple config files
	%{__awk} -v arch="all %{target_arch_dir} %{_target_base_arch} %{_target_cpu}" -f %{SOURCE6} \
%if %{with myown}
		$RPM_SOURCE_DIR/kernel-%{alt_kernel}.config \
%endif
		important.config \
%if %{without vanilla}
%if %{with rescuecd}
		%{SOURCE58} \
		rescue.config \
%endif
		\
%if %{with imq}
		%{SOURCE55} \
%endif
%if %{with vserver}
		%{SOURCE43} \
%endif
%if %{with rt}
		%{SOURCE44} \
%endif
		%{SOURCE41} %{?0:patches} \
%endif
		%{SOURCE20} \
		$RPM_SOURCE_DIR/$Config
}

cd %{objdir}
install -d arch/%{target_arch_dir}
BuildConfig > %{defconfig}
ln -sf %{defconfig} .config
cd -

%{__make} \
	TARGETOBJ=%{targetobj} \
	%{?with_verbose:V=1} \
	oldconfig

%{__awk} %{?debug:-v dieOnError=1} -v infile=%{objdir}/%{defconfig} -f %{SOURCE8} %{objdir}/.config

# build kernel
%{__make} \
	TARGETOBJ=%{targetobj} \
	%{?with_verbose:V=1} \
	all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{MakeOpts} -j1 %{!?with_verbose:-s} modules_install %{?with_firmware:firmware_install} \
	-C %{objdir} \
	%{?with_verbose:V=1} \
	DEPMOD=%{DepMod} \
	mod_compress_cmd=true \
	INSTALL_MOD_PATH=$RPM_BUILD_ROOT \
	INSTALL_FW_PATH=$RPM_BUILD_ROOT/lib/firmware/%{kernel_release} \
	KERNELRELEASE=%{kernel_release}

install -d $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/misc

# create directories which may be missing, to simplyfy %files
install -d $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/kernel/{arch,sound,mm}

# rpm obeys filelinkto checks for ghosted symlinks, convert to files
rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}
touch $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}

# no point embed content for %ghost files. empty them
for a in \
	dep{,.bin} \
	alias{,.bin} \
	devname \
	softdep \
	symbols{,.bin} \
; do
	test -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/modules.$a
	> $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/modules.$a
done

# /boot
install -d $RPM_BUILD_ROOT/boot
cp -a %{objdir}/System.map $RPM_BUILD_ROOT/boot/System.map-%{kernel_release}
cp -aL %{objdir}/.config $RPM_BUILD_ROOT/boot/config-%{kernel_release}
%ifarch %{ix86} %{x8664} x32
	cp -a %{objdir}/arch/%{target_arch_dir}/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
	install -p %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{kernel_release}
%endif
%ifarch ppc ppc64
	install -p %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
	install -p %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{kernel_release}
%endif
%ifarch ia64
	%{__gzip} -cfv %{objdir}/vmlinux > %{objdir}/vmlinuz
	cp -a %{objdir}/vmlinuz $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kernel_release}
	ln -sf efi/vmlinuz-%{kernel_release} $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
%endif
%ifarch alpha sparc sparc64
	%{__gzip} -cfv %{objdir}/vmlinux > %{objdir}/vmlinuz
	cp -a %{objdir}/vmlinuz $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
	install -p %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
	%ifarch sparc
		elftoaout %{objdir}/arch/sparc/boot/image -o %{objdir}/vmlinux.aout
		install -p %{objdir}/vmlinux.aout $RPM_BUILD_ROOT/boot/vmlinux.aout-%{kernel_release}
	%endif
	%ifarch sparc64
		elftoaout %{objdir}/arch/sparc64/boot/image -o %{objdir}/vmlinux.aout
		install -p %{objdir}/vmlinux.aout $RPM_BUILD_ROOT/boot/vmlinux.aout-%{kernel_release}
	%endif
%endif
%ifarch arm
	install -p %{objdir}/arch/arm/boot/zImage $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
%endif

# ghosted initrd
touch $RPM_BUILD_ROOT%{initrd_dir}/initrd-%{kernel_release}.gz
touch $RPM_BUILD_ROOT%{initrd_dir}/initramfs-%{kernel_release}.img

%if "%{_target_base_arch}" != "%{_host_base_arch}"
touch $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/modules.dep
%endif

# /etc/modrobe.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{kernel_release}

install -d $RPM_BUILD_ROOT/etc/sysconfig
install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/kernel

# /usr/src/linux
install -d $RPM_BUILD_ROOT%{_kernelsrcdir}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al %{srcdir}/COPYING $RPM_BUILD_ROOT/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/COPYING
fi

cp -a$l %{srcdir}/* $RPM_BUILD_ROOT%{_kernelsrcdir}
cp -a %{objdir}/Module.symvers $RPM_BUILD_ROOT%{_kernelsrcdir}
cp -aL %{objdir}/.config $RPM_BUILD_ROOT%{_kernelsrcdir}
cp -a %{objdir}/include $RPM_BUILD_ROOT%{_kernelsrcdir}
# copy arch/x86/include/generated
for dir in $(cd %{objdir} && find arch -name generated -type d); do
	cp -a %{objdir}/$dir $RPM_BUILD_ROOT%{_kernelsrcdir}/$dir
	find $RPM_BUILD_ROOT%{_kernelsrcdir}/$dir -name '.*.cmd' -exec rm "{}" ";"
done

# version.h location changed in 3.7, but a lot of external modules don't know about it
# add a compatibility symlink
ln -s ../generated/uapi/linux/version.h $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/version.h

# disable this here, causes a lot of build-time problems and our rpm-build disables it anyway
%{__sed} -i -e 's|\(CONSTIFY_PLUGIN.*:=.*\)|# \1|' $RPM_BUILD_ROOT%{_kernelsrcdir}/Makefile

# collect module-build files and directories
# Usage: kernel-module-build.pl $rpmdir $fileoutdir
fileoutdir=$(pwd)
cd $RPM_BUILD_ROOT%{_kernelsrcdir}
%{__perl} %{topdir}/kernel-module-build.pl %{_kernelsrcdir} $fileoutdir
cd -

for f in `find %{objdir}/scripts -type f -print | grep -v "/\.\|\.o$"` ; do
	ff=${f##%{objdir}/}
	if [ -x "$f" ]; then
		echo "%attr(755,root,root) %{_kernelsrcdir}/$ff" >>files.mb_include_modulebuild_and_dirs
	else
		echo "%{_kernelsrcdir}/$ff" >>files.mb_include_modulebuild_and_dirs
	fi
	echo "%exclude %{_kernelsrcdir}/$ff" >>files.source_exclude_modulebuild_and_dirs
	cp -a "$f" "$RPM_BUILD_ROOT%{_kernelsrcdir}/$ff"
done

%if %{with doc}
# move to %{_docdir} so we wouldn't depend on any kernel package for dirs
install -d $RPM_BUILD_ROOT%{_docdir}
mv $RPM_BUILD_ROOT{%{_kernelsrcdir}/Documentation,%{_docdir}/%{name}-%{version}}

%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/dontdiff
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/Makefile
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/*/Makefile
%{__rm} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/*/*/Makefile
%else
%{__rm} -r $RPM_BUILD_ROOT%{_kernelsrcdir}/Documentation
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}
fi

%post
[ -f /etc/sysconfig/kernel ] && . /etc/sysconfig/kernel
if [[ "$CREATE_SYMLINKS" != [Nn][Oo] ]]; then
%ifarch ia64
	mv -f /boot/efi/vmlinuz{,.old} 2> /dev/null
	ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz
%if 0%{?alt_kernel:1}
	mv -f /boot/efi/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null
	ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz%{_alt_kernel}
%endif
%endif
	mv -f /boot/vmlinuz{,.old} 2> /dev/null
	mv -f /boot/System.map{,.old} 2> /dev/null
	ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz
	ln -sf System.map-%{kernel_release} /boot/System.map
%if 0%{?alt_kernel:1}
	mv -f /boot/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null
	mv -f /boot/System%{_alt_kernel}.map{,.old} 2> /dev/null
	ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz%{_alt_kernel}
	ln -sf System.map-%{kernel_release} /boot/System.map%{_alt_kernel}
%endif
fi

%depmod %{kernel_release}

%if %{without vserver}
%banner -e -a kernel <<EOF

WARNING: Vserver support is DISABLED in this kernel build!

EOF
%endif

%posttrans
# use posttrans to generate initrd after all dependant module packages (-drm, etc) are installed
[ -f /etc/sysconfig/kernel ] && . /etc/sysconfig/kernel
initrd_file=""
if [[ "$USE_GENINITRD" != [Nn][Oo] ]]; then
	/sbin/geninitrd -f --initrdfs=initramfs %{initrd_dir}/initrd-%{kernel_release}.gz %{kernel_release} || :
	initrd_file="initrd-%{kernel_release}.gz"
fi

# if dracut is present then generate full-featured initramfs
if [[ "$USE_DRACUT" != [Nn][Oo] ]] && [ -x /sbin/dracut ]; then
	/sbin/dracut --force --quiet /boot/initramfs-%{kernel_release}.img %{kernel_release}
	[ -n "$initrd_file" ] || initrd_file="initramfs-%{kernel_release}.img"
fi

if [[ "$CREATE_SYMLINKS" != [Nn][Oo] ]]; then
	mv -f %{initrd_dir}/initrd{,.old} 2> /dev/null
	if [ -n "$initrd_file" ] ; then
		ln -sf "$initrd_file" %{initrd_dir}/initrd
	fi
%if 0%{?alt_kernel:1}
	mv -f %{initrd_dir}/initrd%{_alt_kernel}{,.old} 2> /dev/null
	if [ -n "$initrd_file" ] ; then
		ln -sf "$initrd_file" %{initrd_dir}/initrd%{_alt_kernel}
	fi
%endif
fi

# update boot loaders when old package files are gone from filesystem
if [ -x /sbin/update-grub -a -f /etc/sysconfig/grub ]; then
	if [ "$(. /etc/sysconfig/grub; echo ${UPDATE_GRUB:-no})" = "yes" ]; then
		/sbin/update-grub >/dev/null
	fi
fi
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/$initrd_file --install %{kernel_release} --banner "PLD Linux (%{pld_release})%{?alt_kernel: / %{alt_kernel}}"
fi
if [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi
if [ -x /sbin/efi-boot-update ]; then
	/sbin/efi-boot-update --auto || :
fi

%post vmlinux
[ -f /etc/sysconfig/kernel ] && . /etc/sysconfig/kernel
if [[ "$CREATE_SYMLINKS" != [Nn][Oo] ]]; then
	mv -f /boot/vmlinux{,.old} 2> /dev/null
	ln -sf vmlinux-%{kernel_release} /boot/vmlinux
%if 0%{?alt_kernel:1}
	mv -f /boot/vmlinux-%{alt_kernel}{,.old} 2> /dev/null
	ln -sf vmlinux-%{kernel_release} /boot/vmlinux-%{alt_kernel}
%endif
fi

%post drm
%depmod %{kernel_release}

%postun drm
%depmod %{kernel_release}

%post ide
%depmod %{kernel_release}

%postun ide
%depmod %{kernel_release}

%post pcmcia
%depmod %{kernel_release}

%postun pcmcia
%depmod %{kernel_release}

%post sound-alsa
%depmod %{kernel_release}

%postun sound-alsa
%depmod %{kernel_release}

%post sound-oss
%depmod %{kernel_release}

%postun sound-oss
%depmod %{kernel_release}

%post headers
ln -snf %{basename:%{_kernelsrcdir}} %{_prefix}/src/linux%{versuffix}%{_alt_kernel}

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux%{versuffix}%{_alt_kernel} ]; then
		if [ "$(readlink %{_prefix}/src/linux%{versuffix}%{_alt_kernel})" = "linux%{versuffix}%{_alt_kernel}-%{version}" ]; then
			rm -f %{_prefix}/src/linux%{versuffix}%{_alt_kernel}
		fi
	fi
fi

%triggerin module-build -- %{name} = %{epoch}:%{version}-%{release}
ln -sfn %{_kernelsrcdir} /lib/modules/%{kernel_release}/build
ln -sfn %{_kernelsrcdir} /lib/modules/%{kernel_release}/source

%triggerun module-build -- %{name} = %{epoch}:%{version}-%{release}
if [ "$1" = 0 ]; then
	rm -f /lib/modules/%{kernel_release}/{build,source}
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kernel
%ifarch sparc sparc64
/boot/vmlinux.aout-%{kernel_release}
%endif
%ifarch ia64
/boot/efi/vmlinuz-%{kernel_release}
%endif
/boot/vmlinuz-%{kernel_release}
/boot/System.map-%{kernel_release}
/boot/config-%{kernel_release}
%ghost %{initrd_dir}/initrd-%{kernel_release}.gz
%ghost %{initrd_dir}/initramfs-%{kernel_release}.img
%if %{with firmware}
/lib/firmware/%{kernel_release}
%endif

%dir /lib/modules/%{kernel_release}
%dir /lib/modules/%{kernel_release}/kernel
/lib/modules/%{kernel_release}/kernel/arch
/lib/modules/%{kernel_release}/kernel/crypto
/lib/modules/%{kernel_release}/kernel/drivers
%if %{have_drm}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/gpu
%endif
%if %{have_ide}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/*
%endif
/lib/modules/%{kernel_release}/kernel/fs
/lib/modules/%{kernel_release}/kernel/kernel
/lib/modules/%{kernel_release}/kernel/lib
/lib/modules/%{kernel_release}/kernel/net
/lib/modules/%{kernel_release}/kernel/mm
%if %{have_sound}
%dir /lib/modules/%{kernel_release}/kernel/sound
/lib/modules/%{kernel_release}/kernel/sound/ac97_bus.ko*
/lib/modules/%{kernel_release}/kernel/sound/sound*.ko*
%ifnarch sparc
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/pci/cx88/cx88-alsa.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/usb/em28xx/em28xx-alsa.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/pci/saa7134/saa7134-alsa.ko*
%endif
%endif
%dir /lib/modules/%{kernel_release}/misc
%if %{have_pcmcia}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/[!p]*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/pd6729.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
%if %{without rescuecd}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ata/pata_pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/b1pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/usb/gadget/legacy/g_midi.ko*
%endif
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/ide-cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/arcnet/com20020_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/can/softing/softing_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/3com/3c574_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/3com/3c589_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/8390/axnet_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/8390/pcnet_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/amd/nmclan_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/fujitsu/fmvj18x_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/smsc/smc91c92_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/xircom/xirc2ps_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/atmel/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/cisco/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/intersil/hostap/hostap_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/intersil/orinoco/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/marvell/libertas/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/tty/serial/8250/serial_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif
%if %{with myown}
/lib/modules/%{kernel_release}/kernel/sound
%endif
/lib/modules/%{kernel_release}/kernel/security
/lib/modules/%{kernel_release}/kernel/virt

%dir %{_sysconfdir}/modprobe.d/%{kernel_release}

# provided by build
/lib/modules/%{kernel_release}/modules.order
/lib/modules/%{kernel_release}/modules.builtin*

# rest modules.* are ghost (regenerated by post depmod -a invocation)
%ghost /lib/modules/%{kernel_release}/modules.alias
%ghost /lib/modules/%{kernel_release}/modules.alias.bin
%ghost /lib/modules/%{kernel_release}/modules.dep
%ghost /lib/modules/%{kernel_release}/modules.dep.bin
%ghost /lib/modules/%{kernel_release}/modules.devname
%ghost /lib/modules/%{kernel_release}/modules.softdep
%ghost /lib/modules/%{kernel_release}/modules.symbols
%ghost /lib/modules/%{kernel_release}/modules.symbols.bin

# symlinks pointing to kernelsrcdir
%ghost /lib/modules/%{kernel_release}/build
%ghost /lib/modules/%{kernel_release}/source

%ifarch alpha %{ix86} %{x8664} x32 ppc ppc64 sparc sparc64
%files vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{kernel_release}
%endif

%if %{have_drm}
%files drm
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/gpu
%endif

%if %{have_ide}
%files ide
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/ide/*
%if %{have_pcmcia}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/ide-cs.ko*
%endif
%endif

%if %{have_pcmcia}
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/pcmcia/*ko*
/lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/pcmcia*ko*
%if %{without rescuecd}
/lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/b1pcmcia.ko*
/lib/modules/%{kernel_release}/kernel/drivers/ata/pata_pcmcia.ko*
%endif
/lib/modules/%{kernel_release}/kernel/drivers/ide/ide-cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/arcnet/com20020_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/can/softing/softing_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/3com/3c574_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/3com/3c589_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/8390/axnet_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/8390/pcnet_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/amd/nmclan_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/fujitsu/fmvj18x_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/smsc/smc91c92_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/ethernet/xircom/xirc2ps_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/atmel/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/cisco/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/intersil/hostap/hostap_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/intersil/orinoco/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/marvell/libertas/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/tty/serial/8250/serial_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif

%if %{have_sound}
%files sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/sound
%exclude %dir /lib/modules/%{kernel_release}/kernel/sound
%exclude /lib/modules/%{kernel_release}/kernel/sound/ac97_bus.ko*
%exclude /lib/modules/%{kernel_release}/kernel/sound/sound*.ko*
%if %{have_oss}
%exclude /lib/modules/%{kernel_release}/kernel/sound/oss
%endif
%ifnarch sparc
/lib/modules/%{kernel_release}/kernel/drivers/usb/gadget/legacy/g_midi.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/pci/cx88/cx88-alsa.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/usb/em28xx/em28xx-alsa.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/pci/saa7134/saa7134-alsa.ko*
%endif

%if %{have_oss}
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/sound/oss
%endif
%endif

%files headers -f files.headers_exclude_kbuild
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}
%{_kernelsrcdir}/include
%dir %{_kernelsrcdir}/arch
%dir %{_kernelsrcdir}/arch/[!K]*
%{_kernelsrcdir}/arch/*/include
%dir %{_kernelsrcdir}/security
%dir %{_kernelsrcdir}/security/selinux
%{_kernelsrcdir}/security/selinux/include
%{_kernelsrcdir}/.config
%{_kernelsrcdir}/Module.symvers

%files module-build -f files.mb_include_modulebuild_and_dirs
%defattr(644,root,root,755)
%ifarch ppc ppc64
%{_kernelsrcdir}/arch/powerpc/lib/crtsavres.*
%endif
%exclude %dir %{_kernelsrcdir}/arch/um
%{_kernelsrcdir}/arch/*/kernel/asm-offsets*
%{_kernelsrcdir}/arch/*/kernel/sigframe*.h
%{_kernelsrcdir}/drivers/lguest/lg.h
%{_kernelsrcdir}/drivers/media/pci/bt8xx/bttv.h
%{_kernelsrcdir}/kernel/bounds.c
%{_kernelsrcdir}/scripts/basic/*.c
%attr(755,root,root) %{_kernelsrcdir}/scripts/kconfig/*.sh
%{_kernelsrcdir}/scripts/kconfig/*.in
%{_kernelsrcdir}/scripts/kconfig/*_shipped
%{_kernelsrcdir}/scripts/kconfig/*.pl
%{_kernelsrcdir}/scripts/kconfig/*.glade
%{_kernelsrcdir}/scripts/kconfig/*.gperf
%{_kernelsrcdir}/scripts/kconfig/*.cc
%{_kernelsrcdir}/scripts/kconfig/*.y
%{_kernelsrcdir}/scripts/kconfig/*.l
%{_kernelsrcdir}/scripts/kconfig/[c-k]*.c
%{_kernelsrcdir}/scripts/kconfig/[c-k]*.h
%{_kernelsrcdir}/scripts/kconfig/l*.h
%{_kernelsrcdir}/scripts/kconfig/[m-u]*.c
%{_kernelsrcdir}/scripts/kconfig/[m-u]*.h
%{_kernelsrcdir}/scripts/kconfig/lxdialog
%{_kernelsrcdir}/scripts/mod/*.c
%{_kernelsrcdir}/scripts/mod/modpost.h
%attr(755,root,root) %{_kernelsrcdir}/scripts/mkcompile_h
%{_kernelsrcdir}/scripts/mkmakefile
%{_kernelsrcdir}/scripts/module-common.lds
%attr(755,root,root) %{_kernelsrcdir}/scripts/setlocalversion
%{_kernelsrcdir}/scripts/*.c
%{_kernelsrcdir}/scripts/*.h
%attr(755,root,root) %{_kernelsrcdir}/scripts/*.sh
%{_kernelsrcdir}/scripts/selinux/genheaders/*.c
%{_kernelsrcdir}/scripts/selinux/mdp/*.c
%exclude %dir %{_kernelsrcdir}/security
%exclude %dir %{_kernelsrcdir}/security/selinux

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%dir %{_docdir}/%{name}-%{version}

%{_docdir}/%{name}-%{version}/[!jkz]*
%{_docdir}/%{name}-%{version}/[jkz]*.txt
%{_docdir}/%{name}-%{version}/kbuild
%{_docdir}/%{name}-%{version}/kdump
%lang(ja) %{_docdir}/%{name}-%{version}/ja_JP
%lang(ko) %{_docdir}/%{name}-%{version}/ko_KR
%lang(zh_CN) %{_docdir}/%{name}-%{version}/zh_CN
%endif

%if %{with source}
%files source -f files.source_exclude_modulebuild_and_dirs
%defattr(644,root,root,755)
%{_kernelsrcdir}/arch/*/[!Mik]*
%{_kernelsrcdir}/arch/*/kernel/[!M]*
%{_kernelsrcdir}/arch/ia64/install.sh
%{_kernelsrcdir}/arch/m68k/ifpsp060/[!M]*
%{_kernelsrcdir}/arch/m68k/ifpsp060/MISC
%{_kernelsrcdir}/arch/m68k/install.sh
%{_kernelsrcdir}/arch/parisc/install.sh
%{_kernelsrcdir}/arch/x86/ia32/[!M]*
%{_kernelsrcdir}/arch/powerpc/kvm
%ifarch ppc ppc64
%exclude %{_kernelsrcdir}/arch/powerpc/lib/crtsavres.*
%endif
%{_kernelsrcdir}/arch/arm/kvm
%{_kernelsrcdir}/arch/arm64/kvm
%{_kernelsrcdir}/arch/mips/kvm
%{_kernelsrcdir}/arch/s390/kvm
%{_kernelsrcdir}/arch/x86/kvm
%exclude %{_kernelsrcdir}/arch/*/kernel/asm-offsets*
%exclude %{_kernelsrcdir}/arch/*/kernel/sigframe*.h
%exclude %{_kernelsrcdir}/drivers/lguest/lg.h
%exclude %{_kernelsrcdir}/drivers/media/pci/bt8xx/bttv.h
%{_kernelsrcdir}/block
%{_kernelsrcdir}/certs
%{_kernelsrcdir}/crypto
%{_kernelsrcdir}/drivers
%{_kernelsrcdir}/firmware
%{_kernelsrcdir}/fs
%{_kernelsrcdir}/init
%{_kernelsrcdir}/ipc
%{_kernelsrcdir}/kernel
%exclude %{_kernelsrcdir}/kernel/bounds.c
%{_kernelsrcdir}/lib
%{_kernelsrcdir}/mm
%{_kernelsrcdir}/net
%{_kernelsrcdir}/virt
%{_kernelsrcdir}/samples
%{_kernelsrcdir}/scripts/*
%exclude %{_kernelsrcdir}/scripts/Kbuild.include
%exclude %{_kernelsrcdir}/scripts/Makefile*
%exclude %{_kernelsrcdir}/scripts/basic
%exclude %{_kernelsrcdir}/scripts/kconfig
%exclude %{_kernelsrcdir}/scripts/mkcompile_h
%exclude %{_kernelsrcdir}/scripts/mkmakefile
%exclude %{_kernelsrcdir}/scripts/mod
%exclude %{_kernelsrcdir}/scripts/module-common.lds
%exclude %{_kernelsrcdir}/scripts/setlocalversion
%exclude %{_kernelsrcdir}/scripts/*.c
%exclude %{_kernelsrcdir}/scripts/*.h
%exclude %{_kernelsrcdir}/scripts/*.sh
%exclude %dir %{_kernelsrcdir}/scripts/selinux
%exclude %{_kernelsrcdir}/scripts/selinux/Makefile
%exclude %dir %{_kernelsrcdir}/scripts/selinux/genheaders
%exclude %{_kernelsrcdir}/scripts/selinux/genheaders/Makefile
%exclude %{_kernelsrcdir}/scripts/selinux/genheaders/*.c
%exclude %dir %{_kernelsrcdir}/scripts/selinux/mdp
%exclude %{_kernelsrcdir}/scripts/selinux/mdp/Makefile
%exclude %{_kernelsrcdir}/scripts/selinux/mdp/*.c
%{_kernelsrcdir}/sound
%{_kernelsrcdir}/security
%exclude %{_kernelsrcdir}/security/selinux/include
%{_kernelsrcdir}/tools/*
%{_kernelsrcdir}/usr
%{_kernelsrcdir}/COPYING
%{_kernelsrcdir}/CREDITS
%{_kernelsrcdir}/MAINTAINERS
%{_kernelsrcdir}/README
%{_kernelsrcdir}/REPORTING-BUGS
%endif
