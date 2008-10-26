#
# TODO:
# - benchmark NO_HZ & HZ=1000 vs HZ=300 on i686
# - apparmor (needs testing)
# - add a subpackage (kernel-firmware?) for ~35 firmware files
#
# FUTURE:
# - update xen patch
# - pom-ng quake3-conntrack-nat -> nf_conntrack ?
# - pom-ng talk-conntrack-nat -> nf_conntrack ?
# - nf-hipac ?
# - pax hooks for selinux (experimental)
#
# Conditional build:
%bcond_without	source		# don't build kernel-source package
%bcond_without	pcmcia		# don't build pcmcia

%bcond_with	verbose		# verbose build (V=1)
%bcond_with	xen0		# added Xen0 support
%bcond_with	xenU		# added XenU support
%bcond_without	reiser4		# support for reiser4 fs (experimental)

%bcond_without	grsecurity	# don't build grsecurity nor pax at all
%bcond_without	grsec_minimal	# build only minimal subset (proc,link,fifo,shm)
%bcond_with	grsec_full	# build full grsecurity
%bcond_with	pax_full	# build pax and full grsecurity (ie. grsec_full && pax)
%bcond_with	pax		# build pax support

%bcond_with	fbcondecor	# build fbcondecor (disable FB_TILEBLITTING and affected fb modules)
%bcond_with	pae		# build PAE (HIGHMEM64G) support on uniprocessor
%bcond_with	nfsroot		# build with root on NFS support

%bcond_without	imq		# imq support
%bcond_without	wrr		# wrr support
%bcond_without	ipv6		# ipv6 support

%bcond_without	vserver		# support for VServer (enabled by default)
%bcond_without	tuxonice	# support for tuxonice (ex-suspend2) (enabled by default)
%bcond_with	apparmor	# build kernel with apparmor (very exerimental mix)

%bcond_with	rescuecd	# build kernel for our rescue

%bcond_without	smp		# build uniprocessor instead of SMP kernel
%bcond_with	myown		# build with your own config (kernel-myown.config)

%{?debug:%define with_verbose 1}

%if %{without grsecurity}
%undefine	with_grsec_full
%undefine	with_grsec_minimal
%undefine	with_pax
%undefine	with_pax_full
%endif

%if %{with pax_full}
%undefine	with_grsec_minimal
%define		with_grsec_full		1
%define		with_grsecurity		1
%define		with_pax		1
%endif

%if %{with grsec_full}
%undefine	with_grsec_minimal
%define		with_grsecurity		1
%if %{with pax}
%define		with_pax_full		1
%endif
%endif

%if %{with grsec_minimal}
%undefine	with_grsec_full
%undefine	with_pax_full
%define		with_grsecurity		1
%endif

%define		have_drm	1
%define		have_oss	1
%define		have_sound	1

%if %{with rescuecd}
%undefine	with_tuxonice
%undefine	with_grsec_full
%undefine	with_grsec_minimal
%undefine	with_pax
%undefine	with_pax_full
%undefine	with_vserver
%define		have_drm	0
%define		have_sound	0
%endif

%ifarch %{ix86} alpha ppc
%define		have_isa	1
%else
%define		have_isa	0
%endif

%ifarch sparc sparc64
%undefine	with_pcmcia
%define		have_drm	0
%define		have_oss	0
%endif

%define		basever		2.6.27
%define		postver		.4
%define		rel		0.1

%define		_enable_debug_packages			0

%define		squashfs_version	3.3
%define		tuxonice_version	3.0-rc7a
%define		netfilter_snap		20070806
%define		xen_version		3.0.2

%define		_alt_kernel	%{?with_pax:-pax}%{?with_grsec_full:-grsecurity}%{?with_xen0:-xen0}%{?with_xenU:-xenU}%{?with_rescuecd:-rescuecd}%{?with_pae:-pae}%{?with_myown:-myown}%{?with_apparmor:-aa}

# kernel release (used in filesystem and eventually in uname -r)
# modules will be looked from /lib/modules/%{kernel_release}
# localversion is just that without version for "> localversion"
%define		localversion %{rel}
%define		kernel_release %{version}%{?_alt_kernel:%{_alt_kernel}}-%{localversion}

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de.UTF-8):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(et.UTF-8):	Linuxi kernel (ehk operatsioonisüsteemi tuum)
Summary(fr.UTF-8):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl.UTF-8):	Jądro Linuksa
Name:		kernel%{_alt_kernel}
Version:	%{basever}%{postver}
Release:	%{rel}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{basever}.tar.bz2
# Source0-md5:	b3e78977aa79d3754cb7f8143d7ddabd
%if "%{postver}" != "%{nil}"
Source1:	http://www.kernel.org/pub/linux/kernel/v2.6/patch-%{version}.bz2
# Source1-md5:	fa7cb6cf1ee5e796e89905806ffc6f01
%endif

Source3:	kernel-autoconf.h
Source4:	kernel-config.h
Source5:	kernel-ppclibs.Makefile
Source6:	kernel-config.awk
Source7:	kernel-module-build.pl
Source8:	kernel-track-config-change.awk
# not used by kernel.spec, but it's good to have it in SOURCES
Source9:	kernel-config-sort.pl

Source20:	kernel-multiarch.config
Source21:	kernel-x86.config
Source22:	kernel-sparc.config
Source23:	kernel-sparc64.config
Source24:	kernel-alpha.config
Source25:	kernel-powerpc.config
Source26:	kernel-ia64.config

Source40:	kernel-netfilter.config
Source41:	kernel-patches.config
Source42:	kernel-tuxonice.config
Source43:	kernel-vserver.config
Source45:	kernel-grsec.config
Source46:	kernel-xen0.config
Source47:	kernel-xenU.config

Source49:	kernel-pax.config
Source50:	kernel-no-pax.config
Source51:	kernel-grsec_minimal.config
Source55:	kernel-imq.config
Source56:	kernel-reiser4.config
Source57:	kernel-wrr.config

Source58:	kernel-inittmpfs.config
Source59:	kernel-bzip2-lzma.config

# tahoe9xx http://www.tahoe.pl/drivers/tahoe9xx-2.6.24.patch
Patch2:		tahoe9xx-2.6.24.patch

# http://dev.gentoo.org/~spock/projects/fbcondecor/archive/fbcondecor-0.9.4-2.6.25-rc6.patch
Patch3:		kernel-fbcondecor.patch
Patch4:		linux-fbcon-margins.patch

# based on http://mesh.dl.sourceforge.net/sourceforge/squashfs/squashfs3.3.tgz
# squashfs3.3/kernel-patches/linux-2.6.24/squashfs3.3-patch
Patch5:		kernel-squashfs.patch
Patch6:		linux-static-dev.patch

# netfilter related stuff mostly based on patch-o-matic-ng
# snapshot 20061213 with some fixes related to changes in
# netfilter api in 2.6.19 up to 2.6.22. Some modules
# were ported to nf_conntrack. Some of these are unique.

Patch10:	kernel-pom-ng-IPV4OPTSSTRIP.patch
Patch11:	kernel-pom-ng-ipv4options.patch

Patch14:	kernel-pom-ng-ROUTE.patch
Patch16:	kernel-pom-ng-mms-conntrack-nat.patch
Patch22:	kernel-pom-ng-rsh.patch
Patch23:	kernel-pom-ng-rpc.patch

# based on http://mike.it-loops.com/rtsp/rtsp-2.6.26.patch
Patch36:	kernel-nf_rtsp.patch

# http://ftp.linux-vserver.org/pub/people/dhozac/p/k/delta-owner-xid-feat02.diff
Patch37:	kernel-owner-xid.patch

# based on http://www.svn.barbara.eu.org/ipt_account/attachment/wiki/Software/ipt_account-0.1.21-20070804164729.tar.gz?format=raw
Patch38:	kernel-ipt_account.patch

# based on http://www.intra2net.com/de/produkte/opensource/ipt_account/pom-ng-ipt_ACCOUNT-1.12.tgz
Patch39:	kernel-ipt_ACCOUNT.patch

# kernel-2.6.25-layer7-2.18.patch from
# http://switch.dl.sourceforge.net/sourceforge/l7-filter/netfilter-layer7-v2.18.tar.gz
Patch40:	kernel-layer7.patch

# http://www.ssi.bg/~ja/nfct/ipvs-nfct-2.6.25-1.diff
Patch41:	kernel-ipvs-nfct.patch

# based on http://www.balabit.com/downloads/files/tproxy/tproxy-kernel-2.6.25-20080509-164605-1210344365.tar.bz2
#FIXME: this patch needs net_device->nd_dev feature (see net/Kconfig:NET_NS).
#       NET_NS depends on EXPERIMENTAL && !SYSFS && NAMESPACES while we have SYSFS enabled.
#       the https://lists.linux-foundation.org/pipermail/containers/2007-December/008849.html is waiting for merge.
#Patch42:	kernel-tproxy.patch

### End netfilter

# http://zph.bratcheda.org/linux-2.6.25-zph.patch
Patch49:	kernel-zph.patch

# based on http://www.linuximq.net/patchs/linux-2.6.24-imq.diff
# some people report problems when using imq with wrr.
# try unoficial version: http://kapturkiewicz.name/linux-2.6.25-imq1.diff
Patch50:	kernel-imq.patch

# http://www.kernel.org/pub/linux/kernel/people/edward/reiser4/reiser4-for-2.6/reiser4-for-2.6.27.patch.bz2
Patch51:	kernel-reiser4.patch

# http://www.zz9.dk/patches/wrr-linux-071203-2.6.25.patch.gz
Patch52:	kernel-wrr.patch

# http://fatooh.org/esfq-2.6/sfq-2.6.24.1.tar.bz2
Patch53:	esfq-kernel.patch

# http://memebeam.org/free-software/toshiba_acpi/toshiba_acpi-dev_toshiba_test5-linux_2.6.26.patch
Patch54:	linux-2.6-toshiba_acpi.patch

# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	linux-2.6-atm-vbr.patch
Patch56:	linux-2.6-atmdd.patch

# http://www.ntop.org/PF_RING.html 20070610
Patch58:	linux-PF_RING.patch

# http://synce.svn.sourceforge.net/svnroot/synce/trunk/patches/linux-2.6.22-rndis_host-wm5.patch
Patch59:	kernel-rndis_host-wm5.patch

Patch61:	kernel-vesa-upstream.patch

# Project suspend2 renamed to tuxonice
# http://www.tuxonice.net/downloads/all/tuxonice-3.0-rc7a-for-2.6.26.patch.bz2
Patch69:	linux-2.6-suspend2.patch
Patch70:	kernel-suspend2-headers.patch
Patch71:	linux-2.6-suspend2-page.patch
Patch72:	kernel-2.6-ueagle-atm-freezer.patch

# adds some ids for hostap suported cards and monitor_enable from/for aircrack-ng
# http://patches.aircrack-ng.org/hostap-kernel-2.6.18.patch
Patch85:	hostap-kernel-2.6.18.patch

# http://vserver.13thfloor.at/Experimental/patch-2.6.27.3-vs2.3.0.35.7.diff
Patch100:	linux-2.6-vs2.3.patch
Patch101:	kernel-vserver-fixes.patch

# from http://www.cl.cam.ac.uk/Research/SRG/netos/xen/downloads/xen-3.0.2-src.tgz
#Patch120: xen-3.0-2.6.16.patch

# Wake-On-Lan fix for nForce drivers; using http://atlas.et.tudelft.nl/verwei90/nforce2/wol.html
# Fix verified for that kernel version.
Patch130:	linux-2.6-forcedeth-WON.patch

# http://download.filesystems.org/unionfs/unionfs-2.x/unionfs-2.4_for_2.6.26.diff.gz
Patch140:	kernel-unionfs.patch

Patch200:	linux-2.6-ppc-ICE-hacks.patch

# The following patch extend the routing functionality in Linux
# to support static routes (defined by user), new way to use the
# alternative routes, the reverse path protection (rp_filter),
# the NAT processing to use correctly the routing when multiple
# gateways are used.
# http://www.ssi.bg/~ja/routes-2.6.27-15.diff
Patch300:	kernel-routes.patch

Patch1000:	linux-2.6-grsec-minimal.patch

Patch2000:	kernel-small_fixes.patch
Patch2001:	linux-2.6.21.1-pwc-uncompress.patch

# kill some thousands of warnings
# (only warnings, so just remove parts of this patch if conflics)
Patch2500:	linux-2.6-warnings.patch

# based on https://forgesvn1.novell.com/svn/apparmor/trunk/kernel-patches/2.6.25 rev 1266
# repatched and adapted for vserver/grsec changes in vfs API, very experimental
Patch5000:	kernel-apparmor.patch
#Patch5001:	linux-2.6-apparmor-caps.patch

# for rescuecd
# based on http://ftp.leg.uct.ac.za/pub/linux/rip/inittmpfs-2.6.14.diff.gz
Patch7000:	kernel-inittmpfs.patch
# based on http://www.udpcast.linux.lu/download/bzip2-lzma-kernel-2.6.23.12.patch.gz
Patch7001:	kernel-bzip2-lzma.patch

# not ready yet
Patch9997:	pax_selinux_hooks-2.6.20.patch

# based on http://www.grsecurity.net/~paxguy1/pax-linux-2.6.24.6-test45.patch
Patch9998:	kernel-pax.patch

# based on http://www.grsecurity.net/~spender/grsecurity-2.1.12-2.6.26.3-200809012141.patch
Patch9999:	linux-2.6-grsec_full.patch
Patch10000:	linux-2.6-grsec-caps.patch
Patch10001:	linux-2.6-grsec-common.patch
Patch10002:	kernel-grsec_fixes.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 3:2.14.90.0.7
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
%ifarch ppc
BuildRequires:	uboot-mkimage
%endif
BuildRequires:	/sbin/depmod
BuildRequires:	gcc >= 5:3.2
%{?with_rescuecd:BuildRequires:	lzma >= 1:4.42.2}
# for hostname command
BuildRequires:	net-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.217
Autoreqprov:	no
Requires(post):	coreutils
Requires(post):	geninitrd >= 2.57
Requires(post):	module-init-tools >= 0.9.9
Requires:	/sbin/depmod
Requires:	coreutils
Requires:	geninitrd >= 2.57
Requires:	module-init-tools >= 0.9.9
Provides:	%{name}(netfilter) = %{netfilter_snap}
Provides:	%{name}(vermagic) = %{kernel_release}
%if %{with xen0} || %{with xenU}
Provides:	kernel(xen) = %{_xen_version}
%endif
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
Obsoletes:	kernel%{_alt_kernel}-isdn-mISDN
Conflicts:	e2fsprogs < 1.29
Conflicts:	isdn4k-utils < 3.1pre1
Conflicts:	jfsutils < 1.1.3
Conflicts:	module-init-tools < 0.9.10
Conflicts:	nfs-utils < 1.0.5
Conflicts:	oprofile < 0.9
Conflicts:	ppp < 1:2.4.0
Conflicts:	procps < 3.2.0
Conflicts:	quota-tools < 3.09
%if %{with reiserfs4}
Conflicts:	reiser4progs < 1.0.0
%endif
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	udev < 1:071
Conflicts:	util-linux < 2.10o
Conflicts:	xfsprogs < 2.6.0
%if %{with xen0} || %{with xenU} || %{with pae}
ExclusiveArch:	%{ix86}
%if %{with pae}
ExcludeArch:	i386 i486 i586
%endif
%else
ExclusiveArch:	%{ix86} %{x8664} alpha arm ia64 ppc ppc64 sparc sparc64
%endif
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%ifarch %{ix86} %{x8664}
%define		target_arch_dir		x86
%endif
%ifarch ppc ppc64
%define		target_arch_dir		powerpc
%endif
%ifnarch %{ix86} %{x8664} ppc ppc64
%define		target_arch_dir		%{_target_base_arch}
%endif

%define		defconfig	arch/%{target_arch_dir}/defconfig

# No ELF objects there to strip (skips processing 27k files)
%define		_noautostrip	.*%{_kernelsrcdir}/.*
%define		_noautochrpath	.*%{_kernelsrcdir}/.*

%ifarch ia64
%define		initrd_dir	/boot/efi
%else
%define		initrd_dir	/boot
%endif

%define		_kernelsrcdir	/usr/src/linux%{_alt_kernel}-%{version}

%if "%{_target_base_arch}" != "%{_arch}"
	%define CrossOpts ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-
	%define	DepMod /bin/true

	%if "%{_arch}" == "sparc" && "%{_target_base_arch}" == "sparc64"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_arch}" == "sparc64" && "%{_target_base_arch}" == "sparc"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_arch}" == "x86_64" && "%{_target_base_arch}" == "i386"
	%define	CrossOpts ARCH=%{_target_base_arch} CC="%{__cc}"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_target_base_arch}" == ppc || "%{_target_base_arch}" == "ppc64"
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
%define MakeOpts %{CrossOpts} HOSTCC="%{__cc}"

%define __features Netfilter module dated: %{netfilter_snap}\
%{?with_grsec_full:Grsecurity full support - enabled}\
%{?with_pax:PaX support - enabled}\
%{?with_xen0:Xen 0 - enabled}\
%{?with_xenU:Xen U - enabled}\
%{?with_fbcondecor:Fbsplash/fbcondecor - enabled }\
%{?with_nfsroot:Root on NFS - enabled}

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
Autoreqprov:	no

%description drm
DRM kernel modules.

%description drm -l de.UTF-8
DRM Kernel Treiber.

%description drm -l pl.UTF-8
Sterowniki DRM.

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
Autoreqprov:	no

%description pcmcia
PCMCIA modules.

%description pcmcia -l de.UTF-8
PCMCIA Module.

%description pcmcia -l pl.UTF-8
Moduły PCMCIA.

%package libs
Summary:	Libraries for preparing bootable kernel on PowerPCs
Summary(pl.UTF-8):	Biblioteki do przygotowania bootowalnego jądra dla PowerPC
Group:		Base/Kernel
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= 1.3
Obsoletes:	kernel-smp-libs
Autoreqprov:	no

%description libs
Libraries for preparing bootable kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description libs -l pl.UTF-8
Biblioteki do przygotowania bootowalnego jądra dla PowerPC. Skrypt
mkvmlinuz może być do tego przydatny.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(de.UTF-8):	ALSA Kernel Module
Summary(pl.UTF-8):	Sterowniki dźwięku ALSA
Group:		Base/Kernel
Requires(postun):	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-smp-sound-alsa
Autoreqprov:	no

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
Autoreqprov:	no

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
Provides:	%{name}-headers(netfilter) = %{netfilter_snap}
Autoreqprov:	no

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
Conflicts:	rpmbuild(macros) < 1.321
Autoreqprov:	no

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
Autoreqprov:	no

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
Autoreqprov:	no

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
%setup -q -n linux-%{basever}

# hack against warning in pax/grsec
%ifarch alpha
sed -i 's/-Werror//' arch/alpha/kernel/Makefile
%endif

%ifarch ppc
install %{SOURCE5} Makefile.ppclibs
%endif

%if "%{postver}" != "%{nil}"
%{__bzip2} -dc %{SOURCE1} | patch -p1 -s
%endif

# tuxonice:
%if %{with tuxonice}
##ifarch %{ix86} %{x8664} ia64 ppc alpha
%patch69 -p1
%patch70 -p1
%patch71 -p1
# kernel-2.6-ueagle-atm-freezer.patch
%patch72 -p1
##endif
%endif

%patch2 -p1
%if %{with fbcondecor}
%patch3 -p1
%endif
%patch4 -p1

# squashfs
%patch5 -p1

%patch6 -p1

## netfilter
#

# kernel-pom-ng-IPV4OPTSSTRIP.patch
%patch10 -p1

# kernel-pom-ng-ipv4options.patch
%patch11 -p1

# kernel-pom-ng-ROUTE.patch
%patch14 -p1

# kernel-pom-ng-mms-conntrack-nat.patch
%patch16 -p1

# kernel-pom-ng-rsh.patch
%patch22 -p1

# kernel-pom-ng-rpc.patch
%patch23 -p1

# kernel-nf_rtsp.patch
%patch36 -p1

# kernel-owner-xid.patch
%if %{with vserver}
%patch37 -p1
%endif

# kernel-ipt_account.patch
%patch38 -p1

# kernel-ipt_ACCOUNT.patch
%patch39 -p1

# kernel-layer7.patch
#%%patch40 -p1 # NEEDS UPDATE

# ipvs-nfct
#FIXME
#patch41 -p1

##
# end of netfilter

# zph
%patch49 -p1

%if %{with imq}
%patch50 -p1
%endif

# reiser4
%if %{with reiser4}
%patch51 -p1
%endif

# esfq
%patch53 -p1

%if %{with wrr}
%patch52 -p1
%endif

# toshiba_acpi
%patch54 -p1

%patch55 -p1
%patch56 -p1

%patch58 -p1

# kernel-rndis_host-wm5.patch
%patch59 -p1

%patch61 -p1

# hostap enhancements from/for aircrack-ng
%patch85 -p1

# vserver
%if %{with vserver}
%patch100 -p1
%patch101 -p1
%endif

#%if %{with xen0} || %{with xenU}
#%ifarch %{ix86} %{x8664} ia64
#%patch120 -p1
#%endif
#%endif

# tproxy
%if %{without rescuecd} && %{with vserver}
#patch42 -p1
%endif

# forcedeth
%patch130 -p1

# unionfs
%patch140 -p1

%patch2500 -p1

%if %{with rescuecd}
%patch7000 -p1
%patch7001 -p1
%endif

# grsecurity & pax stuff
#
%if %{with pax_full}
%patch9999 -p1
%{?with_vserver:%patch10000 -p1}
%{?with_vserver:%patch10001 -p1}
#{?with_vserver:%patch10002 -p1}
%else

%if %{with grsec_full}
%patch9999 -p1
%{?with_vserver:%patch10000 -p1}
%{?with_vserver:%patch10001 -p1}
#{?with_vserver:%patch10002 -p1}
%else
%if %{with grsec_minimal}
%patch1000 -p1
# remember that we have the same config file for grsec_minimal and
# grsec_full, but the patches are different.
%endif
%endif

%if %{with pax}
# now we have an separate testing pax-only patch - in the future we
# could have single grsecurity patch and will have to prepare separate
# configs for grsec_minimal, grsec_full and pax to support such
# configurations like pax & grsec_minimal.
# So, in a future there could be no patch9998, but only config
# would tell which options should be enabled.
# The second option is to maintain separate pax-only patch.
%patch9998 -p1
#patch9997 -p1 - needs update
%endif

%endif

#
# end of grsecurity & pax stuff

# apparmor
%if %{with apparmor}
%patch5000 -p1
# %patch5001 -p1
%endif

%ifarch ppc ppc64
#patch200 -p1
%endif

# routes
%patch300 -p1

# Small fixes:
%patch2000 -p1
%patch2001 -p1

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{postver}%{?_alt_kernel:%{_alt_kernel}}#g' Makefile

# on sparc this line causes CONFIG_INPUT=m (instead of =y), thus breaking build
sed -i -e '/select INPUT/d' net/bluetooth/hidp/Kconfig

# on sparc64 avoid building break due to NULL pointer type warrning
sed -i -e 's/^EXTRA_CFLAGS := -Werror/EXTRA_CFLAGS := /' arch/sparc64/kernel/Makefile

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' -o -name '.gitignore' ')' -print0 | xargs -0 -r -l512 rm -f

%build
PaXconfig () {
	set -x
	cat <<-EOCONFIG > $1
	%ifarch %{ix86}
		CONFIG_PAX_SEGMEXEC=y
		# performance impact on CPUs without NX bit
		CONFIG_PAX_PAGEEXEC=n
		# Testing KERNEXEC

		CONFIG_HOTPLUG_PCI_COMPAQ_NVRAM=n
		CONFIG_PCI_BIOS=n
		CONFIG_EFI=n
	%endif

	%ifarch ppc64
		CONFIG_PAX_NOELFRELOCS=n
	%endif
	%ifarch ppc
		CONFIG_PAX_EMUTRAMP=y
		CONFIG_PAX_EMUSIGRT=y
		CONFIG_PAX_EMUPLT=y
	%endif

	%ifarch sparc sparc64 alpha
		CONFIG_PAX_EMUPLT=y
	%endif

	# Now we have to check MAC system integration. Grsecurity (full) uses PAX_HAVE_ACL_FLAGS
	# setting (direct acces). grsec_minimal probably have no idea about PaX so we probably
	# could use PAX_NO_ACL_FLAGS, but for testing the hooks setting will be used
	# PAX_HOOK_ACL_FLAGS. SELinux should also be able to make PaX settings via hooks

	%if %{with grsec_full}
		# Hardening grsec options if with pax
		CONFIG_GRKERNSEC_PROC_MEMMAP=y
		# almost rational (see HIDESYM help)
		CONFIG_GRKERNSEC_HIDESYM=y

		# no change needed CONFIG=PAX_HAVE_ACL_FLAGS=y is taken from the kernel-pax.config
	%else
		# selinux or other hooks?
		CONFIG_PAX_HAVE_ACL_FLAGS=n
		CONFIG_PAX_HOOK_ACL_FLAGS=y
	%endif
EOCONFIG

	return 0
}

RescueConfig() {
	set -x
	cat <<-EOCONFIG > $1
		# CONFIG_SOUND is not set
		# CONFIG_AUDIT is not set
		# CONFIG_TR is not set
		# CONFIG_BT is not set
		# CONFIG_VIDEO_DEV is not set
		# CONFIG_DVB_CORE is not set
		# CONFIG_HAMRADIO is not set
		# CONFIG_ARCNET is not set
		# CONFIG_FB is not set
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
		CONFIG_BLK_DEV_LOOP=y
		CONFIG_ISO9660_FS=y
		CONFIG_NLS_UTF8=y
EOCONFIG

	return 0
}

BuildConfig() {
	%{?debug:set -x}
	set -e

	Config="kernel-%{target_arch_dir}.config"
	echo "Building config file for %{_target_cpu} using $Config et al."

	# prepare local and important options
	cat <<-EOCONFIG > important.config
%if 0%{?debug:1}
		CONFIG_DEBUG_SLAB=y
		CONFIG_DEBUG_SLAB_LEAK=y
		CONFIG_DEBUG_PREEMPT=y
		CONFIG_RT_DEADLOCK_DETECT=y
%endif

%if %{without smp}
		CONFIG_SMP=n
%endif

# apparmor, will be moved to external file if works
%if %{with apparmor}
		CONFIG_SECURITY_APPARMOR=y
		CONFIG_SECURITY_APPARMOR_BOOTPARAM_VALUE=1
		CONFIG_SECURITY_APPARMOR_DISABLE=n
		# patch for unionfs not ready yet
		CONFIG_UNION_FS=n
		# some conflict with smack, todo
		CONFIG_SECURITY_SMACK=n
%endif

%if %{without ipv6}
		CONFIG_IPV6=n
%endif

%ifarch i686 athlon pentium3 pentium4
  %if %{with pae}
		CONFIG_HIGHMEM4G=n
		CONFIG_HIGHMEM64G=y
		CONFIG_X86_PAE=y
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

# Temporary disabled RELOCATABLE. Needed only on x86??
%if %{with pax} || %{with grsec_full}
		CONFIG_RELOCATABLE=n
%endif
EOCONFIG

	RescueConfig rescue.config
	PaXconfig pax.config

	# prepare kernel-style config file from multiple config files
	%{__awk} -v arch="all %{target_arch_dir} %{_target_base_arch} %{_target_cpu}" -f %{SOURCE6} \
		important.config \
%if %{with rescuecd}
		%{SOURCE58} \
		%{SOURCE59} \
		rescue.config \
%endif
%if %{with xenU}
		%{SOURCE47} \
%endif
%if %{with xen0}
		%{SOURCE46} \
%endif
		\
%if %{with pax_full}
		%{SOURCE45} \
		%{SOURCE49} \
		pax.config \
%else
  %if %{with grsec_full}
		%{SOURCE45} \
		%{SOURCE50} \
  %else
    %if %{with grsec_minimal}
		%{SOURCE51} \
    %endif
  %endif
  %if %{with pax}
		%{SOURCE49} \
		pax.config \
  %endif
%endif
		\
%if %{with reiser4}
		%{SOURCE56} \
%endif
%if %{with wrr}
		%{SOURCE57} \
%endif
%if %{with imq}
		%{SOURCE55} \
%endif
%if %{with vserver}
		%{SOURCE43} \
%endif
%if %{with tuxonice}
%ifarch %{ix86} %{x8664} ia64 ppc ppc64
		%{SOURCE42} \
%endif
%endif
		%{SOURCE40} %{?0:netfilter} \
		%{SOURCE41} %{?0:patches} \
		%{SOURCE20} \
		$RPM_SOURCE_DIR/$Config \
		> %{defconfig}
}

BuildKernel() {
	%{?debug:set -x}
	echo "Building kernel $1 ..."
	install .config %{defconfig}
	%{__make} %{MakeOpts} mrproper \
		RCS_FIND_IGNORE='-name build-done -prune -o'
	ln -sf %{defconfig} .config

	%{__make} %{MakeOpts} clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
	%{__make} %{MakeOpts} include/linux/version.h \
		%{?with_verbose:V=1}

	%{__make} %{MakeOpts} scripts/mkcompile_h \
		%{?with_verbose:V=1}

# make does vmlinux, modules and bzImage at once
%ifarch sparc64
	%{__make} %{MakeOpts} image \
		%{?with_verbose:V=1}

	%{__make} %{MakeOpts} modules \
		%{?with_verbose:V=1}
%else
	%{__make} %{MakeOpts} \
		%{?with_verbose:V=1}
%endif
}

PreInstallKernel() {
	Config="%{_target_base_arch}"
	KernelVer=%{kernel_release}

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86} %{x8664}
	install arch/x86/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
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
%ifarch arm
	install arch/arm/boot/zImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif

	%{__make} %{MakeOpts} modules_install \
		%{?with_verbose:V=1} \
		DEPMOD=%DepMod \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	# You'd probabelly want to make it somewhat different
	install -d $KERNEL_INSTALL_DIR%{_kernelsrcdir}
	install Module.symvers $KERNEL_INSTALL_DIR%{_kernelsrcdir}/Module.symvers-dist

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	if [ %DepMod = /sbin/depmod ]; then
		/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || :
	fi
	touch $KERNEL_INSTALL_DIR/lib/modules/$KernelVer/modules.dep
	echo "KERNEL RELEASE $KernelVer DONE"
}

KERNEL_BUILD_DIR=`pwd`
echo "-%{localversion}" > localversion

KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel"
rm -rf $KERNEL_INSTALL_DIR
%if %{without myown}
BuildConfig
%else
cat $RPM_SOURCE_DIR/kernel-myown.config > %{defconfig}
%endif
ln -sf %{defconfig} .config
install -d $KERNEL_INSTALL_DIR%{_kernelsrcdir}/include/linux
rm -f include/linux/autoconf.h
%{__make} %{MakeOpts} include/linux/autoconf.h
install include/linux/autoconf.h \
	$KERNEL_INSTALL_DIR%{_kernelsrcdir}/include/linux/autoconf-dist.h
install .config \
	$KERNEL_INSTALL_DIR%{_kernelsrcdir}/config-dist

%{__awk} %{?debug:-v dieOnError=1} -v infile=%{defconfig} -f %{SOURCE8} .config

BuildKernel
PreInstallKernel

%{__make} %{MakeOpts} include/linux/utsrelease.h
cp include/linux/utsrelease.h{,.save}
cp include/linux/version.h{,.save}
cp scripts/mkcompile_h{,.save}

%install
rm -rf $RPM_BUILD_ROOT
umask 022

export DEPMOD=%DepMod

install -d $RPM_BUILD_ROOT%{_kernelsrcdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{kernel_release}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al COPYING $RPM_BUILD_ROOT/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/COPYING
fi

KERNEL_BUILD_DIR=`pwd`

cp -a$l $KERNEL_BUILD_DIR/build-done/kernel/* $RPM_BUILD_ROOT

if [ -e $RPM_BUILD_ROOT/lib/modules/%{kernel_release} ] ; then
	rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/build
	ln -sf %{_kernelsrcdir} $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/build
	install -d $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{cluster,misc}
fi

find . -maxdepth 1 ! -name "build-done" ! -name "." -exec cp -a$l "{}" "$RPM_BUILD_ROOT%{_kernelsrcdir}/" ";"

cd $RPM_BUILD_ROOT%{_kernelsrcdir}

%{__make} %{MakeOpts} mrproper archclean \
	RCS_FIND_IGNORE='-name build-done -prune -o'

if [ -e $KERNEL_BUILD_DIR/build-done/kernel%{_kernelsrcdir}/include/linux/autoconf-dist.h ]; then
	install $KERNEL_BUILD_DIR/build-done/kernel%{_kernelsrcdir}/include/linux/autoconf-dist.h \
		$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
	install	$KERNEL_BUILD_DIR/build-done/kernel%{_kernelsrcdir}/config-dist \
		$RPM_BUILD_ROOT%{_kernelsrcdir}
fi

cp -Rdp$l $KERNEL_BUILD_DIR/include/linux/* \
	$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux

%{__make} %{MakeOpts} mrproper
mv -f include/linux/utsrelease.h.save $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/utsrelease.h
cp include/linux/version.h{.save,}
cp scripts/mkcompile_h{.save,}
rm -rf include/linux/version.h.save
rm -rf scripts/mkcompile_h.save
install %{SOURCE3} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/autoconf.h
install %{SOURCE4} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/config.h

# collect module-build files and directories
perl %{SOURCE7} %{_kernelsrcdir} $KERNEL_BUILD_DIR

# ghosted initrd
touch $RPM_BUILD_ROOT%{initrd_dir}/initrd-%{kernel_release}.gz

# rpm obeys filelinkto checks for ghosted symlinks, convert to files
rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}
touch $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}

# remove unnecessary dir with dead symlink
rm -rf $RPM_BUILD_ROOT/arch/i386

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}
fi

%post
%ifarch ia64
mv -f /boot/efi/vmlinuz{,.old} 2> /dev/null
%{?_alt_kernel:mv -f /boot/efi/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null}
ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz
%{?_alt_kernel:ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz%{_alt_kernel}}
%endif
mv -f /boot/vmlinuz{,.old} 2> /dev/null
%{?_alt_kernel:mv -f /boot/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null}
mv -f /boot/System.map{,.old} 2> /dev/null
%{?_alt_kernel:mv -f /boot/System%{_alt_kernel}.map{,.old} 2> /dev/null}
ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz
%{?_alt_kernel:ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz%{_alt_kernel}}
ln -sf System.map-%{kernel_release} /boot/System.map
%{?_alt_kernel:ln -sf System.map-%{kernel_release} /boot/System.map%{_alt_kernel}}

%depmod %{kernel_release}

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}.gz %{kernel_release}
mv -f %{initrd_dir}/initrd{,.old} 2> /dev/null
%{?_alt_kernel:mv -f %{initrd_dir}/initrd%{_alt_kernel}{,.old} 2> /dev/null}
ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd
%{?_alt_kernel:ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd%{_alt_kernel}}

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{_alt_kernel}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{kernel_release}.gz --install %{kernel_release} --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi

%post vmlinux
mv -f /boot/vmlinux{,.old} 2> /dev/null
%{?alt_kernel:mv -f /boot/vmlinux-%{alt_kernel}{,.old} 2> /dev/null}
ln -sf vmlinux-%{kernel_release} /boot/vmlinux
%{?alt_kernel:ln -sf vmlinux-%{kernel_release} /boot/vmlinux-%{alt_kernel}}

%post libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{kernel_release} %{kernel_release}

%post drm
%depmod %{kernel_release}

%postun drm
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
ln -snf %{basename:%{_kernelsrcdir}} %{_prefix}/src/linux%{_alt_kernel}

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux%{_alt_kernel} ]; then
		if [ "$(readlink %{_prefix}/src/linux%{_alt_kernel})" = "linux%{_alt_kernel}-%{version}" ]; then
			rm -f %{_prefix}/src/linux%{_alt_kernel}
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
%ifarch sparc sparc64
/boot/vmlinux.aout-%{kernel_release}
%endif
%ifarch ia64
/boot/efi/vmlinuz-%{kernel_release}
%endif
/boot/vmlinuz-%{kernel_release}
/boot/System.map-%{kernel_release}
%ghost %{initrd_dir}/initrd-%{kernel_release}.gz
%dir /lib/modules/%{kernel_release}
%dir /lib/modules/%{kernel_release}/kernel
%ifnarch sparc
/lib/modules/%{kernel_release}/kernel/arch
%endif
/lib/modules/%{kernel_release}/kernel/crypto
/lib/modules/%{kernel_release}/kernel/drivers
%if %{have_drm} && %{without myown}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/gpu
%endif
/lib/modules/%{kernel_release}/kernel/fs

# this directory will be removed after disabling rcutorture mod. in 2.6.20.
/lib/modules/%{kernel_release}/kernel/kernel

/lib/modules/%{kernel_release}/kernel/lib
/lib/modules/%{kernel_release}/kernel/net
%if %{have_sound} && %{without myown}
%dir /lib/modules/%{kernel_release}/kernel/sound
/lib/modules/%{kernel_release}/kernel/sound/ac97_bus.ko*
/lib/modules/%{kernel_release}/kernel/sound/sound*.ko*
%ifnarch sparc
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/video/cx88/cx88-alsa.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/video/em28xx/em28xx-alsa.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/video/saa7134/saa7134-alsa.ko*
%endif
%endif
%dir /lib/modules/%{kernel_release}/misc
%if %{with pcmcia} && %{without myown}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/[!p]*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/pd6729.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
%if %{without rescuecd}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ata/pata_pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/b1pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/usb/gadget/g_midi.ko*
%endif
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/b43
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/libertas/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif
%ghost /lib/modules/%{kernel_release}/modules.*
# symlinks pointing to kernelsrcdir
%ghost /lib/modules/%{kernel_release}/build
%ghost /lib/modules/%{kernel_release}/source
%dir %{_sysconfdir}/modprobe.d/%{kernel_release}

%ifarch alpha %{ix86} %{x8664} ppc ppc64 sparc sparc64
%files vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{kernel_release}
%endif

%if %{have_drm} && %{without myown}
%files drm
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/gpu
%endif

%if %{with pcmcia} && %{without myown}
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/pcmcia/*ko*
/lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia/pcmcia*ko*
%if %{without rescuecd}
/lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/b1pcmcia.ko*
/lib/modules/%{kernel_release}/kernel/drivers/telephony/ixj_pcmcia.ko*
%endif
/lib/modules/%{kernel_release}/kernel/drivers/ata/pata_pcmcia.ko*
/lib/modules/%{kernel_release}/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/b43
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/libertas/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif

%ifarch ppc-broken
%if "%{_arch}" == "ppc"
%files libs
%defattr(644,root,root,755)
%dir /boot/libs-%{kernel_release}
/boot/libs-%{kernel_release}/common
/boot/libs-%{kernel_release}/kernel
/boot/libs-%{kernel_release}/lib
/boot/libs-%{kernel_release}/of1275
/boot/libs-%{kernel_release}/openfirmware
/boot/libs-%{kernel_release}/simple
%dir /boot/libs-%{kernel_release}/utils
%attr(755,root,root) /boot/libs-%{kernel_release}/utils/*
/boot/libs-%{kernel_release}/ld.script
%endif
%endif

%if %{have_sound} && %{without myown}
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
/lib/modules/%{kernel_release}/kernel/drivers/usb/gadget/g_midi.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/video/cx88/cx88-alsa.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/video/em28xx/em28xx-alsa.ko*
/lib/modules/%{kernel_release}/kernel/drivers/media/video/saa7134/saa7134-alsa.ko*
%endif

%if %{have_oss} && %{without myown}
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/sound/oss
%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}
%{_kernelsrcdir}/include
%{_kernelsrcdir}/config-dist
%{_kernelsrcdir}/Module.symvers-dist

%files module-build -f aux_files
%defattr(644,root,root,755)
# symlinks pointint to kernelsrcdir
%dir /lib/modules/%{kernel_release}
/lib/modules/%{kernel_release}/build
%{_kernelsrcdir}/Kbuild
%{_kernelsrcdir}/localversion
%{_kernelsrcdir}/arch/*/kernel/asm-offsets*
%{_kernelsrcdir}/arch/*/kernel/sigframe*.h
%{_kernelsrcdir}/drivers/lguest/lg.h
%{_kernelsrcdir}/kernel/bounds.c
%dir %{_kernelsrcdir}/scripts
%dir %{_kernelsrcdir}/scripts/kconfig
%{_kernelsrcdir}/scripts/Kbuild.include
%{_kernelsrcdir}/scripts/Makefile*
%{_kernelsrcdir}/scripts/basic
%{_kernelsrcdir}/scripts/mkmakefile
%{_kernelsrcdir}/scripts/mod
%{_kernelsrcdir}/scripts/setlocalversion
%{_kernelsrcdir}/scripts/*.c
%{_kernelsrcdir}/scripts/*.sh
%{_kernelsrcdir}/scripts/kconfig/*
%{_kernelsrcdir}/scripts/mkcompile_h

%files doc
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}
%{_kernelsrcdir}/Documentation

%if %{with source}
%files source -f aux_files_exc
%defattr(644,root,root,755)
%{_kernelsrcdir}/arch/*/[!Mk]*
%{_kernelsrcdir}/arch/*/kernel/[!M]*
%{_kernelsrcdir}/arch/ia64/kvm
%{_kernelsrcdir}/arch/powerpc/kvm
%{_kernelsrcdir}/arch/s390/kvm
%{_kernelsrcdir}/arch/x86/kvm
%exclude %{_kernelsrcdir}/arch/*/kernel/asm-offsets*
%exclude %{_kernelsrcdir}/arch/*/kernel/sigframe*.h
%exclude %{_kernelsrcdir}/drivers/lguest/lg.h
%{_kernelsrcdir}/block
%{_kernelsrcdir}/crypto
%{_kernelsrcdir}/drivers
%{_kernelsrcdir}/fs
%if %{with grsecurity} && %{without rescuecd}
%{_kernelsrcdir}/grsecurity
%endif
%{_kernelsrcdir}/init
%{_kernelsrcdir}/ipc
%{_kernelsrcdir}/kernel
%exclude %{_kernelsrcdir}/kernel/bounds.c
%{_kernelsrcdir}/lib
%{_kernelsrcdir}/mm
%{_kernelsrcdir}/net
%{_kernelsrcdir}/virt
%{_kernelsrcdir}/scripts/*
%exclude %{_kernelsrcdir}/scripts/Kbuild.include
%exclude %{_kernelsrcdir}/scripts/Makefile*
%exclude %{_kernelsrcdir}/scripts/basic
%exclude %{_kernelsrcdir}/scripts/kconfig
%exclude %{_kernelsrcdir}/scripts/mkmakefile
%exclude %{_kernelsrcdir}/scripts/mod
%exclude %{_kernelsrcdir}/scripts/setlocalversion
%exclude %{_kernelsrcdir}/scripts/*.c
%exclude %{_kernelsrcdir}/scripts/*.sh
%{_kernelsrcdir}/sound
%{_kernelsrcdir}/security
%{_kernelsrcdir}/usr
%{_kernelsrcdir}/COPYING
%{_kernelsrcdir}/CREDITS
%{_kernelsrcdir}/MAINTAINERS
%{_kernelsrcdir}/README
%{_kernelsrcdir}/REPORTING-BUGS
%{_kernelsrcdir}/.mailmap
%endif
