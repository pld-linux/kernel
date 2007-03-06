#
# STATUS: 2.6.20.1-0.11
# - works for me (i686 up)
# - builds on i686 (up & smp) with gcc-3.3.6-4 (Ac)
# - builds on x86_64 (up & smp) with gcc-4.2.0-0.20070214.1.x86_64 (Th)
# - standard config includes vserver, suspend2 and grsec_minimal
# - builds --with vesafb_tng (i686) --with reiser4 (i686/x86_64)
# - builds --with fbsplash (i686)
# - (external) nvidia works with & wo regparm
# - (external) nvidia-legacy works with & wo regparm
# - (external) ati firegl builds (but probably have issues with smp)
# - (external) slmodem builds
# - (external) madwifi-ng works with & wo regparm
# - (external) madwifi-old-openhal builds but have no supported hardware to test
# - (external) lirc builds
# - (external) ipp2p builds
# - (external) truecrypt builds
# - vserver 2.3.0.11 works
# - connlimit works
# - reiser4 builds
# - layer7 builds
# - TARPIT and ROUTE smp locking issues should be resolved
# - pax & grsec_min builds on x86_64, fails on i686
#
# TODO 2.6.20.1
# - fine-tune the ppc configs and test build on ppc
# - test build on sparc, sparc64, alpha
# - grsec_full and pax
# - pax hooks for selinux (experimental)
# - new alsa rc2 - 1.0.14rc2 is in 2.6.20-git10 tree
# - spec cleanup
# - test external modules
# - p200 linux-2.6-ppc-ICE-hacks.patch - untested - ppc needed
# - mms-conntrack-nat - port to nf_conntrack and enable in kernel-netfilter.config
#
# FUTURE:
# - separate PaX and grsecurity support - future
# - update xen patch for 2.6.20
# - wanpipe -> use wanpipe.spec instead ?
# - Linux ABI - needs update.
# - pom-ng quake3-conntrack-nat -> nf_conntrack ?
# - pom-ng rpc -> ?
# - pom-ng rtsp-conntrack -> nf_conntrack ?
# - pom-ng talk-conntrack-nat -> nf_conntrack ?
# - nf-hipac ?
# - update configs for up/smp ia64 - no builder ?
#
# Conditional build:
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	source		# don't build kernel-source package
%bcond_without	pcmcia		# don't build pcmcia
%bcond_without	regparm		# if your blob doesn't work try disable this

%bcond_with	abi		# build ABI support only ix86 !!
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	xen0		# added Xen0 support
%bcond_with	xenU		# added XenU support
%bcond_with	reiser4		# support for reiser4 fs

%bcond_without	grsecurity	# don't build grsecurity nor pax at all
%bcond_without	grsec_minimal	# build only minimal subset (proc,link,fifo,shm)
%bcond_with	grsec_full	# build full grsecurity
%bcond_with	pax_full	# build pax and full grsecurity (ie. grsec_full && pax)
%bcond_with	pax		# build pax support

%bcond_with	fbsplash	# fbsplash instead of bootsplash
%bcond_with	vesafb_tng	# vesafb-tng, vesafb replacement from gentoo
%bcond_with	pae		# build PAE (HIGHMEM64G) support on uniprocessor
%bcond_with	nfsroot		# build with root on NFS support

%bcond_without	ide_acpi	# support for ide-acpi from SuSE
%bcond_without	imq		# imq support
%bcond_without	wrr		# wrr support

%bcond_without	vserver		# support for VServer (enabled by default) 
%bcond_without	suspend2	# support for Suspend2 (enabled by default)

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
%endif

%if %{with grsec_minimal}
%undefine	with_grsec_full
%undefine	with_pax_full
%define		with_grsecurity		1
%endif

%ifarch ia64
# broken
%undefine	with_up
%endif

%ifnarch %{ix86}
%undefine	abi
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

%define		_basever		2.6.20
%define		_postver		.1
%define		_prepatch		%{nil}
%define		_pre_rc			%{nil}
%define		_rc			%{nil}
%define		_rel			0.12

%define		_netfilter_snap		20061213
%define		_nf_hipac_ver		0.9.1

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

%define		squashfs_version	3.2
%define		suspend_version		2.2.9

%define		xen_version		3.0.2

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de.UTF-8):   Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr.UTF-8):   Le Kernel-Linux (La partie centrale du systeme)
Summary(pl.UTF-8):   Jądro Linuksa
Name:		kernel%{?with_pax:-pax}%{?with_grsec_full:-grsecurity}%{?with_xen0:-xen0}%{?with_xenU:-xenU}

%if "%{_prepatch}" == "%{nil}"
Version:	%{_basever}%{_postver}
Release:	%{_rel}
%else
Version:	%{_prepatch}
Release:	0.%{_pre_rc}.%{_rel}
%endif

Epoch:		3
License:	GPL v2
Group:		Base/Kernel
#Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/linux-%{version}%{_rc}.tar.bz2
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{_basever}%{_rc}.tar.bz2
# Source0-md5:	34b0f354819217e6a345f48ebbd8f13e
%if "%{_prepatch}" != "%{nil}"
Source90:	http://www.kernel.org/pub/linux/kernel/v2.6/testing/patch-%{_prepatch}-%{_pre_rc}.bz2
# Source90-md5:	b78873f8a3aff5bdc719fc7fb4c66a9b
%endif
%if "%{_postver}" != "%{nil}"
Source1:	http://www.kernel.org/pub/linux/kernel/v2.6/patch-%{version}.bz2
# Source1-md5:	5739512c396b37d9506bca2afe5aaa1d
%endif

Source3:	kernel-autoconf.h
Source4:	kernel-config.h
Source5:	kernel-ppclibs.Makefile
Source7:	kernel-module-build.pl

# TODO - cleanup
Source14:	http://ace-host.stuart.id.au/russell/files/debian/sarge/kernel-patch-linuxabi/kernel-patch-linuxabi_20060404.tar.gz
# Source14-md5:	f2563a2d748c7480559e8d3ff77eb18a

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
Source34:	kernel-abi.config

Source40:	kernel-netfilter.config
Source41:	kernel-squashfs.config
Source42:	kernel-suspend2.config
Source43:	kernel-vserver.config
Source44:	kernel-vesafb-tng.config
Source45:	kernel-grsec.config
Source46:	kernel-xen0.config
Source47:	kernel-xenU.config

Source49:	kernel-pax.config
Source50:	kernel-no-pax.config
Source51:	kernel-grsec_minimal.config
Source55:	kernel-imq.config
Source56:	kernel-reiser4.config
Source57:	kernel-wrr.config

###
#	Patches
###

# TODO: patch not active for some time 
Patch0:		linux-net-2.6.19.patch
#
# TODO: not compatible - still needed?
# PATA ports on SATA Promise controller; patch based on:
# http://cvs.fedora.redhat.com/viewcvs/*checkout*/rpms/kernel/devel/linux-2.6-sata-promise-pata-ports.patch
Patch1:		linux-2.6-sata-promise-pata-ports.patch

# tahoe9XX http://tahoe.pl/drivers/tahoe9xx-2.6.11.5.patch
Patch2:		tahoe9xx-2.6.11.5.patch

# TODO:	ftp://ftp.openbios.org/pub/bootsplash/kernel/bootsplash-3.1.6-2.6.18.diff
Patch3:		bootsplash-3.1.6-2.6.18.diff
# TODO:	http://dev.gentoo.org/~spock/projects/gensplash/archive/fbsplash-0.9.2-r5-2.6.20-rc6.patch
Patch4:		fbsplash-0.9.2-r5-2.6.20-rc6.patch

# http://dev.gentoo.org/~spock/projects/vesafb-tng/archive/vesafb-tng-1.0-rc2-2.6.20-rc2.patch
Patch5:		vesafb-tng-1.0-rc2-2.6.20-rc2.patch

# Derived from squashfs: http://mesh.dl.sourceforge.net/sourceforge/squashfs/squashfs3.2.tar.gz for linux-2.6.20
# 
Patch6:		squashfs%{squashfs_version}-patch
Patch7:		linux-alpha-isa.patch
Patch8:		linux-fbcon-margins.patch
Patch9:		linux-static-dev.patch

# netfilter p-o-m-ng snap 20061213

# base
Patch10:	pom-ng-IPV4OPTSSTRIP-%{_netfilter_snap}.patch
Patch14:	pom-ng-ipv4options-%{_netfilter_snap}.patch
Patch20:	pom-ng-set-%{_netfilter_snap}.patch
Patch22:	pom-ng-u32-%{_netfilter_snap}.patch

# extra
Patch32:	pom-ng-ROUTE-%{_netfilter_snap}.patch
Patch33:	pom-ng-TARPIT-%{_netfilter_snap}.patch
Patch34:	pom-ng-mms-conntrack-nat-%{_netfilter_snap}.patch
Patch37:	pom-ng-rsh-%{_netfilter_snap}.patch

#external
Patch40:	pom-ng-IPMARK-%{_netfilter_snap}.patch
Patch41:	pom-ng-connlimit-%{_netfilter_snap}.patch
Patch42:	pom-ng-geoip-%{_netfilter_snap}.patch
Patch43:	pom-ng-ipp2p-%{_netfilter_snap}.patch
Patch44:	pom-ng-time-%{_netfilter_snap}.patch

#layer7 with temporary fix
Patch48:	kernel-2.6.18-layer7-2.7.patch
Patch49:	kernel-2.6.18-layer7-2.7-2.6.19-fix.patch

# netfilter patches preparation order:
#
# [pom base]
# can be independently applied on 2.6.19.1 source:
# 	pom-ng-IPV4OPTSSTRIP-20061213.patch
# 	pom-ng-ipv4options-20061213.patch
#	pom-ng-set-20061213.patch
#	pom-ng-u32-20061213.patch
# [pom extra]
#	pom-ng-ROUTE-20061213.patch
# 	pom-ng-TARPIT-20061213.patch
#	pom-ng-mms-conntrack-nat-20061213.patch
#	(note: mms-conntrack-nat depends on ip_conntrack - needs porting to nf_conntrack)
# all below applied to sources with all preceeding patches applied:
#	pom-ng-rsh-20061213.patch
# [pom external]
#	pom-ng-IPMARK-20061213.patch
#	pom-ng-connlimit-20061213.patch
#	(note: connlimit needs an additional patch to work with nf_conntrack -> p301)
#	pom-ng-geoip-20061213.patch
#	pom-ng-ipp2p-20061213.patch
#	pom-ng-time-20061213.patch
#
# layer7: 
# 	kernel-2.6.18-layer7-2.7.patch

###
#	End netfilter
###

# based on 2.6.17 patch from http://www.linuximq.net/patchs/linux-2.6.17-imq1.diff, 
# some stuff moved from net/sched/sch_generic.c to net/core/dev.c for 2.6.19 
# compatibility. not tested. 

Patch50:	linux-2.6.19-imq1.diff

# reiser4 based on ftp://ftp.namesys.com/pub/reiser4-for-2.6/2.6.19/reiser4-for-2.6.19-2.patch.gz
Patch51:	reiser4-for-2.6.19-2.patch

# wrr http://www.zz9.dk/patches/wrr-linux-051111-2.6.20.patch.gz
Patch52:	wrr-linux-051111-2.6.20.patch

# esfq from http://fatooh.org/esfq-2.6/current/esfq-kernel.patch
Patch53:	esfq-kernel.patch

# from http://memebeam.org/free-software/toshiba_acpi/
Patch54:	linux-2.6-toshiba_acpi_0.18-dev_toshiba_test4.patch
# by Baggins request:
# derived from ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch55:	linux-2.6-atm-vbr.patch
Patch56:	linux-2.6-atmdd.patch

Patch57:	linux-2.6-cpuset_virtualization.patch

# Derived from http://www.skd.de/e_en/products/adapters/pci_64/sk-98xx_v20/software/linux/driver/install-8_41.tar.bz2
Patch60:	linux-2.6-sk98lin_8.41.2.3.patch

# based on http://www.suspend2.net/downloads/all/suspend2-2.2.9.7-for-2.6.20.patch.bz2
Patch69:	linux-2.6-suspend2.patch
Patch70:	linux-2.6-suspend2-avoid-redef.patch
Patch71:	linux-2.6-suspend2-page.patch
#Patch72:	linux-2.6-suspend2-off.patch
Patch72:	kernel-2.6-ueagle-atm-freezer.patch

# ide-acpi instead of nx8220 s3 suspend/resume hack
# http://svn.uludag.org.tr/pardus/devel/kernel/kernel/files/suse/ide-acpi-support.patch
Patch75:	linux-2.6-ide-acpi-support.patch

# adds some ids for hostap suported cards and monitor_enable from/for aircrack-ng
# http://patches.aircrack-ng.org/hostap-kernel-2.6.18.patch 
Patch85:	hostap-kernel-2.6.18.patch

# based on http://vserver.13thfloor.at/Experimental/patch-2.6.20.1-vs2.3.0.11.diff
Patch100:	linux-2.6-vs2.3.patch
Patch101:	linux-2.6-vs2.1-suspend2.patch
Patch102:	linux-2.6-vs2.1-128IPs.patch
# Quota on vroot fix, reported upstream
Patch103:	linux-2.6-vs2.3-quota.patch

# from http://www.cl.cam.ac.uk/Research/SRG/netos/xen/downloads/xen-3.0.2-src.tgz
#Patch120:	xen-3.0-2.6.16.patch

# Wake-On-Lan fix for nForce drivers; using http://atlas.et.tudelft.nl/verwei90/nforce2/wol.html
# Fix verified for that kernel version.
Patch130:	linux-2.6-forcedeth-WON.patch

Patch200:	linux-2.6-ppc-ICE-hacks.patch

# http://www.ssi.bg/~ja/routes-2.6.19-12.diff
Patch300:	routes-2.6.19-12.diff
Patch301:	pom-ng-connlimit-20061213_nf_conntrack_port.patch
Patch302:	linux-2.6-layer7_nf_conntrack_port.patch

Patch400:       kernel-bcm43xx-2.6.20_combined.patch

# For compatibility with such blobs like HAL from madwifi-ng
# before we had CONFIG_REGPARM option disabled - it is bconded and disabled now
Patch500:	linux-2.6.20_i386_regparm_off.patch

Patch1000:	linux-2.6-grsec-minimal.patch

Patch2000:	kernel-small_fixes.patch

# Some non-GPL modules (nvidia, nvidia-legacy) looks for the paravirt_ops symbol
Patch2100:	linux-2.6.20-paravirt_ops-needed-by-blobs.patch

#wanpipe
#Patch3000:	wanpipe-beta7-2.3.4.patch

Patch9997:	pax_selinux_hooks-2.6.20.patch

# TODO: http://www.grsecurity.net/~paxguy1/pax-linux-2.6.20.1-test5.patch
Patch9998:	pax-linux-2.6.20.patch

# TODO: http://www.grsecurity.net/~spender/grsecurity-2.1.10-2.6.19.3-200702201828.patch
Patch9999:	grsecurity-2.1.10.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 3:2.14.90.0.7
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
%if %{with xen0} || %{with xenU}
Provides:	kernel(xen) = %{_xen_version}
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
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	udev < %{_udev_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	vserver-packages
Conflicts:	xfsprogs < %{_xfsprogs_ver}
%if %{with xen0} || %{with xenU}
ExclusiveArch:	%{ix86}
%else
ExclusiveArch:	%{ix86} alpha %{x8664} ia64 ppc ppc64 sparc sparc64 arm
%endif
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# No ELF objects there to strip (skips processing 27k files)
%define		_noautostrip	.*%{_kernelsrcdir}/.*

%ifarch ia64
%define		initrd_dir	/boot/efi
%else
%define		initrd_dir	/boot
%endif

# kernel release (used in filesystem and eventually in uname -r)
# modules will be looked from /lib/modules/%{kernel_release}%{?smp}
# _localversion is just that without version for "> localversion"
%define		_localversion %{release}
%define		kernel_release %{version}-%{_localversion}
%define		_kernelsrcdir	/usr/src/linux-%{version}

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

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description -l de.UTF-8
Das Kernel-Paket enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeß-Management, Geräte Ein- und Ausgaben, usw.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description -l fr.UTF-8
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un système d'exploitation Linux. Le noyau traite les
fonctions basiques d'un système d'exploitation: allocation mémoire,
allocation de process, entrée/sortie de peripheriques, etc.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description -l pl.UTF-8
Pakiet zawiera jądro Linuksa niezbędne do prawidłowego działania
Twojego komputera. Zawiera w sobie sterowniki do sprzętu znajdującego
się w komputerze, takiego jak sterowniki dysków itp.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%package vmlinux
Summary:	vmlinux - uncompressed kernel image
Summary(pl.UTF-8):   vmlinux - rozpakowany obraz jądra
Group:		Base/Kernel

%description vmlinux
vmlinux - uncompressed kernel image.

%description vmlinux -l pl.UTF-8
vmlinux - rozpakowany obraz jądra.

%package drm
Summary:	DRM kernel modules
Summary(pl.UTF-8):   Sterowniki DRM
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel-drm = %{drm_xfree_version}
Autoreqprov:	no

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description drm -l pl.UTF-8
Sterowniki DRM (%{drm_xfree_version}).

%package pcmcia
Summary:	PCMCIA modules
Summary(pl.UTF-8):   Moduły PCMCIA
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

%description pcmcia -l pl.UTF-8
Moduły PCMCIA (%{pcmcia_version}).

%package libs
Summary:	Libraries for preparing bootable kernel on PowerPCs
Summary(pl.UTF-8):   Biblioteki do przygotowania bootowalnego jądra dla PowerPC
Group:		Base/Kernel
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description libs
Libraries for preparing bootable kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description libs -l pl.UTF-8
Biblioteki do przygotowania bootowalnego jądra dla PowerPC. Skrypt
mkvmlinuz może być do tego przydatny.

%package sound-alsa
Summary:	ALSA kernel modules
Summary(pl.UTF-8):   Sterowniki dźwięku ALSA
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l pl.UTF-8
Sterowniki dźwięku ALSA (Advanced Linux Sound Architecture).

%package sound-oss
Summary:	OSS kernel modules
Summary(pl.UTF-8):   Sterowniki dźwięku OSS
Group:		Base/Kernel
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Requires:	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-oss
OSS (Open Sound System) drivers.

%description sound-oss -l pl.UTF-8
Sterowniki dźwięku OSS (Open Sound System).

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de.UTF-8):   Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr.UTF-8):   Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl.UTF-8):   Jądro Linuksa w wersji %{version} dla maszyn wieloprocesorowych
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
%if %{with xen0} || %{with xenU}
Provides:	kernel(xen) = %{_xen_version}
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
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	vserver-packages
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description smp -l de.UTF-8
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description smp -l fr.UTF-8
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nécessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand même fonctionner pour les système mono-processeur.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%description smp -l pl.UTF-8
Pakiet zawiera jądro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawierające dwa lub więcej procesorów.
Powinno również dobrze działać na maszynach z jednym procesorem.

Netfilter module dated: %{_netfilter_snap}
%{?with_abi:Linux ABI support - enabled}
%{?with_grsec_full:Grsecurity full support - enabled}
%{?with_pax:PaX and Grsecurity full support - enabled}
%{?with_xen0:Xen 0 - enabled}
%{?with_xenU:Xen U - enabled}
%{?with_fbsplash:Fbsplash - enabled }
%{?with_vesafb_tng:VesaFB New generation - enabled}
%{?with_nfsroot:Root on NFS - enabled}

%package smp-vmlinux
Summary:	vmlinux - uncompressed SMP kernel image
Summary(pl.UTF-8):   vmlinux - rozpakowany obraz jądra SMP
Group:		Base/Kernel

%description smp-vmlinux
vmlinux - uncompressed SMP kernel image.

%description smp-vmlinux -l pl.UTF-8
vmlinux - rozpakowany obraz jądra SMP.

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl.UTF-8):   Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	kernel-drm = %{drm_xfree_version}
Autoreqprov:	no

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description smp-drm -l pl.UTF-8
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package smp-pcmcia
Summary:	PCMCIA modules for SMP kernel
Summary(pl.UTF-8):   Moduły PCMCIA dla maszyn SMP
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

%description smp-pcmcia -l pl.UTF-8
Moduły PCMCIA dla maszyn SMP (%{pcmcia_version}).

%package smp-libs
Summary:	Libraries for preparing bootable SMP kernel on PowerPCs
Summary(pl.UTF-8):   Biblioteki do przygotowania bootowalnego jądra dla wieloprocesorowych PowerPC
Group:		Base/Kernel
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	mkvmlinuz >= %{_mkvmlinuz_ver}
Autoreqprov:	no

%description smp-libs
Libraries for preparing bootable SMP kernel on PowerPCs. Script called
mkvmlinuz may be useful for this.

%description smp-libs -l pl.UTF-8
Biblioteki do przygotowania bootowalnego jądra dla wieloprocesorowych
PowerPC. Skrypt mkvmlinuz może być do tego przydatny.

%package smp-sound-alsa
Summary:	ALSA SMP kernel modules
Summary(pl.UTF-8):   Sterowniki dźwięku ALSA dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-alsa
ALSA (Advanced Linux Sound Architecture) SMP sound drivers.

%description smp-sound-alsa -l pl.UTF-8
Sterowniki dźwięku ALSA (Advanced Linux Sound Architecture) dla maszyn
wieloprocesorowych.

%package smp-sound-oss
Summary:	OSS SMP kernel modules
Summary(pl.UTF-8):   Sterowniki dźwięku OSS dla maszyn wieloprocesorowych
Group:		Base/Kernel
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Requires:	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-oss
OSS (Open Sound System) SMP sound drivers.

%description smp-sound-oss -l pl.UTF-8
Sterowniki OSS (Open Sound System) dla maszyn wieloprocesorowych.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl.UTF-8):   Pliki nagłówkowe jądra Linuksa
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

%description headers -l pl.UTF-8
Pakiet zawiera pliki nagłówkowe jądra, niezbędne do rekompilacji jądra
oraz budowania modułów jądra.

%package module-build
Summary:	Development files for building kernel modules
Summary(pl.UTF-8):   Pliki służące do budowania modułów jądra
Group:		Development/Building
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
Provides:	kernel-module-build = %{epoch}:%{_basever}
Provides:	kernel-module-build = %{epoch}:%{version}-%{release}
Conflicts:	rpmbuild(macros) < 1.321
Autoreqprov:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%description module-build -l pl.UTF-8
Pliki ze drzewa źródeł jądra potrzebne do budowania modułów jądra
Linuksa z zewnętrznych pakietów.

%package source
Summary:	Kernel source tree
Summary(pl.UTF-8):   Kod źródłowy jądra Linuksa
Group:		Development/Building
Requires:	%{name}-module-build = %{epoch}:%{version}-%{release}
Provides:	kernel-source = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l de.UTF-8
Das Kernel-Source-Paket enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
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
Summary(pl.UTF-8):   Dokumentacja do jądra Linuksa
Group:		Documentation
Provides:	kernel-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl.UTF-8
Pakiet zawiera dokumentację do jądra Linuksa pochodzącą z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{_basever}%{_rc} %{?with_abi:-a14}

# borooken in this time.
#patch0 -p1

%ifarch ppc
install %{SOURCE5} Makefile.ppclibs
%endif

# sources 1 and 90 should be mutually exclusive btw.

%if "%{_prepatch}" != "%{nil}"
%{__bzip2} -dc %{SOURCE90} | patch -p1 -s
%endif

%if "%{_postver}" != "%{nil}"
%{__bzip2} -dc %{SOURCE1} | patch -p1 -s
%endif

# TODO 2.6.20 - check this out - promise pata-sata stuff.
#patch1 -p1

# suspend2:
%if %{with suspend2}
%ifarch %{ix86} %{x8664} ia64
%patch69 -p1
# TODO check linux-2.6-suspend2-avoid-redef.patch
#patch70 -p1
%patch71 -p1
# kernel-2.6-ueagle-atm-freezer.patch
%patch72 -p1
%endif
%endif

# reiserfs4
#%{__gzip} -dc %{SOURCE12} | %{__patch} -s -p1

%patch2 -p1

%patch8 -p1

%if !%{with fbsplash}
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
#

# base
%patch10 -p1
%patch14 -p1
%patch20 -p1
%patch22 -p1

## extra
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch37 -p1

## external
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1

## layer7
%patch48 -p1
%patch49 -p1
%patch302 -p1

##
# end of netfilter

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

# TODO check linux-2.6-toshiba_acpi_0.18-dev_toshiba_test4.patch
#patch54 -p1

%patch55 -p1
%patch56 -p1

%ifarch %{ix86} %{x8664} ia64
%patch57 -p1
%endif

# linux-2.6-sk98lin_8.41.2.3.patch
%patch60 -p1

%if %{with ide_acpi}
# ide-acpi instead of nx8220 s3 suspend/resume hack
%patch75 -p1
%endif

# hostap enhancements from/for aircrack-ng 
%patch85 -p1

# vserver
%if %{with vserver}
%patch100 -p1
%ifarch %{ix86} %{x8664} ia64
%patch101 -p1
%endif
%patch102 -p1
%patch103 -p1
%endif

#%if %{with xen0} || %{with xenU}
#%ifarch %{ix86} %{x8664} ia64
#%patch120 -p1
#%endif
#%endif

# forcedeth:
%patch130 -p1

# desables regparms
%if %{without regparm}
%patch500 -p1
%endif

# grsecurity & pax stuff - temporary - work in progress
#

%if %{with pax_full}
%patch9999 -p1
%else 

%if %{with grsec_full}
%patch9999 -p1
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

%ifarch ppc ppc64
%patch200 -p1
%endif

%patch300 -p1
%patch301 -p1

%patch400 -p1
#Small fixes:
%patch2000 -p1

# exporting paravirt_ops as non-GPL-only symbol
%patch2100 -p1

%if %{with abi}
patch -p1 -s < kernel-patch-linuxabi-20060404/linuxabi-2.6.17-0.patch
%endif

# wanpipe
#patch3000 -p1

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION = %{_postver}#g' Makefile

# on sparc this line causes CONFIG_INPUT=m (instead of =y), thus breaking build
sed -i -e '/select INPUT/d' net/bluetooth/hidp/Kconfig

# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' -o -name '.gitignore' ')' -print0 | xargs -0 -r -l512 rm -f

%build
TuneUpConfigForIX86 () {
	set -x
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

PaXconfig () {
	set -x
	%ifarch %{ix86}
		sed -i 's:# CONFIG_PAX_SEGMEXEC is not set:CONFIG_PAX_SEGMEXEC=y:' $1
		sed -i 's:# CONFIG_PAX_DEFAULT_SEGMEXEC is not set:CONFIG_PAX_DEFAULT_SEGMEXEC=y:' $1
		%ifnarch i386 i486
			sed -i 's:# CONFIG_PAX_NOVSYSCALL is not set:CONFIG_PAX_NOVSYSCALL=y:' $1
		%endif

		# Testing KERNEXEC

		# sed -i 's:CONFIG_HOTPLUG_PCI_COMPAQ_NVRAM=y:# CONFIG_HOTPLUG_PCI_COMPAQ_NVRAM is not set:' $1
		# sed -i 's:CONFIG_PCI_BIOS=y:# CONFIG_PCI_BIOS is not set:' $1
		# sed -i 's:CONFIG_EFI=y:# CONFIG_EFI is not set:' $1
		
	%endif
	%ifarch ppc64
		sed -i 's:CONFIG_PAX_NOELFRELOCS=y:# CONFIG_PAX_NOELFRELOCS is not set:' $1
	%endif
	%ifarch ppc
		sed -i 's:# CONFIG_PAX_EMUTRAMP is not set:CONFIG_PAX_EMUTRAMP=y:' $1
	%endif
	%ifarch %{ix8664}
		sed -i 's:# CONFIG_PAX_MEMORY_UDEREF is not set:CONFIG_PAX_MEMORY_UDEREF=y:' $1
	%endif

	# Now we have to check MAC system integration. Grsecurity (full) uses PAX_HAVE_ACL_FLAGS
	# setting (direct acces). grsec_minimal probably have no idea about PaX so we probably 
	# could use PAX_NO_ACL_FLAGS, but for testing the hooks setting will be used
	# PAX_HOOK_ACL_FLAGS. SELinux should also be able to make PaX settings via hooks 

	%if %{with grsec_full}
		# no change needed CONFIG=PAX_HAVE_ACL_FLAGS=y is taken from the kernel-pax.config
	%else
		# grsec_minimal or selinux ?
		sed -i 's:CONFIG_PAX_HAVE_ACL_FLAGS=y:# CONFIG_PAX_HAVE_ACL_FLAGS is not set:' $1
		sed -i 's:# CONFIG_PAX_HOOK_ACL_FLAGS is not set:CONFIG_PAX_HOOK_ACL_FLAGS=y:' $1
	%endif

	return 0
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
%if %{with suspend2}
	cat %{SOURCE42} >> arch/%{_target_base_arch}/defconfig
%endif

%ifarch ppc ppc64
	sed -i "s:CONFIG_SUSPEND2=y:# CONFIG_SUSPEND2 is not set:" arch/%{_target_base_arch}/defconfig
%endif
%if %{with vserver}
	cat %{SOURCE43} >> arch/%{_target_base_arch}/defconfig
%endif

# vesafb-tng
	cat %{SOURCE44} >> arch/%{_target_base_arch}/defconfig

# grsecurity & pax stuff - temporary - work in progress
#

%if %{with pax_full}
	cat %{SOURCE45} >> arch/%{_target_base_arch}/defconfig
	cat %{SOURCE49} >> arch/%{_target_base_arch}/defconfig
	PaXconfig arch/%{_target_base_arch}/defconfig
%else

%if %{with grsec_full}
	cat %{SOURCE45} >> arch/%{_target_base_arch}/defconfig
%else
%if %{with grsec_minimal}
	cat %{SOURCE51} >> arch/%{_target_base_arch}/defconfig
%endif
%endif

%if %{with pax}
	cat %{SOURCE49} >> arch/%{_target_base_arch}/defconfig
	PaXconfig arch/%{_target_base_arch}/defconfig
%else
	cat %{SOURCE50} >> arch/%{_target_base_arch}/defconfig
%endif

%endif

#
# end of grsecurity & pax stuff


%if %{with imq}
	cat %{SOURCE55} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with wrr}
	cat %{SOURCE57} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with reiser4}
	cat %{SOURCE56} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with ide_acpi}
	echo "CONFIG_BLK_DEV_IDEACPI=y" >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with xen0}
	cat %{SOURCE46} >> arch/%{_target_base_arch}/defconfig
%endif

%if %{with xenU}
	cat %{SOURCE47} >> arch/%{_target_base_arch}/defconfig
%endif

	# fbsplash && bootsplash
	echo "CONFIG_FB_SPLASH=y" >> arch/%{_target_base_arch}/defconfig
	echo "CONFIG_BOOTSPLASH=y" >> arch/%{_target_base_arch}/defconfig

%if %{with nfsroot}
	sed -i "s:CONFIG_NFS_FS=m:CONFIG_NFS_FS=y:" arch/%{_target_base_arch}/defconfig
	echo "CONFIG_ROOT_NFS=y" >> arch/%{_target_base_arch}/defconfig
%endif

%ifarch %{ix86}
%if %{with abi}
	cat %{SOURCE34} >> arch/%{_target_base_arch}/defconfig
%endif
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
	echo "Building kernel $1 ..."
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

	%{__make} %CrossOpts scripts/mkcompile_h \
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
	%{__make} %CrossOpts modules_install \
		%{?with_verbose:V=1} \
		DEPMOD=%DepMod \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	# You'd probabelly want to make it somewhat different
	install -d $KERNEL_INSTALL_DIR%{_kernelsrcdir}
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
%if %{with up}
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-UP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig
BuildKernel
PreInstallKernel
%endif


# SMP KERNEL
%if %{with smp}
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-SMP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig smp
BuildKernel smp
PreInstallKernel smp
%endif

%{__make} %CrossOpts include/linux/utsrelease.h
cp include/linux/utsrelease.h{,.save}
cp include/linux/version.h{,.save}
cp scripts/mkcompile_h{,.save}
sed -i 's:smp::' include/linux/utsrelease.h.save

%install
rm -rf $RPM_BUILD_ROOT
umask 022

export DEPMOD=%DepMod

install -d $RPM_BUILD_ROOT%{_kernelsrcdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/%{kernel_release}{,smp}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al COPYING $RPM_BUILD_ROOT/COPYING 2>/dev/null; then
	l=l
	rm -f $RPM_BUILD_ROOT/COPYING
fi

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
cp -Rdp$l $KERNEL_BUILD_DIR/include/linux/* \
	$RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux
%endif

%{__make} %CrossOpts mrproper
mv -f include/linux/utsrelease.h.save $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/utsrelease.h
cp include/linux/version.h{.save,}
cp scripts/mkcompile_h{.save,}
rm -rf include/linux/version.h.save
rm -rf scripts/mkcompile_h.save
install %{SOURCE3} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/autoconf.h
install %{SOURCE4} $RPM_BUILD_ROOT%{_kernelsrcdir}/include/linux/config.h

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
mv -f /boot/efi/vmlinuz /boot/efi/vmlinuz.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{kernel_release} /boot/efi/vmlinuz
%endif
ln -sf vmlinuz-%{kernel_release} /boot/vmlinuz
ln -sf System.map-%{kernel_release} /boot/System.map

%depmod %{kernel_release}

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}.gz %{kernel_release}
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{kernel_release}.gz %{initrd_dir}/initrd

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

%post vmlinux
mv -f /boot/vmlinux /boot/vmlinux.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{kernel_release} /boot/vmlinux

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

%preun smp
rm -f /lib/modules/%{kernel_release}smp/modules.*
if [ -x /sbin/new-kernel-pkg ]; then
	/sbin/new-kernel-pkg --remove %{kernel_release}smp
fi

%post smp
%ifarch ia64
mv -f /boot/efi/vmlinuz /boot/efi/vmlinuz.old 2> /dev/null > /dev/null
%endif
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
%ifarch ia64
ln -sf vmlinuz-%{kernel_release}smp /boot/efi/vmlinuz
%endif
ln -sf vmlinuz-%{kernel_release}smp /boot/vmlinuz
ln -sf System.map-%{kernel_release}smp /boot/System.map

%depmod %{kernel_release}smp

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{kernel_release}smp.gz %{kernel_release}smp
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{kernel_release}smp.gz %{initrd_dir}/initrd

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

%post smp-vmlinux
mv -f /boot/vmlinux /boot/vmlinux.old 2> /dev/null > /dev/null
ln -sf vmlinux-%{kernel_release}smp /boot/vmlinux

%post smp-libs
%{_sbindir}/mkvmlinuz /boot/zImage-%{kernel_release}smp %{kernel_release}smp

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
ln -snf %{basename:%{_kernelsrcdir}} %{_prefix}/src/linux

%postun headers
if [ "$1" = "0" ]; then
	if [ -L %{_prefix}/src/linux ]; then
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
/lib/modules/%{kernel_release}/kernel/fs

# this directory will be removed after disabling rcutorture mod. in 2.6.20.
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
/lib/modules/%{kernel_release}smp/kernel/fs

# see above note.
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
%{?with_up:%{_kernelsrcdir}/config-up}
%{?with_up:%{_kernelsrcdir}/Module.symvers-up}

%files module-build -f aux_files
%defattr(644,root,root,755)
# symlinks pointint to kernelsrcdir
%if %{with up}
%dir /lib/modules/%{kernel_release}
/lib/modules/%{kernel_release}/build
%endif
%if %{with smp}
%dir /lib/modules/%{kernel_release}smp
/lib/modules/%{kernel_release}smp/build
%endif
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
%{_kernelsrcdir}/scripts/mkcompile_h

%files doc
%defattr(644,root,root,755)
%{_kernelsrcdir}/Documentation

%if %{with source}
%files source -f aux_files_exc
%defattr(644,root,root,755)
%if %{with abi}
%{_kernelsrcdir}/abi
%endif /* abi */
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
