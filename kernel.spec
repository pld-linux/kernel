#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
#	TODO
# - check I2C
# - check netfilter
# - check squashfs
# - fix config problem
#
# BCOND:
# _without_smp		- don't build SMP kernel
# _without_up		- don't build UP kernel
# _without_source	- don't build source
# _without_lsm		- don't build LSM/SELinux kernel

%define		_rel		0
%define		test_ver	4
%define		patch_level	0
%define		_bk_ver		2

%if %{test_ver} != 0
%define		test	test%{test_ver}
%else
%define		test	%{nill}
%endif

%if %{_bk_ver} != 0
%define		bk_i	bk%{_bk_ver}
%else
%define		bk_i	%{nill}
%endif

%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')

%define		no_install_post_strip	1
%define		no_install_post_compress_modules	1

%define		pcmcia_version		3.1.22
%define		drm_xfree_version	4.3.0

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.6.0
%if	%{patch_level} != 0
Release:	%{test}%{bk_i}rel%{_rel}pl%{patch_level}
%else
Release:	%{test}%{bk_i}rel%{_rel}
%endif
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{version}-test4.tar.bz2
# Source0-md5:	0c0472d42e56a4b571f92e58b0cf0c55
Source1:	%{name}-autoconf.h
Source20:	%{name}-ia32.config
Source21:	%{name}-ia32-smp.config
#Source50:	%{name}-sparc.config
#Source51:	%{name}-sparc-smp.config
#Source60:	%{name}-sparc64.config
#Source61:	%{name}-sparc64-smp.config
Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config
Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config

Source100:	%{name}-misc.config

# ftp://ftp.kernel.org:/pub/linux/kernel/v2.6/snapshots/
Patch1:		patch-2.6.0-test4-bk2

Patch22:		2.6.0-t3-swim3.patch
Patch23:		squashfs1.3-patch

Patch25:		2.6.0-t4-sis190.patch
Patch26:		2.6.0-t3-eisa-bus.c-lkml.patch
Patch27:		2.6.0-t3-initrd_load-lkml.patch

Patch30:	2.6.0-t3-pmac_ide-lkml.patch
Patch31:	2.6.0-t3-sysfs_mem-lkml.patch
Patch32:	2.6.0-t3-trival-lkml.patch

Patch40:	2.6.0-t3.c99.Documentation-lkml.patch
Patch41:	2.6.0-t3.c99.arch-lkml.patch
Patch42:	2.6.0-t3.c99.arch.ia64-lkml.patch
Patch43:	2.6.0-t3.c99.arch.mips-lkml.patch
Patch44:	2.6.0-t3.c99.arch.sh-lkml.patch
Patch45:	2.6.0-t3.c99.drivers-lkml.patch
Patch46:	2.6.0-t3.c99.fs-lkml.patch
Patch47:	2.6.0-t3.c99.include-lkml.patch
Patch48:	2.6.0-t3.c99.sound-lkml.patch

Patch50:	2.6.0-t3-oprofile-1of3-lkml.patch
Patch51:	2.6.0-t3-oprofile-2of3-lkml.patch
Patch52:	2.6.0-t3-oprofile-3of3-lkml.patch

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	module-init-tools
Buildrequires:	perl
BuildRequires:	binutils >= 2.12
Provides:	%{name}-up = %{version}-%{release}
Provides:	module-info
Autoreqprov:	no
Prereq:		coreutils
Prereq:		module-init-tools >= 0.9.9
Prereq:		geninitrd >= 2.57
Conflicts:	quota < 3.09
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc

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

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Provides:	%{name}-smp = %{version}-%{release}
Provides:	module-info
Prereq:		coreutils
Prereq:		module-init-tools >= 0.9.9
Prereq:		geninitrd >= 2.26
Conflicts:	quota < 3.09
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

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Prereq:		module-init-tools
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

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu³y PCMCIA-CS
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_version}).

%description pcmcia-cs -l pl
Modu³y PCMCIA-CS (%{pcmcia_version}).

%package smp-pcmcia-cs
Summary:	PCMCIA-CS modules for SMP kernel
Summary(pl):	Modu³y PCMCIA-CS dla maszyn SMP
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description smp-pcmcia-cs -l pl
Modu³y PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
Provides:	%{name}-drm = %{drm_xfree_version}
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description drm -l pl
Sterowniki DRM (%{drm_xfree_version}).

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
Provides:	%{name}-drm = %{drm_xfree_version}
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description smp-drm -l pl
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Provides:	i2c-devel = 2.6.1
Provides:	%{name}-headers(netfilter) = 1.2.8
Provides:	%{name}-headers(alsa-drivers)
Provides:	alsa-driver-devel
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
Pakiet zawiera kod ¼ród³owy jadra systemu.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja do kernela
Group:		Base/Kernel
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjê j±dra z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -n linux-%{version}-test4
%patch1 -p1

%patch22 -p1
%patch23 -p1

%patch25 -p1
%patch26 -p1
#%patch27 -p1

%patch30 -p1
%patch31 -p1
#%patch32 -p1

%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
#%patch45 -p1
%patch46 -p1
%patch47 -p1
#%patch48 -p1

#%patch50 -p1
#%patch51 -p1
#%patch52 -p1

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    Makefile.orig >Makefile

%build
BuildKernel() {
	%{?_debug:set -x}
	# is this a special kernel we want to build?
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
%ifarch %{ix86}
	if [ "$smp" = "yes" ]; then
		Config="ia32-smp"
	else
		Config="ia32"
	fi
%else
	if [ "$smp" = "yes" ]; then
		Config="%{_target_cpu}-smp"
	else
		Config="%{_target_cpu}"
	fi
%endif
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi
	echo "BUILDING THE NORMAL KERNEL $*..."
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

%ifarch i386
	mv -f arch/%{base_arch}/defconfig arch/%{base_arch}/defconfig.orig
	sed -e 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/%{base_arch}/defconfig.orig > arch/%{base_arch}/defconfig
%endif

	cat %{SOURCE100} >> arch/%{base_arch}/defconfig
	
	%{__make} mrproper
	ln -sf arch/%{base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} clean
%else
	%{__make} clean
%endif
	%{__make} %{?debug:V=1} include/linux/version.h

%ifarch %{ix86}
	%{__make} %{?debug:V=1} bzImage
%endif
%ifarch sparc
	sparc32 %{__make} %{?debug:V=1} image
%else
%ifnarch %{ix86}
	%{__make} %{?debug:V=1}
%endif
%endif
%ifarch sparc
	sparc32 %{__make} %{?debug:V=1} modules
%else
	%{__make} %{?debug:V=1} modules
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
	%{?debug:V=1} \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
	echo KERNEL RELEASE $KernelVer

	install -d $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux
	if [ "$smp" = "yes" ]; then
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h
	else
		install include/linux/autoconf.h $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h
	fi
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# UP KERNEL
%{!?_without_up:BuildKernel}

# SMP KERNEL
%{!?_without_smp:BuildKernel smp}

# BOOT kernel
%ifnarch i586 i686 athlon
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
%{!?_without_boot:BuildKernel BOOT}
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

install -d $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

KERNEL_BUILD_DIR=`pwd`

KERNEL_BUILD_INSTALL=no
%{!?_without_up:KERNEL_BUILD_INSTALL=yes}
%{!?_without_smp:KERNEL_BUILD_INSTALL=yes}
[ "$KERNEL_BUILD_INSTALL" = "yes" ] && cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf %{_prefix}/src/linux-%{version} \
			$RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done

ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux

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

cat %{SOURCE100} >> .config

cp .config config-up

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

cat %{SOURCE100} >> .config

cp .config config-smp

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux/autoconf.h

if [ -e $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h ]; then
install $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-up.h \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux

if [ -e $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h ]; then
install $KERNEL_INSTALL_DIR/usr/src/linux-%{version}/include/linux/autoconf-smp.h \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux

install $KERNEL_BUILD_DIR-installed/usr/src/linux-%{version}/include/linux/* \
$RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux

%ifarch %{ix86}
ln -sf asm-i386 $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}/include/asm
%endif

%{__make} include/linux/version.h
%{__make} clean

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $KERNEL_INSTALL_DIR

%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -f %{_prefix}/src/linux-%{version}/config-up ] ; then
	ln -s %{_prefix}/src/linux-%{version}/config-up %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

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

if [ -f %{_prefix}/src/linux-%{version}/config-smp ] ; then
	ln -s %{_prefix}/src/linux-%{version}/config-smp %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

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
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release} > /dev/null 2>&1

%post drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release} > /dev/null 2>&1

%postun smp
if [ -L /lib/modules/%{version} ]; then
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%post smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp > /dev/null 2>&1

%post smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp > /dev/null 2>&1

%postun BOOT
if [ -L %{_libdir}/bootdisk/lib/modules/%{version} ]; then
	if [ "`ls -l %{_libdir}/bootdisk/lib/modules/%{version} | awk '{ print $10 }'`" = "%{version}-%{release}BOOT" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_libdir}/bootdisk/lib/modules/%{version}
		fi
	fi
fi

%post headers
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L %{_prefix}/src/linux ]; then
	if [ "`ls -l %{_prefix}/src/linux | awk '{ print $10 }'`" = "linux-%{version}" ]; then
		rm -f %{_prefix}/src/linux
	fi
fi

%if %{?_without_up:0}%{!?_without_up:1}
%files
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia
#drm stuff
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm

/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%files pcmcia-cs
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/*/pcmcia

%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif			# %%{_without_up}

%if %{?_without_smp:0}%{!?_without_smp:1}
%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
#pcmcia stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia
#drm stuff
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*

%files -n kernel-smp-pcmcia-cs
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/*/pcmcia

%files -n kernel-smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif			# %%{_without_smp}

%if %{?_without_boot:0}%{!?_without_boot:1}
%ifnarch i586 i686 athlon 		# narch
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
%endif				# narch
%endif				# %%{_without_boot}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_prefix}/src/linux-%{version}/config-smp
%{_prefix}/src/linux-%{version}/config-up
#%{_prefix}/src/linux-%{version}/.config

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%if %{?_without_source:0}%{!?_without_source:1}
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
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
%{_prefix}/src/linux-%{version}/sound
%{_prefix}/src/linux-%{version}/security
%{_prefix}/src/linux-%{version}%{_prefix}
%{_prefix}/src/linux-%{version}/COPYING
%{_prefix}/src/linux-%{version}/CREDITS
%{_prefix}/src/linux-%{version}/MAINTAINERS
%{_prefix}/src/linux-%{version}/Makefile
%{_prefix}/src/linux-%{version}/README
%{_prefix}/src/linux-%{version}/REPORTING-BUGS
%endif
