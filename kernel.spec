%define		ow_version		2.2.20-ow1
%define		pcmcia_version		3.1.30
%define		freeswan_version	1.8
%define		reiserfs_version	3.5.34
%define		i2c_version		2.6.2
%define		bttv_version		0.7.60
%define		wlan_version		0.3.4
%define		tun_version		1.1
%define         vlan_version            1.0.1
%define		aic7xxx_version		6.2.3-2.2.19
%define		symncr_version		1.7.3c-ncr-3.4.3b
%define		jfs_version		1.0.5
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Name:		kernel
Version:	2.2.20
Release:	7.2
License:	GPL
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	ftp://ftp.openwall.com/linux/linux-%{ow_version}.tar.gz
Source4:	http://www.garloff.de/kurt/linux/dc395/dc395-133.tar.gz
Source5:	ftp://ftp.sourceforge.net/pub/sourceforge/pcmcia-cs/pcmcia-cs-%{pcmcia_version}.tar.gz
Source6:	ftp://ftp.tux.org/tux/roudier/drivers/linux/stable/sym-%{symncr_version}.tar.gz
Source7:	ftp://ftp.linux-wlan.com/linux-wlan/linux-wlan-%{wlan_version}.tar.gz
Source9:	serial-5.05.tar.gz
Source10:	http://vtun.sourceforge.net/tun/tun-%{tun_version}.tar.gz
Source11:	http://scry.wanfear.com/~greear/vlan/vlan.%{vlan_version}.tar.gz
Source12:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-2.2-%{jfs_version}-patch.tar.gz
Source13:	http://www.netroedge.com/~lm78/archive/i2c-%{i2c_version}.tar.gz
Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-i386-BOOT.config
Source23:	%{name}-i586.config
Source24:	%{name}-i586-smp.config
Source25:	%{name}-i686.config
Source26:	%{name}-i686-smp.config
Source27:	%{name}-sparc.config
Source28:	%{name}-sparc-smp.config
Source29:	%{name}-sparc-BOOT.config
Source30:	%{name}-sparc64.config
Source31:	%{name}-sparc64-smp.config
Source32:	%{name}-sparc64-BOOT.config
Source33:	%{name}-alpha.config
Source34:	%{name}-alpha-smp.config
Source35:	%{name}-alpha-BOOT.config
Patch0:		%{name}-pldfblogo.patch
Patch1:		pcmcia-cs-%{pcmcia_version}-smp-compilation-fix.patch
Patch2:		http://people.freebsd.org/~gibbs/linux/linux-aic7xxx-%{aic7xxx_version}.patch.gz
Patch3:		ftp://ftp.reiserfs.org/pub/reiserfs-for-2.2/linux-2.2.19-reiserfs-%{reiserfs_version}-patch.bz2
Patch4:		ftp://ftp.kernel.org/pub/linux/kernel/crypto/v2.2/patch-int-2.2.18.3.gz
Patch5:		linux-2.2.18-freeswan-%{freeswan_version}.patch
Patch6:		wanrouter-v2215.patch.gz
Patch7:		linux-ipv6-addrconf.patch
# based on http://support.3com.com/infodeli/tools/nic/linux/3c90x-1.0.0i.tar.gz
Patch8:		%{name}-3c90x.patch
Patch9:		linux-ipv6-glibc2.2.patch
# based on http://bridge.sourceforge.net/patches/bridge-1.0.2-against-2.2.20.diff
Patch10:	bridge-1.0.2-against-2.2.20.diff
Patch11:	bridge-ipchains-against-1.0.2-against-2.2.20.diff
Patch12:	2.2.21-pre2_VIA.patch
Patch13:	2.2.21-pre2_ati.patch
Patch20:	http://download.sourceforge.net/linux1394/ieee1394-2.2.19-20010527.gz
Patch21:	linux-tasks.patch
Patch22:	%{name}-ipvs-1.0.8-2.2.19.patch
Patch23:	linux-raw.patch
Patch24:	%{name}-panaview_kbd.patch
Patch25:	linux-2.2.19-pci.patch
Patch26:	%{name}-sysctl-ipv6.patch
Patch27:	%{name}-udf.patch
# based on	http://people.redhat.com/mingo/raid-patches/raid-2.2.20-A0
Patch28:	raid-2.2.20-A0.patch.bz2
Patch29:	http://www.ans.pl/ide/ide.2.2.21.01152002-Ole.patch.gz
Patch30:	linux-2.2.18-atm-0.59-fore200e-0.1f.patch.gz
Patch31:	%{name}-flip.patch
Patch33:	%{name}-ipsec-bridge.patch
Patch34:	%{name}-wanrouter-bridge.patch
Patch35:	linux-netdrivers_vlan.patch
Patch36:	atm-unresolved.patch
Patch37:	af-unresolved.patch
Patch38:	linux-2.2.20-pcmcia-without-iee1394.patch.bz2
# based on ftp://ftp.kernel.org/people/andrea/kernels/v2.2/2.2.20pre9aa2/40_lfs-2.2.20pre9aa2-27.bz2
#Patch39:       linux-2.2.20-lfs.patch
Patch40:        %{name}-scripts-include-dir.patch
Patch41:	%{name}-serial-initialisation.patch
Patch42:	%{name}-flip-serial5.05.patch
Patch43:	%{name}-vlan_bridge.patch
Patch44:	tulip-patch-0.91.patch.bz2

Patch100:	jfs-2.2.20-v%{jfs_version}-patch
Patch101:	linux-atm.patch
Patch102:	htb2_2.2.17.diff
Patch103:	bridge-netsyms.patch
#i2o patch from ftp://ftp.adaptec.com/raid/asr/unix/asr_linux_v242_drv.rpm 
Patch104:	dpt_i2o-2.2.19.diff
Patch105:	linux-2.2.19-bttv-%{bttv_version}.patch.bz2
Patch106:	linux-2.2.20-undo-ioport.h.patch.bz2

Patch1500:	linux-sparc_ide_fix.patch.2.2.19
Patch1501:	%{name}-sparc-zs.h.patch
Patch1502:	%{name}-sparc_netsyms.patch
Patch1503:	%{name}-sym53c8xx.patch

# HTB from http://luxik.cdi.cz/~devik/qos/htb/

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	egcs
%endif
%ifarch sparc
BuildRequires:	sparc32
%endif
Provides:	%{name}-up = %{version}
%ifarch %{ix86}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(i2c) = %{i2c_version}
Provides:       i2c = %{i2c_version}
Provides:	bttv = %{bttv_version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Autoreqprov:	no
Prereq:		modutils
Prereq:		fileutils
Prereq:		geninitrd
#Prereq:		rc-boot
Obsoletes:	kernel-modules

#i2c and bttv packages are obsolete
Obsoletes:	i2c-devel
Obsoletes:	kernel-i2c
Obsoletes:	bttv
Obsoletes:	kernel-misc-bttv

ExclusiveArch:	%{ix86} sparc sparc64 alpha
%ifarch		%{ix86}
BuildRequires:	bin86
BuildRequires:	autoconf
BuildRequires:	automake
%endif
Autoreqprov:    no

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
Twojego komputera.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
%ifarch %{ix86}
Provides:	%{name}(reiserfs) = %{version}
Provides:       %{name}(i2c) = %{i2c_version}
Provides:       i2c = %{i2c_version}
Provides:	bttv = %{bttv_version}

%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Prereq:		modutils
Prereq:		fileutils
Prereq:		geninitrd
#Prereq:		rc-boot
Obsoletes:      kernel-modules

#i2c and bttv packages are obsolete
Obsoletes:      i2c-devel
Obsoletes:      kernel-smp-i2c
Obsoletes:      bttv
Obsoletes:      kernel-smp-misc-bttv
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nécessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand même fonctionner pour les système mono-processeur.

%description -l de smp
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Prereq:		modutils
Prereq:		fileutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description -l fr BOOT
Ce package inclut une version allégée du noyau de Linux version
%{version}. Ce kernel et utilisé pour les disquettes de boot
d'installation et ne doivent pas être utilisées pour un système
classique, beaucoup d'options dans le kernel ont étaient désactivées a
cause de la contrainte d'espace.

%description -l de BOOT
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
%ifarch %{ix86}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	i2c-devel = %{i2c_version}
%endif
Provides:	%{name}-headers(ipvs) = %{version}
Provides:	%{name}-headers(rawio) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbedne do rekompilacji j±dra
oraz niektórych programów.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja j±dra
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê j±dra z katalogu
/usr/src/linux/Documentation.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuxa
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
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
%setup -q -a3 -a4 -a5 -a6 -a7 -a9 -a10 -a11 -a13 -n linux

%patch0 -p1
%patch1 -p0
# disable aic7xxx patch on sparc (this must be reported to aic7xxx driver maintainer)
%ifnarch sparc sparc64
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
#%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
#%patch39 -p1
%patch40 -p1
%patch44 -p1

# preparing linux/README file to backup
mv README README.kernel
# unpacking %{SOURCE12}
tar zxvf %{SOURCE12}
# move jfs README file to README.jfs
mv README README.jfs
# back kernel README file
mv README.kernel README

# 802.1Q VLANs
%patch43 -p1
patch -p1 -s <vlan.%{vlan_version}/vlan_2.2.patch

cd serial-5.05
%patch41 -p1
%patch42 -p1
./install-in-kernel ../
cd .. 

# i2c
%ifarch %{ix86}
cd i2c-%{i2c_version}
mkpatch/mkpatch.pl . ../../linux | (cd ../../linux; patch -p1 -s)
cd ..
%patch105 -p1
%patch106 -p1
%endif

# 2.2.20ow1
patch -p1 -s <linux-%{ow_version}/linux-%{ow_version}.diff

# symbios drivers
mv sym-%{symncr_version}/*.{c,h} drivers/scsi
mv sym-%{symncr_version}/{README,ChangeLog}.* Documentation

# Tekram DC395/315 U/UW SCSI host driver
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# JFS 1.0.5
patch -p1 -s <jfs-2.2.common-v%{jfs_version}-patch

%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

%patch1500 -p1
%patch1501 -p1
%ifarch sparc64
%patch1502 -p1
%endif
%patch1503 -p1

%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a special kernel we want to build?
	if [ "$1" = "BOOT" ]; then
		Config="%{_target_cpu}-BOOT"
		KernelVer=%{version}
		echo BUILDING A KERNEL FOR BOOT...
	elif [ -n "$1" ] ; then
		Config="%{_target_cpu}"-$1
		KernelVer=%{version}-%{release}$1
		echo BUILDING A KERNEL FOR $1...
	else
		Config="%{_target_cpu}"
		KernelVer=%{version}-%{release}
		echo BUILDING THE NORMAL KERNEL...
	fi
	cp $RPM_SOURCE_DIR/kernel-$Config.config arch/$RPM_ARCH/defconfig

%ifarch %{ix86}
	perl -p -i -e "s/-m486//" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=486/-m486 -DCPU=486/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=586/-mpentium -DCPU=586/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=686/-mpentiumpro -DCPU=686/" arch/i386/Makefile
%endif

	%{__make} mrproper
	ln -sf arch/$RPM_ARCH/defconfig .config

%ifarch sparc
	sparc32 %{__make} oldconfig
	sparc32 %{__make} dep 
%else
	%{__make} oldconfig
	%{__make} dep
%endif
	make include/linux/version.h 

%ifarch %{ix86} alpha sparc
	KERNELCC="egcs"
%endif
%ifarch sparc64
	KERNELCC="sparc64-linux-gcc"
%endif

%ifarch %{ix86}
	%{__make} bzImage EXTRAVERSION="-%{release}"
%else
%ifarch sparc
	sparc32 %{__make} boot EXTRAVERSION="-%{release}"
%else
	%{__make} boot EXTRAVERSION="-%{release}"
%endif
%endif
%ifarch sparc
	sparc32 %{__make} modules EXTRAVERSION="-%{release}"
%else
	%{__make} modules EXTRAVERSION="-%{release}"
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
     %{__make} INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR modules_install KERNELRELEASE=$KernelVer
}

BuildPCMCIA() {
if [ "$1" = "BOOT" ]; then
	PCMCIA_APM=--apm
	KernelVer=%{version}
	echo BUILDING A KERNEL PCMCIA MODULES FOR BOOT...
elif [ -n "$1" ] ; then
	PCMCIA_APM=--apm
	KernelVer=%{version}-%{release}$1
	echo BUILDING A KERNEL PCMCIA MODULES FOR $1...
else
	PCMCIA_APM=--noapm
	KernelVer=%{version}-%{release}
	echo BUILDING THE NORMAL KERNEL PCMCIA MODULES...
fi
cd pcmcia-cs-%{pcmcia_version}
%{__make} clean
./Configure \
	--noprompt \
	--trust \
	--cardbus \
	--current \
	--pnp \
	--srctree \
	$PCMCIA_APM \
	--kernel=$KERNEL_BUILD_DIR \
	--moddir=/lib/modules/$KernelVer \
	--kflags="-march=%{_target_cpu}" \
	--target=$KERNEL_INSTALL_DIR

mv config.mk config.mk.bak
mv Makefile Makefile.bak
mv clients/Makefile clients/Makefile.bak
sed "s/^MODDIR=.*/MODDIR=\/lib\/modules\/$KernelVer/" config.mk.bak > config.mk
sed "s/^DIRS =.*//" Makefile.bak > Makefile
sed "s/.*= 8390\..$//" clients/Makefile.bak > clients/Makefile

%{__make} all
#	CC=egcs \
#	CFLAGS="$RPM_OPT_FLAGS -Wall -Wstrict-prototypes -pipe" \
#	MFLAG="$RPM_OPT_FLAGS -O"

#	XFLAGS="$RPM_OPT_FLAGS -O -pipe -I../include -I$KERNEL_BUILD_DIR/include -D__KERNEL__ -DEXPORT_SYMTAB"

%{__make} PREFIX=$KERNEL_INSTALL_DIR install
cd ..

# Linux WLAN package extension for PCMCIA
cd linux-wlan-%{wlan_version}
%{__make} clean
mv config.mk config.mk.bak
kernelbase=`echo $KERNEL_BUILD_DIR| sed -e "sm/m\\\\\/mg"`
sed "s/^MODULES_DIR=.*/MODULES_DIR=$kernelbase-installed\/lib\/modules\/$KernelVer/" config.mk.bak > config.mk.bak2
sed "s/^MAKE_CS=.*/MAKE_CS=y/" config.mk.bak2 > config.mk.bak3
sed "s/^LINUX_SRC=.*/LINUX_SRC=$kernelbase/" config.mk.bak3 > config.mk.bak4
sed "s/^PCMCIA_SRC=.*/PCMCIA_SRC=$kernelbase\/pcmcia-cs-%{pcmcia_version}/" config.mk.bak4 > config.mk

cd driver
%{__make} all
	CC=egcs \
	CFLAGS="$RPM_OPT_FLAGS -Wall -Wstrict-prototypes -pipe" \
	XFLAGS="$RPM_OPT_FLAGS -O -pipe -I../include -I$KERNEL_BUILD_DIR/include -I$KERNEL_BUILD_DIR/pcmcia-cs-%{pcmcia_version}/include -D__KERNEL__ -DEXPORT_SYMTAB"

%{__make} PREFIX=$KERNEL_INSTALL_DIR install

cd ../..

cd tun-%{tun_version}
aclocal
autoconf
(cd linux
aclocal
autoconf)
%configure \
	--with-kernel="$KERNEL_BUILD_DIR"
make
install linux/tun.o "$KERNEL_INSTALL_DIR/lib/modules/$KernelVer/net"
cd ..

}


KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed

rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR


# NORMAL KERNEL
BuildKernel
%ifarch %{ix86}
BuildPCMCIA
%endif

# SMP-ENABLED KERNEL
BuildKernel smp
%ifarch %{ix86}
BuildPCMCIA smp
%endif

# BOOT kernel
%ifnarch i586 i686
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

BuildKernel BOOT
%ifarch %{ix86}
BuildPCMCIA BOOT
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed"
cp -a $KERNEL_INSTALL_DIR/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT%{_includedir}/asm

bzip2 -dc %{SOURCE0} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/
mv -f $RPM_BUILD_ROOT%{_prefix}/src/linux $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux
gzip -dc %{SOURCE9} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{SOURCE11} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH0}
%ifnarch sparc sparc64
gzip -dc %{PATCH2} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
%endif
bzip2 -dc %{PATCH3} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{PATCH4} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH5}
gzip -dc %{PATCH6} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH7}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH8}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH9}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH10}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH11}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH12}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH13}
gzip -dc %{PATCH20} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH21}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH22}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH23}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH24}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH25}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH26}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH27}
bzip2 -dc %{PATCH28} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{PATCH29} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH30} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH31}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH33}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH34}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH35}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH36}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH37}
#patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH39}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH40}
bzip2 -dc %{PATCH44} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH37}

# preparing linux/README file to backup
mv $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README.kernel
# unpacking %{SOURCE12}
gzip -dc %{SOURCE12} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
# move jfs README file to README.jfs
mv $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README.jfs
# back kernel README file
mv $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README.kernel $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/README

# VLAN
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH43}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} <vlan.%{vlan_version}/vlan_2.2.patch
rm -rf vlan.%{vlan_version}/

#serial
cd serial-5.05
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}/serial-5.05 < %{PATCH41}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}/serial-5.05 < %{PATCH42}
./install-in-kernel $RPM_BUILD_ROOT/usr/src/linux-%{version}
cd ..
rm -rf serial-5.05/

# i2c
%ifarch %{ix86}
tar xfz %{SOURCE13}
cd i2c-%{i2c_version}
mkpatch/mkpatch.pl . $RPM_BUILD_ROOT/usr/src/linux-%{version} | (cd $RPM_BUILD_ROOT/usr/src/linux-%{version}; patch -p1 -s)
cd ..
rm -rf i2c-%{i2c_version}/
bzip2 -dc %{PATCH105} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
bzip2 -dc %{PATCH106} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
%endif

# 2.2.20ow
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} <linux-%{ow_version}/linux-%{ow_version}.diff
rm -rf linux-%{ow_version}/

# symbios drivers
tar zxf %{SOURCE6}
mv sym-%{symncr_version}/*.{c,h} $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/scsi
mv sym-%{symncr_version}/{README,ChangeLog}.* $RPM_BUILD_ROOT/usr/src/linux-%{version}/Documentation
rm -rf sym-%{symncr_version}

# jfs 1.0.5
#patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH104}
patch -s -p1 -d  $RPM_BUILD_ROOT/usr/src/linux-%{version} < jfs-2.2.common-v%{jfs_version}-patch
# remove all jfs patches from linux/ directory
rm $RPM_BUILD_ROOT/usr/src/linux-%{version}/jfs-*


patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH101}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH102}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH103}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH104}

patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1500}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1501}
%ifarch sparc64
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1502}
%endif
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1503}

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}

%{__make} mrproper
find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f

install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config

%{__make} oldconfig
mv include/linux/autoconf.h include/linux/autoconf-up.h

install $RPM_SOURCE_DIR/kernel-%{_target_cpu}-smp.config .config
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

# add a rc-boot info
#install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rc-boot/images
#cat >$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rc-boot/images/pld-%{version}-%{release} <<EOF
#TYPE=linux
#ROOT=auto
#KERNEL=/boot/vmlinuz-%{version}-%{release}
#INITRD=/boot/initrd-%{version}-%{release}.gz
#EOF

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-installed


%post
test ! -f /boot/vmlinuz || mv -f /boot/vmlinuz /boot/vmlinuz.old
test ! -f /boot/System.map || mv -f /boot/System.map /boot/System.map.old
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

geninitrd /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
test ! -f /boot/initrd || mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

depmod -a -F /boot/System.map %{version}-%{release}

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

geninitrd /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
test ! -f /boot/initrd || mv -f /boot/initrd /boot/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}smp

depmod -a -F /boot/System.map %{version}-%{release}smp

%postun
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz


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
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}
%attr(600,root,root) /boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}/atm
%endif
/lib/modules/%{version}-%{release}/block
/lib/modules/%{version}-%{release}/cdrom
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}/fc4
%endif
/lib/modules/%{version}-%{release}/fs
/lib/modules/%{version}-%{release}/ipv4
/lib/modules/%{version}-%{release}/ipv6
/lib/modules/%{version}-%{release}/misc
/lib/modules/%{version}-%{release}/net
/lib/modules/%{version}-%{release}/scsi
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/usb
/lib/modules/%{version}-%{release}/video
%endif
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/pcmcia
%endif
#%config(missingok) %{_sysconfdir}/sysconfig/rc-boot/images

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}smp
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}smp
%attr(600,root,root) /boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}smp/atm
%endif
/lib/modules/%{version}-%{release}smp/block
/lib/modules/%{version}-%{release}smp/cdrom
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}/fc4
%endif
/lib/modules/%{version}-%{release}smp/fs
/lib/modules/%{version}-%{release}smp/ipv4
/lib/modules/%{version}-%{release}smp/ipv6
/lib/modules/%{version}-%{release}smp/misc
/lib/modules/%{version}-%{release}smp/net
/lib/modules/%{version}-%{release}smp/scsi
%ifarch %{ix86} 
/lib/modules/%{version}-%{release}smp/usb
/lib/modules/%{version}-%{release}smp/video
%endif
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/pcmcia
%endif
#%config(missingok) %{_sysconfdir}/sysconfig/rc-boot/images

%ifnarch i586 i686
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc
%{_libdir}/bootdisk/boot/vmlinux-%{version}
%endif
%{_libdir}/bootdisk/boot/vmlinuz-%{version}
%{_libdir}/bootdisk/boot/System.map-%{version}
%dir %{_libdir}/bootdisk/lib/modules/%{version}
#%{_libdir}/bootdisk/lib/modules/%{version}/atm
%{_libdir}/bootdisk/lib/modules/%{version}/block
%ifnarch sparc sparc64 alpha
%{_libdir}/bootdisk/lib/modules/%{version}/cdrom
%endif
%{_libdir}/bootdisk/lib/modules/%{version}/fs
#%{_libdir}/bootdisk/lib/modules/%{version}/ipv4
%{_libdir}/bootdisk/lib/modules/%{version}/ipv6
%{_libdir}/bootdisk/lib/modules/%{version}/misc
%{_libdir}/bootdisk/lib/modules/%{version}/net
%{_libdir}/bootdisk/lib/modules/%{version}/scsi
%ifarch %{ix86} 
%{_libdir}/bootdisk/lib/modules/%{version}/usb
%endif
%ifarch i386
%{_libdir}/bootdisk/lib/modules/%{version}/pcmcia
%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
#%ifarch sparc sparc64
#%{_includedir}/asm-sparc*
#%endif
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/modules
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/security
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
