#
# TODO:
#		ALL
#
# Conditional build:
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	source		# don't build kernel-source package
%bcond_without	pcmcia		# don't build pcmcia
%bcond_without	vesafb_tng	# build without vesafb-tng patch applied (breaks other fb modules)

%bcond_with     preemptive      # build preemptive kernel
%bcond_with	suspend2	# build software suspend support
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	vserver		# added vserver.
%bcond_with	xen		# added Xen support.
%bcond_without	grsecurity	# don't build grsecurity at all
%bcond_without	grsec_minimal	# build only minimal subset (proc,link,fifo,shm)
%bcond_with	grsec_full	# build full grsecurity

%{?debug:%define with_verbose 1}

%if %{without grsecurity}
%undefine	with_grsec_full
%undefine	with_grsec_minimal
%endif

%if %{with grsec_full}
%undefine	with_grsec_minimal
%define		with_grsecurity		1
%endif

%if %{with grsec_minimal}
%undefine	with_grsec_full
%define		with_grsecurity		1
%endif

%if %{with grsec_full} && %{with vserver}
full grsecurity conflicts with vserver
%endif

%ifarch sparc
# sparc32 is missing important updates from 2.5 cycle - won't build.
%undefine	with_smp
%endif

%ifarch ia64
# broken
%undefine	with_up
%endif

%define		have_drm	1
%define		have_oss	1
%define		have_sound	1

%ifarch %{ix86} alpha ppc
%define		have_isa	1
%else
%define		have_isa	0
%endif

#ifarch	ppc64 ppc
#define		_target_base_arch	powerpc
#endif

%ifarch sparc sparc64
%undefine	with_pcmcia
%define		have_drm	0
%define		have_oss	0
%endif

## Program required by kernel to work.
%define		_binutils_ver		2.12.1
%define		_util_linux_ver		2.10o
%define		_module_init_tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_reiser4progs_ver	1.0.0
%define		_xfsprogs_ver		2.6.0
%define		_pcmcia_cs_ver		3.1.21
%define		_pcmciautils_ver	004
%define		_quota_tools_ver	3.09
%define		_ppp_ver		1:2.4.0
%define		_isdn4k_utils_ver	3.1pre1
%define		_nfs_utils_ver		1.0.5
%define		_procps_ver		3.2.0
%define		_oprofile_ver		0.9
%define		_udev_ver		071
%define		_mkvmlinuz_ver		1.3

%define		_rel			0.1

%define		_netfilter_snap		20060329
%define		_nf_hipac_ver		0.9.1

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

%define		squashfs_version	3.0
%define		suspend_version		2.2.1

%define		xen_version		3.0.2

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel%{?with_grsec_full:-grsecurity}%{?with_vserver:-vserver}%{?with_xen:-xen}%{?with_preemptive:-preempt}
%define		_postver	.9
#define		_postver	%{nil}
Version:	2.6.16%{_postver}
Release:	%{_rel}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
%define		_rc	%{nil}
#define		_rc	-rc5
#Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/linux-%{version}%{_rc}.tar.bz2
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{version}%{_rc}.tar.bz2
# Source0-md5:	d1b670c17c1dd49ddc614e480df0ec73
Source1:	kernel-autoconf.h
Source2:	kernel-config.h
#Source3:	http://www.kernel.org/pub/linux/kernel/v2.6/snapshots/patch-2.6.14%{_rc}-git2.bz2
## Source3-md5:	3db58f38e8a3c001d1a18eb1ee27db3b
Source5:	kernel-ppclibs.Makefile
#Source6:	http://people.redhat.com/mingo/debloating-patches/debloating-patches-2.6.15-rc7.tar.gz
## Source6-md5:	ca7a1cdef3e5c95f182d039cebd92b5e

Source10:	http://suspend2.net/downloads/all/suspend2-2.2.1-for-2.6.16.tar.bz2
# Source10-md5:	a235b258487dcce5db8a6f52a3b13bc3
Source12:	ftp://ftp.namesys.com/pub/reiser4-for-2.6/2.6.16/reiser4-for-2.6.16-1.patch.gz
# Source12-md5:	f51303b5e445432b974a729b76036c40

Source20:	kernel-i386.config
Source21:	kernel-i386-smp.config
Source22:	kernel-x86_64.config
Source23:	kernel-x86_64-smp.config
Source24:	kernel-sparc.config
Source25:	kernel-sparc-smp.config
Source26:	kernel-sparc64.config
Source27:	kernel-sparc64-smp.config
Source28:	kernel-alpha.config
Source29:	kernel-alpha-smp.config
Source30:	kernel-ppc.config
Source31:	kernel-ppc-smp.config
Source32:	kernel-ia64.config
Source33:	kernel-ia64-smp.config

Source40:	kernel-netfilter.config
Source41:	kernel-squashfs.config
Source42:	kernel-suspend2.config
Source43:	kernel-vserver.config
Source44:	kernel-vesafb-tng.config
Source45:	kernel-grsec.config

###
#	Patches
###

# tahoe9XX http://tahoe.pl/drivers/tahoe9xx-2.6.11.5.patch
Patch2:		tahoe9xx-2.6.11.5.patch

#	http://dev.gentoo.org/~spock/projects/gensplash/archive/fbsplash-0.9.2-r5-2.6.16.patch
Patch4:		fbsplash-0.9.2-r5-2.6.16.patch
Patch5:		linux-2.6-vesafb-tng.patch

# directly from http://mesh.dl.sourceforge.net/sourceforge/squashfs/squashfs3.0.tar.gz
#		from linux-2.6.15
Patch6:		squashfs%{squashfs_version}-patch

Patch7:		linux-alpha-isa.patch
Patch8:		linux-fbcon-margins.patch
Patch9:		linux-static-dev.patch

# netfilter snap
## submitted

## base
Patch10:	pom-ng-IPV4OPTSSTRIP-%{_netfilter_snap}.patch
Patch11:	pom-ng-connlimit-%{_netfilter_snap}.patch
Patch12:	pom-ng-expire-%{_netfilter_snap}.patch
Patch13:	pom-ng-fuzzy-%{_netfilter_snap}.patch
Patch14:	pom-ng-ipv4options-%{_netfilter_snap}.patch
Patch15:	pom-ng-nth-%{_netfilter_snap}.patch
Patch16:	pom-ng-osf-%{_netfilter_snap}.patch
Patch17:	pom-ng-psd-%{_netfilter_snap}.patch
Patch18:	pom-ng-quota-%{_netfilter_snap}.patch
Patch19:	pom-ng-random-%{_netfilter_snap}.patch
Patch20:	pom-ng-set-%{_netfilter_snap}.patch
Patch21:	pom-ng-time-%{_netfilter_snap}.patch
Patch22:	pom-ng-u32-%{_netfilter_snap}.patch

## extra
Patch30:	pom-ng-ACCOUNT-%{_netfilter_snap}.patch
Patch31:	pom-ng-IPMARK-%{_netfilter_snap}.patch
Patch32:	pom-ng-ROUTE-%{_netfilter_snap}.patch
Patch33:	pom-ng-TARPIT-%{_netfilter_snap}.patch
Patch34:	pom-ng-account-%{_netfilter_snap}.patch
Patch35:	pom-ng-ipp2p-%{_netfilter_snap}.patch
Patch36:	pom-ng-rpc-%{_netfilter_snap}.patch

###
#	End netfilter
###

# from http://www.linuximq.net/patchs/linux-2.6.16-imq2.diff
Patch50:	linux-2.6.16-imq2.diff

# from http://bluetooth-alsa.sourceforge.net/sco-mtu.patch
Patch51:	sco-mtu.patch

# support for HDAPS (Hard Disk Active Protection System)
# that can be found in IBM/Lenovo ThinkPad laptops
# from: http://www.dresco.co.uk/hdaps/hdaps_protect.20060326.patch
Patch52:	linux-hdaps_protect.patch

# esfq
# from http://fatooh.org/esfq-2.6/current/esfq-kernel.patch
Patch53:	esfq-kernel.patch

# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	linux-2.6-atm-vbr.patch
Patch56:	linux-2.6-atmdd.patch

Patch57:	linux-2.6-cpuset_virtualization.patch

# Derived from http://www.skd.de/e_en/products/adapters/pci_64/sk-98xx_v20/software/linux/driver/install-8_31.tar.bz2
Patch60:	linux-2.6-sk98lin-8.31.2.3.patch

# vserver from: http://vserver.13thfloor.at/Experimental/patch-2.6.16-vs2.1.1-rc15.diff
Patch100:	linux-2.6-vs2.1.patch
Patch101:	linux-2.6-vs2.1-grsec-minimal.patch

# from http://www.cl.cam.ac.uk/Research/SRG/netos/xen/downloads/xen-3.0.2-src.tgz
Patch120:	xen-3.0-2.6.16.patch


Patch1000:	linux-2.6-grsec-minimal.patch
# grsecurity snap for 2.6.16.
# from http://www.grsecurity.net/~spender/grsecurity-2.1.9-2.6.16-200603292139.patch
## [pl]nienaklada sie 
#Patch9999:	grsecurity-2.1.9-2.6.16-200603292139.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 3:2.14.90.0.7
BuildRequires:	diffutils
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
BuildRequires:	gcc >= 5:3.2
BuildRequires:	module-init-tools
# for hostname command
BuildRequires:	net-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.217
Autoreqprov:	no
Requires:	coreutils
Requires:	geninitrd >= 2.57
Requires:	module-init-tools >= 0.9.9
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	kernel(nf-hipac) = %{_nf_hipac_ver}
Provides:	kernel(realtime-lsm) = 0.1.1
Provides:	kernel(xen) = %{_xen_version}
Provides:	kernel-misc-fuse
Provides:	kernel-net-hostap = 0.4.4
Provides:	kernel-net-ieee80211
Provides:	kernel-net-ipp2p = 1:0.8.0
Provides:	kernel-net-ipw2100 = 1.1.3
Provides:	kernel-net-ipw2200 = 1.0.8
Provides:	module-info
Obsoletes:	kernel-misc-fuse
Obsoletes:	kernel-modules
Obsoletes:	kernel-net-hostap
Obsoletes:	kernel-net-ieee80211
Obsoletes:	kernel-net-ipp2p
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
Conflicts:	oprofile < %{_oprofile_ver}
Conflicts:	ppp < %{_ppp_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	udev < %{_udev_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
%if %{with xen}
ExclusiveArch:	%{ix86}
%else
ExclusiveArch:	%{ix86} alpha %{x8664} ia64 ppc ppc64 sparc sparc64
%endif
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch ia64
%define		initrd_dir	/boot/efi
%else
%define		initrd_dir	/boot
%endif

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

%package vmlinux
Summary:	vmlinux - uncompressed kernel image
Summary(pl):	vmlinux - rozpakowany obraz j±dra
Group:		Base/Kernel

%description vmlinux
vmlinux - uncompressed kernel image.

%description vmlinux -l pl
vmlinux - rozpakowany obraz j±dra.

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel-drm = %{drm_xfree_version}
Autoreqprov:	no

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description drm -l pl
Sterowniki DRM (%{drm_xfree_version}).

%package pcmcia
Summary:	PCMCIA modules
Summary(pl):	Modu³y PCMCIA
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel(pcmcia)
Provides:	kernel-pcmcia = %{pcmcia_version}
Conflicts:	pcmcia-cs < %{_pcmcia_cs_ver}
Conflicts:	pcmciautils < %{_pcmciautils_ver}
Autoreqprov:	no

%description pcmcia
PCMCIA modules (%{pcmcia_version}).

%description pcmcia -l pl
Modu³y PCMCIA (%{pcmcia_version}).

%package libs
Summary:	Libraries for preparing bootable kernel on PowerPCs
Summary(pl):	Biblioteki do przygotowania bootowalnego j±dra dla PowerPC
Group:		Base/Kernel
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description libs
Libraries for preparing bootable kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description libs -l pl
Biblioteki do przygotowania bootowalnego j±dra dla PowerPC. Skrypt
mkvmlinuz mo¿e byæ do tego przydatny.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l pl
Sterowniki d¼wiêku ALSA (Advanced Linux Sound Architecture).

%package sound-oss
Summary:	OSS kernel modules
Summary(pl):	Sterowniki d¼wiêku OSS
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-oss
OSS (Open Sound System) drivers.

%description sound-oss -l pl
Sterowniki d¼wiêku OSS (Open Sound System).

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl):	J±dro Linuksa w wersji %{version} dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires:	coreutils
Requires:	geninitrd >= 2.26
Requires:	module-init-tools >= 0.9.9
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	kernel(nf-hipac) = %{_nf_hipac_ver}
Provides:	kernel(realtime-lsm) = 0.1.1
Provides:	kernel(xen) = %{_xen_version}
Provides:	kernel-smp-misc-fuse
Provides:	kernel-smp-net-hostap = 0.4.4
Provides:	kernel-smp-net-ieee80211
Provides:	kernel-smp-net-ipp2p = 1:0.8.0
Provides:	kernel-smp-net-ipw2100 = 1.1.3
Provides:	kernel-smp-net-ipw2200 = 1.0.8
Provides:	module-info
Obsoletes:	kernel-smp-misc-fuse
Obsoletes:	kernel-smp-net-hostap
Obsoletes:	kernel-smp-net-ieee80211
Obsoletes:	kernel-smp-net-ipp2p
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
Conflicts:	oprofile < %{_oprofile_ver}
Conflicts:	ppp < %{_ppp_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
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

%package smp-vmlinux
Summary:	vmlinux - uncompressed SMP kernel image
Summary(pl):	vmlinux - rozpakowany obraz j±dra SMP
Group:		Base/Kernel

%description smp-vmlinux
vmlinux - uncompressed SMP kernel image.

%description smp-vmlinux -l pl
vmlinux - rozpakowany obraz j±dra SMP.

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	kernel-drm = %{drm_xfree_version}
Autoreqprov:	no

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description smp-drm -l pl
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package smp-pcmcia
Summary:	PCMCIA modules for SMP kernel
Summary(pl):	Modu³y PCMCIA dla maszyn SMP
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	kernel(pcmcia)
Provides:	kernel-pcmcia = %{pcmcia_version}
Conflicts:	pcmcia-cs < %{_pcmcia_cs_ver}
Conflicts:	pcmciautils < %{_pcmciautils_ver}
Autoreqprov:	no

%description smp-pcmcia
PCMCIA modules for SMP kernel (%{pcmcia_version}).

%description smp-pcmcia -l pl
Modu³y PCMCIA dla maszyn SMP (%{pcmcia_version}).

%package smp-libs
Summary:	Libraries for preparing bootable SMP kernel on PowerPCs
Summary(pl):	Biblioteki do przygotowania bootowalnego j±dra dla wieloprocesorowych PowerPC
Group:		Base/Kernel
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description smp-libs
Libraries for preparing bootable SMP kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description smp-libs -l pl
Biblioteki do przygotowania bootowalnego j±dra dla wieloprocesorowych
PowerPC. Skrypt mkvmlinuz mo¿e byæ do tego przydatny.

%package smp-sound-alsa
Summary:	ALSA SMP kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-alsa
ALSA (Advanced Linux Sound Architecture) SMP sound drivers.

%description smp-sound-alsa -l pl
Sterowniki d¼wiêku ALSA (Advanced Linux Sound Architecture) dla maszyn
wieloprocesorowych.

%package smp-sound-oss
Summary:	OSS SMP kernel modules
Summary(pl):	Sterowniki d¼wiêku OSS dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-oss
OSS (Open Sound System) SMP sound drivers.

%description smp-sound-oss -l pl
Sterowniki OSS (Open Sound System) dla maszyn wieloprocesorowych.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra Linuksa
Group:		Development/Building
Provides:	kernel-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-headers(agpgart) = %{version}
Provides:	kernel-headers(alsa-drivers)
Provides:	kernel-headers(bridging) = %{version}
Provides:	kernel-headers(netfilter) = %{_netfilter_snap}
Provides:	kernel-headers(reiserfs) = %{version}
Provides:	kernel-i2c-devel
Obsoletes:	kernel-i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbêdne do rekompilacji j±dra
oraz budowania modu³ów j±dra.

%package module-build
Summary:	Development files for building kernel modules
Summary(pl):	Pliki s³u¿±ce do budowania modu³ów j±dra
Group:		Development/Building
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-module-build = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%description module-build -l pl
Pliki ze drzewa ¼róde³ j±dra potrzebne do budowania modu³ów j±dra
Linuksa z zewnêtrznych pakietów.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuksa
Group:		Development/Building
Requires:	%{name}-module-build = %{epoch}:%{version}-%{release}
Provides:	kernel-source = %{epoch}:%{version}-%{release}
Autoreqprov:	no

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
Group:		Documentation
Provides:	kernel-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê do j±dra Linuksa pochodz±c± z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{version}%{_rc} -a10

%ifarch ppc
install %{SOURCE5} Makefile.ppclibs
%endif

%if %{with suspend2}
for i in suspend2-%{suspend_version}-for-2.6.16/*.patch; do
patch -p1 -s < $i
done
patch -p1 -s < suspend2-%{suspend_version}-for-2.6.16/3010-fork-non-conflicting-pages-for-copyback
%endif

# reiserfs4
%{__gzip} -dc %{SOURCE12} | %{__patch} -s -p1

%patch2 -p1

%patch4 -p1

%ifarch %{ix86}
%if %{with vesafb_tng}
%patch5 -p1
%endif
%endif

%patch6 -p1

%patch7 -p1
%patch8 -p1
%patch9 -p1

## netfilter
# submitted

# base
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1

## extra
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1

##
# end of netfilter

%patch50 -p1

%patch51 -p1

%patch52 -p1

%patch53 -p1


%patch55 -p1
%patch56 -p1

%ifarch %{ix86} ia64 x86_64
%patch57 -p1
%endif

%patch60 -p1

%if %{with vserver}
%patch100 -p1
%if %{with grsec_minimal}
%patch101 -p1
%endif
%endif

%if %{with xen}
%ifarch %{ix86}
%patch120 -p1
%endif
%else
echo "Arch: $arch is not supported by Xen"
%endif

%if %{with grsec_minimal} && %{without vserver}
%patch1000 -p1
%endif
%if %{with grsec_full} && %{without vserver}
#patch9999 -p1
%endif

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{_postver}#g' Makefile

# on sparc this line causes CONFIG_INPUT=m (instead of =y), thus breaking build
sed -i -e '/select INPUT/d' net/bluetooth/hidp/Kconfig

%build
TuneUpConfigForIX86 () {
%ifarch %{ix86}
    %ifnarch i386
	sed -i 's:CONFIG_M386=y:# CONFIG_M386 is not set:' $1
    %endif
    %ifarch i486
	sed -i 's:# CONFIG_M486 is not set:CONFIG_M486=y:' $1
    %endif
    %ifarch i586
	sed -i 's:# CONFIG_M586 is not set:CONFIG_M586=y:' $1
    %endif
    %ifarch i686
	sed -i 's:# CONFIG_M686 is not set:CONFIG_M686=y:' $1
    %endif
    %ifarch pentium3
	sed -i 's:# CONFIG_MPENTIUMIII is not set:CONFIG_MPENTIUMIII=y:' $1
    %endif
    %ifarch pentium4
	sed -i 's:# CONFIG_MPENTIUM4 is not set:CONFIG_MPENTIUM4=y:' $1
    %endif
    %ifarch athlon
	sed -i 's:# CONFIG_MK7 is not set:CONFIG_MK7=y:' $1
    %endif
    %ifarch pentium3 pentium4 athlon
#	kernel-i386-smp.config contains 64G support by default.
	%if %{with up}
	    sed -i "s:CONFIG_HIGHMEM4G=y:# CONFIG_HIGHMEM4G is not set:" $1
	    sed -i "s:# CONFIG_HIGHMEM64G is not set:CONFIG_HIGHMEM64G=y\nCONFIG_X86_PAE=y:" $1
	%endif
    %endif
    %ifarch i686 pentium3 pentium4 athlon
	sed -i 's:CONFIG_MATH_EMULATION=y:# CONFIG_MATH_EMULATION is not set:' $1
    %endif
    %if %{with regparm}
	sed -i 's:# CONFIG_REGPARM is not set:CONFIG_REGPARM=y:' $1
    %endif
%endif
}

%if "%{_target_base_arch}" != "%{_arch}"
    CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
    DepMod=/bin/true
    %if "%{_arch}" == "sparc" && "%{_target_base_arch}" == "sparc64"
	DepMod=/sbin/depmod
    %endif
    %if "%{_arch}" == "x86_64" && "%_target_base_arch}" == "i386"
	CrossOpts="ARCH=%{_target_base_arch}"
	DepMod=/sbin/depmod
    %endif
%else
    CrossOpts=""
    DepMod=/sbin/depmod
%endif


BuildConfig() {
	%{?debug:set -x}
	# is this a special kernel we want to build?
	smp=
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
	if [ "$smp" = "yes" ]; then
		Config="%{_target_base_arch}-smp"
	else
		Config="%{_target_base_arch}"
	fi
	KernelVer=%{version}-%{release}$1

	echo "Building config file [using $Config.conf] for KERNEL $1..."
	cat $RPM_SOURCE_DIR/kernel-$Config.config > arch/%{_target_base_arch}/defconfig

	TuneUpConfigForIX86 arch/%{_target_base_arch}/defconfig

%ifarch ppc ppc64
	if [ "$smp" = "yes" ]; then
		install %{SOURCE31} arch/%{_target_base_arch}/defconfig
	else
		install %{SOURCE30} arch/%{_target_base_arch}/defconfig
	fi
%endif

%ifarch ppc64
	sed -i "s:# CONFIG_PPC64 is not set:CONFIG_PPC64=y:" arch/%{_target_base_arch}/defconfig
%endif

	# netfilter
	cat %{SOURCE40} >> arch/%{_target_base_arch}/defconfig

	# squashfs
	cat %{SOURCE41} >> arch/%{_target_base_arch}/defconfig

%if %{with suspend2}
	cat %{SOURCE42} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with vserver}
	sed -i 's/^CONFIG_VMSPLIT_//g' arch/%{_target_base_arch}/defconfig
	cat %{SOURCE43} >> arch/%{_target_base_arch}/defconfig
%endif

	# vesafb-tng
%if %{with vesafb_tng}
	cat %{SOURCE44} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with grsecurity}
	cat %{SOURCE45} >> arch/%{_target_base_arch}/defconfig
%endif

	# fbsplash
	echo "CONFIG_FB_SPLASH=y" >> arch/%{_target_base_arch}/defconfig


%if %{with preemptive}
	sed -i "s:CONFIG_PREEMPT_NONE=y:# CONFIG_PREEMPT_NONE is not set:" arch/%{_target_base_arch}/defconfig
	sed -i "s:# CONFIG_PREEMPT is not set:CONFIG_PREEMPT=y:" arch/%{_target_base_arch}/defconfig
	echo "# CONFIG_DEBUG_PREEMPT is not set" >> arch/%{_target_base_arch}/defconfig
%endif
	
%{?debug:sed -i "s:# CONFIG_DEBUG_SLAB is not set:CONFIG_DEBUG_SLAB=y:" arch/%{_target_base_arch}/defconfig}
%{?debug:sed -i "s:# CONFIG_DEBUG_PREEMPT is not set:CONFIG_DEBUG_PREEMPT=y:" arch/%{_target_base_arch}/defconfig}
%{?debug:sed -i "s:# CONFIG_RT_DEADLOCK_DETECT is not set:CONFIG_RT_DEADLOCK_DETECT=y:" arch/%{_target_base_arch}/defconfig}

	ln -sf arch/%{_target_base_arch}/defconfig .config
	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
	rm -f include/linux/autoconf.h
	%{__make} $CrossOpts include/linux/autoconf.h
	if [ "$smp" = "yes" ]; then
		install include/linux/autoconf.h \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h
		install .config \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/config-smp
	else
		install include/linux/autoconf.h \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h
		install .config \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/config-up
	fi
}

BuildKernel() {
	%{?debug:set -x}
	echo "Building kernel $1 ..."
	%{__make} $CrossOpts mrproper \
		RCS_FIND_IGNORE='-name build-done -prune -o'
	ln -sf arch/%{_target_base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%else
	%{__make} $CrossOpts clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%endif
	%{__make} $CrossOpts include/linux/version.h \
		%{?with_verbose:V=1}


# make does vmlinux, modules and bzImage at once
%ifarch sparc sparc64
%ifarch sparc64
	%{__make} $CrossOpts image \
		%{?with_verbose:V=1}

	%{__make} $CrossOpts modules \
		%{?with_verbose:V=1}
%else
	sparc32 %{__make} \
		%{?with_verbose:V=1}
%endif
%else
	%{__make} $CrossOpts \
		%{?with_verbose:V=1}
%endif
}

PreInstallKernel() {
	smp=
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
	if [ "$smp" = "yes" ]; then
		Config="%{_target_base_arch}-smp"
	else
		Config="%{_target_base_arch}"
	fi
	KernelVer=%{version}-%{release}$1

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86} %{x8664}
	install arch/%{_target_base_arch}/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
%endif
%ifarch alpha sparc sparc64
	gzip -cfv vmlinux > vmlinuz
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinuz $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%ifarch sparc
	elftoaout arch/sparc/boot/image -o vmlinux.aout
	install vmlinux.aout $KERNEL_INSTALL_DIR/boot/vmlinux.aout-$KernelVer
%endif
%ifarch sparc64
	elftoaout arch/sparc64/boot/image -o vmlinux.aout
	install vmlinux.aout $KERNEL_INSTALL_DIR/boot/vmlinux.aout-$KernelVer
%endif
%endif
%ifarch ppc ppc64
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch ppc-broken
	%{__make} -f Makefile.ppclibs install \
		DESTDIR=$KERNEL_INSTALL_DIR/boot/libs-$KernelVer
%endif
%ifarch ia64
	gzip -cfv vmlinux > vmlinuz
	install -d $KERNEL_INSTALL_DIR/boot/efi
	install vmlinuz $KERNEL_INSTALL_DIR/boot/efi/vmlinuz-$KernelVer
	ln -sf efi/vmlinuz-$KernelVer $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
	%{__make} $CrossOpts modules_install \
		%{?with_verbose:V=1} \
		DEPMOD=$DepMod \
     		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	if [ "$smp" = "yes" ]; then
		install Module.symvers \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/Module.symvers-smp
	else
		install Module.symvers \
			$KERNEL_INSTALL_DIR/usr/src/linux-%{version}/Module.symvers-up
	fi

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	[ -z "$CrossOpts" ] && \
	/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || echo
	[ ! -z "$CrossOpts" ] && \
	touch $KERNEL_INSTALL_DIR/lib/modules/$KernelVer/modules.dep
	echo "KERNEL RELEASE $KernelVer DONE"
}

KERNEL_BUILD_DIR=`pwd`
echo "-%{release}" > localversion
#install -m 644 %{SOURCE50} FAQ-pl

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
%if %{with smp}
BuildKernel smp
PreInstallKernel smp
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

%if "%{_target_base_arch}" != "%{_arch}"
    CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
    export DEPMOD=/bin/true
    %if "%{_arch}" == "sparc" && "%{_target_base_arch}" == "sparc64"
	unset DEPMOD
    %endif
    %if "%{_arch}" == "x86_64" && "%{_target_base_arch}" == "i386"
	CrossOpts="ARCH=%{_target_base_arch}"
	unset DEPMOD
    %endif
%else
    CrossOpts=""
%endif


install -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{version}-%{release}{,smp}

KERNEL_BUILD_DIR=`pwd`

%if %{with up} || %{with smp}
cp -a $KERNEL_BUILD_DIR/build-done/kernel-*/* $RPM_BUILD_ROOT
%endif

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf %{_prefix}/src/linux-%{version} \
			$RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		install -d $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/misc
	fi
done

ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux

find . -maxdepth 1 ! -name "build-done" ! -name "." -exec cp -a "{}" "$RPM_BUILD_ROOT/usr/src/linux-%{version}/" ";"

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

%{__make} $CrossOpts mrproper \
	RCS_FIND_IGNORE='-name build-done -prune -o'

find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/config-up \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}
fi

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/config-smp \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}
fi

%if %{with up} || %{with smp}
# UP or SMP
install $KERNEL_BUILD_DIR/build-done/kernel-*/usr/src/linux-%{version}/include/linux/* \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
%endif

%{__make} $CrossOpts mrproper
%{__make} $CrossOpts include/linux/version.h
install %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/include/linux/autoconf.h
install %{SOURCE2} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/include/linux/config.h

%if %{with up} || %{with smp}
# ghosted initrd
touch $RPM_BUILD_ROOT/boot/initrd-%{version}-%{release}{,smp}.gz
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%preun
rm -f /lib/modules/%{version}-%{release}/modules.*
if [ -x /sbin/new-kernel-pkg ]; then
    /sbin/new-kernel-pkg --remove %{version}-%{release}
fi

%post
%ifarch ia64
mv -f /boot/efi/vmlinuz /boot/efi/vmlinuz.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{version}-%{release} /boot/efi/vmlinuz
%endif
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

%depmod %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{version}-%{release}.gz %{initrd_dir}/initrd

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_grsec_full:grsecurity}%{?with_vserver:vserver}%{?with_xen:Xen}%{?with_preemptive:preempt}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{version}-%{release}.gz --install %{version}-%{release} --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi

%post vmlinux
mv -f /boot/vmlinux /boot/vmlinux.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{version}-%{release} /boot/vmlinux

%post libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{version}-%{release} %{version}-%{release}

%post drm
%depmod %{version}-%{release}

%postun drm
%depmod %{version}-%{release}

%post pcmcia
%depmod %{version}-%{release}

%postun pcmcia
%depmod %{version}-%{release}

%post sound-alsa
%depmod %{version}-%{release}

%postun sound-alsa
%depmod %{version}-%{release}

%post sound-oss
%depmod %{version}-%{release}

%postun sound-oss
%depmod %{version}-%{release}

%preun smp
rm -f /lib/modules/%{version}-%{release}smp/modules.*
if [ -x /sbin/new-kernel-pkg ]; then
    /sbin/new-kernel-pkg --remove %{version}-%{release}smp
fi

%post smp
%ifarch ia64
mv -f /boot/efi/vmlinuz /boot/efi/vmlinuz.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{version}-%{release}smp /boot/efi/vmlinuz
%endif
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

%depmod %{version}-%{release}smp

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{version}-%{release}smp.gz %{initrd_dir}/initrd

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_grsec_full:grsecurity}%{?with_vserver:vserver}%{?with_xen:Xen}%{?with_preemptive:preempt}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{version}-%{release}smp.gz --install %{version}-%{release}smp --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi

%post smp-vmlinux
mv -f /boot/vmlinux /boot/vmlinux.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{version}-%{release}smp /boot/vmlinux

%post smp-libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{version}-%{release}smp %{version}-%{release}smp

%post smp-drm
%depmod %{version}-%{release}smp

%postun smp-drm
%depmod %{version}-%{release}smp

%post smp-pcmcia
%depmod %{version}-%{release}smp

%postun smp-pcmcia
%depmod %{version}-%{release}smp

%post smp-sound-alsa
%depmod %{version}-%{release}smp

%postun smp-sound-alsa
%depmod %{version}-%{release}smp

%post smp-sound-oss
%depmod %{version}-%{release}smp

%postun smp-sound-oss
%depmod %{version}-%{release}smp

%post headers
# TODO: avoid %%post here and package symlink?
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux ]; then
		if [ "`ls -l %{_prefix}/src/linux | awk '{ print $10 }'`" = "linux-%{version}" ]; then
			rm -f %{_prefix}/src/linux
		fi
	fi
fi

%if %{with up}
%files
%defattr(644,root,root,755)
#doc FAQ-pl
%ifarch sparc sparc64
/boot/vmlinux.aout-%{version}-%{release}
%endif
%ifarch ia64
/boot/efi/vmlinuz-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%ghost /boot/initrd-%{version}-%{release}.gz
%dir /lib/modules/%{version}-%{release}
%dir /lib/modules/%{version}-%{release}/kernel
%ifnarch sparc
/lib/modules/%{version}-%{release}/kernel/arch
%endif
/lib/modules/%{version}-%{release}/kernel/crypto
/lib/modules/%{version}-%{release}/kernel/drivers
%if %{have_drm}
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif
%if %{have_oss} && %{have_isa}
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/media/radio/miropcm20.ko*
%endif
/lib/modules/%{version}-%{release}/kernel/fs
/lib/modules/%{version}-%{release}/kernel/kernel
/lib/modules/%{version}-%{release}/kernel/lib
/lib/modules/%{version}-%{release}/kernel/net
/lib/modules/%{version}-%{release}/kernel/security
%if %{have_sound}
%dir /lib/modules/%{version}-%{release}/kernel/sound
/lib/modules/%{version}-%{release}/kernel/sound/soundcore.*
%endif
%dir /lib/modules/%{version}-%{release}/misc
%if %{with pcmcia}
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*
%dir %{_sysconfdir}/modprobe.d/%{version}-%{release}

%ifarch alpha %{ix86} %{x8664} ppc ppc64 sparc sparc64
%files vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{version}-%{release}
%endif

%if %{have_drm}
%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif

%if %{with pcmcia}
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/telephony/ixj_pcmcia.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif

%ifarch ppc-broken
%if "%{_arch}" == "ppc"
%files libs
%defattr(644,root,root,755)
%dir /boot/libs-%{version}-%{release}
/boot/libs-%{version}-%{release}/common
/boot/libs-%{version}-%{release}/kernel
/boot/libs-%{version}-%{release}/lib
/boot/libs-%{version}-%{release}/of1275
/boot/libs-%{version}-%{release}/openfirmware
/boot/libs-%{version}-%{release}/simple
%dir /boot/libs-%{version}-%{release}/utils
%attr(755,root,root) /boot/libs-%{version}-%{release}/utils/*
/boot/libs-%{version}-%{release}/ld.script
%endif
%endif

%if %{have_sound}
%files sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound
%exclude %dir /lib/modules/%{version}-%{release}/kernel/sound
%exclude /lib/modules/%{version}-%{release}/kernel/sound/soundcore.*
%if %{have_oss}
%exclude /lib/modules/%{version}-%{release}/kernel/sound/oss
%endif

%if %{have_oss}
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound/oss
%if %{have_isa}
/lib/modules/%{version}-%{release}/kernel/drivers/media/radio/miropcm20.ko*
%endif
%endif
%endif			# %%{have_sound}
%endif			# %%{with up}

%if %{with smp}
%files smp
%defattr(644,root,root,755)
#doc FAQ-pl
%ifarch ia64
/boot/efi/vmlinuz-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%ghost /boot/initrd-%{version}-%{release}smp.gz
%dir /lib/modules/%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp/kernel
%ifnarch sparc
/lib/modules/%{version}-%{release}smp/kernel/arch
%endif
/lib/modules/%{version}-%{release}smp/kernel/crypto
/lib/modules/%{version}-%{release}smp/kernel/drivers
%if %{have_drm}
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif
%if %{have_oss} && %{have_isa}
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/media/radio/miropcm20.ko*
%endif
/lib/modules/%{version}-%{release}smp/kernel/fs
/lib/modules/%{version}-%{release}smp/kernel/kernel
/lib/modules/%{version}-%{release}smp/kernel/lib
/lib/modules/%{version}-%{release}smp/kernel/net
/lib/modules/%{version}-%{release}smp/kernel/security
%if %{have_sound}
%dir /lib/modules/%{version}-%{release}smp/kernel/sound
/lib/modules/%{version}-%{release}smp/kernel/sound/soundcore.*
%endif
%dir /lib/modules/%{version}-%{release}smp/misc
%if %{with pcmcia}
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/usb/host/sl811_cs.ko*
%endif
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*
%dir %{_sysconfdir}/modprobe.d/%{version}-%{release}smp

%ifarch alpha %{ix86} %{x8664} ppc ppc64 sparc sparc64
%files smp-vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{version}-%{release}smp
%endif

%if %{have_drm}
%files smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif

%if %{with pcmcia}
%files smp-pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/ixj_pcmcia.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/usb/host/sl811_cs.ko*
%endif

%ifarch ppc-broken
%if "%{_arch}" == "ppc"
%files smp-libs
%defattr(644,root,root,755)
%dir /boot/libs-%{version}-%{release}smp
/boot/libs-%{version}-%{release}smp/common
/boot/libs-%{version}-%{release}smp/kernel
/boot/libs-%{version}-%{release}smp/lib
/boot/libs-%{version}-%{release}smp/of1275
/boot/libs-%{version}-%{release}smp/openfirmware
/boot/libs-%{version}-%{release}smp/simple
%dir /boot/libs-%{version}-%{release}smp/utils
%attr(755,root,root) /boot/libs-%{version}-%{release}smp/utils/*
/boot/libs-%{version}-%{release}smp/ld.script
%endif
%endif

%if %{have_sound}
%files smp-sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound
%exclude %dir /lib/modules/%{version}-%{release}smp/kernel/sound
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/soundcore.*
%if %{have_oss}
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/oss
%endif

%if %{have_oss}
%files smp-sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound/oss
%if %{have_isa}
/lib/modules/%{version}-%{release}smp/kernel/drivers/media/radio/miropcm20.ko*
%endif
%endif
%endif			# %%{have_sound}
%endif			# %%{with smp}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%if %{with smp}
%{_prefix}/src/linux-%{version}/config-smp
%{_prefix}/src/linux-%{version}/Module.symvers-smp
%endif
%{_prefix}/src/linux-%{version}/config-up
%{?with_up:%{_prefix}/src/linux-%{version}/Module.symvers-up}

%files module-build
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Kbuild
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/localversion
%dir %{_prefix}/src/linux-%{version}/arch
%dir %{_prefix}/src/linux-%{version}/arch/*
%{_prefix}/src/linux-%{version}/arch/*/Makefile*
%{_prefix}/src/linux-%{version}/*/Kconfig*
%{_prefix}/src/linux-%{version}/*/*/Kconfig*
%{_prefix}/src/linux-%{version}/*/*/*/Kconfig*
%{_prefix}/src/linux-%{version}/*/*/*/*/Kconfig*
%{_prefix}/src/linux-%{version}/*/*/*/*/*/Kconfig*
%dir %{_prefix}/src/linux-%{version}/arch/*/kernel
%{_prefix}/src/linux-%{version}/arch/*/kernel/Makefile
%{_prefix}/src/linux-%{version}/arch/*/kernel/asm-offsets.*
%{_prefix}/src/linux-%{version}/arch/*/kernel/sigframe.h
%dir %{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/scripts/Kbuild.include
%{_prefix}/src/linux-%{version}/scripts/Makefile*
%{_prefix}/src/linux-%{version}/scripts/basic
%{_prefix}/src/linux-%{version}/scripts/mkmakefile
%{_prefix}/src/linux-%{version}/scripts/mod
%{_prefix}/src/linux-%{version}/scripts/setlocalversion
%{_prefix}/src/linux-%{version}/scripts/*.c
%{_prefix}/src/linux-%{version}/scripts/*.sh
%{_prefix}/src/linux-%{version}/scripts/kconfig/*

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%if %{with source}
%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch/*/[!Mk]*
%{_prefix}/src/linux-%{version}/arch/*/kernel/[!M]*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/asm-offsets.*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/sigframe.h
%exclude %{_prefix}/src/linux-%{version}/*/Kconfig*
%exclude %{_prefix}/src/linux-%{version}/*/*/Kconfig*
%exclude %{_prefix}/src/linux-%{version}/*/*/*/Kconfig*
%exclude %{_prefix}/src/linux-%{version}/*/*/*/*/Kconfig*
%exclude %{_prefix}/src/linux-%{version}/*/*/*/*/*/Kconfig*
%{_prefix}/src/linux-%{version}/block
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%if %{with grsecurity}
%{_prefix}/src/linux-%{version}/grsecurity
%endif
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts/*
%exclude %{_prefix}/src/linux-%{version}/scripts/Kbuild.include
%exclude %{_prefix}/src/linux-%{version}/scripts/Makefile*
%exclude %{_prefix}/src/linux-%{version}/scripts/basic
%exclude %{_prefix}/src/linux-%{version}/scripts/kconfig
%exclude %{_prefix}/src/linux-%{version}/scripts/mkmakefile
%exclude %{_prefix}/src/linux-%{version}/scripts/mod
%exclude %{_prefix}/src/linux-%{version}/scripts/setlocalversion
%exclude %{_prefix}/src/linux-%{version}/scripts/*.c
%exclude %{_prefix}/src/linux-%{version}/scripts/*.sh
%{_prefix}/src/linux-%{version}/sound
%{_prefix}/src/linux-%{version}/security
%{_prefix}/src/linux-%{version}/usr
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%endif
