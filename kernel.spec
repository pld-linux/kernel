%define		ow_version		2.2.20-ow2
%define		pcmcia_version		3.1.30
%define		freeswan_version	1.8
%define		reiserfs_version	3.5.35
%define		i2c_version		2.6.2
%define		bttv_version		0.7.60
%define		wlan_version		0.3.4
%define		tun_version		1.1
%define		vlan_version		1.0.1
%define		aic7xxx_version		6.2.3-2.2.19
%define		symncr_version		1.7.3c-ncr-3.4.3b
%define		jfs_version		1.0.5
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J╠dro Linuksa
Summary(ru):	Ядро Linux
Summary(uk):	Ядро Linux
Name:		kernel
Version:	2.2.21
Release:	1.2
License:	GPL
Group:		Base/Kernel
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
Source36:	%{name}-ppc.config
Source37:	%{name}-ppc-smp.config
Source38:	%{name}-ppc-BOOT.config
Patch0:		%{name}-pldfblogo.patch
Patch1:		pcmcia-cs-%{pcmcia_version}-smp-compilation-fix.patch
Patch2:		http://people.freebsd.org/~gibbs/linux/linux-aic7xxx-%{aic7xxx_version}.patch.gz
Patch3:		ftp://ftp.reiserfs.org/pub/reiserfs-for-2.2/linux-2.2.20-reiserfs-%{reiserfs_version}.diff.bz2
Patch4:		ftp://ftp.kernel.org/pub/linux/kernel/crypto/v2.2/patch-int-2.2.18.3.gz
Patch5:		linux-2.2.18-freeswan-%{freeswan_version}.patch
Patch6:		wanrouter-v2215.patch.gz
# based on http://bridge.sourceforge.net/patches/bridge-1.0.2-against-2.2.20.diff
Patch10:	bridge-1.0.2-against-2.2.20.diff
Patch11:	bridge-ipchains-against-1.0.2-against-2.2.20.diff
Patch12:	linux-ipv6-pld.patch

Patch20:	http://download.sourceforge.net/linux1394/ieee1394-2.2.19-20010527.gz
Patch21:	linux-tasks.patch
Patch22:	%{name}-ipvs-1.0.8-2.2.19.patch
Patch23:	linux-raw.patch
Patch24:	%{name}-panaview_kbd.patch
Patch25:	linux-2.2.19-pci.patch
Patch27:	%{name}-udf.patch
# based on	http://people.redhat.com/mingo/raid-patches/raid-2.2.20-A0
Patch28:	raid-2.2.20-A0.patch.bz2
# based on	http://www.ans.pl/ide/testing/ide.2.2.21.02042002-Ole.patch.gz
Patch29:	ide.2.2.21.07102002-PLD.patch.gz
Patch30:	linux-2.2.18-atm-0.59-fore200e-0.1f.patch.gz
Patch31:	%{name}-flip.patch
Patch33:	%{name}-ipsec-bridge.patch
Patch34:	%{name}-wanrouter-bridge.patch
Patch35:	linux-netdrivers_vlan.patch
Patch36:	atm-unresolved.patch
Patch38:	linux-2.2.20-pcmcia-without-iee1394.patch.bz2
# based on ftp://ftp.kernel.org/people/andrea/kernels/v2.2/2.2.20pre9aa2/40_lfs-2.2.20pre9aa2-27.bz2
Patch40:	2.2.21-pre2_Makefile.patch
Patch41:	%{name}-serial-initialisation.patch
Patch42:	%{name}-flip-serial5.05.patch
Patch43:	%{name}-vlan_bridge.patch
Patch44:	tulip-patch-0.91.patch.bz2
Patch100:	jfs-2.2.20-v%{jfs_version}-patch
Patch101:	linux-atm.patch
# HTB from http://luxik.cdi.cz/~devik/qos/htb/
Patch102:	htb2_2.2.17.diff
#i2o patch from ftp://ftp.adaptec.com/raid/asr/unix/asr_linux_v242_drv.rpm
Patch104:	dpt_i2o-2.2.19.diff
Patch105:	linux-2.2.19-bttv-%{bttv_version}.patch.bz2
Patch106:	linux-2.2.20-undo-ioport.h.patch.bz2
Patch107:	linux-2.2.20-icn-unresolved.patch.bz2
Patch108:	linux-2.2.20-agp_backport.patch.bz2
Patch109:	dc395-MAINTAINERS.patch
Patch110:	%{name}-nfs-fixes.patch
Patch111:	linux-2.2.20-pcilynx_unresolved.patch
Patch112:	linux-2.2.20-lfs.patch
Patch113:	bigmem-2.2.19pre3-21.bz2

Patch302:	ow2-fix-2.2.21-rc3.patch

Patch500:	2.2.20-reiserfs_ppc.patch
Patch501:	2.2.21-ppc-smp.patch
Patch502:	linux-2.2.19-ieee1394-ppc.patch.bz2
Patch503:	2.2.20-ppc_ide.patch
Patch504:	2.2.21-enable_ibmraid-ppc.patch
Patch505:	2.2.21-ppc_asm.patch
Patch506:	2.2.21-ppc_8.patch
Patch507:	2.2.21-ppc_ieee1394.patch
Patch1500:	linux-sparc_ide_fix.patch.2.2.19
Patch1501:	%{name}-sparc-zs.h.patch
Patch1502:	%{name}-sym53c8xx.patch
Patch1503:	%{name}-sparc_netsyms.patch

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	rpm-build >= 4.0.2-53
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	%{kgcc_package}
%endif
%ifarch sparc
BuildRequires:	sparc32
%endif
Provides:	%{name}-up = %{version}-%{release}
%ifarch %{ix86} ppc
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(i2c) = %{i2c_version}
Provides:	i2c = %{i2c_version}
Provides:	bttv = %{bttv_version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Autoreqprov:	no
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
#Prereq:		rc-boot
Obsoletes:	kernel-modules

#i2c and bttv packages are obsolete
Obsoletes:	kernel-i2c
Obsoletes:	bttv
Obsoletes:	kernel-misc-bttv

ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
%ifarch		%{ix86}
BuildRequires:	bin86
BuildRequires:	autoconf
BuildRequires:	automake
%endif
Autoreqprov:	no

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enthДlt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist fЭr grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeъ-Management, GerДte Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un systХme d'exploitation Linux. Le noyau traite les
fonctions basiques d'un systХme d'exploitation: allocation mИmoire,
allocation de process, entrИe/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j╠dro Linuksa niezbЙdne do prawidЁowego dziaЁania
Twojego komputera.

%description -l ru
Этот пакет содержит ядро Linux, которое необходимо для того, чтобы
система загрузилась и работала. Набор драйверов устройств, включенных
в ядро, ограничен до минимума. Большинство устройств поддерживаются
при помощи модулей, загружаемых после загрузки ядра.

Также этот пакет содержит модули, обеспечивающие поддержку всех
устройств, поддерживаемых в Linux на сегодняшний день.

%description -l uk
Цей пакет м╕стить ядро Linux, яке необх╕дне для того, щоб система
загрузилася ╕ працювала. К╕льк╕сть драйвер╕в перифер╕йних пристро╖в,
вбудованих в ядро, обмежена до м╕н╕мума. Б╕льш╕сть пристро╕в
п╕дтримуються за допомогою модул╕в, що загружаються п╕сля загрузки
ядра.

Також цей пакет м╕стить модул╕, що забезпечують п╕дтримку вс╕х
перифер╕йних пристро╕в, як╕ Linux п╕дтриму╓ на сьогодняшн╕й день.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} fЭr Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl):	Kernel %{version} skompilowany na maszyny SMP
Group:		Base/Kernel
Provides:	%{name} = %{version}-%{release}
%ifarch %{ix86} ppc
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(i2c) = %{i2c_version}
Provides:	i2c = %{i2c_version}
Provides:	bttv = %{bttv_version}

%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
Prereq:		rc-boot
Obsoletes:	kernel-modules

# i2c and bttv packages are obsolete
Obsoletes:	kernel-smp-i2c
Obsoletes:	bttv
Obsoletes:	kernel-smp-misc-bttv
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description smp -l de
Dieses Paket enthДlt eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird fЭr Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description smp -l fr
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nИcessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand mЙme fonctionner pour les systХme mono-processeur.

%description smp -l pl
Ten pakiet zawiera wersjЙ SMP j╠dra Linuksa w wersji %{version}. Jest
wymagany wyЁ╠cznie na maszynach z dwoma b╠d╪ wiЙksz╠ liczb╠ CPU,
jednak©e powinien dziaЁaФ prawidЁowo tak©e na jednoprocesorowych.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} fЭr Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Summary(pl):	Kernel %{version} u©ywany na instalacyjnych dyskach startowych
Group:		Base/Kernel
PreReq:		modutils
PreReq:		fileutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description BOOT -l de
Dieses Paket enthДlt eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l fr
Ce package inclut une version allИgИe du noyau de Linux version
%{version}. Ce kernel et utilisИ pour les disquettes de boot
d'installation et ne doivent pas Йtre utilisИes pour un systХme
classique, beaucoup d'options dans le kernel ont Иtaient dИsactivИes a
cause de la contrainte d'espace.

%description BOOT -l pl
Ten pakiet zawiera okrojon╠ wersjЙ kernela %{version}. U©ywana jest
wyЁ╠cznie na instalacyjnych dyskach startowych i nie powinna byФ
u©ywana na dziaЁaj╠cym systemie, jako ©e wiele opcji jest wyЁ╠czonych
ze wzglЙdu na wymagania rozmiarowe.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nagЁСwkowe j╠dra
Group:		Base/Kernel
%ifarch %{ix86} ppc
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	i2c-devel = %{i2c_version}
%endif
Provides:	%{name}-headers(ipvs) = %{version}
Provides:	%{name}-headers(rawio) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Obsoletes:	i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nagЁСwkowe j╠dra, niezbedne do rekompilacji j╠dra
oraz niektСrych programСw.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja j╠dra
Group:		Base/Kernel
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjЙ j╠dra z katalogu
/usr/src/linux/Documentation.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ╪rСdЁowy j╠dra Linuksa
Summary(ru):	Исходные тексты ядра Linux
Summary(uk):	Вих╕дн╕ тексти ядра Linux
Group:		Base/Kernel
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

%description source -l de
Das Kernel-Source-Paket enthДlt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurЭckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien kЖnnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nИcessaires pour compiler la plupart des
programmes C, car il dИpend de constantes dИfinies dans le code
source. Les sources peuvent Йtre aussi utilisИe pour compiler un noyau
personnalisИ pour avoir de meilleures performances sur des matИriels
particuliers.

%description source -l pl
Pakiet zawiera kod ╪rСdЁowy jadra systemu. Jest wymagany do budowania
wiЙkszo╤ci programСw C, jako ©e s╠ one zale©ne od staЁych tutaj
zawartych. Mo©esz rСwnie© skompilowaФ wЁasne j╠dro, lepiej dopasowane
do twojego sprzЙtu.

%description source -l ru
Это исходные тексты ядра Linux. Используя их, вы можете построить свое
ядро, которое лучше настроено на ваш набор устройств.

%description source -l uk
Це вих╕дн╕ тексти ядра Linux. Використовуючи ╖х ви можете побудувати
ваше власне ядро, яке краще настро╓но на конф╕гурац╕ю вашо╖ машини.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	ModuЁy PCMCIA-CS 
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
Requires(post):		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_version}).

%description -l pl pcmcia-cs
ModuЁy PCMCIA-CS (%{pcmcia_version}).

%package smp-pcmcia-cs
Summary:	PCMCIA-CS modules for SMP kernel
Summary(pl):	ModuЁy PCMCIA-CS dla maszyn SMP
Group:		Base/Kernel
Group(pl):	Podstawowe/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
Requires(post):		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description -l pl smp-pcmcia-cs
ModuЁy PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

%prep
%setup -q -a3 -a4 -a5 -a6 -a7 -a9 -a10 -a11 -a13 -n linux

# first we should apply dzimi patch for vanilla kernel to get b50 work!
%patch506 -p1

%patch0 -p1
%patch1 -p0
# disable aic7xxx patch on sparc (this must be reported to aic7xxx driver maintainer)
%ifnarch sparc sparc64 ppc
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch38 -p1
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

%ifnarch ppc
cd serial-5.05
%patch41 -p1
%patch42 -p1
./install-in-kernel ../
cd ..
%endif

# i2c
%ifarch %{ix86} ppc
cd i2c-%{i2c_version}
mkpatch/mkpatch.pl . ../../linux | (cd ../../linux; patch -p1 -s)
cd ..
%patch105 -p1
%patch106 -p1
%endif

# 2.2.20ow2
%patch302 -p1
patch -p1 -s <linux-%{ow_version}/linux-%{ow_version}.diff

# symbios drivers
mv sym-%{symncr_version}/*.{c,h} drivers/scsi
mv sym-%{symncr_version}/{README,ChangeLog}.* Documentation

# Tekram DC395/315 U/UW SCSI host driver
%patch109 -p1
patch -p1 -s <dc395/dc395-integ22.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# JFS 1.0.5
%patch100 -p1
patch -p1 -s <jfs-2.2.common-v%{jfs_version}-patch

%patch101 -p1
%patch102 -p1
%patch104 -p1
%patch107 -p1
%patch108 -p1
%patch110 -p1
%patch111 -p1

%ifarch ppc
#enable lfs on ppc
#%patch112 -p1
%patch500 -p1
%patch501 -p1
%patch502 -p1
%patch503 -p1
%patch504 -p1
%patch505 -p1
%patch507 -p1
%endif

%ifnarch ppc sparc sparc64
%patch113 -p1
%endif

%ifarch sparc sparc64
%patch1500 -p1
%patch1501 -p1
%endif
%ifarch sparc64
%patch1503 -p1
%endif
#%patch1502 -p1

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
	KERNELCC="%{kgcc}"
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
%ifarch ppc
	%{__make} vmlinux EXTRAVERSION="-%{release}"
%else
	%{__make} boot EXTRAVERSION="-%{release}"
%endif
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

%ifarch ppc
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
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
#	CC=%{kgcc} \
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
	CC=%{kgcc} \
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
%ifnarch i586 i686 ppc
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
mv -f $RPM_BUILD_ROOT%{_kernelsrcdir} $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT%{_kernelsrcdir}
gzip -dc %{SOURCE9} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{SOURCE11} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH506}

patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH0}
%ifnarch sparc sparc64 ppc
gzip -dc %{PATCH2} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
%endif
bzip2 -dc %{PATCH3} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{PATCH4} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH5}
gzip -dc %{PATCH6} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH10}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH11}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH12}

gzip -dc %{PATCH20} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH21}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH22}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH23}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH24}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH25}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH27}
bzip2 -dc %{PATCH28} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
gzip -dc %{PATCH29} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH30} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH31}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH33}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH34}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH35}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH36}
#patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH39}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH40}
bzip2 -dc %{PATCH44} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

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
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/vlan.%{vlan_version}/vlan_2.2.patch
rm -rf $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/vlan.%{vlan_version}/

#serial
%ifnarch ppc
cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/serial-5.05
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}/serial-5.05 < %{PATCH41}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}/serial-5.05 < %{PATCH42}
./install-in-kernel $RPM_BUILD_ROOT/usr/src/linux-%{version}
cd ..
%endif
rm -rf $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/serial-5.05/

# i2c
%ifarch %{ix86}
gzip -dc %{SOURCE13} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/i2c-%{i2c_version}
mkpatch/mkpatch.pl . $RPM_BUILD_ROOT/usr/src/linux-%{version} | (cd $RPM_BUILD_ROOT/usr/src/linux-%{version}; patch -p1 -s)
cd ..
rm -rf i2c-%{i2c_version}/
bzip2 -dc %{PATCH105} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
bzip2 -dc %{PATCH106} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
%endif

# 2.2.20ow
gzip -dc %{SOURCE3} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH302}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT/usr/src/linux-%{version}/linux-%{ow_version}/linux-%{ow_version}.diff
rm -rf $RPM_BUILD_ROOT/usr/src/linux-%{version}/linux-%{ow_version}/

# symbios drivers
gzip -dc %{SOURCE6} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
mv $RPM_BUILD_ROOT/usr/src/linux-%{version}/sym-%{symncr_version}/*.{c,h} $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/scsi
mv $RPM_BUILD_ROOT/usr/src/linux-%{version}/sym-%{symncr_version}/{README,ChangeLog}.* $RPM_BUILD_ROOT/usr/src/linux-%{version}/Documentation
rm -rf $RPM_BUILD_ROOT/usr/src/linux-%{version}sym-%{symncr_version}

# Tekram DC395/315 U/UW SCSI host driver
gzip -dc %{SOURCE4} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH109}
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} <dc395/dc395-integ22.diff
install dc395/dc395x_trm.? dc395/README.dc395x $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/scsi/
rm -rf dc395/

# jfs 1.0.5
gzip -dc %{SOURCE12} | tar -xf - -C $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH100}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/jfs-2.2.common-v%{jfs_version}-patch
# remove all jfs patches from linux/ directory
rm $RPM_BUILD_ROOT/usr/src/linux-%{version}/jfs-*


patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH101}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH102}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH104}
bzip2 -dc %{PATCH107} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
bzip2 -dc %{PATCH108} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH110}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH111}
%ifarch ppc
#patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH112}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH500}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH501}
bzip2 -dc %{PATCH502} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH503}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH504}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH505}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH507}
%endif

%ifnarch ppc sparc sparc64
bzip2 -dc %{PATCH113} | patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}
%endif

%ifarch sparc sparc64
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1500}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1501}
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1502}
%endif
%ifarch sparc64
patch -s -p1 -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version} < %{PATCH1503}
%endif

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}

%{__make} mrproper
find -name "*~" -print | xargs rm -f
find -name "*.orig" -print | xargs rm -f

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
rm -rf drivers/char/hfmodem/gentbl

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

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

depmod -a -F /boot/System.map %{version}-%{release}

geninitrd /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
test ! -f /boot/initrd || mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}


%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}smp

depmod -a -F /boot/System.map %{version}-%{release}smp

geninitrd /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
test ! -f /boot/initrd || mv -f /boot/initrd /boot/initrd.old 2> /dev/null > /dev/null
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun smp
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%postun smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

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
%ifarch alpha sparc ppc
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}
%attr(600,root,root) /boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
%ifnarch sparc sparc64 ppc
/lib/modules/%{version}-%{release}/atm
%endif
/lib/modules/%{version}-%{release}/block
/lib/modules/%{version}-%{release}/cdrom
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}/fc4
%endif
/lib/modules/%{version}-%{release}/fs
/lib/modules/%{version}-%{release}/ieee1394
/lib/modules/%{version}-%{release}/ipv4
/lib/modules/%{version}-%{release}/ipv6
/lib/modules/%{version}-%{release}/misc
/lib/modules/%{version}-%{release}/net
/lib/modules/%{version}-%{release}/scsi
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/usb
/lib/modules/%{version}-%{release}/video
%endif
#%config(missingok) %{_sysconfdir}/sysconfig/rc-boot/images

%files pcmcia-cs
%defattr(644,root,root,755)
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/pcmcia
%endif

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc ppc
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}smp
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}smp
%attr(600,root,root) /boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
%ifnarch sparc sparc64 ppc
/lib/modules/%{version}-%{release}smp/atm
%endif
/lib/modules/%{version}-%{release}smp/block
/lib/modules/%{version}-%{release}smp/cdrom
%ifarch sparc sparc64
/lib/modules/%{version}-%{release}/fc4
%endif
/lib/modules/%{version}-%{release}smp/fs
/lib/modules/%{version}-%{release}smp/ieee1394
/lib/modules/%{version}-%{release}smp/ipv4
/lib/modules/%{version}-%{release}smp/ipv6
/lib/modules/%{version}-%{release}smp/misc
/lib/modules/%{version}-%{release}smp/net
/lib/modules/%{version}-%{release}smp/scsi
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/usb
/lib/modules/%{version}-%{release}smp/video
%endif
#%config(missingok) %{_sysconfdir}/sysconfig/rc-boot/images

%files -n kernel-smp-pcmcia-cs
%defattr(644,root,root,755)
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/pcmcia
%endif

%ifnarch i586 i686 ppc
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
%ifarch ppc
%{_kernelsrcdir}/include/asm-ppc
%endif

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
