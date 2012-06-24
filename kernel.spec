#
# TODO:
#	- test pax stuff (btw. tested ok in softmode)
#	- prepare config for non SEGMEXEC capable archs (ie not x86/32bit)
#	- patch scripts/Makefile.xen not to require bash
#       - make PAE usage configurable when Xen is on
#		ALL
# WARNING: Kernels from 2.6.16.X series not work under OldWorldMac
#
# Conditional build:
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	source		# don't build kernel-source package
%bcond_without	pcmcia		# don't build pcmcia

%bcond_with	grsec_full	# build full grsecurity
%bcond_with	pax		# build PaX and full grsecurity
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	xen0		# added Xen0 support
%bcond_with	xenU		# added XenU support
%bcond_without	grsecurity	# don't build grsecurity at all
%bcond_without	grsec_minimal	# build only minimal subset (proc,link,fifo,shm)

%bcond_without	bootsplash	# build with bootsplash instead of fbsplash
%bcond_with	vesafb_tng	# vesafb-tng, vesafb replacement from gentoo
%bcond_with	pae		# build PAE (HIGHMEM64G) support on uniprocessor
%bcond_with	nfsroot		# build with root on NFS support
%bcond_with	reiserfs4	# build with ReiserFS 4 support
%bcond_with	ext2compiled		# compile ext2 into kernel to be able to boot from ext2 rootfs

%{?debug:%define with_verbose 1}

%if !%{with grsecurity}
%undefine	with_grsec_full
%undefine	with_grsec_minimal
%undefine	with_pax
%endif

%if %{with pax}
%undefine	with_grsec_minimal
%undefine	with_grsec_full
%define		with_grsecurity		1
%endif

%if %{with grsec_full}
%undefine	with_grsec_minimal
%define		with_grsecurity		1
%endif

%if %{with grsec_minimal}
%undefine	with_grsec_full
%undefine	with_pax
%define		with_grsecurity		1
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

%ifarch sparc sparc64
%undefine	with_pcmcia
%define		have_drm	0
%define		have_oss	0
%endif

%if %{with xen0}
%define		xen	xen0
%define		dashxen	\-xen0
%define		pae	1
%else
%if %{with xenU}
%define		xen	xenU
%define		dashxen	\-xenU
%define		pae	1
%else
%define		xen	%{nil}
%define		dashxen	%{nil}
%endif
%endif

## Programs required by kernel to work.
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

%define		_netfilter_snap		20060504
%define		_nf_hipac_ver		0.9.1

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

%define		squashfs_version	3.1
%define		suspend_version		2.2.5

%define		xen_version		3.0.2

%define		_basever	2.6.16
%define		_postver	.38
%define		_rel		1
%define		_subname	%{?with_pax:-pax}%{?with_grsec_full:-grsecurity}%{?with_xen0:-xen0}%{?with_xenU:-xenU}
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J�dro Linuksa
Name:		kernel%{_subname}
Version:	%{_basever}%{_postver}
Release:	%{_rel}%{?with_ext2compiled:ext2}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{_basever}.tar.bz2
# Source0-md5:	9a91b2719949ff0856b40bc467fd47be
Source1:	kernel-autoconf.h
Source2:	kernel-config.h
Source3:	http://www.kernel.org/pub/linux/kernel/v2.6/patch-%{version}.bz2
# Source3-md5:	a8e834d5234105892e1e03db7fa7af9e

Source5:	kernel-ppclibs.Makefile
Source7:	kernel-module-build.pl

Source10:	http://suspend2.net/downloads/all/suspend2-%{suspend_version}-for-2.6.16.9.tar.bz2
# Source10-md5:	34345b1f7ad1505f6b264427a21e8a04
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
Source46:	kernel-xen0.config
Source47:	kernel-xenU.config
Source48:	kernel-xen-extra.config
Source49:	kernel-grsec+pax.config
###
#	Patches
###

#
# PATA ports on SATA Promise controller; patch based on:
# http://cvs.fedora.redhat.com/viewcvs/*checkout*/rpms/kernel/devel/linux-2.6-sata-promise-pata-ports.patch
#
Patch1:		linux-2.6-sata-promise-pata-ports.patch

# tahoe9XX http://tahoe.pl/drivers/tahoe9xx-2.6.11.5.patch
Patch2:		tahoe9xx-2.6.11.5.patch

#	ftp://ftp.openbios.org/pub/bootsplash/kernel/bootsplash-3.1.6-2.6.15.diff
Patch3:		bootsplash-3.1.6-2.6.15.diff
#	http://dev.gentoo.org/~spock/projects/gensplash/archive/fbsplash-0.9.2-r5-2.6.16.patch
Patch4:		fbsplash-0.9.2-r5-2.6.16.patch
Patch5:		linux-2.6-vesafb-tng.patch

# directly from http://mesh.dl.sourceforge.net/sourceforge/squashfs/squashfs3.1.tar.gz
#		from linux-2.6.16
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
Patch34:	pom-ng-XOR-%{_netfilter_snap}.patch
Patch35:	pom-ng-account-%{_netfilter_snap}.patch
Patch36:	ipp2p-0.8.2.patch
Patch37:	pom-ng-rpc-%{_netfilter_snap}.patch
Patch38:	pom-ng-unclean-%{_netfilter_snap}.patch

###
#	End netfilter
###

# from http://www.linuximq.net/patchs/linux-2.6.16-imq2.diff
Patch50:	linux-2.6.16-imq2.diff

# from http://bluetooth-alsa.sourceforge.net/sco-mtu.patch
Patch51:	sco-mtu.patch

# esfq
# from http://fatooh.org/esfq-2.6/current/esfq-kernel.patch
Patch53:	esfq-kernel.patch

Patch54:	linux-iforce-trust_ffrm.patch
# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	linux-2.6-atm-vbr.patch
Patch56:	linux-2.6-atmdd.patch

Patch57:	linux-2.6-cpuset_virtualization.patch

# Derived from http://www.skd.de/e_en/products/adapters/pci_64/sk-98xx_v20/software/linux/driver/install-8_31.tar.bz2
Patch60:	linux-2.6-sk98lin-8.31.2.3.patch

Patch70:	linux-2.6-suspend2-avoid-redef.patch
Patch71:	linux-2.6-suspend2-page.patch
Patch72:	suspend2-2.2.5-for-2.6.16.37-fix.patch

Patch81:	linux-2.6-md.patch

# vserver from: http://vserver.13thfloor.at/Experimental/patch-2.6.16-vs2.1.1-rc15.diff
Patch100:	linux-2.6-vs2.1.patch
Patch101:	linux-2.6-vs2.1-suspend2.patch
Patch102:	linux-2.6-vs2.1-128IPs.patch
Patch103:	linux-vcontext-selinux.patch

# from http://www.cl.cam.ac.uk/Research/SRG/netos/xen/downloads/xen-3.0.2-src.tgz
Patch120:	xen-3.0-2.6.16.patch
Patch121:	linux-xen-page_alloc.patch

# from  http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/iw266_we20-6.diff
Patch140:	linux-2.6.16-we20-6.patch

Patch200:	linux-2.6-ppc-ICE-hacks.patch
Patch201:	linux-2.6-x86_64-stack-protector.patch
Patch202:	linux-2.6-unwind-through-signal-frames.patch

# Wake-On-Lan patch for nVidia nForce ethernet driver forcedeth
Patch250:	linux-2.6.16-forcedeth-WON.patch

Patch1000:	linux-2.6-grsec-minimal.patch

Patch1200:	linux-2.6-apparmor.patch
Patch1201:	linux-2.6-apparmor-caps.patch

# grsecurity snap for 2.6.16.14
# based on http://www.grsecurity.net/~spender/grsecurity-2.1.9-2.6.16.14-200605060936.patch
Patch9999:	grsecurity-2.1.9-2.6.16.14.patch
Patch10000:	linux-2.6-grsec-caps.patch

URL:		http://www.kernel.org/
%if %{with xen0} || %{with xenU}
BuildRequires:	bash
%endif
BuildRequires:	binutils >= 3:2.14.90.0.7
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
BuildRequires:	gcc >= 5:3.2
BuildRequires:	/sbin/depmod
# for hostname command
BuildRequires:	net-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.217
Autoreqprov:	no
Requires(post):	coreutils
Requires(post):	geninitrd >= 2.57
Requires(post):	module-init-tools >= 0.9.9
Requires:	coreutils
Requires:	geninitrd >= 2.57
Requires:	module-init-tools >= 0.9.9
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	kernel(nf-hipac) = %{_nf_hipac_ver}
Provides:	kernel(realtime-lsm) = 0.1.1
%if %{with xen0}
Provides:	kernel(xen0) = %{xen_version}
%endif
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
%if %{with reiserfs4}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
%endif
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	udev < %{_udev_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	vserver-packages
Conflicts:	xfsprogs < %{_xfsprogs_ver}
%if %{with xen0} || %{with xenU}
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

# kernel release (used in filesystem and eventually in uname -r)
# modules will be looked from /lib/modules/%{kernel_release}%{?smp}
# _localversion is just that without version for "> localversion"
%define		_localversion %{release}%{xen}
%define		kernel_release %{version}-%{_localversion}
%define		_kernelsrcdir	/usr/src/linux%{_subname}-%{version}

%if "%{_target_base_arch}" != "%{_arch}"
	%define	CrossOpts ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-
	%define	DepMod /bin/true

	%if "%{_arch}" == "sparc" && "%{_target_base_arch}" == "sparc64"
	%define	DepMod /sbin/depmod
	%endif

	%if "%{_arch}" == "x86_64" && "%{_target_base_arch}" == "i386"
	%define	CrossOpts ARCH=%{_target_base_arch}
	%define	DepMod /sbin/depmod
	%endif

%else
	%define CrossOpts CC="%{__cc}"
	%define	DepMod /sbin/depmod
%endif

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enth�lt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist f�r grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Proze�-Management, Ger�te Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un syst�me d'exploitation Linux. Le noyau traite les
fonctions basiques d'un syst�me d'exploitation: allocation m�moire,
allocation de process, entr�e/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j�dro Linuksa niezb�dne do prawid�owego dzia�ania
Twojego komputera. Zawiera w sobie sterowniki do sprz�tu znajduj�cego
si� w komputerze, takiego jak sterowniki dysk�w itp.

%package vmlinux
Summary:	vmlinux - uncompressed kernel image
Summary(pl):	vmlinux - rozpakowany obraz j�dra
Group:		Base/Kernel

%description vmlinux
vmlinux - uncompressed kernel image.

%description vmlinux -l pl
vmlinux - rozpakowany obraz j�dra.

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
Summary(pl):	Modu�y PCMCIA
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
Modu�y PCMCIA (%{pcmcia_version}).

%package libs
Summary:	Libraries for preparing bootable kernel on PowerPCs
Summary(pl):	Biblioteki do przygotowania bootowalnego j�dra dla PowerPC
Group:		Base/Kernel
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description libs
Libraries for preparing bootable kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description libs -l pl
Biblioteki do przygotowania bootowalnego j�dra dla PowerPC. Skrypt
mkvmlinuz mo�e by� do tego przydatny.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(pl):	Sterowniki d�wi�ku ALSA
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l pl
Sterowniki d�wi�ku ALSA (Advanced Linux Sound Architecture).

%package sound-oss
Summary:	OSS kernel modules
Summary(pl):	Sterowniki d�wi�ku OSS
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-oss
OSS (Open Sound System) drivers.

%description sound-oss -l pl
Sterowniki d�wi�ku OSS (Open Sound System).

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} f�r Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl):	J�dro Linuksa w wersji %{version} dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(post):	coreutils
Requires(post):	geninitrd >= 2.57
Requires(post):	module-init-tools >= 0.9.9
Requires:	coreutils
Requires:	geninitrd >= 2.26
Requires:	module-init-tools >= 0.9.9
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	kernel(nf-hipac) = %{_nf_hipac_ver}
Provides:	kernel(realtime-lsm) = 0.1.1
%if %{with xen0}
Provides:	kernel(xen0) = %{xen_version}
%endif
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
%if %{with reiserfs4}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
%endif
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	vserver-packages
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description smp -l de
Dieses Paket enth�lt eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird f�r Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description smp -l fr
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et n�cessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand m�me fonctionner pour les syst�me mono-processeur.

%description smp -l pl
Pakiet zawiera j�dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj�ce dwa lub wi�cej procesor�w.
Powinno r�wnie� dobrze dzia�a� na maszynach z jednym procesorem.

%package smp-vmlinux
Summary:	vmlinux - uncompressed SMP kernel image
Summary(pl):	vmlinux - rozpakowany obraz j�dra SMP
Group:		Base/Kernel

%description smp-vmlinux
vmlinux - uncompressed SMP kernel image.

%description smp-vmlinux -l pl
vmlinux - rozpakowany obraz j�dra SMP.

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
Summary(pl):	Modu�y PCMCIA dla maszyn SMP
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
Modu�y PCMCIA dla maszyn SMP (%{pcmcia_version}).

%package smp-libs
Summary:	Libraries for preparing bootable SMP kernel on PowerPCs
Summary(pl):	Biblioteki do przygotowania bootowalnego j�dra dla wieloprocesorowych PowerPC
Group:		Base/Kernel
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description smp-libs
Libraries for preparing bootable SMP kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description smp-libs -l pl
Biblioteki do przygotowania bootowalnego j�dra dla wieloprocesorowych
PowerPC. Skrypt mkvmlinuz mo�e by� do tego przydatny.

%package smp-sound-alsa
Summary:	ALSA SMP kernel modules
Summary(pl):	Sterowniki d�wi�ku ALSA dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-alsa
ALSA (Advanced Linux Sound Architecture) SMP sound drivers.

%description smp-sound-alsa -l pl
Sterowniki d�wi�ku ALSA (Advanced Linux Sound Architecture) dla maszyn
wieloprocesorowych.

%package smp-sound-oss
Summary:	OSS SMP kernel modules
Summary(pl):	Sterowniki d�wi�ku OSS dla maszyn wieloprocesorowych
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
Summary(pl):	Pliki nag��wkowe j�dra Linuksa
Group:		Development/Building
Provides:	kernel-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-headers(agpgart) = %{version}
Provides:	kernel-headers(alsa-drivers)
Provides:	kernel-headers(bridging) = %{version}
Provides:	kernel-headers(netfilter) = %{_netfilter_snap}
Provides:	kernel-headers(reiserfs) = %{version}
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%description headers -l pl
Pakiet zawiera pliki nag��wkowe j�dra, niezb�dne do rekompilacji j�dra
oraz budowania modu��w j�dra.

%package module-build
Summary:	Development files for building kernel modules
Summary(pl):	Pliki s�u��ce do budowania modu��w j�dra
Group:		Development/Building
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-module-build = %{epoch}:%{_basever}
Provides:	kernel-module-build = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%description module-build -l pl
Pliki ze drzewa �r�de� j�dra potrzebne do budowania modu��w j�dra
Linuksa z zewn�trznych pakiet�w.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod �r�d�owy j�dra Linuksa
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
Das Kernel-Source-Paket enth�lt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zur�ckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien k�nnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont n�cessaires pour compiler la plupart des
programmes C, car il d�pend de constantes d�finies dans le code
source. Les sources peuvent �tre aussi utilis�e pour compiler un noyau
personnalis� pour avoir de meilleures performances sur des mat�riels
particuliers.

%description source -l pl
Pakiet zawiera kod �r�d�owy j�dra systemu.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja do j�dra Linuksa
Group:		Documentation
Provides:	kernel-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacj� do j�dra Linuksa pochodz�c� z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{_basever} -a10
%{__bzip2} -dc %{SOURCE3} | patch -p1 -s

%ifarch ppc
install %{SOURCE5} Makefile.ppclibs
%endif

%patch1 -p1

%patch72 -p0
for i in suspend2-%{suspend_version}-for-2.6.16.9/[0-9]*; do
patch -p1 -s < $i
done
%patch70 -p1
%patch71 -p1

# reiserfs4
%if %{with reiserfs4}
%{__gzip} -dc %{SOURCE12} | %{__patch} -s -p1
%endif

%patch2 -p1

%patch8 -p1
%if %{with bootsplash}
%patch3 -p1
%else
%patch4 -p1
%endif

%ifarch %{ix86}
%{?with_vesafb_tng:%patch5 -p1}
%endif

%patch6 -p1

%patch7 -p1
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
%patch37 -p1
%patch38 -p1

##
# end of netfilter

%patch50 -p1

%patch51 -p1

%patch53 -p1

%patch54 -p1

%patch55 -p1
%patch56 -p1


%ifarch %{ix86} %{x8664} ia64
%patch57 -p1
%endif

%patch60 -p1

%patch81 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1

%if %{with xen0} || %{with xenU}
%ifarch %{ix86} %{x8664} ia64
%patch120 -p1
%patch121 -p1
%endif
%endif

%patch140 -p1

%ifarch ppc ppc64
%patch200 -p1
%endif
%ifarch %{x8664}
%patch201 -p1
%endif
%ifarch ppc ppc64 %{ix86} %{x8664}
%patch202 -p1
%endif

%patch250 -p1

%patch1200 -p1
%patch1201 -p1

%if %{with grsec_minimal}
%patch1000 -p1
%endif
%if %{with grsec_full}
%patch9999 -p1
%patch10000 -p1
%endif

%if %{with pax}
%patch9999 -p1
%patch10000 -p1
%endif

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{_postver}#g' Makefile

# on sparc this line causes CONFIG_INPUT=m (instead of =y), thus breaking build
sed -i -e '/select INPUT/d' net/bluetooth/hidp/Kconfig

# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' -o -name '.gitignore' ')' -print0 | xargs -0 -r -l512 rm -f

%build
TuneUpConfigForIX86 () {
%ifarch %{ix86}
	pae=
	[ "$2" = "yes" ] && pae=yes
	%if %{with pae}
	pae=yes
	%endif
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
	%ifarch i686 athlon pentium3 pentium4
	if [ "$pae" = "yes" ]; then
		sed -i "s:CONFIG_HIGHMEM4G=y:# CONFIG_HIGHMEM4G is not set:" $1
		sed -i "s:# CONFIG_HIGHMEM64G is not set:CONFIG_HIGHMEM64G=y\nCONFIG_X86_PAE=y:" $1
	fi
	sed -i 's:CONFIG_MATH_EMULATION=y:# CONFIG_MATH_EMULATION is not set:' $1
	%endif
	return 0
%endif
}

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
	KernelVer=%{kernel_release}$1

	echo "Building config file [using $Config.conf] for KERNEL $1..."
	cat $RPM_SOURCE_DIR/kernel-$Config.config > arch/%{_target_base_arch}/defconfig

	TuneUpConfigForIX86 arch/%{_target_base_arch}/defconfig "$smp"

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
	# suspend2
	cat %{SOURCE42} >> arch/%{_target_base_arch}/defconfig
%ifarch ppc ppc64
	sed -i "s:CONFIG_SUSPEND2=y:# CONFIG_SUSPEND2 is not set:" arch/%{_target_base_arch}/defconfig
%endif
	# vserver
	cat %{SOURCE43} >> arch/%{_target_base_arch}/defconfig
	# vesafb-tng
	cat %{SOURCE44} >> arch/%{_target_base_arch}/defconfig

%if %{with grsecurity}
	%if %{with pax}
		cat %{SOURCE49} >> arch/%{_target_base_arch}/defconfig
	%else
		cat %{SOURCE45} >> arch/%{_target_base_arch}/defconfig
	%endif
%endif

%if %{with xen0} || %{with xenU}
	sed -i "s:CONFIG_X86_PC=y:# CONFIG_X86_PC is not set:" arch/%{_target_base_arch}/defconfig
	sed -i "s:CONFIG_RIO=[ym]:# CONFIG_RIO is not set:" arch/%{_target_base_arch}/defconfig

	# framebuffer devices generally don't work with xen
	# and kernel will crash on boot if vesafb-tng is compiled in (even if off by default)
	sed -i "s:CONFIG_FB=y:# CONFIG_FB is not set:" arch/%{_target_base_arch}/defconfig

	cat %{SOURCE48} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with xen0}
	cat %{SOURCE46} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with xenU}
	cat %{SOURCE47} >> arch/%{_target_base_arch}/defconfig
%endif

	# fbsplash
	echo "CONFIG_FB_SPLASH=y" >> arch/%{_target_base_arch}/defconfig
	# bootsplash
	echo "CONFIG_BOOTSPLASH=y" >> arch/%{_target_base_arch}/defconfig

%if %{with nfsroot}
	sed -i "s:CONFIG_NFS_FS=m:CONFIG_NFS_FS=y:" arch/%{_target_base_arch}/defconfig
	echo "CONFIG_ROOT_NFS=y" >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with ext2compiled}
	sed -i 's,CONFIG_EXT2_FS=m,CONFIG_EXT2_FS=y,' arch/%{_target_base_arch}/defconfig
%endif

%{?debug:sed -i "s:# CONFIG_DEBUG_SLAB is not set:CONFIG_DEBUG_SLAB=y:" arch/%{_target_base_arch}/defconfig}
%{?debug:sed -i "s:# CONFIG_DEBUG_PREEMPT is not set:CONFIG_DEBUG_PREEMPT=y:" arch/%{_target_base_arch}/defconfig}
%{?debug:sed -i "s:# CONFIG_RT_DEADLOCK_DETECT is not set:CONFIG_RT_DEADLOCK_DETECT=y:" arch/%{_target_base_arch}/defconfig}

	if [ "$smp" = "yes" ]; then
		sed -e 's:CONFIG_LOCALVERSION="":CONFIG_LOCALVERSION="smp":'	\
			-i arch/%{_target_base_arch}/defconfig
	fi

	ln -sf arch/%{_target_base_arch}/defconfig .config
	install -d $KERNEL_INSTALL_DIR%{_kernelsrcdir}/include/linux
	rm -f include/linux/autoconf.h
	%{__make} %CrossOpts include/linux/autoconf.h
	if [ "$smp" = "yes" ]; then
		install include/linux/autoconf.h \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/include/linux/autoconf-smp.h
		install .config \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/config-smp
	else
		install include/linux/autoconf.h \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/include/linux/autoconf-up.h
		install .config \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/config-up
	fi
}

BuildKernel() {
	%{?debug:set -x}
	echo "Building kernel${1:+ $1}..."
	%{__make} %CrossOpts mrproper \
		RCS_FIND_IGNORE='-name build-done -prune -o'
	ln -sf arch/%{_target_base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%else
	%{__make} %CrossOpts clean \
		RCS_FIND_IGNORE='-name build-done -prune -o'
%endif
	%{__make} %CrossOpts include/linux/version.h \
		%{?with_verbose:V=1}

# make does vmlinux, modules and bzImage at once
%ifarch sparc sparc64
%ifarch sparc64
	%{__make} %CrossOpts image \
		%{?with_verbose:V=1}

	%{__make} %CrossOpts modules \
		%{?with_verbose:V=1}
%else
	sparc32 %{__make} \
		%{?with_verbose:V=1}
%endif
%else
	%{__make} %CrossOpts \
%if %{with xen0} || %{with xenU}
		SHELL=/bin/bash \
%endif
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
	KernelVer=%{kernel_release}$1

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86} %{x8664}
%if %{with xen0} || %{with xenU}
	install vmlinuz $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%else
	install arch/%{_target_base_arch}/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
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
	%{__make} %CrossOpts modules_install \
		%{?with_verbose:V=1} \
		DEPMOD=%DepMod \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	if [ "$smp" = "yes" ]; then
		install Module.symvers \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/Module.symvers-smp
	else
		install Module.symvers \
			$KERNEL_INSTALL_DIR%{_kernelsrcdir}/Module.symvers-up
	fi

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	if [ %DepMod = /sbin/depmod ]; then
		/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || :
	else
		touch $KERNEL_INSTALL_DIR/lib/modules/$KernelVer/modules.dep
	fi
	echo "KERNEL RELEASE $KernelVer DONE"
}

KERNEL_BUILD_DIR=`pwd`
echo "-%{_localversion}" > localversion

#install -m 644 %{SOURCE50} FAQ-pl

# UP KERNEL
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-UP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig
%if %{with up}
BuildKernel
PreInstallKernel
%endif

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
install -d $RPM_BUILD_ROOT

umask 022
# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al COPYING $RPM_BUILD_ROOT/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/COPYING
fi

export DEPMOD=%DepMod

install -d $RPM_BUILD_ROOT%{_kernelsrcdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{kernel_release}{,smp}

KERNEL_BUILD_DIR=`pwd`

%if %{with up} || %{with smp}
cp -a$l $KERNEL_BUILD_DIR/build-done/kernel-*/* $RPM_BUILD_ROOT
%endif

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{kernel_release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{kernel_release}$i/build
		ln -sf %{_kernelsrcdir} \
			$RPM_BUILD_ROOT/lib/modules/%{kernel_release}$i/build
		install -d $RPM_BUILD_ROOT/lib/modules/%{kernel_release}$i/{cluster,misc}
	fi
done

find . -maxdepth 1 ! -name "build-done" ! -name "." -exec cp -a$l "{}" "$RPM_BUILD_ROOT%{_kernelsrcdir}/" ";"

cd $RPM_BUILD_ROOT%{_kernelsrcdir}

%{__make} %CrossOpts mrproper \
	RCS_FIND_IGNORE='-name build-done -prune -o'

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-UP%{_kernelsrcdir}/include/linux/autoconf-up.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-UP%{_kernelsrcdir}/include/linux/autoconf-up.h \
	$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-UP%{_kernelsrcdir}/config-up \
	$RPM_BUILD_ROOT%{_kernelsrcdir}
fi

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-SMP%{_kernelsrcdir}/include/linux/autoconf-smp.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-SMP%{_kernelsrcdir}/include/linux/autoconf-smp.h \
	$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-SMP%{_kernelsrcdir}/config-smp \
	$RPM_BUILD_ROOT%{_kernelsrcdir}
fi

%if %{with up} || %{with smp}
# UP or SMP
install $KERNEL_BUILD_DIR/build-done/kernel-*%{_kernelsrcdir}/include/linux/* \
	$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
%endif

%{__make} %CrossOpts mrproper
%{__make} %CrossOpts include/linux/version.h
install %{SOURCE1} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/autoconf.h
install %{SOURCE2} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/config.h

# collect module-build files and directories
perl %{SOURCE7} %{_kernelsrcdir} $KERNEL_BUILD_DIR

%if %{with up} || %{with smp}
# ghosted initrd
touch $RPM_BUILD_ROOT/boot/initrd-%{kernel_release}{,smp}.gz
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%preun
rm -f /lib/modules/%{kernel_release}/modules.*
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}
fi

%post
%ifarch ia64
mv -f /boot/efi/vmlinuz%{dashxen} /boot/efi/vmlinuz%{dashxen}.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz%{dashxen} /boot/vmlinuz%{dashxen}.old 2> /dev/null > /dev/null
mv -f /boot/System.map%{dashxen} /boot/System.map%{dashxen}.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz%{dashxen}
%endif
ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz%{dashxen}
ln -sf System.map-%{kernel_release} /boot/System.map%{dashxen}

%depmod %{kernel_release}

%if !%{with xenU}
/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}.gz %{kernel_release}
mv -f %{initrd_dir}/initrd%{dashxen} %{initrd_dir}/initrd%{dashxen}.old 2> /dev/null > /dev/null
ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd%{dashxen}

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_pax:pax}%{?with_grsec_full:grsecurity}%{?with_xen0:Xen0}%{?with_xenU:XenU}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{kernel_release}.gz --install %{kernel_release} --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi
%endif

%post vmlinux
mv -f /boot/vmlinux%{dashxen} /boot/vmlinux%{dashxen}.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{kernel_release} /boot/vmlinux%{dashxen}

%post libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{version}-%{release} %{version}-%{release}

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

%preun smp
rm -f /lib/modules/%{kernel_release}smp/modules.*
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}smp
fi

%post smp
%ifarch ia64
mv -f /boot/efi/vmlinuz /boot/efi/vmlinuz.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz%{dashxen} /boot/vmlinuz%{dashxen}.old 2> /dev/null > /dev/null
mv -f /boot/System.map%{dashxen} /boot/System.map%{dashxen}.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{version}-%{release}smp /boot/efi/vmlinuz
%endif
ln -sf vmlinuz-%{kernel_release}smp /boot/vmlinuz%{dashxen}
ln -sf System.map-%{kernel_release}smp /boot/System.map%{dashxen}

%depmod %{kernel_release}smp

%if !%{with xenU}
/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}smp.gz %{kernel_release}smp
mv -f %{initrd_dir}/initrd%{dashxen} %{initrd_dir}/initrd%{dashxen}.old 2> /dev/null > /dev/null
ln -sf initrd-%{kernel_release}smp.gz %{initrd_dir}/initrd%{dashxen}

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_pax:pax}%{?with_grsec_full:grsecurity}%{?with_xen0:Xen0}%{?with_xenU:XenU}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{kernel_release}smp.gz --install %{kernel_release}smp --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi
%endif

%post smp-vmlinux
mv -f /boot/vmlinux%{dashxen} /boot/vmlinux%{dashxen}.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{kernel_release}smp /boot/vmlinux%{dashxen}

%post smp-libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{version}-%{release}smp %{version}-%{release}smp

%post smp-drm
%depmod %{kernel_release}smp

%postun smp-drm
%depmod %{kernel_release}smp

%post smp-pcmcia
%depmod %{kernel_release}smp

%postun smp-pcmcia
%depmod %{kernel_release}smp

%post smp-sound-alsa
%depmod %{kernel_release}smp

%postun smp-sound-alsa
%depmod %{kernel_release}smp

%post smp-sound-oss
%depmod %{kernel_release}smp

%postun smp-sound-oss
%depmod %{kernel_release}smp

%post headers
rm -f %{_prefix}/src/linux
ln -snf %{basename:%{_kernelsrcdir}} %{_prefix}/src/linux%{_subname}

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux ]; then
		# FIXME: shouldn't here be 'linux%{_subname}' ?
		if [ "$(readlink %{_prefix}/src/linux)" = "linux-%{version}" ]; then
			rm -f %{_prefix}/src/linux
		fi
	fi
fi

%if %{with up}
%files
%defattr(644,root,root,755)
#doc FAQ-pl
%ifarch sparc sparc64
/boot/vmlinux.aout-%{kernel_release}
%endif
%ifarch ia64
/boot/efi/vmlinuz-%{kernel_release}
%endif
/boot/vmlinuz-%{kernel_release}
/boot/System.map-%{kernel_release}
%ghost /boot/initrd-%{kernel_release}.gz
%dir /lib/modules/%{kernel_release}
%dir /lib/modules/%{kernel_release}/kernel
%ifnarch sparc
/lib/modules/%{kernel_release}/kernel/arch
%endif
/lib/modules/%{kernel_release}/kernel/crypto
/lib/modules/%{kernel_release}/kernel/drivers
%if %{have_drm}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/char/drm
%endif
%if %{have_oss} && %{have_isa} && !%{with xen0} && !%{with xenU}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/media/radio/miropcm20.ko*
%endif
/lib/modules/%{kernel_release}/kernel/fs
/lib/modules/%{kernel_release}/kernel/kernel
/lib/modules/%{kernel_release}/kernel/lib
/lib/modules/%{kernel_release}/kernel/net
/lib/modules/%{kernel_release}/kernel/security
%if %{have_sound}
%dir /lib/modules/%{kernel_release}/kernel/sound
/lib/modules/%{kernel_release}/kernel/sound/soundcore.*
%endif
%dir /lib/modules/%{kernel_release}/misc
%if %{with pcmcia}
%exclude /lib/modules/%{kernel_release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{kernel_release}/kernel/drivers/usb/host/sl811_cs.ko*
%endif
/lib/modules/%{kernel_release}/build
%ghost /lib/modules/%{kernel_release}/modules.*
%dir %{_sysconfdir}/modprobe.d/%{kernel_release}

%ifarch alpha %{ix86} %{x8664} ppc ppc64 sparc sparc64
%files vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{kernel_release}
%endif

%if %{have_drm}
%files drm
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/char/drm
%endif

%if %{with pcmcia}
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/drivers/pcmcia
/lib/modules/%{kernel_release}/kernel/drivers/*/pcmcia
/lib/modules/%{kernel_release}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{kernel_release}/kernel/drivers/telephony/ixj_pcmcia.ko*
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

%if %{have_sound}
%files sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/sound
%exclude %dir /lib/modules/%{kernel_release}/kernel/sound
%exclude /lib/modules/%{kernel_release}/kernel/sound/soundcore.*
%if %{have_oss}
%exclude /lib/modules/%{kernel_release}/kernel/sound/oss
%endif

%if %{have_oss}
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}/kernel/sound/oss
%if %{have_isa} && !%{with xen0} && !%{with xenU}
/lib/modules/%{kernel_release}/kernel/drivers/media/radio/miropcm20.ko*
%endif
%endif
%endif			# %%{have_sound}
%endif			# %%{with up}

%if %{with smp}
%files smp
%defattr(644,root,root,755)
#doc FAQ-pl
%ifarch ia64
/boot/efi/vmlinuz-%{kernel_release}smp
%endif
/boot/vmlinuz-%{kernel_release}smp
/boot/System.map-%{kernel_release}smp
%ghost /boot/initrd-%{kernel_release}smp.gz
%dir /lib/modules/%{kernel_release}smp
%dir /lib/modules/%{kernel_release}smp/kernel
%ifnarch sparc
/lib/modules/%{kernel_release}smp/kernel/arch
%endif
/lib/modules/%{kernel_release}smp/kernel/crypto
/lib/modules/%{kernel_release}smp/kernel/drivers
%if %{have_drm}
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/char/drm
%endif
%if %{have_oss} && %{have_isa} && !%{with xen0} && !%{with xenU}
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/media/radio/miropcm20.ko*
%endif
/lib/modules/%{kernel_release}smp/kernel/fs
/lib/modules/%{kernel_release}smp/kernel/kernel
/lib/modules/%{kernel_release}smp/kernel/lib
/lib/modules/%{kernel_release}smp/kernel/net
/lib/modules/%{kernel_release}smp/kernel/security
%if %{have_sound}
%dir /lib/modules/%{kernel_release}smp/kernel/sound
/lib/modules/%{kernel_release}smp/kernel/sound/soundcore.*
%endif
%dir /lib/modules/%{kernel_release}smp/misc
%if %{with pcmcia}
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/ide/legacy/ide-cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/serial/serial_cs.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/telephony/ixj_pcmcia.ko*
%exclude /lib/modules/%{kernel_release}smp/kernel/drivers/usb/host/sl811_cs.ko*
%endif
/lib/modules/%{kernel_release}smp/build
%ghost /lib/modules/%{kernel_release}smp/modules.*
%dir %{_sysconfdir}/modprobe.d/%{kernel_release}smp

%ifarch alpha %{ix86} %{x8664} ppc ppc64 sparc sparc64
%files smp-vmlinux
%defattr(644,root,root,755)
/boot/vmlinux-%{kernel_release}smp
%endif

%if %{have_drm}
%files smp-drm
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}smp/kernel/drivers/char/drm
%endif

%if %{with pcmcia}
%files smp-pcmcia
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}smp/kernel/drivers/pcmcia
/lib/modules/%{kernel_release}smp/kernel/drivers/*/pcmcia
/lib/modules/%{kernel_release}smp/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/ide/legacy/ide-cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/isdn/hardware/avm/avm_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/net/wireless/hostap/hostap_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/serial/serial_cs.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/telephony/ixj_pcmcia.ko*
/lib/modules/%{kernel_release}smp/kernel/drivers/usb/host/sl811_cs.ko*
%endif

%ifarch ppc-broken
%if "%{_arch}" == "ppc"
%files smp-libs
%defattr(644,root,root,755)
%dir /boot/libs-%{kernel_release}smp
/boot/libs-%{kernel_release}smp/common
/boot/libs-%{kernel_release}smp/kernel
/boot/libs-%{kernel_release}smp/lib
/boot/libs-%{kernel_release}smp/of1275
/boot/libs-%{kernel_release}smp/openfirmware
/boot/libs-%{kernel_release}smp/simple
%dir /boot/libs-%{kernel_release}smp/utils
%attr(755,root,root) /boot/libs-%{kernel_release}smp/utils/*
/boot/libs-%{kernel_release}smp/ld.script
%endif
%endif

%if %{have_sound}
%files smp-sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}smp/kernel/sound
%exclude %dir /lib/modules/%{kernel_release}smp/kernel/sound
%exclude /lib/modules/%{kernel_release}smp/kernel/sound/soundcore.*
%if %{have_oss}
%exclude /lib/modules/%{kernel_release}smp/kernel/sound/oss
%endif

%if %{have_oss}
%files smp-sound-oss
%defattr(644,root,root,755)
/lib/modules/%{kernel_release}smp/kernel/sound/oss
%if %{have_isa} && !%{with xen0} && !%{with xenU}
/lib/modules/%{kernel_release}smp/kernel/drivers/media/radio/miropcm20.ko*
%endif
%endif
%endif			# %%{have_sound}
%endif			# %%{with smp}

%files headers
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}
%{_kernelsrcdir}/include
%if %{with smp}
%{_kernelsrcdir}/config-smp
%{_kernelsrcdir}/Module.symvers-smp
%endif
%{_kernelsrcdir}/config-up
%{?with_up:%{_kernelsrcdir}/Module.symvers-up}

%files module-build -f aux_files
%defattr(644,root,root,755)
%{_kernelsrcdir}/Kbuild
%{_kernelsrcdir}/localversion
%{_kernelsrcdir}/arch/*/kernel/asm-offsets.*
%{_kernelsrcdir}/arch/*/kernel/sigframe.h
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

%files doc
%defattr(644,root,root,755)
%{_kernelsrcdir}/Documentation

%if %{with source}
%files source -f aux_files_exc
%defattr(644,root,root,755)
%{_kernelsrcdir}/arch/*/[!Mk]*
%{_kernelsrcdir}/arch/*/kernel/[!M]*
%exclude %{_kernelsrcdir}/arch/*/kernel/asm-offsets.*
%exclude %{_kernelsrcdir}/arch/*/kernel/sigframe.h
%{_kernelsrcdir}/block
%{_kernelsrcdir}/crypto
%{_kernelsrcdir}/drivers
%{_kernelsrcdir}/fs
%if %{with grsecurity}
%{_kernelsrcdir}/grsecurity
%endif
%{_kernelsrcdir}/init
%{_kernelsrcdir}/ipc
%{_kernelsrcdir}/kernel
%{_kernelsrcdir}/lib
%{_kernelsrcdir}/mm
%{_kernelsrcdir}/net
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
%endif
