#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# _without_grsec	- build kernel without grsecurity patch
# _with_preemptible	- build with Preemptible patch
# _with_o1_sched	- build with new O(1) scheduler
# _with_acpi		- build with acpi support
# _without_smp		- don't build SMP kernel
# _without_up		- don't build UP kernel
#
%define		test_build		0
%define		krelease		2.45
#
%define base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')
#
%define		pre_version		pre1
%define		ipvs_version		1.0.0
%define		freeswan_version	1.97
%define		wlan_version		0.1.13
%define		sym_ncr_version		sym-1.7.3c-ncr-3.4.3b
%define		IPperson_version	20020427-2.4.18
%define		grsec_version		1.9.4-2.4.18
%define		aic_version		6.2.3-2.4.7
%define		jfs_version		2.4-1.0.18
%define		lvm_version		1.0.4
%define		evms_version		1.0.1
%define		tridentfb_version	0.7.0
%define		ntfs_version		2.0.7d	
%define		drm_xfree_version	4.2.0
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.4.18
Release:	%{krelease}%{?_with_preemptible:_pr}%{?_with_o1_sched:_o1}%{?_with_acpi:_acpi}
License:	GPL
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-140.tar.gz
Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
# Don't use following patch, it may hang the NIC (baggins)
#Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.4.0-test3-fore200e-0.2g.tar.gz
# based on cvs cvs@pserver.samba.org:/cvsroot netfilter
Source7:	netfilter-15042002.tar.gz
Source10:	ftp://ftp.linux-wlan.org/pub/linux-wlan-ng/linux-wlan-ng-%{wlan_version}.tar.gz
# new -> ftp://ftp.tux.org/pub/roudier/drivers/portable/sym-2.1.x/sym-2.1.16-20011028.tar.gz
Source11:	ftp://ftp.tux.org/pub/people/gerard-roudier/drivers/linux/stable/%{sym_ncr_version}.tar.gz
Source12:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source13:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-%{jfs_version}.tar.gz
Source14:	http://www.xfree86.org/~alanh/linux-drm-%{drm_xfree_version}-kernelsource.tar.gz
Source20:	%{name}-ia32.config
Source21:	%{name}-ia32-smp.config
Source50:	%{name}-sparc.config
Source51:	%{name}-sparc-smp.config
Source60:	%{name}-sparc64.config
Source61:	%{name}-sparc64-smp.config
Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config
Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config
Source1001:	%{name}-abi.config
Source1002:	%{name}-addon.config
Source1003:	%{name}-netfilter.config
Source1004:	%{name}-ipvs.config
Source1666:	%{name}-grsec.config
Source1667:	%{name}-int.config
Source1999:	%{name}-preemptive.config

# New features

Patch0:		%{name}-pldfblogo.patch
# from ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/patch-int-2.4.3.1.gz
Patch1:		patch-int-%{version}.1.bz2
# from ftp://ftp.xs4all.nl/pub/crypto/freeswan/freeswan-*
Patch2:		linux-%{version}-freeswan-%{freeswan_version}.patch.gz
# from  http://home.sch.bme.hu/~cell/br2684/dist/010402/br2684-against2.4.2.diff
Patch4:		br2684-against2.4.17.diff
# from ftp://linux-xfs.sgi.com/projects/xfs/download/patches/
Patch5:		linux-2.4.18-xfs-20020517.patch.gz
# from ftp://ftp.kernel.org/pub/linux/kernel/people/sct/ext3/v2.4/
Patch6:		linux-2.4.18-ext3-0.9.18.patch
# Homepage of ABI:	http://linux-abi.sourceforge.net/
# from ftp://ftp.kernel.org/pub/linux/kernel/people/hch/linux-abi/v2.4/linux-abi-2.4.15.0.patch.bz2 
Patch7:		linux-abi-2.4.17.0.patch.bz2
Patch8:		http://www.uow.edu.au/~andrewm/linux/cpus_allowed.patch
# from http://grsecurity.net/grsecurity-%{grsec_version}.patch
Patch9:		grsecurity-%{grsec_version}.patch
# Preemptive kernel  patch
Patch10:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/preempt-kernel/v2.4/preempt-%{name}-rml-%{version}-4.patch

Patch11:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/netdev-random/v2.4/netdev-random-core-rml-%{version}-1.patch
Patch12:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/netdev-random/v2.4/netdev-random-drivers-rml-%{version}-1.patch
Patch13:	http://www.linuxvirtualserver.org/software/kernel-2.4/linux-%{version}-ipvs-%{ipvs_version}.patch.gz
Patch14:	http://people.redhat.com/mingo/O(1)-scheduler/sched-O1-2.4.18-pre8-K3.patch

Patch15:	http://luxik.cdi.cz/~devik/qos/htb/v2/htb2_2.4.17.diff

# from ftp://ftp.kernel.org/pub/linux/kernel/people/dwmw2/linux-2.4.19-shared-zlib.bz2
Patch16:	linux-2.4.19-shared-zlib.bz2
Patch17:	%{name}-gcc31.patch
Patch18:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-%{version}-patch
Patch19:	http://unc.dl.sourceforge.net/sourceforge/linux-ntfs/linux-2.4.18-ntfs-%{ntfs_version}.patch.bz2

Patch20:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/preempt-kernel/v2.4/ingo-O1-sched/preempt-%{name}-rml-%{version}-rc1-ingo-K3-1.patch

Patch21:	linux-2.4.18-hpfs.patch

# ftp://ftp.samba.org/pub/unpacked/ppp/linux/mppe/
Patch22:	linux-2.4.18-mppe.patch

# Assorted bugfixes

# from LKML
Patch100:	linux-scsi-debug-bug.patch
Patch101:	linux-2.4.2-raw-ip.patch
Patch102:	PCI_ISA_bridge.patch
Patch103:	linux-2.4.2-nvram-hdd.patch
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch105:	linux-2.4.2-pcnet-parms.patch
Patch106:	http://www.kernel.org/pub/linux/kernel/people/hedrick/ide-%{version}/ide.%{version}-rc1.02152002.patch.bz2
Patch107:	linux-reiserfs-rename.patch
Patch108:	linux-alpha-nfs-2.4.2.patch
Patch109:	linux-2.4-string.patch
# raid5 xor fix for PIII/P4, should go away shortly
Patch110:	linux-2.4.0-raid5xor.patch
# disable some networking printk's
Patch111:	linux-2.4.1-netdebug.patch
# SCSI Reset patch for clustering stuff
Patch112:	linux-2.4.1-scsi-reset.patch
# Add an ioctl to the block layer so we can be EFI compliant
Patch113:	linux-2.4.2-blkioctl-sector.patch
# fix lun probing on multilun RAID chassis
Patch115:	linux-2.4.12-scsi_scan.patch
# fix pcnet32 networkdriver load vs ifconfig races
Patch116:	linux-2.4.3-pcnet32.patch
# fix rawio
Patch117:	linux-2.4.3-rawio.patch
Patch120:	linux-2.4.10-aironet.patch
Patch121:	linux-2.4.10-cpqfc.patch
# Created from lvm.tgz:LVM/PATCHES by doing make
Patch122:	lvm-%{lvm_version}-%{version}.patch.gz
# fixed xquad_portio
Patch123:	xquad_portio.fix
# 
Patch124:	linux-proc_net_dev-counter-fix.patch
Patch125:	01-sigxfs-vs-blkdev.patch
Patch126:	linux-2.4.18-SPARC64-ide.h-fix.patch
Patch127:	%{name}-2.4.18-SPARC64-PLD.patch
Patch128:	linux-AXP.patch
Patch129:	%{name}-Makefile-include-fix.patch
Patch130:	%{name}-2.4.17-netsyms-export-fix.patch
Patch131:	%{name}-2.4.18-personality.patch

Patch132:	linux-2.4.18.secfix.patch
Patch133:	linux-2.4.18-netsyms-fix.patch

Patch134:	linux-2.4.12-riva-ppc.patch.bz2
Patch135:	linux-2.4.18-pre4-agp_uninorth-ppc.patch.bz2

# EVMS support (http://www.sourceforge.net/projects/evms/)
Patch136:	evms-%{evms_version}-linux-2.4.patch
Patch137:	evms-linux-2.4.18-common-files.patch

# 
Patch138:	http://www.cymes.de/members/joker/projects/kernel/pbbuttons.patch

# from http://www.drfruitcake.com/linux/dma-bp.html
Patch139:	http://www.uwsg.iu.edu/hypermail/linux/kernel/0201.2/att-1802/01-neofb-0.3.1-linux-2.4.18-pre6.patch

# from http://prdownloads.sourceforge.net/tridentfb/tridentfb-%{tridentfb_version}.tgz 
Patch140:	linux-2.4.18-tridentfb.patch
Patch141:	linux-tulip-vlan.patch
Patch142:	linux-modules-fixed.patch
Patch143:	linux-ppc-procesor.patch
Patch144:	amd762_irq_router.patch

# Patches fixing other patches or 3rd party sources ;)

# patch to fix missing EXPORT_SYMBOLS from IDE patch
Patch900:	ide-EXPORT_SYMBOL.fix
Patch901:	netfilter-ip_nat_pptp.patch
Patch902:	linux-2.4.19pre7-VIA.patch
Patch903:	linux-PPC-SMP.patch
Patch904:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
# tweaks for grsecurity, description inside patch
Patch906:	linux-grsecurity-fixes.patch
Patch907:	linux-loop-hvr-2.4.16.0.patch
Patch908:	ippersonality-post.patch
Patch909:	linux-53c7,8xx-build.fix
Patch910:	dc395-PLD.fix
Patch911:	linux-o1-sched-grsec-pre.patch
Patch912:	linux-o1-sched-grsec-post.patch
Patch913:	linux-o1-sched-abi.patch
Patch914:	linux-o1-sched-pre.patch
Patch915:	linux-o1-sched-post.patch
Patch916:	linux-o1-sched-evms.patch

# DRM (note that this doesn't fix drm when running on 386 or 486 CPU!)
Patch950:	linux-drm-%{drm_xfree_version}-force-cmpxchg.patch

# Marcelo's -pre
#Patch1000:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/testing/patch-2.4.16-%{pre_version}.gz

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	%{kgcc_package}
%endif
BuildRequires:	modutils
Buildrequires:	perl
BuildRequires:	rpm >= 4.0.4
Provides:	%{name}-up = %{version}-%{release}
Provides:	module-info
Provides:	i2c = 2.6.1
Provides:	bttv = 0.7.83
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd >= 2.13
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
%ifarch		%{ix86}
BuildRequires:	bin86
%endif
# conflicts section
Conflicts:	iptables < 1.2.6
Conflicts:	lvm < 1.0.4

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
Pakiet zawiera j±dro Linuxa niezbêdne do prawid³owego dzia³ania
Twojego komputera. Zawiera w sobie sterowniki do sprzêtu znajduj±cego
siê w komputerze, takich jak karty muzyczne, sterowniki dysków, etc.


%if%{?_without_smp:0}%{!?_without_smp:1}
%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Provides:	%{name} = %{version}-%{release}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Prereq:		modutils
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description -l de smp
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nécessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand même fonctionner pour les système mono-processeur.

%description -l pl smp
Pakiet zawiera j±dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj±ce dwa lub wiêcej procesorów.
Powinno równie¿ dobrze dzia³aæ na maszynach z jednym procesorem.
%endif 

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Prereq:		modutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description -l de BOOT
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description -l pl BOOT
Pakiet zawiera j±dro Linuksa dedykowane dyskietkom startowym i powinno
byæ u¿ywane jedynie podczas instalacji systemu. Wiele u¿ytecznych
opcji zosta³o wy³±czonych, aby jak najbardziej zmniejszyæ jego
rozmiar.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu³y PCMCIA-CS 
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
Prereq:		%{name}-up = %{version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_version}).

%description -l pl pcmcia-cs
Modu³y PCMCIA-CS (%{pcmcia_version}).

%package smp-pcmcia-cs
Summary:	PCMCIA-CS modules for SMP kernel
Summary(pl):	Modu³y PCMCIA-CS dla maszyn SMP
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
Prereq:		%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description -l pl smp-pcmcia-cs
Modu³y PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:       %{name}-drm = %{drm_xfree_version}
Prereq:		%{name}-up = %{version}-%{release}

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description -l pl drm
Sterowniki DRM (%{drm_xfree_version}).

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:       %{name}-drm = %{drm_xfree_version}
Prereq:		%{name}-smp = %{version}-%{release}

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description -l pl smp-drm
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Provides:	i2c-devel = 2.6.1
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbedne do rekompilacji j±dra
oraz niektórych programów.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuxa
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Autoreqprov:	no
Requires:	%{name}-headers = %{version}-%{release}
%ifarch %{ix86}
Requires:	bin86
%endif

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description -l de source
Das Kernel-Source-Paket enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description -l fr source
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nécessaires pour compiler la plupart des
programmes C, car il dépend de constantes définies dans le code
source. Les sources peuvent être aussi utilisée pour compiler un noyau
personnalisé pour avoir de meilleures performances sur des matériels
particuliers.

%description source -l pl
Pakiet zawiera kod ¼ród³owy jadra systemu.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja do kernela
Group:		Base/Kernel
Group(cs):	Základ/Jádro
Group(da):	Basal/Kerne
Group(de):	Grundsätzlich/Kern
Group(es):	Base/Núcleo
Group(fr):	Base/Noyau
Group(is):	Grunnforrit/Kjarninn
Group(it):	Base/Kernel
Group(ja):	¥Ù¡¼¥¹/¥«¡¼¥Í¥ë
Group(no):	Basis/Kjerne
Group(pl):	Podstawowe/J±dro
Group(pt):	Base/Núcleo
Group(ru):	âÁÚÁ/ñÄÒÏ
Group(sl):	Osnova/Jedro
Group(sv):	Bas/Kärna
Group(uk):	âÁÚÁ/ñÄÒÏ
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description -l pl doc
Pakiet zawiera dokumentacjê j±dra z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -a3 -a5 -a7 -a10 -a11 -a12 -a13 -a14 -n linux
#%patch1000 -p1
#%patch0 -p1
%patch16 -p1
%patch1 -p1
%patch907 -p1
%patch132 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch19 -p1
#%patch7 -p1
%if %{?_with_o1_sched:1}%{!?_with_o1_sched:0}
%ifarch %{ix86}
%patch914 -p1
%patch14 -p1
%patch915 -p1
%else
echo "Scheduler din't work on ARCH diffetern than Intel x86"
%endif
%else
%patch8 -p1
%endif
%if %{?_with_o1_sched:1}%{!?_with_o1_sched:0}
%ifarch%{ix86}
%patch911 -p1
%else
echo "Scheduler din't work on ARCH diffetern than Intel x86"
%endif
%endif
%patch9 -p1
%patch906 -p0
%if %{?_with_o1_sched:1}%{!?_with_o1_sched:0}
%ifarch%{ix86}
%patch912 -p1
%else
echo "Scheduler din't work on ARCH diffetern than Intel x86"
%endif
%endif
%patch15 -p1
%patch17 -p1

%patch100 -p0
%patch101 -p1
%patch102 -p0
%patch103 -p0
%patch105 -p1
%patch106 -p1
#%patch107 -p1
#%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p2
%patch113 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch124 -p1

%patch904 -p0

# XFree DRM
%ifarch %{ix86}
%patch950 -p0
%endif
rm -rf drivers/char/drm
cp -f drm/Makefile.kernel drm/Makefile
mv -f drm drivers/char

# Tekram DC395/315 U/UW SCSI host driver
echo Adding Tekram DC395/315 driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Fore 200e ATM NIC
echo Adding FORE 200e ATM driver
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch
#patch -p1 -s <linux-2.4.0-test3-fore200e-0.2g/linux-2.4.0-test3-fore200e-0.2g.patch

# Netfilter
echo Adding Netfilter snapshot from 15.04.2002
(KERNEL_DIR=`pwd` ; export KERNEL_DIR
cd netfilter-patches/patch-o-matic/extra
cd ..
ANS=""
for suite in submitted pending base extra pld ; do
	for i in `echo ${suite}/*.patch.ipv6` `echo ${suite}/*.patch` ; do
		ANS="${ANS}y\n\n"
	done
done
echo -e $ANS | ./runme pld)

patch -p1 < netfilter-patches/patch-o-matic/pld/log.patch
%patch901 -p0

# IPVS
echo Adding IPVS
%patch13 -p1

# Remove -g from drivers/atm/Makefile and net/ipsec/Makefile
mv -f drivers/atm/Makefile drivers/atm/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*//g' drivers/atm/Makefile.orig > drivers/atm/Makefile

# Free S/Wan
echo Adding Free S/Wan
mv -f net/ipsec/Makefile net/ipsec/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*-g//g' net/ipsec/Makefile.orig > net/ipsec/Makefile

# install NCR/Symbios controler
echo Adding NCR/Symbios controler
mv %{sym_ncr_version}/*.{c,h} drivers/scsi
mv %{sym_ncr_version}/{README,ChangeLog}.* Documentation
rm -rf %{sym_ncr_version}

# IP personality
echo Adding IP Personality 
patch -p1 -s <ippersonality-%{IPperson_version}/patches/ippersonality-20020427-linux-2.4.18.diff
%patch908 -p1

# JFS
echo Adding JFS
%patch18 -p1

echo Fixed compile process for 53c7,8xx driver
# fix 53c7,8xx build
%patch909 -p0

#preemptble kernel patch
%{?_with_preemptible:echo Installing Preemptible patch}
%{?_with_preemptible:%{?_with_o1_sched:%patch20 -p1}}
%{?_with_preemptible:%{!?_with_o1_sched:%patch10 -p1}}

# netdev-random
echo Installing Net Dev Random patch
%patch11 -p1
%patch12 -p1

%patch125 -p1

# fixed SPARC64 compilation
%ifarch sparc64
echo Fixed SPARC 64 compilation.
%patch127 -p1
%patch126 -p1
%endif

#fixed AXP compilation
%ifarch alpha
echo Fixed SYSCALL errors for DEC Alpha arch.
%patch128 -p0
%endif

# Fided include path
%patch129 -p0

#Fixed sysctl export symbols.
%patch130 -p0

%patch133 -p0

%ifarch ppc
%patch134 -p1
%patch135 -p1
%endif

# EVMS
%patch136 -p1
%patch137 -p1
%{?_with_o1_sched:%patch916 -p1}

%ifarch %{ix86}
%patch139 -p1
%endif

# Trident FB
echo Replacing Trident FB module.
%patch140 -p1

# VIA Southbridge update
echo Updating VIA Southbridge
%patch902 -p1

%patch903 -p0

%ifarch ppc
%patch138 -p1
%patch143 -p0
%endif

%patch141 -p1
%patch142 -p1

#HPFS fix.
%patch21 -p1

# MPPE (ppp)
%patch22 -p1

# ADM router
%patch144 -p1

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
%ifarch %{ix86} alpha sparc ppc
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= %{kgcc}/g' \
%endif
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    Makefile.orig >Makefile


%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a special kernel we want to build?
	BOOT=
	smp=
	if [ -n "$1" ] ; then
		if [ "$1" = "BOOT" ] ; then
			BOOT=yes
		fi
		if [ "$1" = "smp" ] ; then
			smp=yes
		fi
%ifarch %{ix86}
	if [ "$smp" ]; then
		Config="ia32"-$1
	fi
%else
	if [ "$smp" ]; then
		Config="%{_target_cpu}"-$1
	fi
%endif
	else
%ifarch %{ix86}
		Config="ia32"
%else
		Config="%{_target_cpu}"
%endif
	fi
	if [ "$BOOT" ]; then
	KernelVer=%{version}-%{release}BOOT
	else
	KernelVer=%{version}-%{release}$1
	fi
	echo BUILDING THE NORMAL KERNEL $1...
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
	cat %{SOURCE1001} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1002} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1003} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1004} >> arch/%{base_arch}/defconfig
%if %{?_with_preemptive:1}%{!?_with_preemptive:0}
	cat %{SOURCE1999} >> arch/%{base_arch}/defconfig
%endif
%if %{?_with_acpi:1}%{!?_with_acpi:0}
	echo "CONFIG_ACPI=y" >> arch/%{base_arch}/defconfig
	echo "# CONFIG_ACPI_DEBUG is not set" >> arch/%{base_arch}/defconfig
	echo "CONFIG_SERIAL_ACPI=y" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_BUSMGR=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_SYS=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_CPU=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_BUTTON=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_AC=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_EC=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_CMBATT=m" >> arch/%{base_arch}/defconfig
	echo "CONFIG_ACPI_THERMAL=m" >> arch/%{base_arch}/defconfig
%endif
	if [ "$BOOT" ] ; then
		echo "# CONFIG_GRKERNSEC is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_CRYPTO is not set" >> arch/%{base_arch}/defconfig
		echo "CONFIG_ROMFS_FS=y" >> arch/%{base_arch}/defconfig
	else
		cat %{SOURCE1667} >> arch/%{base_arch}/defconfig
		cat %{SOURCE1666} >> arch/%{base_arch}/defconfig
	fi
%ifarch i386
	mv -f arch/%{base_arch}/defconfig arch/%{base_arch}/defconfig.orig
	sed -e 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/%{base_arch}/defconfig.orig > arch/%{base_arch}/defconfig
%endif

	%{__make} mrproper
	ln -sf arch/%{base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} oldconfig
	sparc32 %{__make} dep clean
%else
	%{__make} oldconfig
	%{__make} dep clean
%endif
	%{__make} include/linux/version.h
	
%ifarch %{ix86}
	%{__make} bzImage
%endif
%ifarch sparc
	sparc32 %{__make} boot
%else
%ifnarch %{ix86}
	%{__make}
%endif
%endif
%ifarch sparc
	sparc32 %{__make} modules
%else
	%{__make} modules
%endif

	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
%ifarch %{ix86}
	cp arch/i386/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch alpha sparc sparc64
	gzip -cfv vmlinux > vmlinuz
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinuz $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch ppc
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
     %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
	echo KERNEL RELEASE $KernelVer
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# make drivers/scsi/ missing files
	(cd drivers/scsi; make -f M)
	
# UP KERNEL
%if %{?_without_up:0}%{!?_without_up:1}
BuildKernel 
%endif

%if !%{test_build}
# SMP KERNEL
%if %{?_without_smp:0}%{!?_without_smp:1}
BuildKernel smp
%endif			# %{_without_smp}

# BOOT kernel
%ifnarch i586 i686 athlon
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
BuildKernel BOOT
%endif

%endif			# %{test_build}

%install
rm -rf $RPM_BUILD_ROOT
umask 022

install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
ln -sf %{_prefix}/src/linux-%{version} $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done
ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux

%ifarch sparc sparc64
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT%{_includedir}/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT%{_includedir}/asm-sparc64
sh %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}/

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

%{__make} mrproper
find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f


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
cat %{SOURCE1001} >> .config
cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1666} >> .config
cat %{SOURCE1667} >> .config
%if %{?_with_preemptive:1}%{!?_with_preemptive:0}
	cat %{SOURCE1999} >> .config
%endif

%{__make} oldconfig
mv include/linux/autoconf.h include/linux/autoconf-up.h

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

cat %{SOURCE1001} >> .config
cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1666} >> .config
cat %{SOURCE1667} >> .config
%if %{?_with_preemptive:1}%{!?_with_preemptive:0}
	cat %{SOURCE1999} >> .config
%endif

%{__make} oldconfig
mv include/linux/autoconf.h include/linux/autoconf-smp.h

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux/autoconf.h

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
%{__make} symlinks 
%{__make} include/linux/version.h
%{__make} "`pwd`/include/linux/modversions.h"

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well, after we fix the paths

%{__make} depend 
find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" | \
while read file ; do
	mv $file $file.old
	sed -e "s|$RPM_BUILD_ROOT\(/usr/src/linux\)|\1|g" < $file.old > $file
	rm -f $file.old
done

%{__make} clean
rm -f scripts/mkdep
rm -f drivers/net/hamradio/soundmodem/gentbl

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-installed

%if %{?_without_up:0}%{!?_without_up:1}
%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null 
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

if [ ! -L /lib/modules/%{version} -] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi
%endif			# %{_without_up}

%if %{?_without_smp:0}%{!?_without_smp:1}
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
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi
%endif			# %{_without_smp}

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

%if %{?_without_up:0}%{!?_without_up:1}
%postun
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz
%endif			# %{_without_up}

%if %{?_without_smp:0}%{!?_without_smp:1}
%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz
%endif			# %{_without_smp}

%postun BOOT
if [ -L %{_libdir}/bootdisk/lib/modules/%{version} ]; then 
	if [ "`ls -l %{_libdir}/bootdisk/lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}BOOT" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_libdir}/bootdisk/lib/modules/%{version}
		fi
	fi
fi

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L /usr/src/linux ]; then 
	if [ "`ls -l /usr/src/linux | awk '{ print $11 }'`" = "linux-%{version}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /usr/src/linux
		fi
	fi
fi


%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%post smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%post drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%post smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%if %{?_without_up:0}%{!?_without_up:1}
%files
%defattr(644,root,root,755)
%ifarch alpha sparc ppc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o
%ifnarch ppc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/ide/ide-cs.o
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o
%endif
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*
%endif			# %{_without_up}

#%if !%{test_build}

%files pcmcia-cs
%defattr(644,root,root,755)
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/pcmcia
%endif
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o
/lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o
%ifnarch ppc
/lib/modules/%{version}-%{release}/kernel/drivers/ide/ide-cs.o
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o
/lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o
%endif

%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm

%if %{?_without_smp:0}%{!?_without_smp:1}
%files -n kernel-smp-pcmcia-cs
%defattr(644,root,root,755)
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/pcmcia
%endif
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o
%ifnarch ppc
/lib/modules/%{version}-%{release}smp/kernel/drivers/ide/ide-cs.o
/lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/avmb1/avm_cs.o
/lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hisax/*_cs.o
/lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/*_pcmcia.o
%endif

%files -n kernel-smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o
%ifnarch ppc
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/ide/ide-cs.o
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/avmb1/avm_cs.o
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hisax/*_cs.o
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/*_pcmcia.o
%endif
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*
%endif			# %{_without_smp}

%ifnarch i586 i686 athlon 		# narch
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc ppc		# arch
%{_libdir}/bootdisk/boot/vmlinux-%{version}-%{release}BOOT
%endif				#arch
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%ifarch i386			# i386_arch
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/pcmcia
%endif				# i386_arch
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/build
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*
%endif				# narch

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%files source
%defattr(644,root,root,755)
#%{_prefix}/src/linux-%{version}/abi
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/grsecurity
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kdb
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/.config
%{_prefix}/src/linux-%{version}/.depend
%{_prefix}/src/linux-%{version}/.hdepend
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%{_prefix}/src/linux-%{version}/Rules.make
