#
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.5.20
Release:	dj3_0.2
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.5/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-i386-BOOT.config
Source23:	%{name}-i586.config
Source24:	%{name}-i586-smp.config
Source25:	%{name}-i686.config
Source26:	%{name}-i686-smp.config
Source27:	%{name}-athlon.config
Source28:	%{name}-athlon-smp.config

Patch1:		http://www.kernel.org/pub/linux/kernel/people/davej/patches/2.5/%{version}/patch-%{version}-dj3.diff.gz

#This shit is because now only x86 is supported
ExclusiveArch:	%{ix86}
# /shit
ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	egcs
BuildRequires:	modutils
BuildRequires:	perl
BuildRequires:  ncurses-devel
Provides:	%{name}-up = %{version}
Provides:	module-info
# i2c is not yet ready so it's not provided, sorry
# Provides:	i2c = 2.6.1
Provides:	alsa-driver
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd
Obsoletes:	kernel-modules
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


%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(pl):	Kernel %{version} skompilowany na maszyny SMP
Group:		Base/Kernel
Provides:	%{name} = %{version}-%{release}
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
Obsoletes:	kernel-modules
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
Ten pakiet zawiera wersjê SMP j±dra Linuksa w wersji %{version}. Jest
wymagany wy³±cznie na maszynach z dwoma b±d¼ wiêksz± liczb± CPU,
jednak¿e powinien dzia³aæ prawid³owo tak¿e na jednoprocesorowych.


%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Summary(pl):	Kernel %{version} u¿ywany na instalacyjnych dyskach startowych
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
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l fr
Ce package inclut une version allégée du noyau de Linux version
%{version}. Ce kernel et utilisé pour les disquettes de boot
d'installation et ne doivent pas être utilisées pour un système
classique, beaucoup d'options dans le kernel ont étaient désactivées a
cause de la contrainte d'espace.

%description BOOT -l pl
Ten pakiet zawiera okrojon± wersjê kernela %{version}. U¿ywana jest
wy³±cznie na instalacyjnych dyskach startowych i nie powinna byæ
u¿ywana na dzia³aj±cym systemie, jako ¿e wiele opcji jest wy³±czonych
ze wzglêdu na wymagania rozmiarowe.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
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
Autoreqprov:	no
Requires:	%{name}-headers = %{version}
Requires:	bin86

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

%prep
%setup -q -n linux-%{version}
%patch1 -p1

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= gcc/g' \
    -e 's/HOSTCC.*gcc/HOSTCC	= gcc/g' \
    Makefile.orig >Makefile


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
	cp $RPM_SOURCE_DIR/kernel-$Config.config arch/i386/defconfig
	%{__make} mrproper
	ln -sf arch/i386/defconfig .config
	%{__make} oldconfig
	%{__make} dep
	%{__make} include/linux/version.h
	KERNELCC="%{kgcc}"
	%{__make} bzImage EXTRAVERSION="-%{release}"
	%{__make} modules EXTRAVERSION="-%{release}"
	mkdir -p $KERNEL_INSTALL_DIR/boot
	install System.map $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer
	cp arch/i386/boot/bzImage $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
	%{__make} INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR modules_install KERNELRELEASE=$KernelVer
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# UP Kernel

BuildKernel

# SMP Kernel
BuildKernel smp

# BOOT kernel - #temporary disable build kernel-BOOT
%ifnarch i586 i686 athlon 
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR
BuildKernel BOOT
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed"
cp -a $KERNEL_INSTALL_DIR/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm

cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}/

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

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
#%{__make} symlinks
%{__make} include/linux/version.h

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well, after we fix the paths

#%{__make} depend
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
rm -rf $RPM_BUILD_DIR/linux-%{version}-installed

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
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
/lib/modules/%{version}-%{release}/build
/lib/modules/%{version}-%{release}/modules.dep
/lib/modules/%{version}-%{release}/modules.*map
/lib/modules/%{version}-%{release}/modules.generic_string

%files smp
%defattr(644,root,root,755)
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}smp
%attr(600,root,root) /boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
/lib/modules/%{version}-%{release}smp/build
/lib/modules/%{version}-%{release}smp/modules.dep
/lib/modules/%{version}-%{release}smp/modules.*map
/lib/modules/%{version}-%{release}smp/modules.generic_string

%ifnarch i586 i686 athlon
%files BOOT
%defattr(644,root,root,755)
%{_libdir}/bootdisk/boot/vmlinuz-%{version}
%{_libdir}/bootdisk/boot/System.map-%{version}
%dir %{_libdir}/bootdisk/lib/modules/%{version}
%{_libdir}/bootdisk/lib/modules/%{version}/kernel
/lib/modules/%{version}-%{release}smp/modules.dep
/lib/modules/%{version}-%{release}smp/modules.*map
/lib/modules/%{version}-%{release}smp/modules.generic_string
%endif

%files headers
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}-%{version}
%{_kernelsrcdir}-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation

%files source
%defattr(644,root,root,755)
%{_kernelsrcdir}-%{version}/arch
%{_kernelsrcdir}-%{version}/drivers
%{_kernelsrcdir}-%{version}/fs
%{_kernelsrcdir}-%{version}/init
%{_kernelsrcdir}-%{version}/ipc
%{_kernelsrcdir}-%{version}/kernel
%{_kernelsrcdir}-%{version}/lib
%{_kernelsrcdir}-%{version}/mm
%{_kernelsrcdir}-%{version}/net
%{_kernelsrcdir}-%{version}/scripts
%{_kernelsrcdir}-%{version}/.config
#FIXME: this should be on, but not yet
#%{_kernelsrcdir}-%{version}/.depend
#%{_kernelsrcdir}-%{version}/.hdepend
%{_kernelsrcdir}-%{version}/COPYING
%{_kernelsrcdir}-%{version}/CREDITS
%{_kernelsrcdir}-%{version}/MAINTAINERS
%{_kernelsrcdir}-%{version}/Makefile
%{_kernelsrcdir}-%{version}/README
%{_kernelsrcdir}-%{version}/REPORTING-BUGS
%{_kernelsrcdir}-%{version}/Rules.make
