#
# TODO:
#		- add distcc support (and don't break crossbuild!)
#		- move em8300/lirc/iriverfs/squashfs stuff to separeated specs
#
# Conditional build:
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	source		# don't build kernel-source package
%bcond_with	grsecurity	# enable grsecurity
%bcond_with	pax		# enable PaX (depends on grsecurity)
%bcond_with	omosix		# enable openMosix (conflicts with grsecurity/vserver)
%bcond_with	vserver		# enable vserver (conflicts with grsecurity/omosix)
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	preemptive	# build preemptive kernel
%bcond_with	regparm		# (ix86) use register arguments (this break binary-only modules)
%bcond_with	em8300		# DXR3/Hollywood
%bcond_with	xen0		# build Xen0 kernel
%bcond_with	xenU		# build XenU kernel

%if %{with xen0} || %{with xenU}
%define with_xen 1
%endif

%if !%{with grsecurity}
%undefine	with_pax
%endif

%ifnarch %{ix86} %{x8664} ppc
%undefine	with_omosix
%endif

%if %{with omosix}
%undefine	with_smp
%endif

%if %{with omosix} && %{with vserver}
openmosix conflicts with vserver
%endif

%if %{with grsecurity} && %{with omosix}
grsecurity conflicts with omosix
%endif

%if %{with grsecurity} && %{with vserver}
grsecurity conflicts with vserver
%endif

%if %{with xen} && %{with grsecurity}
xen conflicts with grsecurity
%endif

%if %{with xen0} && %{with xenU}
xen0 conflicts with xenU
%endif

%{?debug:%define with_verbose 1}

%ifarch sparc
# sparc32 is missing important updates from 2.5 cycle - won't build
%undefine	with_smp
%endif
%ifarch ia64
# broken
%undefine	with_up
%endif

%if %{with xen}
# xen (for now) is only UP
%undefine	with_smp
%endif

## Program required by kernel to work.
%define		_binutils_ver		2.12
%define		_util_linux_ver		2.10o
%define		_module_init_tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_reiser4progs_ver	1.0.0
%define		_xfsprogs_ver		2.6.0
%define		_pcmcia_cs_ver		3.1.21
%define		_quota_tools_ver	3.09
%define		_PPP_ver		2.4.0
%define		_isdn4k_utils_ver	3.1pre1
%define		_nfs_utils_ver		1.0.5
%define		_procps_ver		3.2.0
%define		_oprofile_ver		0.5.3

%define		_rel		0.1

%define		_netfilter_snap		20050622

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel%{?with_grsecurity:-grsecurity}%{?with_omosix:-openmosix}%{?with_vserver:-vserver}%{?with_xen0:-xen0}%{?with_xenU:-xenU}
%define		_postver	.2
#define		_postver	%{nil}
Version:	2.6.12%{_postver}
Release:	%{_rel}
Epoch:		3
License:	GPL v2
Group:		Base/Kernel
%define		_rc	%{nil}
#define		_rc	-rc3
#Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/linux-%{version}%{_rc}.tar.bz2
Source0:	http://www.kernel.org/pub/linux/kernel/v2.6/linux-%{version}%{_rc}.tar.bz2
# Source0-md5:	6ee5bf307335e58193c8d2ac0d35677b
Source1:	kernel-autoconf.h
Source2:	kernel-config.h

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
Source34:	kernel-xen0.config
#Source35:	kernel-xen0-smp.config
#Source36:	kernel-xenU.config

Source40:	kernel.FAQ-pl

Source80:	kernel-netfilter.config
Source90:	kernel-grsec.config
Source91:	kernel-grsec+pax.config
Source92:	kernel-omosix.config
Source93:	kernel-vserver.config
Source94:	kernel-em8300.config
Source95:	kernel-linuxabi.config
Source96:	kernel-ocfs2.config

Patch0:		2.6.0-ksyms-add.patch
Patch1:		linux-2.6-version.patch
Patch2:		linux-2.6-biarch-build.patch
Patch3:		2.6.0-t9-acpi_osl-lkml.patch
Patch4:		linux-kbuild-extmod.patch
Patch5:		kernel-MAX_INIT_ARGS.patch

Patch10:	2.6.0-powernow-k7.patch

Patch12:	2.6.0-omnikeys.patch
Patch13:	2.6.1-rc2-VLAN-NS83820-lkml.patch
Patch14:	linux-2.6-omnibook-20040916.patch
Patch15:	linux-2.6-enable-broken-advansys.patch
Patch16:	linux-alpha-isa.patch
Patch17:	linux-fbcon-margins.patch

Patch19:	2.6.5-3C920b-Tornado.patch
Patch20:	2.6.5-i386-cmpxchg.patch
Patch21:	2.6.6-serial-fifo-lkml.patch

Patch25:	2.6.7-alpha_compile.patch
Patch26:	2.6.7-ppc-asm-defs.patch
Patch27:	linux-ppc-oops.patch
Patch28:	linux-2.6-sparc-ksyms.patch
Patch29:	linux-2.6-ppc-no-pc-serial.patch
Patch30:	2.6.x-TGA-fbdev-lkml.patch
Patch31:	linux-2.6-ppc-no-i8042.patch

# netfilter
Patch50:	linux-2.6-pom-ng-branch.diff

Patch52:	linux-2.6-esfq.patch
# http://www.linuximq.net/patchs/linux-2.6.9-imq1.diff
Patch53:	2.6.10-imq.patch
Patch54:	2.6.4-wrr.patch

# frpm http://www.ssi.bg/~ja/#routers
Patch56:	routes-2.6.12-12.diff
# http://developer.osdl.org/shemminger/skge/
Patch57:	linux-2.6-skge-0.5.patch
# http://www.edoceo.com/creo/inotify/
Patch58:	inotify-2.6.12.patch
# derived from http://www.syskonnect.com/syskonnect/support/driver/zip/linux/install-8_18.tar.bz2
Patch59:	linux-2.6-sk98lin-8.18.2.2.patch
# http://dev.gentoo.org/~spock/projects/gensplash/
Patch60:	fbsplash-0.9.2-r3-2.6.12-rc3.patch
# reserve dynamic minors for fbsplash and device mapper
Patch61:	linux-static-dev.patch
Patch62:	linux-2.6-lirc-0.7.patch
# http://ifp-driver.sourceforge.net/
Patch63:	iriverfs-r0.1.0.1.patch
Patch64:	squashfs2.1-patch
Patch65:	reiser4-2.6.12-mm1.patch
Patch66:	linux-2.6-alsa-1.0.9plus-20050622.patch

# http://tahoe.pl/patch.htm
Patch80:	http://www.tahoe.pl/drivers/tahoe9xx-2.6.4-5.patch
# psmouse extension for ThinkPad laptops from http://www.clarkson.edu/~evanchsa/
Patch81:	trackpoint-2.6.11.patch

# derived from http://ftp.kernel.org/pub/linux/kernel/people/lenb/acpi/patches/release/2.6.12/
Patch90:	acpi-20050408-2.6.12.diff

# http://www.kismetwireless.net/download.shtml#orinoco2611
Patch95:	orinoco-2.6.12-rfmon-dragorn-1.diff

Patch100:	linux-2.6-nvidia-pci-ids.patch
Patch101:	linux-2.6-pty-is-losing-bytes.patch
Patch102:	linux-2.6-smbfs.patch
Patch103:	linux-2.6-iriver-backing-device-capability-information-fix.patch
#Patch104:	linux-2.6-dst-cache-overflow.patch		NEEDS UPDATE
Patch105:	linux-2.6-net-sundance-ip100A-pciids.patch
Patch106:	linux-2.6-null-tty-driver-oops.patch
Patch107:	linux-2.6-sata-sil-mod15write-workaround.patch
Patch108:	linux-2.6-tty-races.patch
Patch109:	linux-2.6-jiffies-rounding.patch
Patch110:	linux-2.6-cputime-misscalculation.patch
Patch111:	linux-2.6-vfs-two-read-without-clear-between.patch
Patch112:	linux-2.6-via82c586-irq-routing.patch

# derived from http://adsl-brisbane.lubemobile.com.au/ras/debian/sarge/kernel-patch-linuxabi/
Patch135:	linux-2.6-unix-abi.patch

# derived from http://www.grsecurity.net/grsecurity-2.1.5-2.6.11.7-200504111924.patch.gz
Patch200:	grsecurity-2.1.5-2.6.11.7-200504111924.patch
# http://openmosix.snarc.org/files/releases/2.6/
# derived from openMosix-r570.patch
Patch201:	linux-2.6-omosix.patch
# vserver-2.0-pre4
Patch202:	linux-2.6-vs2.patch
# xen 2.0.6 http://www.cl.cam.ac.uk/Research/SRG/netos/xen/index.html
Patch203:	linux-xen-2.0.6.patch

Patch400:	kernel-gcc4.patch
Patch401:	kernel-hotfixes.patch
Patch402:	linux-em8300-2.6.11.2.patch

#from:
## http://www.kernel.org/pub/linux/kernel/people/gregkh/gregkh-2.6/gregkh-05-devfs/devfs-die-die-die.patch
Patch500:	devfs-die-die-die.patch

Patch502:	ocfs2-2005.06.17.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 2.14.90.0.7
BuildRequires:	diffutils
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
BuildRequires:	module-init-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.217
Autoreqprov:	no
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
PreReq:		geninitrd >= 2.57
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	module-info
Obsoletes:	kernel-modules
Obsoletes:	kernel-net-ipp2p
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	reiser4progs < %{_reiser4progs_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	PPP < %{_PPP_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	oprofile < %{_oprofile_ver}
%if %{with xen}
ExclusiveArch:	%{ix86}
%else
ExclusiveArch:	%{ix86} alpha %{x8664} ia64 ppc sparc sparc64
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

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
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
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	kernel-pcmcia = %{pcmcia_version}
Provides:	kernel(pcmcia)
Conflicts:	pcmcia-cs < %{_pcmcia_cs_ver}
Autoreqprov:	no

%description pcmcia
PCMCIA modules (%{pcmcia_version}).

%description pcmcia -l pl
Modu³y PCMCIA (%{pcmcia_version}).

%package sound-alsa
Summary:	ALSA kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description sound-alsa
ALSA (Advanced Linux Sound Architecture) sound drivers.

%description sound-alsa -l pl
Sterowniki d¼wiêku ALSA (Advanced Linux Sound Architecture).

%package sound-oss
Summary:	OSS kernel modules
Summary(pl):	Sterowniki d¼wiêku OSS
Group:		Base/Kernel
PreReq:		%{name}-up = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-up = %{epoch}:%{version}-%{release}
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
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
PreReq:		geninitrd >= 2.26
Provides:	kernel = %{epoch}:%{version}-%{release}
Provides:	kernel(netfilter) = %{_netfilter_snap}
Provides:	module-info
Obsoletes:	kernel-smp-net-ipp2p
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	PPP < %{_PPP_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
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

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
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
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Provides:	kernel-pcmcia = %{pcmcia_version}
Provides:	kernel(pcmcia)
Conflicts:	pcmcia-cs < %{_pcmcia_cs_ver}
Autoreqprov:	no

%description smp-pcmcia
PCMCIA modules for SMP kernel (%{pcmcia_version}).

%description smp-pcmcia -l pl
Modu³y PCMCIA dla maszyn SMP (%{pcmcia_version}).

%package smp-sound-alsa
Summary:	ALSA SMP kernel modules
Summary(pl):	Sterowniki d¼wiêku ALSA dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
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
PreReq:		%{name}-smp = %{epoch}:%{version}-%{release}
Requires(postun):	%{name}-smp = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description smp-sound-oss
OSS (Open Sound System) SMP sound drivers.

%description smp-sound-oss -l pl
Sterowniki OSS (Open Sound System) dla maszyn wieloprocesorowych.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra Linuksa
Group:		Base/Kernel
Provides:	kernel-headers(agpgart) = %{version}
Provides:	kernel-headers(reiserfs) = %{version}
Provides:	kernel-headers(bridging) = %{version}
Provides:	kernel-i2c-devel
Provides:	kernel-headers(netfilter) = %{_netfilter_snap}
Provides:	kernel-headers(alsa-drivers)
Provides:	kernel-headers = %{epoch}:%{version}-%{release}
Obsoletes:	kernel-i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel
or building kernel modules.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbêdne do rekompilacji j±dra
oraz budowania modu³ów j±dra.

%package module-build
Summary:	Development files for building kernel modules
Summary(pl):	Pliki s³u¿±ce do budowania modu³ów j±dra
Group:		Base/Kernel
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
Group:		Base/Kernel
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
Group:		Base/Kernel
Provides:	kernel-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê do j±dra Linuksa pochodz±c± z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{version}%{_rc}

%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch10 -p1

%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%patch19 -p1
%patch20 -p1
%patch21 -p1

%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
## %patch30 -p1 - broken or included in kernel
%patch31 -p1

%patch50 -p0
mv -f {,netfilter.}status

%patch52 -p1
%patch53 -p1
%patch54 -p1

%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1

%patch80 -p1
%patch81 -p1

%patch90 -p1
%patch95 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
#patch104 -p1		NEEDS UPDATE
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1

%ifarch %{ix86}
%patch135 -p1
%endif

%if %{with grsecurity}
echo Grsecurity not implemented
##patch200 -p1
%endif
%if %{with omosix}
%{__patch} -p1 -F3 < %{PATCH201}
%endif
%if %{with vserver}
%patch202 -p1
%endif
%if %{with xen}
%patch203 -p1
%endif

%patch400 -p1
%patch401 -p1
%if %{with em8300}
%patch402 -p1
%endif

# probably not needed
##%patch500 -p1
%patch502 -p1

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
    %ifarch i686 pentium3 pentium4
	sed -i 's:CONFIG_MATH_EMULATION=y:# CONFIG_MATH_EMULATION is not set:' $1
    %endif
    %if %{with regparm}
	sed -i 's:# CONFIG_REGPARM is not set:CONFIG_REGPARM=y:' $1
    %endif
    cat %{SOURCE95} >> $1
%endif
}

%if "%{_target_base_arch}" != "%{_arch}"
    CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
    export DEPMOD=/bin/true
    %if "%{_arch}" == "x86_64"
	%if "%{_target_base_arch}" == "i386"
	    CrossOpts="ARCH=%{_target_base_arch}"
	    unset DEPMOD
	%endif
    %endif
%else
    CrossOpts=""
%endif

%if %{with xen}
CrossOpts="ARCH=xen"
%define _main_target_base_arch	i386
%define _target_base_arch	xen
%endif

BuildConfig() {
	%{?debug:set -x}
	# is this a special kernel we want to build?
	smp=
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
	xen=
	%{?with_xen0:xen="0"}
	%{?with_xenU:xen="U"}
	if [ "$smp" = "yes" ]; then
		Config="%{_target_base_arch}$xen-smp"
	else
		Config="%{_target_base_arch}$xen"
	fi
	KernelVer=%{version}-%{release}$1
	echo "Building config file for KERNEL $1..."
	cat $RPM_SOURCE_DIR/kernel-$Config.config > arch/%{_target_base_arch}/defconfig
	TuneUpConfigForIX86 arch/%{_target_base_arch}/defconfig

%if %{with preemptive}
	sed -i 's:# CONFIG_PREEMPT is not set:CONFIG_PREEMPT=y:' arch/%{_target_base_arch}/defconfig
%endif

	cat %{SOURCE80} >> arch/%{_target_base_arch}/defconfig

%if %{with grsecurity}
	cat %{!?with_pax:%{SOURCE90}}%{?with_pax:%{SOURCE91}} >> arch/%{_target_base_arch}/defconfig
%endif
%if %{with omosix}
	cat %{SOURCE92} >> arch/%{_target_base_arch}/defconfig
%endif
%if %{with vserver}
	cat %{SOURCE93} >> arch/%{_target_base_arch}/defconfig
%endif
%if %{with em8300}
	cat %{SOURCE94} >> arch/%{_target_base_arch}/defconfig
%endif
##  ocfs2 config
	cat %{SOURCE96} >> arch/%{_target_base_arch}/defconfig

	ln -sf arch/%{_target_base_arch}/defconfig .config
	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
	rm -f include/linux/autoconf.h
%if %{with xen}
	%{__make} $CrossOpts oldconfig
%endif
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

%if %{with xen}
	%{__make} $CrossOpts oldconfig
%endif

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
%if %{with xen}
	install vmlinuz $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%else
	install arch/%{_target_base_arch}/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
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
%ifarch ppc
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch ia64
	gzip -cfv vmlinux > vmlinuz
	install -d $KERNEL_INSTALL_DIR/boot/efi
	install vmlinuz $KERNEL_INSTALL_DIR/boot/efi/vmlinuz-$KernelVer
	ln -sf efi/vmlinuz-$KernelVer $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
	%{__make} $CrossOpts modules_install \
		%{?with_verbose:V=1} \
     		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	[ -z $CrossOpts ] && \
	/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || echo
	[ ! -z $CrossOpts ] && \
	touch $KERNEL_INSTALL_DIR/modules.dep

	echo "KERNEL RELEASE $KernelVer DONE"

}

KERNEL_BUILD_DIR=`pwd`
echo "-%{release}" > localversion
install -m 644 %{SOURCE40} FAQ-pl

# UP KERNEL
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-UP"
rm -rf $KERNEL_INSTALL_DIR
BuildConfig
%{?with_up:BuildKernel}
%{?with_up:PreInstallKernel}
# SMP KERNEL
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/kernel-SMP"
rm -rf $KERNEL_INSTALL_DIR
%if !%{with xen}
BuildConfig smp
%{?with_smp:BuildKernel smp}
%{?with_smp:PreInstallKernel smp}
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

%if "%{_target_base_arch}" != "%{_arch}"
    CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
    export DEPMOD=/bin/true
    %if "%{_arch}" == "x86_64"
	%if "%{_target_base_arch}" == "i386"
	    CrossOpts="ARCH=%{_target_base_arch}"
	    unset DEPMOD
	%endif
    %endif
%else
    CrossOpts=""
%endif

%if %{with xen}
CrossOpts="ARCH=xen"
%define _main_target_base_arch	i386
%define _target_base_arch	xen
%endif

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

# ghosted initrd
touch $RPM_BUILD_ROOT/boot/initrd-%{version}-%{release}{,smp}.gz

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
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old
ln -sf initrd-%{version}-%{release}.gz %{initrd_dir}/initrd

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_grsecurity:grsecurity}%{?with_omosix:openMosix}%{?with_vserver:vserver}%{?with_xen0:Xen0}%{?with_xenU:XenU}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{version}-%{release}.gz --install %{version}-%{release} --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi

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
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz %{initrd_dir}/initrd

if [ -x /sbin/new-kernel-pkg ]; then
	if [ -f /etc/pld-release ]; then
		title=$(sed 's/^[0-9.]\+ //' < /etc/pld-release)
	else
		title='PLD Linux'
	fi

	ext='%{?with_grsecurity:grsecurity}%{?with_omosix:openMosix}%{?with_vserver:vserver}%{?with_xen0:Xen0}%{?with_xenU:XenU}'
	if [ "$ext" ]; then
		title="$title $ext"
	fi

	/sbin/new-kernel-pkg --initrdfile=%{initrd_dir}/initrd-%{version}-%{release}smp.gz --install %{version}-%{release}smp --banner "$title"
elif [ -x /sbin/rc-boot ]; then
	/sbin/rc-boot 1>&2 || :
fi

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
%doc FAQ-pl
%ifarch alpha ppc
/boot/vmlinux-%{version}-%{release}
%endif
%ifarch sparc sparc64
/boot/vmlinux-%{version}-%{release}
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
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/kernel/abi
%endif
%ifnarch ppc sparc
/lib/modules/%{version}-%{release}/kernel/arch
%endif
/lib/modules/%{version}-%{release}/kernel/crypto
/lib/modules/%{version}-%{release}/kernel/drivers
/lib/modules/%{version}-%{release}/kernel/fs
/lib/modules/%{version}-%{release}/kernel/lib
/lib/modules/%{version}-%{release}/kernel/net
/lib/modules/%{version}-%{release}/kernel/security
%dir /lib/modules/%{version}-%{release}/kernel/sound
/lib/modules/%{version}-%{release}/kernel/sound/soundcore.*
%dir /lib/modules/%{version}-%{release}/misc
%ifnarch sparc sparc64
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko*
%endif
%ifnarch sparc sparc64
#drm stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%ifnarch sparc sparc64
%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif

%ifnarch sparc sparc64
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{version}-%{release}/kernel/drivers/serial/serial_cs.ko*
%endif

%files sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound
%exclude %dir /lib/modules/%{version}-%{release}/kernel/sound
%exclude /lib/modules/%{version}-%{release}/kernel/sound/soundcore.*
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/sound/oss
%endif

%ifnarch sparc sparc64
%files sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/sound/oss
%endif
%endif			# %%{with up}

%if %{with smp}
%files smp
%defattr(644,root,root,755)
%doc FAQ-pl
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
%ifarch ia64
/boot/efi/vmlinuz-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%ghost /boot/initrd-%{version}-%{release}smp.gz
%dir /lib/modules/%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp/kernel
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/kernel/abi
%endif
%ifnarch ppc sparc
/lib/modules/%{version}-%{release}smp/kernel/arch
%endif
/lib/modules/%{version}-%{release}smp/kernel/crypto
/lib/modules/%{version}-%{release}smp/kernel/drivers
/lib/modules/%{version}-%{release}smp/kernel/fs
/lib/modules/%{version}-%{release}smp/kernel/lib
/lib/modules/%{version}-%{release}smp/kernel/net
/lib/modules/%{version}-%{release}smp/kernel/security
%dir /lib/modules/%{version}-%{release}smp/kernel/sound
/lib/modules/%{version}-%{release}smp/kernel/sound/soundcore.*
%dir /lib/modules/%{version}-%{release}smp/misc
%ifnarch sparc sparc64
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko*
%endif
%ifnarch sparc sparc64
#drm stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*

%ifnarch sparc sparc64
%files smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif

%ifnarch sparc sparc64
%files smp-pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/parport_cs.ko*
/lib/modules/%{version}-%{release}smp/kernel/drivers/serial/serial_cs.ko*
%endif

%files smp-sound-alsa
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound
%exclude %dir /lib/modules/%{version}-%{release}smp/kernel/sound
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/soundcore.*
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/oss
%endif

%ifnarch sparc sparc64
%files smp-sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound/oss
%endif
%endif			# %%{with smp}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%if !%{with xen}
%{_prefix}/src/linux-%{version}/config-smp
%endif
%{_prefix}/src/linux-%{version}/config-up

%files module-build
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/localversion
%dir %{_prefix}/src/linux-%{version}/arch
%dir %{_prefix}/src/linux-%{version}/arch/*
%{_prefix}/src/linux-%{version}/arch/*/Makefile*
%dir %{_prefix}/src/linux-%{version}/arch/*/kernel
%{_prefix}/src/linux-%{version}/arch/*/kernel/Makefile
%{_prefix}/src/linux-%{version}/arch/*/kernel/asm-offsets.*
%{_prefix}/src/linux-%{version}/arch/*/kernel/sigframe.h
%dir %{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/scripts/Makefile*
%{_prefix}/src/linux-%{version}/scripts/basic
%{_prefix}/src/linux-%{version}/scripts/mod
%{_prefix}/src/linux-%{version}/scripts/*.c
%{_prefix}/src/linux-%{version}/scripts/*.sh

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%if %{with source}
%files source
%defattr(644,root,root,755)
%ifarch %{ix86}
%{_prefix}/src/linux-%{version}/abi
%endif
%{_prefix}/src/linux-%{version}/arch/*/[!Mk]*
%{_prefix}/src/linux-%{version}/arch/*/kernel/[!M]*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/asm-offsets.*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/sigframe.h
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%if %{with grsecurity}
%{_prefix}/src/linux-%{version}/grsecurity
%endif
%if %{with omosix}
%{_prefix}/src/linux-%{version}/hpc
%endif
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts/*
%exclude %{_prefix}/src/linux-%{version}/scripts/Makefile*
%exclude %{_prefix}/src/linux-%{version}/scripts/basic
%exclude %{_prefix}/src/linux-%{version}/scripts/mod
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
