#
# SEE PLD-doc/maintainers file before you edit this file!!
#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# TODO:
#		- check I2C
#		- fix lirc_sasem (usb api)
#		- update HP-OmniBook patchset (2.6.1-all-in-1.patch)
#		- reiserfs4
#		- update grsecurity patch
#		- update i2o patchset
#		- update software suspend patch
#		- add distcc support (and don't break crossbuild!)
#
# Conditional build:
%bcond_without	BOOT		# don't build BOOT kernel
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	source		# don't build kernel-source package
%bcond_without	grsec		# build without grsec
%bcond_with	pax		# enable PaX
%bcond_with	execshield	# build without exec-shield
%bcond_with	pramfs		# build pramfs support (EXPERIMENTAL)
%bcond_with	verbose		# verbose build (V=1)
%bcond_with	preemptive	# build preemptive kernel
%bcond_with	fbsplash	# build with fbsplash
%bcond_with	swsuspend	# build with software suspend v2 (EXPERIMENTAL)

%{?debug:%define with_verbose 1}

# see TODO
%if %{with grsec}
%undefine	with_grsec
%endif

%if !%{with grsec}
%undefine	with_pax
%endif

%ifarch sparc
# sparc32 is missing important updates from 2.5 cycle - won't build
%undefine	with_smp
%endif
%ifarch ia64
# broken
%undefine	with_up
%endif

%ifarch i586 i686 pentium3 pentium4 athlon
%undefine	with_BOOT
%endif
# temporary as BOOT is not finished yet
%undefine	with_BOOT

## Program required by kernel to work.
%define		_binutils_ver		2.12
%define		_util_linux_ver		2.10o
%define		_module_init_tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_xfsprogs_ver		2.6.0
%define		_pcmcia_cs_ver		3.1.21
%define		_quota_tools_ver	3.09
%define		_PPP_ver		2.4.0
%define		_isdn4k_utils_ver	3.1pre1
%define		_nfs_utils_ver		1.0.5
%define		_procps_ver		3.2.0
%define		_oprofile_ver		0.5.3

#define		_post_ver	.1
%define		_post_ver	%{nil}
%define		_rel		0.21
%define		_cset		20040913_2305
%define		_apply_cset	1

%define		_netfilter_snap		20040629

%define		_enable_debug_packages			0
%define		no_install_post_strip			1
%define		no_install_post_chrpath			1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0
#define		pwc_version		9.0.2

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel
Version:	2.6.9%{_post_ver}
Release:	%{_rel}
Epoch:		3
License:	GPL
Group:		Base/Kernel
#define		_rc	%{nil}
%define		_rc	-rc2
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/linux-%{version}%{_rc}.tar.bz2
# Source0-md5:	b3d4a5c384d56ab974d1ac864b995ac4
#Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}%{_rc}.tar.bz2
Source1:	%{name}-autoconf.h
#Source2:	http://www.smcc.demon.nl/webcam/pwc-%{pwc_version}.tar.gz
Source4:	http://ftp.kernel.org/pub/linux/kernel/v2.6/testing/cset/cset-%{_cset}.txt.bz2
# Source4-md5:	3d47b367d32efe0d3031b8091cb42346

Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-x86_64.config
Source23:	%{name}-x86_64-smp.config
Source24:	%{name}-sparc.config
Source25:	%{name}-sparc-smp.config
Source26:	%{name}-sparc64.config
Source27:	%{name}-sparc64-smp.config
Source28:	%{name}-alpha.config
Source29:	%{name}-alpha-smp.config
Source30:	%{name}-ppc.config
Source31:	%{name}-ppc-smp.config
Source32:	%{name}-ia64.config
Source33:	%{name}-ia64-smp.config

Source40:	%{name}.FAQ-pl

Source80:	%{name}-netfilter.config
Source90:	%{name}-grsec.config
Source91:	%{name}-grsec+pax.config

Patch0:		2.6.0-ksyms-add.patch

Patch2:		2.6.0-t6-usb-irq.patch
Patch3:		2.6.0-t7-memleak-lkml.patch
Patch4:		2.6.0-t7-memleak2-lkml.patch
#Patch5:	2.6.0-t8-swap-include-lkml.patch
Patch6:		2.6.0-t8-VLSI-ix86-lkml.patch

Patch8:		2.6.0-t8-umsdos-lkml.patch
Patch9:		2.6.0-t9-acpi_osl-lkml.patch

#Patch11:	2.6.8.1-qos-and-routing-conflict.patch	-- obsolete
Patch12:	2.6.1-rc2-VLAN-NS83820-lkml.patch
Patch13:	2.6.2-Initio9100U-Kconfig.patch
# http://www.consultmatt.co.uk/downloads/patches/kernel/2.6/
Patch14:	2.6.1-all-in-1.patch

Patch16:	linux-alpha-isa.patch
Patch17:	2.6.4-psion-5mx.patch
Patch18:	2.6.5-sparc64-missing-include.patch
Patch19:	2.6.5-3C920b-Tornado.patch
Patch20:	2.6.5-i386-cmpxchg.patch
Patch21:	2.6.6-serial-fifo-lkml.patch
Patch22:	2.6.6-qsort-updated-lkml.patch
Patch23:	2.6.6-xfs-qsort-lkml.patch
#Patch24:	2.6.7-bridge_sysfs-lkml.patch
Patch25:	2.6.7-alpha_compile.patch
Patch26:	2.6.7-ppc-asm-defs.patch

Patch28:	2.6.7-ppc-ipr-div.patch

#Patch30:	2.6.x-ppp_mppe.patch
#Patch31:	2.6.x-SGI_VW-fbdev-lkml.patch	-- obsolete
Patch32:	2.6.x-TGA-fbdev-lkml.patch
Patch33:	linux-kbuild-extmod.patch
Patch34:	2.6.8-cpu_feature.patch

# framebuffer fixes
Patch41:	linux-fbcon-margins.patch

# netfilter
Patch50:	2.6.7-pom-ng-%{_netfilter_snap}.patch
# http://www.barbara.eu.org/~quaker/ipt_account/
Patch51:	2.6.6-ipt_account.patch
# http://l7-filter.sourceforge.net/
Patch52:	2.6.8-ipt_layer7.patch
Patch53:	2.6.4-rc1-01-esfq-imq.patch
Patch54:	2.6.4-rc1-02-imq-nat-support.patch
Patch55:	2.6.4-wrr.patch
Patch56:	linux-2.6-netfilter-syms.patch

# pseudo terminal fix for older glibc
#Patch60:	%{name}-pts.patch
Patch61:	%{name}-MAX_INIT_ARGS.patch

# http://tahoe.pl/patch.htm
Patch70:	http://www.tahoe.pl/drivers/tahoe9xx-2.6.4-5.patch

# Spock discontinued porting bootsplash to new kernel versions
# but he introduced a rewrite of bootsplash called gensplash.
# http://dev.gentoo.org/~spock/projects/gensplash/
Patch72:	fbsplash-0.9-r7-2.6.9-rc1.patch
Patch73:	squashfs2.0-patch
# http://dl.sourceforge.net/pramfs/
Patch74:	pramfs-2.6.4.patch
Patch75:	ftp://ftp.kernel.org/pub/linux/kernel/people/mbligh/patches/2.6.6-rc3/2.6.6-rc3-mjb1/350-autoswap
# http://lirc.sourceforge.net/software/snapshots/lirc-0.7.0pre7.tar.bz2
Patch76:	2.6.8-lirc-0.7.0-pre7.patch
# http://i2o.shadowconnect.com/
# NEEDS UPDATE
Patch77:	2.6.8-i2o-build_105.patch.gz
Patch78:	i2o-build_105-fixes.patch

# derived from official grsecurity-2.0.1-2.6.7.patch
# NEEDS UPDATE
Patch90:	%{name}-grsec-2.0.1.patch

# http://lkml.org/lkml/2004/6/2/233
Patch91:	http://people.redhat.com/mingo/exec-shield/exec-shield-nx-2.6.7-A0
Patch92:	exec-shield-make-peace-with-grsecurity.patch

# frpm http://www.ssi.bg/~ja/#routers
#Patch100:	00_static_routes-2.6.0-test1-8.diff
#Patch101:	01_alt_routes-2.5.50-8.diff
#Patch102:	01_arp_prefsrc-2.5.50-5.diff <- not applied. needs checkout
#Patch103:	05_nf_reroute-2.6.7-10.diff

# http://sources.redhat.com/cluster/
# NEED UPDATE
#Patch200:	linux-cluster-cman.patch
#Patch201:	linux-cluster-dlm.patch
#Patch202:	linux-cluster-gfs.patch
#Patch203:	linux-cluster-gnbd.patch

# suspend/resume
# http://softwaresuspend.berlios.de/
Patch219:	linux-2.6-software-suspend-2.0.0.105.patch.gz
Patch220:	linux-2.6-via-agpc-resume-suspend-support.patch

# hotfixes
Patch300:	linux-2.6-sparc-ksyms.patch
Patch301:	linux-2.6-ppc-ksyms.patch
Patch302:	2.6.7-kill-warnings.patch
Patch303:	%{name}-hotfixes.patch

URL:		http://www.kernel.org/
BuildRequires:	binutils >= 2.14.90.0.7
BuildRequires:	diffutils
%ifarch sparc sparc64
BuildRequires:	elftoaout
%endif
BuildRequires:	module-init-tools
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.153
Autoreqprov:	no
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
PreReq:		geninitrd >= 2.57
Provides:	%{name}-up = %{epoch}:%{version}-%{release}
Provides:	module-info
Provides:	%{name}(netfilter) = %{_netfilter_snap}
Obsoletes:	kernel-modules
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
ExclusiveArch:	%{ix86} alpha amd64 ia64 ppc sparc sparc64
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
Provides:	%{name}-drm = %{drm_xfree_version}
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
Provides:	%{name}-pcmcia = %{pcmcia_version}
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
Provides:	alsa-driver
Obsoletes:	alsa-driver
Obsoletes:	alsa-driver-up
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
Provides:	%{name} = %{epoch}:%{version}-%{release}
Provides:	module-info
Provides:	%{name}(netfilter) = %{_netfilter_snap}
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
Provides:	%{name}-drm = %{drm_xfree_version}
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
Provides:	%{name}-pcmcia = %{pcmcia_version}
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
Provides:	alsa-driver
Obsoletes:	alsa-driver
Obsoletes:	alsa-driver-smp
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

%package module-build
Summary:	Development files for building kernel modules
Summary(pl):	Pliki s³u¿±ce do budowania modu³ów j±dra
Group:		Base/Kernel
Requires:	%{name}-headers = %{epoch}:%{version}-%{release}
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
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê do j±dra Linuksa pochodz±c± z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{version}%{_rc}

%if "%{_apply_cset}" != "0"
bzcat %{SOURCE4} | patch -p1 -s
%endif

%patch0 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p1
#patch5 -p1
%patch6 -p1

%patch8 -p1
%patch9 -p1

%patch12 -p1
%patch13 -p1
%patch14 -p1

%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
#patch24 -p1
%patch25 -p1
%patch26 -p1

#patch30 -p1

%patch32 -p1
%patch33 -p1

%patch41 -p1

# netfilter
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1

#patch60 -p1
%patch61 -p1

%patch70 -p1

%if %{with fbsplash}
%patch72 -p1
%endif
%patch73 -p1
%if %{with parmfs}
%patch74 -p1
%endif
%patch75 -p1
%patch76 -p1
# see TODO
#patch77 -p1
#patch78 -p1

#cp -f pwc-%{pwc_version}/2.6/pwc* drivers/usb/media
rm -rf pwc-%{pwc_version}

#grsec
%ifarch alpha %{ix86} ia64 ppc sparc sparc64 amd64
%if %{with grsec}
# see TODO
#patch90 -p1
%endif
%endif

%if %{with execshield}
install %{PATCH91} exec-shield.patch
%if %{with grsec}
patch -s exec-shield.patch < %{PATCH92}
%endif
patch -p1 -s < exec-shield.patch
%endif

# routers
#patch100 -p1
#patch101 -p1
#patch102 -p1 # <- not applayed need checkout
#patch103 -p1

# cluster
#patch200 -p1
#patch201 -p1
#patch202 -p1
#patch203 -p1

# suspend/resume
%if %{with swsuspend}
%ifarch %{ix86}
%patch219 -p1
%endif
%patch220 -p1
%endif

# hotfixes
%patch300 -p1
%patch301 -p1
%patch302 -p1
%patch303 -p1

# Fix EXTRAVERSION in main Makefile
sed -i 's#EXTRAVERSION =.*#EXTRAVERSION =#g' Makefile

sed -i 's:\-pipe::' arch/*/Makefile

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
%endif
}

%if "%{_target_base_arch}" != "%{_arch}"
CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
%else
CrossOpts=""
%endif

BuildConfig (){
	%{?_debug:set -x}
	# is this a special kernel we want to build?
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
	if [ "$smp" = "yes" ]; then
		Config="%{_target_base_arch}-smp"
	else
		Config="%{_target_base_arch}"
	fi
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi
	echo "Building config file for KERNEL $1..."
	cat $RPM_SOURCE_DIR/kernel-$Config.config > arch/%{_target_base_arch}/defconfig
	TuneUpConfigForIX86 arch/%{_target_base_arch}/defconfig

%if %{with preemptive}
	sed -i 's:# CONFIG_PREEMPT is not set:CONFIG_PREEMPT=y:' arch/%{_target_base_arch}/defconfig
%endif

#	netfilter	
	cat %{SOURCE80} >> arch/%{_target_base_arch}/defconfig
#	grsecurity
%if !%{with pax}
	cat %{SOURCE90} >> arch/%{_target_base_arch}/defconfig
%else
	cat %{SOURCE91} >> arch/%{_target_base_arch}/defconfig
%endif

	ln -sf arch/%{_target_base_arch}/defconfig .config
	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
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

ConfigBOOT()
{
	Config="%{_target_base_arch}"
	cat $RPM_SOURCE_DIR/kernel-$Config.config > arch/%{_target_base_arch}/defconfig
%ifarch i386
	echo "CONFIG_M386=y" >> arch/%{_target_base_arch}/defconfig
%endif
%ifarch i486
	echo "CONFIG_M486=y" >> arch/%{_target_base_arch}/defconfig
%endif
%ifarch i386 i486 i586
	sed -i 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/%{_target_base_arch}/defconfig
%endif
	cat <<EOF >>arch/%{_target_base_arch}/defconfig
	# CONFIG_APM is not set
	# CONFIG_ACPI is not set
	# CONFIG_ACPI_BOOT is not set
	# CONFIG_MTD is not set
	# CONFIG_NETFILTER is not set
	# CONFIG_WAN is not set
	# CONFIG_ATM is not set
	# CONFIG_HOTPLUG_PCI is not set
	# CONFIG_NET_SCHED is not set
	# CONFIG_X86_MCE is not set
	# CONFIG_MTRR is not set
	# CONFIG_PM is not set
	# CONFIG_CPU_FREQ is not set
	# CONFIG_DRM is not set
	# CONFIG_FTAPE is not set
	# CONFIG_WATCHDOG is not set
	# CONFIG_DVB is not set
	# CONFIG_DVB_CORE is not set
	# CONFIG_VIDEO_DEV is not set
	# CONFIG_SECURITY is not set
	# CONFIG_SOUND is not set
	# CONFIG_USB_AUDIO is not set
	# CONFIG_INPUT_JOYSTICK is not set
	# CONFIG_OMNIBOOK is not set
	# CONFIG_NET_RADIO is not set
	# CONFIG_HOTPLUG is not set
	# CONFIG_QUOTA is not set
	# CONFIG_REGPARM is not set
	# CONFIG_SCSI_LOGGING is not set
	CONFIG_PACKET=m
	CONFIG_UNIX=m
	# CONFIG_DEV_APPLETALK is not set
	# CONFIG_ECONET_AUNUDP is not set
	# CONFIG_HIPPI is not set
	# CONFIG_TR is not set
	# CONFIG_INPUT_MISC is not set
	# CONFIG_INPUT_TOUCHSCREEN is not set
	# CONFIG_PROFILING is not set
	# CONFIG_DEBUG_KERNEL is not set
	# CONFIG_DEBUG_SPINLOCK_SLEEP is not set
	# CONFIG_FRAME_POINTER is not set
	# CONFIG_LBD is not set
	# CONFIG_SLIP is not set
	# CONFIG_PPP is not set
	# CONFIG_PLIP is not set
	# CONFIG_FDDI is not set
	# CONFIG_HAMRADIO is not set
	# CONFIG_NETPOLL_RX is not set
	# CONFIG_NETPOLL_TRAP is not set
	# CONFIG_FB is not set
EOF
	ln -sf arch/%{_target_base_arch}/defconfig .config

	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
	%{__make} $CrossOpts include/linux/autoconf.h
	if [ "$smp" = "yes" ]; then
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h
	else
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h
	fi
}

BuildKernel() {
	%{?_debug:set -x}
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
	%{__make} image \
		%{?with_verbose:V=1}

	%{__make} modules \
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

PreInstallKernel (){
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
	if [ "$smp" = "yes" ]; then
		Config="%{_target_base_arch}-smp"
	else
		Config="%{_target_base_arch}"
	fi
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86} amd64
	install arch/%{_target_base_arch}/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
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
#?	install vmlinux $KERNEL_INSTALL_DIR/boot/efi/vmlinux-$KernelVer
	install vmlinuz $KERNEL_INSTALL_DIR/boot/efi/vmlinuz-$KernelVer
	ln -sf efi/vmlinuz-$KernelVer $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
	%{__make} $CrossOpts modules_install \
		%{?with_verbose:V=1} \
     		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer

	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || echo

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

%if %{with BOOT}
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR/build-done/BOOT"
rm -rf $KERNEL_INSTALL_DIR
ConfigBOOT
BuildKernel BOOT
PreInstallKernel BOOT
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022
%if "%{_target_base_arch}" != "%{_arch}"
CrossOpts="ARCH=%{_target_base_arch} CROSS_COMPILE=%{_target_cpu}-pld-linux-"
%else
CrossOpts=""
%endif

install -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
install -d $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}{,smp}/misc

install %{SOURCE40} FAQ-pl

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

find . ! -name "build-done" ! -name "." -maxdepth 1 -exec cp -a "{}" "$RPM_BUILD_ROOT/usr/src/linux-%{version}/" ";"

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

%{__make} $CrossOpts mrproper \
	RCS_FIND_IGNORE='-name build-done -prune -o'
find -name "*~" -exec rm -f "{}" ";"
find -name "*.orig" -exec rm -f "{}" ";"

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/include/linux/autoconf-up.h \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-UP/usr/src/linux-%{version}/config-up \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
fi

if [ -e $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h ]; then
install $KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/include/linux/autoconf-smp.h \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
install	$KERNEL_BUILD_DIR/build-done/kernel-SMP/usr/src/linux-%{version}/config-smp \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
fi

%if %{with up} || %{with smp}
# UP or SMP
install $KERNEL_BUILD_DIR/build-done/kernel-*/usr/src/linux-%{version}/include/linux/* \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux
%endif

%{__make} $CrossOpts mrproper
%{__make} $CrossOpts include/linux/version.h
install %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/include/linux/autoconf.h

%clean
rm -rf $RPM_BUILD_ROOT

%preun
rm -f /lib/modules/%{version}-%{release}/modules.*

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

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
%depmod %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old
ln -sf initrd-%{version}-%{release}.gz %{initrd_dir}/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%postun
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f %{initrd_dir}/initrd-%{version}-%{release}.gz

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

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}
%depmod %{version}-%{release}smp

/sbin/geninitrd -f --initrdfs=rom %{initrd_dir}/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f %{initrd_dir}/initrd %{initrd_dir}/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz %{initrd_dir}/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%postun smp
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f %{initrd_dir}/initrd-%{version}-%{release}smp.gz

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
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
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
%ifnarch sparc sparc64
#oss sound stuff
%exclude /lib/modules/%{version}-%{release}/kernel/sound/oss
%endif
#alsa sound stuff
%exclude /lib/modules/%{version}-%{release}/kernel/sound/core
%exclude /lib/modules/%{version}-%{release}/kernel/sound/drivers
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/sound/i2c
%exclude /lib/modules/%{version}-%{release}/kernel/sound/isa
%exclude /lib/modules/%{version}-%{release}/kernel/sound/pci
%exclude /lib/modules/%{version}-%{release}/kernel/sound/synth
%exclude /lib/modules/%{version}-%{release}/kernel/sound/usb
%endif
%ifarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/sound/sparc
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
/lib/modules/%{version}-%{release}/kernel/sound/core
/lib/modules/%{version}-%{release}/kernel/sound/drivers
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}/kernel/sound/i2c
/lib/modules/%{version}-%{release}/kernel/sound/isa
/lib/modules/%{version}-%{release}/kernel/sound/pci
/lib/modules/%{version}-%{release}/kernel/sound/synth
/lib/modules/%{version}-%{release}/kernel/sound/usb
%endif
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}/kernel/sound/sparc
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
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
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
%ifnarch sparc sparc64
#oss sound stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/oss
%endif
#alsa sound stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/core
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/drivers
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/i2c
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/isa
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/pci
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/synth
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/usb
%endif
%ifarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/sound/sparc
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
/lib/modules/%{version}-%{release}smp/kernel/sound/core
/lib/modules/%{version}-%{release}smp/kernel/sound/drivers
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}smp/kernel/sound/i2c
/lib/modules/%{version}-%{release}smp/kernel/sound/isa
/lib/modules/%{version}-%{release}smp/kernel/sound/pci
/lib/modules/%{version}-%{release}smp/kernel/sound/synth
/lib/modules/%{version}-%{release}smp/kernel/sound/usb
%endif
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}smp/kernel/sound/sparc
%endif

%ifnarch sparc sparc64
%files smp-sound-oss
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/sound/oss
%endif
%endif			# %%{with smp}

%if %{with BOOT}
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
%endif				# %%{with BOOT}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_prefix}/src/linux-%{version}/config-smp
%{_prefix}/src/linux-%{version}/config-up

%files module-build
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Makefile
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
#%%{_prefix}/src/linux-%{version}/netfilter-patch-o-matic

%if %{with source}
%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch/*/[!Mk]*
%{_prefix}/src/linux-%{version}/arch/*/kernel/[!M]*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/asm-offsets.*
%exclude %{_prefix}/src/linux-%{version}/arch/*/kernel/sigframe.h
%{_prefix}/src/linux-%{version}/cluster
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%if %{with grsec}
%{_prefix}/src/linux-%{version}/grsecurity
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
