Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Summary(ru):	ñÄÒÏ Linux
Summary(uk):	ñÄÒÏ Linux
Name:		kernel-vanilla
Version:	2.4.19
Release:	0
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	kernel-autoconf.h
Source2:	kernel-BuildASM.sh
Source20:	kernel-i386.config
Source21:	kernel-i386-smp.config
Source22:	kernel-i386-BOOT.config
Source23:	kernel-i586.config
Source24:	kernel-i586-smp.config
Source25:	kernel-i686.config
Source26:	kernel-i686-smp.config
Source36:	kernel-ppc.config
Source37:	kernel-ppc-smp.config
Source38:	kernel-ppc-BOOT.config

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
Autoreqprov:	no
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
#Prereq:		rc-boot
Obsoletes:	kernel-modules

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
Twojego komputera.

%description -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÑÄÒÏ Linux, ËÏÔÏÒÏÅ ÎÅÏÂÈÏÄÉÍÏ ÄÌÑ ÔÏÇÏ, ÞÔÏÂÙ
ÓÉÓÔÅÍÁ ÚÁÇÒÕÚÉÌÁÓØ É ÒÁÂÏÔÁÌÁ. îÁÂÏÒ ÄÒÁÊ×ÅÒÏ× ÕÓÔÒÏÊÓÔ×, ×ËÌÀÞÅÎÎÙÈ
× ÑÄÒÏ, ÏÇÒÁÎÉÞÅÎ ÄÏ ÍÉÎÉÍÕÍÁ. âÏÌØÛÉÎÓÔ×Ï ÕÓÔÒÏÊÓÔ× ÐÏÄÄÅÒÖÉ×ÁÀÔÓÑ
ÐÒÉ ÐÏÍÏÝÉ ÍÏÄÕÌÅÊ, ÚÁÇÒÕÖÁÅÍÙÈ ÐÏÓÌÅ ÚÁÇÒÕÚËÉ ÑÄÒÁ.

ôÁËÖÅ ÜÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÍÏÄÕÌÉ, ÏÂÅÓÐÅÞÉ×ÁÀÝÉÅ ÐÏÄÄÅÒÖËÕ ×ÓÅÈ
ÕÓÔÒÏÊÓÔ×, ÐÏÄÄÅÒÖÉ×ÁÅÍÙÈ × Linux ÎÁ ÓÅÇÏÄÎÑÛÎÉÊ ÄÅÎØ.

%description -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÑÄÒÏ Linux, ÑËÅ ÎÅÏÂÈ¦ÄÎÅ ÄÌÑ ÔÏÇÏ, ÝÏÂ ÓÉÓÔÅÍÁ
ÚÁÇÒÕÚÉÌÁÓÑ ¦ ÐÒÁÃÀ×ÁÌÁ. ë¦ÌØË¦ÓÔØ ÄÒÁÊ×ÅÒ¦× ÐÅÒÉÆÅÒ¦ÊÎÉÈ ÐÒÉÓÔÒÏ§×,
×ÂÕÄÏ×ÁÎÉÈ × ÑÄÒÏ, ÏÂÍÅÖÅÎÁ ÄÏ Í¦Î¦ÍÕÍÁ. â¦ÌØÛ¦ÓÔØ ÐÒÉÓÔÒÏ¦×
Ð¦ÄÔÒÉÍÕÀÔØÓÑ ÚÁ ÄÏÐÏÍÏÇÏÀ ÍÏÄÕÌ¦×, ÝÏ ÚÁÇÒÕÖÁÀÔØÓÑ Ð¦ÓÌÑ ÚÁÇÒÕÚËÉ
ÑÄÒÁ.

ôÁËÏÖ ÃÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÍÏÄÕÌ¦, ÝÏ ÚÁÂÅÚÐÅÞÕÀÔØ Ð¦ÄÔÒÉÍËÕ ×Ó¦È
ÐÅÒÉÆÅÒ¦ÊÎÉÈ ÐÒÉÓÔÒÏ¦×, ÑË¦ Linux Ð¦ÄÔÒÉÍÕ¤ ÎÁ ÓØÏÇÏÄÎÑÛÎ¦Ê ÄÅÎØ.

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
Prereq:		rc-boot
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
Summary(pl):	Kod ¼ród³owy j±dra Linuksa
Summary(ru):	éÓÈÏÄÎÙÅ ÔÅËÓÔÙ ÑÄÒÁ Linux
Summary(uk):	÷ÉÈ¦ÄÎ¦ ÔÅËÓÔÉ ÑÄÒÁ Linux
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
Pakiet zawiera kod ¼ród³owy jadra systemu. Jest wymagany do budowania
wiêkszo¶ci programów C, jako ¿e s± one zale¿ne od sta³ych tutaj
zawartych. Mo¿esz równie¿ skompilowaæ w³asne j±dro, lepiej dopasowane
do twojego sprzêtu.

%description source -l ru
üÔÏ ÉÓÈÏÄÎÙÅ ÔÅËÓÔÙ ÑÄÒÁ Linux. éÓÐÏÌØÚÕÑ ÉÈ, ×Ù ÍÏÖÅÔÅ ÐÏÓÔÒÏÉÔØ Ó×ÏÅ
ÑÄÒÏ, ËÏÔÏÒÏÅ ÌÕÞÛÅ ÎÁÓÔÒÏÅÎÏ ÎÁ ×ÁÛ ÎÁÂÏÒ ÕÓÔÒÏÊÓÔ×.

%description source -l uk
ãÅ ×ÉÈ¦ÄÎ¦ ÔÅËÓÔÉ ÑÄÒÁ Linux. ÷ÉËÏÒÉÓÔÏ×ÕÀÞÉ §È ×É ÍÏÖÅÔÅ ÐÏÂÕÄÕ×ÁÔÉ
×ÁÛÅ ×ÌÁÓÎÅ ÑÄÒÏ, ÑËÅ ËÒÁÝÅ ÎÁÓÔÒÏ¤ÎÏ ÎÁ ËÏÎÆ¦ÇÕÒÁÃ¦À ×ÁÛÏ§ ÍÁÛÉÎÉ.

%prep
%setup -q -n linux

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

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed

rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# NORMAL KERNEL
BuildKernel

# SMP-ENABLED KERNEL
BuildKernel smp

# BOOT kernel
%ifnarch i586 i686 ppc
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

BuildKernel BOOT
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
%ifarch alpha sparc ppc
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}
%attr(600,root,root) /boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
#%ifnarch sparc sparc64 ppc
#/lib/modules/%{version}-%{release}/atm
#%endif
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

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc ppc
%attr(600,root,root) /boot/vmlinux-%{version}-%{release}smp
%endif
%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}smp
%attr(600,root,root) /boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
#%ifnarch sparc sparc64 ppc
#/lib/modules/%{version}-%{release}smp/atm
#%endif
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
#%ifarch i386
#%{_libdir}/bootdisk/lib/modules/%{version}/pcmcia
#%endif
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
#%{_prefix}/src/linux-%{version}/crypto
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
#%{_prefix}/src/linux-%{version}/security
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
