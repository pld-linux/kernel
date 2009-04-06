#
# NOTE:
# the following bcond combos will not work
# - without_vserver and any of the following
#   - with_apparmor
#   - with_grsec_minimal
#   - with_grsec_full
#   - with_tomoyo
#
# TODO:
# - benchmark NO_HZ & HZ=1000 vs HZ=300 on i686
# - add a subpackage (kernel-firmware?) for ~35 firmware files
#
# FUTURE:
# - pom-ng quake3-conntrack-nat -> nf_conntrack ?
# - pom-ng talk-conntrack-nat -> nf_conntrack ?
# - nf-hipac ?
# - pax hooks for selinux (experimental)
#
# HOWTO:
# - update main config: ./kernel-config-sort.pl ./BUILD/kernel-*/linux-2.6.29 kernel-multiarch.config
#
# Conditional build:
%bcond_without	source		# don't build kernel-source package
%bcond_without	pcmcia		# don't build pcmcia

%bcond_with	verbose		# verbose build (V=1)
%bcond_without	reiser4		# support for reiser4 fs (experimental)

%bcond_without	grsecurity	# don't build grsecurity nor pax at all
%bcond_without	grsec_minimal	# build only minimal subset (proc,link,fifo,shm)
%bcond_without	grsec_full	# build full grsecurity
%bcond_with	pax_full	# build pax and full grsecurity (ie. grsec_full && pax)
%bcond_with	pax		# build pax support

%bcond_with	fbcondecor	# build fbcondecor (disable FB_TILEBLITTING and affected fb modules)
%bcond_with	pae		# build PAE (HIGHMEM64G) support on uniprocessor
%bcond_with	nfsroot		# build with root on NFS support

%bcond_with	imq		# imq support
%bcond_with	wrr		# wrr support (broken on 2.6.29)
%bcond_with	esfq		# esfq support (broken on 2.6.29)
%bcond_without	ipv6		# ipv6 support

%bcond_without	vserver		# support for VServer (enabled by default)
%bcond_without	tuxonice	# support for tuxonice (ex-suspend2) (enabled by default)
%bcond_without	apparmor	# build kernel with apparmor (exerimental mix)
%bcond_with	tomoyo		# build kernel with tomoyo support [ disables apparmor ]

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
%undefine	with_apparmor
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

%define		basever		2.6.29
%define		postver		.1
%define		rel		0.1

%define		_enable_debug_packages			0

%define		squashfs_version	3.4
%define		tuxonice_version	3.0
%define		netfilter_snap		20070806

%if %{without rescuecd}
%define		__alt_kernel	%{?with_pax:pax}%{!?with_grsec_full:nogrsecurity}%{!?with_apparmor:noaa}%{?with_pae:pae}%{?with_myown:myown}
%else
%define		__alt_kernel	rescuecd
%endif

%if "%{__alt_kernel}" != ""
%define		alt_kernel	%{__alt_kernel}
%endif

# kernel release (used in filesystem and eventually in uname -r)
# modules will be looked from /lib/modules/%{kernel_release}
# localversion is just that without version for "> localversion"
%define		localversion	%{rel}
%define		kernel_release	%{version}%{?alt_kernel:_%{alt_kernel}}-%{localversion}

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
# Source0-md5:	64921b5ff5cdadbccfcd3820f03be7d8
%if "%{postver}" != "%{nil}"
Source1:	http://www.kernel.org/pub/linux/kernel/v2.6/patch-%{version}.bz2
# Source1-md5:	87c6fbf4096b644d66d4da8bb00641a5
%endif

Source3:	kernel-autoconf.h
Source4:	kernel-config.h
Source5:	kernel-ppclibs.Makefile
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

Source40:	kernel-netfilter.config
Source41:	kernel-patches.config
Source42:	kernel-tuxonice.config
Source43:	kernel-vserver.config
Source45:	kernel-grsec.config

Source49:	kernel-pax.config
Source50:	kernel-no-pax.config
Source51:	kernel-grsec_minimal.config
Source55:	kernel-imq.config
Source56:	kernel-reiser4.config
Source57:	kernel-wrr.config

Source58:	kernel-inittmpfs.config
Source59:	kernel-bzip2-lzma.config

Source6000:	http://globalbase.dl.sourceforge.jp/tomoyo/30297/ccs-patch-1.6.6-20090202.tar.gz
# Source6000-md5:	cceb1731d3720030eac34ed128848b32

# tahoe9xx http://www.tahoe.pl/drivers/tahoe9xx-2.6.24.patch
Patch2:		kernel-tahoe9xx.patch

# http://dev.gentoo.org/~spock/projects/fbcondecor/archive/fbcondecor-0.9.4-2.6.25-rc6.patch
Patch3:		kernel-fbcondecor.patch
Patch4:		kernel-fbcon-margins.patch

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

# based on kernel-2.6.25-layer7-2.20.patch from
# http://switch.dl.sourceforge.net/sourceforge/l7-filter/netfilter-layer7-v2.20.tar.gz
Patch40:	kernel-layer7.patch

# http://www.ssi.bg/~ja/nfct/ipvs-nfct-2.6.28-1.diff
Patch41:	kernel-ipvs-nfct.patch

# based on http://www.balabit.com/downloads/files/tproxy/tproxy-kernel-2.6.25-20080509-164605-1210344365.tar.bz2
#FIXME: this patch needs net_device->nd_dev feature (see net/Kconfig:NET_NS).
#       NET_NS depends on EXPERIMENTAL && !SYSFS && NAMESPACES while we have SYSFS enabled.
#       the https://lists.linux-foundation.org/pipermail/containers/2007-December/008849.html is waiting for merge.
#Patch42:	kernel-tproxy.patch

### End netfilter

# http://zph.bratcheda.org/linux-2.6.26.3-zph.patch
Patch49:	kernel-zph.patch

# based on http://www.linuximq.net/patchs/linux-2.6.24-imq.diff
# some people report problems when using imq with wrr.
# try unoficial version: http://kapturkiewicz.name/linux-2.6.25-imq1.diff
Patch50:	kernel-imq.patch

# http://www.kernel.org/pub/linux/kernel/people/edward/reiser4/reiser4-for-2.6/reiser4-for-2.6.28.patch.bz2
Patch51:	kernel-reiser4.patch

# http://www.zz9.dk/patches/wrr-linux-071203-2.6.25.patch.gz
Patch52:	kernel-wrr.patch

# http://fatooh.org/esfq-2.6/sfq-2.6.24.1.tar.bz2
Patch53:	kernel-esfq.patch

# http://memebeam.org/free-software/toshiba_acpi/toshiba_acpi-dev_toshiba_test5-linux_2.6.26.patch
Patch54:	kernel-toshiba_acpi.patch

# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	kernel-atm-vbr.patch
Patch56:	kernel-atmdd.patch

# http://www.ntop.org/PF_RING.html 20070610
Patch58:	kernel-PF_RING.patch

# http://synce.svn.sourceforge.net/svnroot/synce/trunk/patches/linux-2.6.22-rndis_host-wm5.patch
Patch59:	kernel-rndis_host-wm5.patch

# Project suspend2 renamed to tuxonice
# http://www.tuxonice.net/downloads/all/tuxonice-3.0-for-head.patch.bz2
Patch69:	kernel-tuxonice.patch
Patch70:	kernel-tuxonice-headers.patch

# adds some ids for hostap suported cards and monitor_enable from/for aircrack-ng
# http://patches.aircrack-ng.org/hostap-kernel-2.6.18.patch
Patch85:	kernel-hostap.patch

# Taken from http://download.opensuse.org/factory/repo/src-oss/suse/src/kernel-source-2.6.27.7-3.1.src.rpm
Patch90:	kernel-mpt-fusion.patch

# based on http://vserver.13thfloor.at/Experimental/patch-2.6.29-vs2.3.0.36.9-pre3.diff
Patch100:	kernel-vserver-2.3.patch
Patch101:	kernel-vserver-fixes.patch

# Wake-On-Lan fix for nForce drivers; using http://atlas.et.tudelft.nl/verwei90/nforce2/wol.html
# Fix verified for that kernel version.
Patch130:	kernel-forcedeth-WON.patch

# http://download.filesystems.org/unionfs/unionfs-2.x/unionfs-2.5.1_for_2.6.28.1.diff.gz
Patch140:	kernel-unionfs.patch
Patch141:	kernel-unionfs-apparmor.patch

# aufs1, http://aufs.sourceforge.net/
Patch145:	kernel-aufs.patch
Patch146:	kernel-aufs-support.patch
Patch147:	kernel-aufs-apparmor.patch

Patch150:	kernel-ppc-crtsavres.patch

Patch200:	kernel-ppc-ICE-hacks.patch

# The following patch extend the routing functionality in Linux
# to support static routes (defined by user), new way to use the
# alternative routes, the reverse path protection (rp_filter),
# the NAT processing to use correctly the routing when multiple
# gateways are used.
# http://www.ssi.bg/~ja/routes-2.6.28-16.diff
Patch300:	kernel-routes.patch

Patch1000:	kernel-grsec-minimal.patch

Patch2000:	kernel-small_fixes.patch
Patch2001:	kernel-pwc-uncompress.patch
Patch2003:	kernel-regressions.patch

# kill some thousands of warnings
# (only warnings, so just remove parts of this patch if conflics)
Patch2500:	kernel-warnings.patch

# based on https://forgesvn1.novell.com/svn/apparmor/trunk/kernel-patches/2.6.27 rev 1303
# repatched and adapted for vserver/grsec changes in vfs API, experimental
Patch5000:	kernel-apparmor.patch
# with grsec_full version
Patch5001:	kernel-apparmor-after-grsec_full.patch
Patch5002:	kernel-apparmor-common.patch

# tomoyo based on patch from ccs-patch-1.6.6-20090202 tarball
Patch6000:	kernel-tomoyo-with-apparmor.patch
Patch6001:	kernel-tomoyo-without-apparmor.patch

# for rescuecd
# based on http://ftp.leg.uct.ac.za/pub/linux/rip/inittmpfs-2.6.14.diff.gz
Patch7000:	kernel-inittmpfs.patch

# http://lkml.org/lkml/2009/3/26/267
Patch7001:	kernel-bzip2-lzma.patch

# not ready yet
Patch9997:	kernel-pax_selinux_hooks.patch

# based on http://www.grsecurity.net/~paxguy1/pax-linux-2.6.24.6-test45.patch
Patch9998:	kernel-pax.patch

# based on http://www.grsecurity.net/~spender/grsecurity-2.1.14-2.6.29-200903281534.patch
# NOTE: put raw upstream patches on kernel-grsec_full.patch:GRSECURITY_RAW for reference
#       (since upstream deletes older patches)
Patch9999:	kernel-grsec_full.patch
Patch10000:	kernel-grsec-caps.patch
Patch10001:	kernel-grsec-common.patch
Patch10002:	kernel-grsec_fixes.patch
Patch10003:	kernel-grsec-no-stupid-SbO.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 3:2.18
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
%ifarch ppc
BuildRequires:	uboot-mkimage
%endif
AutoReqProv:	no
BuildRequires:	/sbin/depmod
BuildRequires:	gcc >= 5:3.2
BuildRequires:	xz >= 1:4.999.7
# for hostname command
BuildRequires:	net-tools
BuildRequires:	perl-base
BuildRequires:	rpm-build >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.217
Requires(post):	coreutils
Requires(post):	geninitrd >= 10000-3
Requires(post):	module-init-tools >= 0.9.9
Requires:	/sbin/depmod
Requires:	coreutils
Requires:	geninitrd >= 10000-3
Requires:	module-init-tools >= 0.9.9
Provides:	%{name}(netfilter) = %{netfilter_snap}
Provides:	%{name}(vermagic) = %{kernel_release}
Obsoletes:	kernel%{_alt_kernel}-isdn-mISDN
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
Conflicts:	udev < 1:081
Conflicts:	util-linux < 2.10o
Conflicts:	util-vserver < 0.30.215-10
Conflicts:	xfsprogs < 2.6.0
%if %{with pae}
ExcludeArch:	i386 i486 i586
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
%ifarch sparc sparc64
%define		target_arch_dir		sparc
%endif
%ifnarch %{ix86} %{x8664} ppc ppc64 sparc sparc64
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

%define		topdir		%{_builddir}/%{name}-%{version}
%define		srcdir		%{topdir}/linux-%{basever}
%define		objdir		%{topdir}/%{targetobj}
%define		targetobj	%{_target_base_arch}-gcc-%(%{kgcc} -dumpversion)

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
%define MakeOpts %{CrossOpts} HOSTCC="%{__cc}"

%define __features Netfilter module dated: %{netfilter_snap}\
%{?with_grsec_full:Grsecurity full support - enabled}\
%{?with_pax:PaX support - enabled}\
%{?with_fbcondecor:Fbsplash/fbcondecor - enabled }\
%{?with_nfsroot:Root on NFS - enabled}\
%{?with_apparmor:apparmor support - enabled}\
%{?with_tomoyo:tomoyo support - enabled}

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

%package dirs
Summary:	common dirs for kernel packages
Summary(pl.UTF-8):	Katalogi wspólne dla pakietów kernela
Group:		Base/Kernel

%description dirs
This package provides common dirs shared between various kernel
packages.

%description dirs -l pl.UTF-8
Katalog ten udostepnia katalogi współdzielone pomiędzy różnymi
pakietami kernela.

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
%setup -qc
ln -s %{SOURCE7} kernel-module-build.pl
ln -s %{SOURCE10} Makefile
cd linux-%{basever}

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
##endif
%endif

# XXX: 2.6.29 - need update
#%patch2 -p1

%if %{with fbcondecor}
%patch3 -p1
%endif
%patch4 -p1

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
%patch40 -p1

# ipvs-nfct
%patch41 -p1

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
%if %{with esfq}
%patch53 -p1
%endif

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

# hostap enhancements from/for aircrack-ng
%patch85 -p1

# LSI MPT Fusion driver update (by LSI via SUSE folks)
%patch90 -p1

# vserver
%if %{with vserver}
%patch100 -p1
%patch101 -p1
%endif

# tproxy
%if %{without rescuecd} && %{with vserver}
#patch42 -p1
%endif

# forcedeth
%patch130 -p1

# unionfs
%patch140 -p1
%{?with_apparmor:%patch141 -p1}

# 2.6.29 FIXME - needs port to creds
#%patch145 -p1
#%patch146 -p1
#%{?with_apparmor:%patch147 -p1}

%patch2500 -p1

%if %{with rescuecd}
%patch7000 -p1
%endif

# merged into 2.6.30 git :)
%patch7001 -p1

# grsecurity & pax stuff
#
%if %{with pax_full}
%patch9999 -p1
%{?with_vserver:%patch10000 -p1}
%{?with_vserver:%patch10001 -p1}
%{?with_vserver:%patch10002 -p1}
%{?with_vserver:%patch10003 -p1}
%else

%if %{with grsec_full}
%patch9999 -p1
%{?with_vserver:%patch10000 -p1}
%{?with_vserver:%patch10001 -p1}
%{?with_vserver:%patch10002 -p1}
%{?with_vserver:%patch10003 -p1}
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
%if %{with grsec_full} || %{with pax_full}
%patch5001 -p1
%patch5002 -p1
%else
%patch5000 -p1
%patch5002 -p1
%endif
%endif

# tomoyo
%if %{with tomoyo}
	tar xzf %{SOURCE6000}
	%if %{with apparmor}
%patch6000 -p1
	%else
%patch6001 -p1
	%endif
%endif

%patch150 -p1

%ifarch ppc ppc64
#patch200 -p1
%endif

# routes
%patch300 -p1

# Small fixes:
%patch2000 -p1
%patch2001 -p1
#%patch2003 -p1

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{postver}%{?alt_kernel:_%{alt_kernel}}#g' Makefile

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' -o -name '.gitignore' ')' -print0 | xargs -0 -r -l512 rm -f

%build
install -d %{objdir}
cat > %{targetobj}.mk <<'EOF'
# generated by %{name}.spec
KERNELSRC		:= %{_builddir}/%{name}-%{version}/linux-%{basever}
KERNELOUTPUT	:= %{objdir}

SRCARCH		:= %{target_arch_dir}
ARCH		:= %{_target_base_arch}
Q			:= %{!?with_verbose:@}
MAKE_OPTS	:= %{MakeOpts}
DEFCONFIG   := %{defconfig}
EOF

PaXconfig() {
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
		CONFIG_AUFS=y
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

%if %{without smp}
		CONFIG_SMP=n
%endif

# apparmor, will be moved to external file if works
%if %{with apparmor}
		CONFIG_SECURITY_APPARMOR=y
		CONFIG_SECURITY_APPARMOR_BOOTPARAM_VALUE=1
		CONFIG_SECURITY_APPARMOR_DISABLE=n
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

%if %{with rescuecd}
	RescueConfig rescue.config
%endif
%if %{with pax_full} || %{with pax}
	PaXconfig pax.config
%endif

	# prepare kernel-style config file from multiple config files
	%{__awk} -v arch="all %{target_arch_dir} %{_target_base_arch} %{_target_cpu}" -f %{SOURCE6} \
		important.config \
%if %{with rescuecd}
		%{SOURCE58} \
		%{SOURCE59} \
		rescue.config \
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
%if %{with tomoyo}
		config.ccs \
%endif
		%{SOURCE40} %{?0:netfilter} \
		%{SOURCE41} %{?0:patches} \
		%{SOURCE20} \
		$RPM_SOURCE_DIR/$Config
}

cd %{objdir}
install -d arch/%{target_arch_dir}
%if %{without myown}
BuildConfig > %{defconfig}
%else
cat $RPM_SOURCE_DIR/kernel-myown.config > %{defconfig}
%endif
ln -sf %{defconfig} .config
cd -

%{__make} TARGETOBJ=%{targetobj} oldconfig

%{__awk} %{?debug:-v dieOnError=1} -v infile=%{objdir}/%{defconfig} -f %{SOURCE8} %{objdir}/.config

# build kernel
%{__make} TARGETOBJ=%{targetobj} all

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{MakeOpts} %{!?with_verbose:-s} modules_install firmware_install \
	-C %{objdir} \
	%{?with_verbose:V=1} \
	DEPMOD=%{DepMod} \
	INSTALL_MOD_PATH=$RPM_BUILD_ROOT \
	INSTALL_FW_PATH=$RPM_BUILD_ROOT/lib/firmware/%{kernel_release} \
	KERNELRELEASE=%{kernel_release}

install -d $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/misc

# rpm obeys filelinkto checks for ghosted symlinks, convert to files
rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}
touch $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/{build,source}

# /boot
install -d $RPM_BUILD_ROOT/boot
cp -a %{objdir}/System.map $RPM_BUILD_ROOT/boot/System.map-%{kernel_release}
%ifarch %{ix86} %{x8664}
cp -a %{objdir}/arch/%{target_arch_dir}/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
install %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{kernel_release}
%endif
%ifarch ppc ppc64
install %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
install %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinux-%{kernel_release}
%endif
%ifarch ia64
%{__gzip} -cfv %{objdir}/vmlinux > %{objdir}/vmlinuz
cp -a %{objdir}/vmlinuz $RPM_BUILD_ROOT/boot/efi/vmlinuz-%{kernel_release}
ln -sf efi/vmlinuz-%{kernel_release} $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
%endif
%ifarch alpha sparc sparc64
	%{__gzip} -cfv %{objdir}/vmlinux > %{objdir}/vmlinuz
	cp -a %{objdir}/vmlinuz $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
	install %{objdir}/vmlinux $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
%ifarch sparc
	elftoaout %{objdir}/arch/sparc/boot/image -o %{objdir}/vmlinux.aout
	install %{objdir}/vmlinux.aout $RPM_BUILD_ROOT/boot/vmlinux.aout-%{kernel_release}
%endif
%ifarch sparc64
	elftoaout %{objdir}/arch/sparc64/boot/image -o %{objdir}/vmlinux.aout
	install %{objdir}/vmlinux.aout $RPM_BUILD_ROOT/boot/vmlinux.aout-%{kernel_release}
%endif
%ifarch arm
	install %{objdir}/arch/arm/boot/zImage $RPM_BUILD_ROOT/boot/vmlinuz-%{kernel_release}
%endif
%endif

# ghosted initrd
touch $RPM_BUILD_ROOT%{initrd_dir}/initrd-%{kernel_release}.gz

%if "%{_target_base_arch}" != "%{_arch}"
touch $RPM_BUILD_ROOT/lib/modules/%{kernel_release}/modules.dep
%endif

# /etc/modrobe.d
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{kernel_release}

# /usr/src/linux
install -d $RPM_BUILD_ROOT%{_kernelsrcdir}
# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al %{srcdir}/COPYING $RPM_BUILD_ROOT/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/COPYING
fi

cp -a$l %{srcdir}/* $RPM_BUILD_ROOT%{_kernelsrcdir}
cp -a %{objdir}/Module.symvers $RPM_BUILD_ROOT%{_kernelsrcdir}/Module.symvers-dist
cp -aL %{objdir}/.config $RPM_BUILD_ROOT%{_kernelsrcdir}/config-dist
cp -a %{objdir}/include/linux/autoconf.h $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/autoconf-dist.h
cp -a %{objdir}/include/linux/{utsrelease,version}.h $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/autoconf.h
cp -a %{SOURCE4} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/config.h

# collect module-build files and directories
# Usage: kernel-module-build.pl $rpmdir $fileoutdir
fileoutdir=$(pwd)
cd $RPM_BUILD_ROOT%{_kernelsrcdir}
%{__perl} %{topdir}/kernel-module-build.pl %{_kernelsrcdir} $fileoutdir
cd -

%clean
rm -rf $RPM_BUILD_ROOT

%preun
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}
fi

%post
%ifarch ia64
mv -f /boot/efi/vmlinuz{,.old} 2> /dev/null
%{?alt_kernel:mv -f /boot/efi/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null}
ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz
%{?alt_kernel:ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz%{_alt_kernel}}
%endif
mv -f /boot/vmlinuz{,.old} 2> /dev/null
%{?alt_kernel:mv -f /boot/vmlinuz%{_alt_kernel}{,.old} 2> /dev/null}
mv -f /boot/System.map{,.old} 2> /dev/null
%{?alt_kernel:mv -f /boot/System%{_alt_kernel}.map{,.old} 2> /dev/null}
ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz
%{?alt_kernel:ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz%{_alt_kernel}}
ln -sf System.map-%{kernel_release} /boot/System.map
%{?alt_kernel:ln -sf System.map-%{kernel_release} /boot/System.map%{_alt_kernel}}

%depmod %{kernel_release}

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}.gz %{kernel_release}
mv -f %{initrd_dir}/initrd{,.old} 2> /dev/null
%{?alt_kernel:mv -f %{initrd_dir}/initrd%{_alt_kernel}{,.old} 2> /dev/null}
ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd
%{?alt_kernel:ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd%{_alt_kernel}}

if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{kernel_release}.gz --install %{kernel_release} --banner "PLD Linux (%{pld_release})%{?alt_kernel: / %{alt_kernel}}"
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
/lib/firmware/%{kernel_release}

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
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/ide-cs.ko*
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

%files dirs
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}

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
/lib/modules/%{kernel_release}/kernel/drivers/ide/ide-cs.ko*
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
%{_kernelsrcdir}/include
%dir %{_kernelsrcdir}/arch
%dir %{_kernelsrcdir}/arch/[!K]*
%{_kernelsrcdir}/arch/*/include
%dir %{_kernelsrcdir}/security
%dir %{_kernelsrcdir}/security/selinux
%{_kernelsrcdir}/security/selinux/include
%{_kernelsrcdir}/config-dist
%{_kernelsrcdir}/Module.symvers-dist

%files module-build -f aux_files
%defattr(644,root,root,755)
%ifarch ppc ppc64
%{_kernelsrcdir}/arch/powerpc/lib/crtsavres.*
%endif
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
%dir %{_kernelsrcdir}/scripts/selinux
%{_kernelsrcdir}/scripts/selinux/Makefile
%dir %{_kernelsrcdir}/scripts/selinux/mdp
%{_kernelsrcdir}/scripts/selinux/mdp/Makefile
%{_kernelsrcdir}/scripts/selinux/mdp/*.c

%files doc
%defattr(644,root,root,755)
%{_kernelsrcdir}/Documentation

%if %{with source}
%files source -f aux_files_exc
%defattr(644,root,root,755)
%{_kernelsrcdir}/arch/*/[!Mik]*
%{_kernelsrcdir}/arch/*/kernel/[!M]*
%{_kernelsrcdir}/arch/ia64/ia32/[!M]*
%{_kernelsrcdir}/arch/ia64/install.sh
%{_kernelsrcdir}/arch/m68k/ifpsp060/[!M]*
%{_kernelsrcdir}/arch/m68k/ifpsp060/MISC
%{_kernelsrcdir}/arch/parisc/install.sh
%{_kernelsrcdir}/arch/x86/ia32/[!M]*
%{_kernelsrcdir}/arch/ia64/kvm
%{_kernelsrcdir}/arch/powerpc/kvm
%ifarch ppc ppc64
%exclude %{_kernelsrcdir}/arch/powerpc/lib/crtsavres.*
%endif
%{_kernelsrcdir}/arch/s390/kvm
%{_kernelsrcdir}/arch/x86/kvm
%exclude %{_kernelsrcdir}/arch/*/kernel/asm-offsets*
%exclude %{_kernelsrcdir}/arch/*/kernel/sigframe*.h
%exclude %{_kernelsrcdir}/drivers/lguest/lg.h
%{_kernelsrcdir}/block
%{_kernelsrcdir}/crypto
%{_kernelsrcdir}/drivers
%{_kernelsrcdir}/firmware
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
%{_kernelsrcdir}/samples
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
%exclude %{_kernelsrcdir}/security/selinux/include
%{_kernelsrcdir}/usr
%{_kernelsrcdir}/COPYING
%{_kernelsrcdir}/CREDITS
%{_kernelsrcdir}/MAINTAINERS
%{_kernelsrcdir}/README
%{_kernelsrcdir}/REPORTING-BUGS
%endif
