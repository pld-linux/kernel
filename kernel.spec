#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# _with_lids		- build LIDS enabled kernels
# _without_grsec	- build kernel without grsecurity patch
#
# WARNING: grsec needs manual tweaking, read note in the patch for details
#
%define		test_build		0
#
%define		pre_version		pre9
%define		lids_version		1.0.11-2.4.6
%define		ipvs_version		0.9.4
%define		freeswan_version	snap2001sep27b
%define 	aacraid_version		1.0.6
%define		wlan_version		0.1.9
%define		sym_ncr_version		sym-1.7.3c-ncr-3.4.3b
%define		vlan_version		1.4
%define		IPperson_version	20010724-2.4.7
%define		grsec_version		1.8-2.4.7
%define		aic_version		6.2.3-2.4.7
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.4.7
Release:	10
License:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-132.tar.gz
Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
# Don't use following patch, it may hang the NIC (baggins)
#Source5:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.4.0-test3-fore200e-0.2g.tar.gz
Source6:	http://www.xs4all.nl/~sgraaf/i8255/i8255-0.2.tar.gz
Source7:	linux-2.4.7-netfilter-20010928.tar.gz
Source8:	http://www.lids.org/download/lids-%{lids_version}.tar.gz
Source9:	http://www.linuxvirtualserver.org/software/kernel-2.4/ipvs-%{ipvs_version}.tar.gz
Source10:	http://www.linux-wlan.com/linux-wlan/linux-wlan-ng-%{wlan_version}.tar.gz
Source11:	ftp://ftp.tux.org/pub/people/gerard-roudier/drivers/linux/stable/%{sym_ncr_version}.tar.gz
Source12:	http://scry.wanfear.com/~greear/vlan/vlan.%{vlan_version}.tar.gz
Source13:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source14:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-2.4-1.0.6-patch.tar.gz
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
Source1000:	%{name}-lids.config
Source1001:	%{name}-abi.config
Source1002:	%{name}-grsec.config
Source1003:	%{name}-addon.config
Source1004:	%{name}-xfs.config
Source1005:	%{name}-netfilter.config
Source1006:	%{name}-ipvs.config
Source1007:	%{name}-ippersonality.config

# New features

Patch0:		%{name}-pldfblogo.patch
#Patch1:		ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/patch-int-2.4.3.1.gz
Patch1:		patch-int-2.4.5.0.gz
Patch2:		linux-2.4.7-freeswan-%{freeswan_version}.patch.gz
# http://domsch.com/linux/aacraid/linux-2.4.4-aacraid-043001.patch
Patch3:		linux-2.4.4-aacraid-043001.patch
# http://home.sch.bme.hu/~cell/br2684/dist/010402/br2684-against2.4.2.diff
Patch4:		br2684-against2.4.7.diff
# ftp://linux-xfs.sgi.com/projects/xfs/download/
Patch5:		linux-2.4.7-xfs-20010726.patch.gz
# Compressed iso9660 filesystem
Patch6:		ftp://ftp.kernel.org/pub/linux/kernel/people/hpa/zisofs+filemap-2.4.7-1.diff.gz
Patch7:		linux-abi-2.4.3-PLD.patch
Patch8:		http://www.uow.edu.au/~andrewm/linux/cpus_allowed.patch
# grsecurity patch http://www.getrewted.net/
Patch9:		linux-grsecurity-%{grsec_version}.patch
# EXT3
# http://www.uow.edu.au/~andrewm/linux/ext3/
Patch10:	http://www.zip.com.au/~akpm/ext3-2.4-0.9.5-247.gz

# Assorted bugfixes

# Quota fixes
# Patch100:	ftp://atrey.karlin.mff.cuni.cz/pub/local/jack/quota/v2.4/quota-fix-2.4.6-2.diff.gz
Patch100:	quota-fix-2.4.7-1.diff.gz
# from LKML
Patch101:	linux-scsi-debug-bug.patch
Patch102:	linux-2.4.7-oom-killer.patch
Patch103:	linux-2.4.2-raw-ip.patch
Patch104:	PCI_ISA_bridge.patch
Patch105:	linux-2.4.2-nvram-hdd.patch
Patch106:	linux-2.4-fix-kapm.patch
Patch107:	epca-fix-missing-unregister-driver.patch
Patch108:	ramdisk-VM.fix
Patch109:	linux-ram-disk-free.patch
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch110:	linux-2.4.2-pcnet-parms.patch
# Kernel crashes during making reiser-module:
Patch111:	%{name}-reiser.patch
Patch112:	ftp://ftp.kernel.org/pub/linux/kernel/people/hedrick/ide-2.4.3/ide.2.4.6-p1.06062001.patch.gz
Patch113:	linux-reiserfs-rename.patch
Patch114:	linux-via-fixes.patch
Patch115:	linux-alpha-nfs-2.4.2.patch
Patch116:	linux-2.4-string.patch
# raid5 xor fix for PIII/P4, should go away shortly
Patch117:	linux-2.4.0-raid5xor.patch
# disable some networking printk's
Patch118:	linux-2.4.1-netdebug.patch
# SCSI Reset patch for clustering stuff
Patch119:	linux-2.4.1-scsi-reset.patch
# Add an ioctl to the block layer so we can be EFI compliant
Patch120:	linux-2.4.2-blkioctl-sector.patch
# fix for non-atomic bit clear in eepro100 driver on alpha
Patch121:	linux-2.4.2-eepro100-alpha.patch
# Patch from Doug to fix i810 recording
Patch122:	linux-2.4.2-i810_audio.patch
# OHCI IRQ sanity check
Patch123:	linux-2.4.2-ohci-irq.patch
# fix lun probing on multilun RAID chassis
Patch124:	linux-2.4.2-scsi_scan.patch
# work around Latitude C600 resume problem (bios bug)
Patch125:	linux-2.4.3-latitudec600.patch
# fix pcnet32 networkdriver load vs ifconfig races
Patch126:	linux-2.4.3-pcnet32.patch
# fix rawio
Patch127:	linux-2.4.3-rawio.patch
# extra PnP id for sb32awe
Patch128:	linux-2.4.3-sb.patch
# ideraid driver updates
Patch129:	linux-2.4.5-ideraid.patch
# Pete's IDETAPE fixes
Patch130:	linux-2.4.6-idetape.patch
# don't allocate highmem pages on non-highmem machines
Patch131:	linux-2.4.6-nohighmem.patch
# another sb16 pnp id
Patch132:	linux-2.4.6-sb_id.patch
# DAC960 build fix
Patch133:	linux-2.4.7-DAC960-completion.patch
# Reiserfs fixes
Patch134:	ftp://ftp.reiserfs.org/pub/reiserfs-for-2.4/2.4.7.pending/2.4.7-old-format.dif.bz2
Patch135:	ftp://ftp.reiserfs.org/pub/reiserfs-for-2.4/2.4.7.pending/2.4.7-unlink-truncate-rename-rmdir.dif.bz2
Patch136:	ftp://ftp.reiserfs.org/pub/reiserfs-for-2.4/2.4.7.pending/journal-replay.patch
Patch137:	ftp://ftp.reiserfs.org/pub/reiserfs-for-2.4/2.4.7.pending/panic-in-reiserfs_read_super.patch
Patch138:	linux-quota-bug.patch
Patch139:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
Patch140:	linux-UDF.fix
Patch141:	http://people.FreeBSD.org/~gibbs/linux/linux-aic7xxx-%{aic_version}.patch.gz

# Patches fixing other patches or 3rd party sources ;)

Patch900:	kernel-i8255-asm-fix.patch
Patch901:	dc395-patch-PLD-fix.patch
# patch to fix LIDS stupidity
Patch902:	linux-lids-fixpatch.patch
# patch to fix problem wit ABI and LIDS
Patch903:	linux-lids-with-abi.patch
Patch904:	linux-vlan-fixpatch.patch
Patch905:	linux-ipvs+ext3.patch
Patch906:	linux-ext3-quota.patch
# tweaks for grsecurity, description inside patch
Patch907:	linux-grsecurity-fixes.patch

# Linus's -pre
#Patch1000:	ftp://ftp.kernel.org/pub/linux/kernel/testing/patch-2.4.7-%{pre_version}.gz

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	egcs
%endif
Provides:	%{name}-up = %{version}
Provides:	module-info
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha
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
%{?_with_lids:%setup -q -a3 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -n linux}
%{!?_with_lids:%setup -q -a3 -a5 -a6 -a7 -a9 -a10 -a11 -a12 -a13 -a14 -n linux}
#%patch1000 -p1
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch10 -p1
%patch100 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%if%{?_without_grsec:0}%{!?_without_grsec:1}
%patch9 -p1
%patch907 -p1
%endif

%patch101 -p0
%patch102 -p0
%patch103 -p1
%patch104 -p0
%patch105 -p0
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p4
#%patch112 -p1
%patch113 -p1
%patch114 -p1
%ifarch alpha
%patch115 -p1
%endif
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p2
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p0
%patch140 -p0
%patch141 -p1

%patch900 -p0 
%patch901 -p0
%patch906 -p1

# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Fore 200e ATM NIC
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch
#patch -p1 -s <linux-2.4.0-test3-fore200e-0.2g/linux-2.4.0-test3-fore200e-0.2g.patch

# Netfilter
echo Adding Netfilter
for i in netfilter-patches/* ; do
	if [ -f $i -a "$i" != "netfilter-patches/isapplied" ] ; then
		patch -p1 <$i
	fi
done
(KERNEL_DIR=`pwd` ; export KERNEL_DIR
cd netfilter-patches/patch-o-matic
ANS=""
for i in `echo *.patch.ipv6` `echo *.patch` ; do ANS="${ANS}y\n" ; done
echo -e $ANS | ./runme)

%if %{?_with_lids:1}%{!?_with_lids:0}
# LIDS
echo Adding LIDS
cd lids-%{lids_version}
%patch903 -p1
cd ..
patch -p1 -s <lids-%{lids_version}/lids-%{lids_version}.patch
%endif

# IPVS
echo Adding IPVS
%patch905 -p1
for i in ipvs-%{ipvs_version}/*.diff ; do
	patch -p1 -s <$i
done
mkdir net/ipv4/ipvs
cp ipvs-%{ipvs_version}/ipvs/*.{c,h,in} net/ipv4/ipvs
cp ipvs-%{ipvs_version}/ipvs/linux_net_ipv4_ipvs_Makefile net/ipv4/ipvs/Makefile

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

# 802.1Q VLANs
echo Adding VLANs
cd vlan
%patch904 -p1
cd ..
patch -p1 -s <vlan/vlan_2.4.patch

# IP personality
echo Adding IP Personality 
patch -p1 -s <ippersonality-%{IPperson_version}/patches/ippersonality-20010724-linux-2.4.7.diff

# JFS
echo Adding JFS
patch -p1 -s <jfs-2.4.common-v1.0.6-patch
patch -p1 -s <jfs-2.4.7-v1.0.6-patch

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
	if [ -n "$1" ] ; then
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
		ExtraVer="-%{release}$1"
		echo BUILDING A KERNEL FOR $1...
		shift
	else
%ifarch %{ix86}
		Config="ia32"
%else
		Config="%{_target_cpu}"
%endif
		KernelVer=%{version}-%{release}
		ExtraVer="-%{release}"
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
	cat %{SOURCE1005} >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1006} >> arch/$RPM_ARCH/defconfig
	cat %{SOURCE1007} >> arch/$RPM_ARCH/defconfig
	if [ "$LIDS" = "lids" ] ; then
		echo ENABLING LIDS...
		cat %{SOURCE1000} >> arch/$RPM_ARCH/defconfig
		KernelVer="${KernelVer}-lids"
		ExtraVer="${ExtraVer}-lids"
	fi

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
	%{__make} boot
%endif
%endif
%ifarch sparc
	sparc32 %{__make} modules
%else
	%{__make} modules
%endif

	mkdir -p $KERNEL_BUILD_DIR-installed/boot
	install System.map $KERNEL_BUILD_DIR-installed/boot/System.map-$KernelVer
%ifarch %{ix86}
	cp arch/i386/boot/bzImage $KERNEL_BUILD_DIR-installed/boot/vmlinuz-$KernelVer
%endif
%ifarch alpha sparc sparc64
	gzip -cfv vmlinux > vmlinuz
	install vmlinux $KERNEL_BUILD_DIR-installed/boot/vmlinux-$KernelVer
	install vmlinuz $KERNEL_BUILD_DIR-installed/boot/vmlinuz-$KernelVer
%endif
     %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_BUILD_DIR-installed \
	KERNELRELEASE=$KernelVer
}

KERNEL_BUILD_DIR=`pwd`
rm -rf $KERNEL_BUILD_DIR-installed
install -d $KERNEL_BUILD_DIR-installed

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
BuildKernel BOOT
%endif
%endif

# building i8255 module
%{__make} -C i8255

%install
umask 022
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{include,src/linux-%{version}-%{release}}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" "-lids" smp smp-lids BOOT ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf /usr/src/linux-%{version}-%{release} $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done
ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT/usr/include/linux
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

%ifarch sparc sparc64
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT/usr/include/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT/usr/include/asm-sparc64
sh %{SOURCE2} $RPM_BUILD_ROOT/usr/include
cp -a %{SOURCE2} $RPM_BUILD_ROOT/usr/include/asm/BuildASM
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}-%{release}/

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}-%{release}

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
cat %{SOURCE1005} >> .config
cat %{SOURCE1006} >> .config
cat %{SOURCE1007} >> .config

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
cat %{SOURCE1005} >> .config
cat %{SOURCE1006} >> .config
cat %{SOURCE1007} >> .config

%{__make} oldconfig
mv include/linux/autoconf.h include/linux/autoconf-smp.h

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}-%{release}/include/linux/autoconf.h

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
%{__make} symlinks 
%{__make} include/linux/version.h
%{__make} "`pwd`/include/linux/modversions.h"

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well, after we fix the paths

%{__make} depend 
find $RPM_BUILD_ROOT/usr/src/linux-%{version}-%{release} -name ".*depend" | \
while read file ; do
	mv $file $file.old
	sed -e "s|$RPM_BUILD_ROOT\(/usr/src/linux\)|\1|g" < $file.old > $file
	rm -f $file.old
done

%{__make} clean
rm -f scripts/mkdep

%if %{?_with_lids:1}%{!?_with_lids:0}
# LIDS config
cat %{SOURCE1000} >> $RPM_BUILD_ROOT/usr/src/linux-%{version}-%{release}/.config.lids
%endif

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-installed

# do this for upgrades...in case the old modules get removed we have
# loopback in the kernel so that mkinitrd will work.
#%pre modules
%pre
/sbin/modprobe loop 2> /dev/null > /dev/null
exit 0

%pre smp
/sbin/modprobe loop 2> /dev/null > /dev/null
exit 0

%pre BOOT
/sbin/modprobe loop 2> /dev/null > /dev/null
exit 0

%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null 
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

%if %{?_with_lids:1}%{!?_with_lids:0}
%post lids
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}-lids /boot/vmlinuz
ln -sf System.map-%{version}-%{release}-lids /boot/System.map

geninitrd -f --fs=rom /boot/initrd-%{version}-%{release}-lids.gz %{version}-%{release}-lids
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}-lids.gz /boot/initrd

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
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

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
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

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp-lids /lib/modules/%{version}
%endif

%post BOOT
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}BOOT /boot/vmlinuz
ln -sf System.map-%{version}-%{release}BOOT /boot/System.map

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}BOOT /lib/modules/%{version}

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
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}BOOT" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version}-%{release} /usr/src/linux

%postun headers
if [ -L /usr/src/linux ]; then 
	if [ "`ls -l /usr/src/linux | awk '{ print $11 }'`" = "linux-%{version}-%{release}" ]; then
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
/boot/vmlinux-%{version}-%{release}BOOT
%endif
/boot/vmlinuz-%{version}-%{release}BOOT
/boot/System.map-%{version}-%{release}BOOT
%dir /lib/modules/%{version}-%{release}BOOT
%ifarch i386
/lib/modules/%{version}-%{release}BOOT/pcmcia
%endif
/lib/modules/%{version}-%{release}BOOT/kernel
/lib/modules/%{version}-%{release}BOOT/build
/lib/modules/%{version}-%{release}BOOT/modules.dep
/lib/modules/%{version}-%{release}BOOT/modules.*map
/lib/modules/%{version}-%{release}BOOT/modules.generic_string
%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir /usr/src/linux-%{version}-%{release}
/usr/src/linux-%{version}-%{release}/include
/usr/include/asm
/usr/include/linux

%files source
%defattr(-,root,root,755)
/usr/src/linux-%{version}-%{release}/Documentation
/usr/src/linux-%{version}-%{release}/abi
/usr/src/linux-%{version}-%{release}/arch
/usr/src/linux-%{version}-%{release}/crypto
/usr/src/linux-%{version}-%{release}/drivers
/usr/src/linux-%{version}-%{release}/fs
/usr/src/linux-%{version}-%{release}/grsecurity
/usr/src/linux-%{version}-%{release}/i8255
/usr/src/linux-%{version}-%{release}/init
/usr/src/linux-%{version}-%{release}/ipc
/usr/src/linux-%{version}-%{release}/kdb
/usr/src/linux-%{version}-%{release}/kernel
/usr/src/linux-%{version}-%{release}/lib
/usr/src/linux-%{version}-%{release}/mm
/usr/src/linux-%{version}-%{release}/net
/usr/src/linux-%{version}-%{release}/scripts
/usr/src/linux-%{version}-%{release}/.config
%{?_with_lids:/usr/src/linux-%{version}-%{release}/.config.lids}
/usr/src/linux-%{version}-%{release}/.depend
/usr/src/linux-%{version}-%{release}/.hdepend
/usr/src/linux-%{version}-%{release}/COPYING
/usr/src/linux-%{version}-%{release}/CREDITS
/usr/src/linux-%{version}-%{release}/MAINTAINERS
/usr/src/linux-%{version}-%{release}/Makefile
/usr/src/linux-%{version}-%{release}/README
/usr/src/linux-%{version}-%{release}/REPORTING-BUGS
/usr/src/linux-%{version}-%{release}/Rules.make
