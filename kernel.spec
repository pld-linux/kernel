#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# _with_lids		- build LIDS enabled kernels
# _without_grsec	- build kernel without grsecurity patch
# _with_preemptive	- build with Preemptive patch
#
%define		test_build		0
#
%define		pre_version		pre1
%define		lids_version		1.0.14-2.4.9
%define		ipvs_version		0.9.8
%define		freeswan_version	snap2001sep23b
%define 	aacraid_version		1.0.6
%define		wlan_version		0.1.10
%define		sym_ncr_version		sym-1.7.3c-ncr-3.4.3b
%define		IPperson_version	20010724-2.4.7
%define		grsec_version		1.9-2.4.16
%define		aic_version		6.2.3-2.4.7
%define		jfs_version		2.4-1.0.10
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.4.16
Release:	0.5
License:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-134.tar.gz
Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
# Don't use following patch, it may hang the NIC (baggins)
#Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.4.0-test3-fore200e-0.2g.tar.gz
# based on cvs cvs@pserver.samba.org:/cvsroot netfilter
Source7:	linux-2.4.16-netfilter-20011201.tar.gz
Source8:	http://www.lids.org/download/lids-%{lids_version}.tar.gz
Source10:	ftp://ftp.linux-wlan.org/pub/linux-wlan-ng/linux-wlan-ng-%{wlan_version}.tar.gz
# new -> ftp://ftp.tux.org/pub/roudier/drivers/portable/sym-2.1.x/sym-2.1.16-20011028.tar.gz
Source11:	ftp://ftp.tux.org/pub/people/gerard-roudier/drivers/linux/stable/%{sym_ncr_version}.tar.gz
Source12:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source13:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-%{jfs_version}-patch.tar.gz
Source20:	%{name}-ia32.config
Source21:	%{name}-ia32-smp.config
Source22:	%{name}-i386-BOOT.config
Source50:	%{name}-sparc.config
Source51:	%{name}-sparc-smp.config
Source52:	%{name}-sparc-BOOT.config
Source60:	%{name}-sparc64.config
Source61:	%{name}-sparc64-smp.config
Source62:	%{name}-sparc64-BOOT.config
Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config
Source72:	%{name}-alpha-BOOT.config
Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config
Source1000:	%{name}-lids.config
Source1001:	%{name}-abi.config
Source1002:	%{name}-addon.config
Source1003:	%{name}-netfilter.config
Source1004:	%{name}-ipvs.config
Source1666:	%{name}-grsec.config

# New features

Patch0:		%{name}-pldfblogo.patch
#Patch1:		ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/patch-int-2.4.3.1.gz
Patch1:		patch-int-2.4.15.0.gz
Patch2:		linux-2.4.10-freeswan-%{freeswan_version}.patch.gz
# http://domsch.com/linux/aacraid/linux-2.4.9-aacraid-20010816.patch
Patch3:		linux-2.4.9-aacraid-20010816.patch
# http://home.sch.bme.hu/~cell/br2684/dist/010402/br2684-against2.4.2.diff
Patch4:		br2684-against2.4.15.diff
# ftp://linux-xfs.sgi.com/projects/xfs/download/patches/
Patch5:		linux-2.4.16-xfs-20011129.patch.gz
# Homepage of ABI : http://linux-abi.sourceforge.net/
#ftp://ftp.kernel.org/pub/linux/kernel/people/hch/linux-abi/v2.4/linux-abi-2.4.15.0.patch.bz2
Patch7:		linux-abi-2.4.15.0.patch.bz2
Patch8:		http://www.uow.edu.au/~andrewm/linux/cpus_allowed.patch
# grsecurity patch http://www.getrewted.net/
# http://grsecurity.net/grsecurity-%{grsec_version}.patch
Patch9:		grsecurity-%{grsec_version}.patch
# Preemptive kernel  patch
Patch10:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/preempt-kernel/v2.4/preempt-kernel-rml-2.4.16-1.patch

Patch11:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/netdev-random/v2.4/netdev-random-core-rml-2.4.16-1.patch
Patch12:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/netdev-random/v2.4/netdev-random-drivers-rml-2.4.16-1.patch
Patch13:	http://www.linuxvirtualserver.org/software/kernel-2.4/linux-%{version}-ipvs-%{ipvs_version}.patch.gz

# Assorted bugfixes

# from LKML
Patch100:	linux-scsi-debug-bug.patch
Patch101:	linux-2.4.2-raw-ip.patch
Patch102:	PCI_ISA_bridge.patch
Patch103:	linux-2.4.2-nvram-hdd.patch
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch105:	linux-2.4.2-pcnet-parms.patch
Patch106:	http://linuxdiskcert.org/ide.2.4.16-p1.11242001.patch.bz2
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
# extra PnP id for sb32awe
Patch118:	linux-2.4.3-sb.patch
# another sb16 pnp id
Patch119:	linux-2.4.6-sb_id.patch
Patch120:	linux-2.4.10-aironet.patch
Patch121:	linux-2.4.10-cpqfc.patch
# Created from lvm.tgz:LVM/PATCHES by doing make
Patch122:	linux-2.4.16-lvm-1.0.1rc4.patch
# fixed xquad_portio
Patch123:	xquad_portio.fix
# 
Patch124:	linux-proc_net_dev-counter-fix.patch

# Patches fixing other patches or 3rd party sources ;)

# patch to fix missing EXPORT_SYMBOLS from IDE patch
Patch900:	ide-EXPORT_SYMBOL.fix
# patch fixing problem with ABI and LIDS
Patch901:	linux-lids-with-abi.patch
# patch fixing LIDS stupidity
#Patch903:	linux-lids-fixpatch.patch
Patch904:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
# tweaks for grsecurity, description inside patch
Patch906:	linux-grsecurity-fixes.patch
Patch909:	linux-53c7,8xx-build.fix
Patch910:	dc395-PLD.fix

# Marcelo's -pre
#Patch1000:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/testing/patch-2.4.16-%{pre_version}.gz

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	egcs
%endif
BuildRequires:	modutils
Buildrequires:	perl
Provides:	%{name}-up = %{version}
Provides:	module-info
Provides:	i2c = 2.6.1
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
%ifarch		%{ix86}
BuildRequires:	bin86
%endif
#BuildRequires:	kernel-headers

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

%if %{?_with_lids:1}%{!?_with_lids:0}
%package lids
Summary:	LIDS enabled kernel version %{version}
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Prereq:		modutils
Autoreqprov:	no

%description lids
This package includes a LIDS enabled version of the Linux %{version} kernel.
It is required only when you want maximum security.

See http://www.lids.org/ for details.

%description -l pl lids
Pakiet zawiera j±dro Linuksa w wersji %{version} z w³±czonym LIDS.
Jest ono wymagane jedynie gdy potrzebne jest maksymalne bezpieczeñstwo.

Szczegó³y pod http://www.lids.org/.
%endif

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
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
Pakiet zawiera j±dro SMP Linuksa w wersji %{version}. Jest ono wymagane
przez komputery zawieraj±ce dwa lub wiêcej procesorów. Powinno równie¿ dobrze 
dzia³aæ na maszynach z jednym procesorem.

%if %{?_with_lids:1}%{!?_with_lids:0}
%package lids-smp
Summary:	LIDS enabled kernel version %{version} compiled for SMP machines
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Prereq:		modutils
Autoreqprov:	no

%description lids-smp
This package includes a LIDS enabled SMP version of the Linux %{version}
kernel. It is required only on machines with two or more CPUs, when you want
maximum security.

See http://www.lids.org/ for details.

%description -l pl lids-smp
Pakiet zawiera j±dro SMP Linuksa w wersji %{version} z w³±czonym LIDS.
Jest ono wymagane przez komputery zawieraj±ce dwa lub wiêcej procesorów,
jedynie gdy wymagane jest maksymalne bezpieczeñstwo.

Szczegó³y pod http://www.lids.org/.
%endif

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
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

%description -l fr BOOT
Ce package inclut une version allégée du noyau de Linux version
%{version}. Ce kernel et utilisé pour les disquettes de boot
d'installation et ne doivent pas être utilisées pour un système
classique, beaucoup d'options dans le kernel ont étaient désactivées a
cause de la contrainte d'espace.
#'
%description -l pl BOOT
Pakiet zawiera j±dro Linuksa dedykowane dyskietkom startowym i powinno 
byæ u¿ywane jedynie podczas instalacji systemu. Wiele u¿ytecznych opcji
zosta³o wy³±czonych, aby jak najbardziej zmniejszyæ jego rozmiar.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
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
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no
Requires:	%{name}-headers = %{version}
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

%prep
%{?_with_lids:%setup -q -a3 -a5 -a7 -a8 -a10 -a11 -a12 -a13 -n linux}
%{!?_with_lids:%setup -q -a3 -a5 -a7 -a10 -a11 -a12 -a13 -n linux}
#%patch1000 -p1
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch7 -p1
%patch8 -p1
%if%{?_without_grsec:0}%{!?_without_grsec:1}
%ifarch %{ix86}
%patch9 -p1
%patch906 -p1
%endif
%endif

%patch100 -p0
%patch101 -p1
%patch102 -p0
%patch103 -p0
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p2
%patch113 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p0
%patch123 -p1
%patch124 -p1

%patch900 -p0
%patch904 -p0

# Tekram DC395/315 U/UW SCSI host driver
echo Adding Tekram DC395/315 driver
%patch910 -p0
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Fore 200e ATM NIC
echo Adding FORE 200e ATM driver
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch
#patch -p1 -s <linux-2.4.0-test3-fore200e-0.2g/linux-2.4.0-test3-fore200e-0.2g.patch

# Netfilter
echo Adding Netfilter
(KERNEL_DIR=`pwd` ; export KERNEL_DIR
cd netfilter-patches/patch-o-matic
ANS=""
for suite in pending base extra pld ; do
	for i in `echo ${suite}/*.patch.ipv6` `echo ${suite}/*.patch` ; do
		ANS="${ANS}y\n"
	done
done
echo -e $ANS | ./runme pld)

%if %{?_with_lids:1}%{!?_with_lids:0}
# LIDS
echo Adding LIDS
cd lids-%{lids_version}
%patch901 -p1
cd ..
patch -p1 -s <lids-%{lids_version}/lids-%{lids_version}.patch
%endif

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
patch -p1 -s <ippersonality-%{IPperson_version}/patches/ippersonality-20010724-linux-2.4.7.diff

# JFS
echo Adding JFS
patch -p1 -s <jfs-2.4.common-1.0.10-patch
patch -p1 -s <jfs-2.4.7-1.0.10-patch

echo Fixed compile process for 53c7,8xx driver
# fix 53c7,8xx build
%patch909 -p0

#preemptive kernel patch
echo Installing Preemptive patch
%if%{?_with_preemptive:1}%{!?_with_preemptive:0}
%patch10 -p1
%endif

# netdev-random
echo Installing Net Dev Random patch
%patch11 -p1
%patch12 -p1

%ifarch %{x86}
%patch7 -p1
%endif

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
%ifarch %{ix86} alpha sparc
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= egcs/g' \
%endif
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    Makefile.orig >Makefile


%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a LIDS enabled kernel?
	if [ "$1" = "lids" ] ; then
		LIDS="lids"
		shift
	else
		LIDS=""
	fi
	# is this a special kernel we want to build?
	BOOT=
	if [ -n "$1" ] ; then
		if [ "$1" = "BOOT" ] ; then
			BOOT=yes
		fi
%ifarch %{ix86}
		if [ "$1" = "BOOT" ] ; then
			Config="%{_target_cpu}"-$1
		else
			Config="ia32"-$1
		fi
%else
		Config="%{_target_cpu}"-$1
%endif
		KernelVer=%{version}-%{release}$1
		echo BUILDING A KERNEL FOR $1...
		shift
	else
%ifarch %{ix86}
		Config="ia32"
%else
		Config="%{_target_cpu}"
%endif
		KernelVer=%{version}-%{release}
		echo BUILDING THE NORMAL KERNEL...
	fi
	:> arch/$RPM_ARCH/defconfig
%ifarch i386
	echo "CONFIG_M386=y" > arch/$RPM_ARCH/defconfig
%endif
%ifarch i586
	echo "CONFIG_M586=y" > arch/$RPM_ARCH/defconfig
%endif
%ifarch i686
	echo "CONFIG_M686=y" > arch/$RPM_ARCH/defconfig
%endif
	cat $RPM_SOURCE_DIR/kernel-$Config.config >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1001} >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1002} >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1003} >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1004} >> arch/$RPM_ARCH/defconfig
%ifarch %{ix86}
	if [ "$BOOT" ] ; then
		echo "# CONFIG_GRKERNSEC is not set" >> arch/$RPM_ARCH/defconfig
	else
		cat %{SOURCE1666} >> arch/$RPM_ARCH/defconfig
	fi
%endif
	if [ "$LIDS" = "lids" ] ; then
		echo ENABLING LIDS...
		cat %{SOURCE1000} >> arch/$RPM_ARCH/defconfig
		KernelVer="${KernelVer}-lids"
	fi
%ifarch i386
	mv -f arch/$RPM_ARCH/defconfig arch/$RPM_ARCH/defconfig.orig
	sed -e 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/$RPM_ARCH/defconfig.orig > arch/$RPM_ARCH/defconfig
%endif

	%{__make} mrproper
	ln -sf arch/$RPM_ARCH/defconfig .config

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
%else
%ifarch sparc
	sparc32 %{__make} boot
%else
%ifarch ppc
	%{__make}
%else
	%{__make} boot
%endif
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
     %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# make drivers/scsi/ missing files
	(cd drivers/scsi; make -f M)
	
# UP KERNEL
BuildKernel 

%if !%{test_build}
# SMP KERNEL
BuildKernel smp

%if %{?_with_lids:1}%{!?_with_lids:0}
# UP LIDS KERNEL
BuildKernel lids

# SMP LIDS KERNEL
BuildKernel lids smp
%endif

# BOOT kernel
%ifnarch i586 i686
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
BuildKernel BOOT
%endif
%endif

%install
umask 022
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" "-lids" smp smp-lids ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf /usr/src/linux-%{version} $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done
ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

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

%ifarch i386
echo "CONFIG_M386=y" > .config
%endif
%ifarch i586
echo "CONFIG_M586=y" > .config
%endif
%ifarch i686
echo "CONFIG_M686=y" > .config
%endif

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32.config >> .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config
%endif

cat %{SOURCE1001} >> .config
cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1666} >> .config

%{__make} oldconfig
mv include/linux/autoconf.h include/linux/autoconf-up.h

%ifarch i386
echo "CONFIG_M386=y" > .config
%endif
%ifarch i586
echo "CONFIG_M586=y" > .config
%endif
%ifarch i686
echo "CONFIG_M686=y" > .config
%endif

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32-smp.config >> .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}-smp.config .config
%endif

cat %{SOURCE1001} >> .config
cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1666} >> .config

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

%if %{?_with_lids:1}%{!?_with_lids:0}
# LIDS config
cat %{SOURCE1000} >> $RPM_BUILD_ROOT/usr/src/linux-%{version}/.config.lids
%endif

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-installed

%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null 
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%if %{?_with_lids:1}%{!?_with_lids:0}
%post lids
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}-lids /boot/vmlinuz
ln -sf System.map-%{version}-%{release}-lids /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}-lids.gz %{version}-%{release}-lids
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}-lids.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}-lids /lib/modules/%{version}
%endif

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}

%if %{?_with_lids:1}%{!?_with_lids:0}
%post lids-smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp-lids /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp-lids /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}smp-lids.gz %{version}-%{release}smp-lids
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp-lids.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp-lids /lib/modules/%{version}
%endif

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
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%if %{?_with_lids:1}%{!?_with_lids:0}
%postun lids
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}-lids" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}-lids.gz
%endif

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%if %{?_with_lids:1}%{!?_with_lids:0}
%postun lids-smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp-lids" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp-lids.gz
%endif

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

%files
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/pcmcia
%endif
/lib/modules/%{version}-%{release}/kernel
/lib/modules/%{version}-%{release}/build
/lib/modules/%{version}-%{release}/modules.dep
/lib/modules/%{version}-%{release}/modules.*map
/lib/modules/%{version}-%{release}/modules.generic_string

%if !%{test_build}
%if %{?_with_lids:1}%{!?_with_lids:0}
%files lids
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}-lids
%endif
/boot/vmlinuz-%{version}-%{release}-lids
/boot/System.map-%{version}-%{release}-lids
%dir /lib/modules/%{version}-%{release}-lids
%ifarch %{ix86}
/lib/modules/%{version}-%{release}-lids/pcmcia
%endif
/lib/modules/%{version}-%{release}-lids/kernel
/lib/modules/%{version}-%{release}-lids/build
/lib/modules/%{version}-%{release}-lids/modules.dep
/lib/modules/%{version}-%{release}-lids/modules.*map
/lib/modules/%{version}-%{release}-lids/modules.generic_string
%endif

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/pcmcia
%endif
/lib/modules/%{version}-%{release}smp/kernel
/lib/modules/%{version}-%{release}smp/build
/lib/modules/%{version}-%{release}smp/modules.dep
/lib/modules/%{version}-%{release}smp/modules.*map
/lib/modules/%{version}-%{release}smp/modules.generic_string

%if %{?_with_lids:1}%{!?_with_lids:0}
%files lids-smp
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}smp-lids
%endif
/boot/vmlinuz-%{version}-%{release}smp-lids
/boot/System.map-%{version}-%{release}smp-lids
%dir /lib/modules/%{version}-%{release}smp-lids
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp-lids/pcmcia
%endif
/lib/modules/%{version}-%{release}smp-lids/kernel
/lib/modules/%{version}-%{release}smp-lids/build
/lib/modules/%{version}-%{release}smp-lids/modules.dep
/lib/modules/%{version}-%{release}smp-lids/modules.*map
/lib/modules/%{version}-%{release}smp-lids/modules.generic_string
%endif

%ifnarch i586 i686
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc
%{_libdir}/bootdisk/boot/vmlinux-%{version}-%{release}BOOT
%endif
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%ifarch i386
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/pcmcia
%endif
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/build
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.dep
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*map
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.generic_string
%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files source
%defattr(-,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
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
%{?_with_lids:%{_prefix}/src/linux-%{version}/.config.lids}
%{_prefix}/src/linux-%{version}/.depend
%{_prefix}/src/linux-%{version}/.hdepend
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%{_prefix}/src/linux-%{version}/Rules.make
