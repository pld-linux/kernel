#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
%define		test_build		0
#
%define		pre_version		pre1
%define		lids_version		1.0.7-2.4.3
%define		ipvs_version		0.2.8
%define		freeswan_version	snap2001feb24b
%define 	aacraid_version		1.0.6
%define		wlan_version		0.1.7
%define		sym_ncr_version		sym-1.7.3-ncr-3.4.3
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.4.4
Release:	1
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
Source7:	linux-netfilter-patches-20010504.tar.gz
Source8:	http://www.lids.org/download/lids-%{lids_version}.tar.gz
Source9:	http://www.linuxvirtualserver.org/software/kernel-2.4/ipvs-%{ipvs_version}.tar.gz
Source10:	http://www.linux-wlan.com/linux-wlan/linux-wlan-ng-%{wlan_version}.tar.gz
Source11:	ftp://ftp.tux.org/pub/people/gerard-roudier/drivers/linux/stable/%{sym_ncr_version}.tar.gz
Source12:	http://www.komacke.com/ftp/rl2isa-driver/rl2_driver.tgz
Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-i386-BOOT.config
Source30:	%{name}-i586.config
Source31:	%{name}-i586-smp.config
Source40:	%{name}-i686.config
Source41:	%{name}-i686-smp.config
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

# New features

Patch0:		%{name}-pldfblogo.patch
Patch1:		ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/patch-int-2.4.3.1.gz
Patch2:		linux-2.4.2-freeswan-%{freeswan_version}.patch.gz
## orginal are here: http://domsch.com/linux/aacraid/linux-2.4.3-aacraid-030101.patch
## this need small changes to applay in PLD.
Patch3:		linux-2.4.3-aacraid-030101.patch
# Reiserfs/NFS patches
Patch4:		linux-nfsd_operations.patch
# http://home.sch.bme.hu/~cell/br2684/dist/010402/br2684-against2.4.2.diff
Patch5:		br2684-against2.4.4.diff
# XFS patches
#Patch6:		ftp://linux-xfs.sgi.com/projects/xfs/download/latest/patches/linux-2.4.4-core-xfs-1.0.patch.gz
#Patch7:		ftp://linux-xfs.sgi.com/projects/xfs/download/latest/patches/linux-2.4-xfs-1.0.patch.gz
#Patch8:		linux-2.4-xfs-nfsdops.patch
# Compressed iso9660 filesystem
Patch9:		ftp://ftp.kernel.org/pub/linux/kernel/people/hpa/filemap-2.4.4-1.diff.gz
Patch10:	ftp://ftp.kernel.org/pub/linux/kernel/people/hpa/zisofs-2.4.5-pre1-5.diff.gz
Patch11:	linux-abi-2.4.3.0-PLD.patch
Patch12:	http://www.uow.edu.au/~andrewm/linux/cpus_allowed.patch

# Assorted bugfixes

# Quota fixes
# ftp://atrey.karlin.mff.cuni.cz/pub/local/jack/quota/v2.4/quota-fix-2.4.3-1.diff
Patch100:	quota-fix-2.4.4-1.diff.gz
# from LKML
Patch101:	linux-scsi-debug-bug.patch
Patch102:	linux-2.4.2-oom-killer.patch
Patch103:	linux-2.4.2-raw-ip.patch
Patch104:	PCI_ISA_bridge.patch
Patch105:	linux-2.4.2-nvram-hdd.patch
Patch106:	linux-2.4-fix-kapm.patch
Patch107:	patch-uk3
Patch108:	patch-uk5
Patch109:	epca-fix-missing-unregister-driver.patch
Patch110:	ramdisk-VM.fix
Patch111:	linux-2.4.2-Davicom-card.patch
Patch112:	linux-ram-disk-free.patch
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch113:	linux-2.4.2-pcnet-parms.patch
# Kernel crashes during making reiser-module:
Patch114:	%{name}-reiser.patch
Patch115:	ftp://ftp.kernel.org/pub/linux/kernel/people/hedrick/ide-2.4.3/ide.2.4.3-p4.03132001.patch.gz

# Patches fixing other patches or 3rd party sources ;)

Patch900:	kernel-i8255-asm-fix.patch
Patch901:	dc395-patch-PLD-fix.patch
# aacraid fix
Patch902:	http://domsch.com/linux/aacraid/linux-2.4.3-axboe-scsi-max-sec.patch
Patch903:	rl2-include.patch
# work around bugs in windows95/2000 VJ header compression implementations.
Patch904:	ipvs-ip_select_ident.patch
# patch for fix LIDS install
Patch905:	linux-lids-1.0.7-PLD.fix

# Adaptec AIC7XXX patch rewriten to PLD.
# orginal was here.
# http://people.FreeBDS.org/~gibbs/linux/linux-aic7xxx-6.1.13-2.4.4.patch.gz
Patch906:	linux-aic7xxx-6.1.13-PLD.patch.gz

# Linus's -pre
Patch1000:	ftp://ftp.kernel.org/pub/linux/kernel/testing/patch-2.4.5-%{pre_version}.gz

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	egcs
%endif
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
%setup -q -a3 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -n linux
%patch1000 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch12 -p1

%patch100 -p1
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
#%patch111 -p0
%patch112 -p1
%patch113 -p1
%patch114 -p4
%patch115 -p1

%patch900 -p0 
%patch901 -p0
%patch902 -p1

# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Fore 200e ATM NIC
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch
#patch -p1 -s <linux-2.4.0-test3-fore200e-0.2g/linux-2.4.0-test3-fore200e-0.2g.patch

# Netfilter
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

# LIDS
%patch905 -p0
patch -p1 -s <lids-%{lids_version}/lids-%{lids_version}.patch

# IPVS
for i in ipvs-%{ipvs_version}/*.diff ; do
	patch -p1 -s <$i
done
mkdir net/ipv4/ipvs
cp ipvs-%{ipvs_version}/ipvs/*.{c,h,in} net/ipv4/ipvs
cp ipvs-%{ipvs_version}/ipvs/linux_net_ipv4_ipvs_Makefile net/ipv4/ipvs/Makefile
patch -p1 -s < %{PATCH904}

# Remove -g from drivers/atm/Makefile and net/ipsec/Makefile
mv -f drivers/atm/Makefile drivers/atm/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*//g' drivers/atm/Makefile.orig > drivers/atm/Makefile

# Free S/Wan
mv -f net/ipsec/Makefile net/ipsec/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*-g//g' net/ipsec/Makefile.orig > net/ipsec/Makefile

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

## install NCR/Symbios controler
mv %{sym_ncr_version}/*.{c,h} drivers/scsi
mv %{sym_ncr_version}/{README,ChangeLog}.* Documentation
rm -rf %{sym_ncr_version}

## install RangeLAN2 driver
#mv rl2-1.7.1 drivers/net/rl2
#%patch903 -p1

## must be here, in other time make errors with LIDS
%patch11 -p1

## Adaptec AIC7XXX patch
%patch906 -p1

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
		Config="%{_target_cpu}"-$1
		KernelVer=%{version}-%{release}$1
		echo BUILDING A KERNEL FOR $1...
		shift
	else
		Config="%{_target_cpu}"
		KernelVer=%{version}-%{release}
		echo BUILDING THE NORMAL KERNEL...
	fi
	cp $RPM_SOURCE_DIR/kernel-$Config.config arch/$RPM_ARCH/defconfig
	if [ "$LIDS" = "lids" ] ; then
		echo ENABLING LIDS...
		cat %{SOURCE1000} >> arch/$RPM_ARCH/defconfig
		KernelVer="${KernelVer}-lids"
	fi

	%{__make} mrproper
	ln -sf arch/$RPM_ARCH/defconfig .config

%ifarch sparc
	sparc32 %{__make} oldconfig
	sparc32 %{__make} dep
%else
	%{__make} oldconfig
	%{__make} dep
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

# UP LIDS KERNEL
BuildKernel lids

# SMP LIDS KERNEL
BuildKernel lids smp

# BOOT kernel
%ifnarch i586 i686
BuildKernel BOOT
%endif
%endif

# building i8255 module
%{__make} -C i8255

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" "-lids" smp smp-lids BOOT ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf /usr/src/linux-%{version} $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done
ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux

bzip2 -dc %{SOURCE0} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/
mv -f $RPM_BUILD_ROOT/usr/src/linux $RPM_BUILD_ROOT/usr/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

gzip -dc %{SOURCE3} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE5} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE6} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE7} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE8} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE9} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE10} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{SOURCE11} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/linux-%{version}

# Pre patch
gzip -dc %{PATCH1000} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}

patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH0}
gzip -dc %{PATCH1} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH2} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH3}
gzip -dc %{PATCH4} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH5}
gzip -dc %{PATCH6} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH7} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH8}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH9}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH10}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH12}

gzip -dc %{PATCH100} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH101}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH102}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH103}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH104}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH105}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH106}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH107}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH108}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH109}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH110}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH111}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH112}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH113}
patch -p4 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH114}
gzip -dc %{PATCH115} | patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version}

patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH900}
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH901}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH902}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH903}

# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT/usr/src/linux-%{version}/dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Fore 200e ATM NIC
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT/usr/src/linux-%{version}/linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch
#patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT/usr/src/linux-%{version}/linux-2.4.0-test3-fore200e-0.2g/linux-2.4.0-test3-fore200e-0.2g.patch

# Netfilter
(cd $RPM_BUILD_ROOT/usr/src/linux-%{version}
for i in netfilter-patches/* ; do
	if [ -f $i -a "$i" != "netfilter-patches/isapplied" ] ; then
		patch -p1 <$i
	fi
done
(KERNEL_DIR=`pwd` ; export KERNEL_DIR
cd netfilter-patches/patch-o-matic
ANS=""
for i in `echo *.patch.ipv6` `echo *.patch` ; do ANS="${ANS}y\n" ; done
echo -e $ANS | ./runme))

# LIDS
patch -p0 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH905}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT/usr/src/linux-%{version}/lids-%{lids_version}/lids-%{lids_version}.patch
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}-smp.config $RPM_BUILD_ROOT/usr/src/linux-%{version}/.config.lids

# IPVS
for i in $RPM_BUILD_ROOT/usr/src/linux-%{version}/ipvs-%{ipvs_version}/*.diff ; do
	patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $i
done
mkdir $RPM_BUILD_ROOT/usr/src/linux-%{version}/net/ipv4/ipvs
cp $RPM_BUILD_ROOT/usr/src/linux-%{version}/ipvs-%{ipvs_version}/ipvs/*.{c,h,in} $RPM_BUILD_ROOT/usr/src/linux-%{version}/net/ipv4/ipvs
cp $RPM_BUILD_ROOT/usr/src/linux-%{version}/ipvs-%{ipvs_version}/ipvs/linux_net_ipv4_ipvs_Makefile $RPM_BUILD_ROOT/usr/src/linux-%{version}/net/ipv4/ipvs/Makefile
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH904}

# Remove -g from drivers/atm/Makefile
mv -f $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/atm/Makefile \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/atm/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*//g' $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/atm/Makefile.orig \
	> $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/atm/Makefile

# Fix EXTRAVERSION and CC in main Makefile
mv -f $RPM_BUILD_ROOT/usr/src/linux-%{version}/Makefile $RPM_BUILD_ROOT/usr/src/linux-%{version}/Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION = -%{release}/g' \
%ifarch %{ix86} alpha sparc
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= egcs/g' \
%endif
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    $RPM_BUILD_ROOT/usr/src/linux-%{version}/Makefile.orig >$RPM_BUILD_ROOT/usr/src/linux-%{version}/Makefile

%ifarch sparc sparc64
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT%{_includedir}/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT%{_includedir}/asm-sparc64
sh $RPM_SOURCE_DIR/kernel-BuildASM.sh $RPM_BUILD_ROOT%{_includedir}
cp -a $RPM_SOURCE_DIR/kernel-BuildASM.sh $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

## SymBios/NCR drivers install
mv $RPM_BUILD_ROOT/usr/src/linux-%{version}/%{sym_ncr_version}/*.{c,h} $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/scsi
mv $RPM_BUILD_ROOT/usr/src/linux-%{version}/%{sym_ncr_version}/{README,ChangeLog}.* $RPM_BUILD_ROOT/usr/src/linux-%{version}/Documentation
rm -rf $RPM_BUILD_ROOT/usr/src/linux-%{version}/%{sym_ncr_version}

patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH11}

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

# LIDS config
cat %{SOURCE1000} >> $RPM_BUILD_ROOT/usr/src/linux-%{version}/.config.lids

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

%postun lids
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}-lids" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}-lids.gz

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%postun lids-smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp-lids" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp-lids.gz

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
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/i8255
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/.config
%{_prefix}/src/linux-%{version}/.config.lids
%{_prefix}/src/linux-%{version}/.depend
%{_prefix}/src/linux-%{version}/.hdepend
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%{_prefix}/src/linux-%{version}/Rules.make
