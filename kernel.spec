Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuksa
Summary(ru):	ñÄÒÏ Linux
Summary(uk):	ñÄÒÏ Linux
Name:		kernel
Version:	2.4.20
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-BuildASM.sh
Source2:	%{name}-alpha-BOOT.config
Source3:	%{name}-alpha.config
Source4:	%{name}-alpha-smp.config
Source5:	%{name}-athlon.config
Source6:	%{name}-athlon-smp.config
Source7:	%{name}-i386-BOOT.config
Source8:	%{name}-i386.config
Source9:	%{name}-i386-smp.config
Source10:	%{name}-i586.config
Source11:	%{name}-i586-smp.config
Source12:	%{name}-i686.config
Source13:	%{name}-i686-smp.config
Source14:	%{name}-ppc-BOOT.config
Source15:	%{name}-ppc.config
Source16:	%{name}-ppc-smp.config
Source17:	%{name}-sparc64-BOOT.config
Source18:	%{name}-sparc64.config
Source19:	%{name}-sparc64-smp.config
Source20:	%{name}-sparc-BOOT.config
Source21:	%{name}-sparc.config
Source22:	%{name}-sparc-smp.config
Source23:	%{name}-autoconf.h
Patch0:		ftp://ftp.kernel.org/pub/linux/kernel/v2.4/testing/patch-2.4.21-rc2.bz2
ExclusiveOS:	Linux
Autoreqprov:	no
URL:		http://www.kernel.org/
%ifarch sparc
BuildRequires:	sparc32
%endif
Provides:	%{name}-up = %{version}-%{release}
Autoreqprov:	no
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
#Prereq:	rc-boot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kernel-modules

%define		no_install_post_strip                   yes
%define		no_install_post_compress_modules        yes
%ifarch i386 sparc sparcv9 sparcv9 alpha
%define		_with_boot				1
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

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu³y PCMCIA-CS
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
Requires(post):	%{name}-up = %{version}-%{release}
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
Requires(post):	%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description smp-pcmcia-cs -l pl
Modu³y PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

%prep
%setup -q -n linux-%{version}
%patch0 -p1

find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f
%ifarch %{ix86}
	perl -p -i -e "s/-m486//" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=486/-m486 -DCPU=486/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=586/-mpentium -DCPU=586/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=686/-mpentiumpro -DCPU=686/" arch/i386/Makefile
%endif

%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a special kernel we want to build?
	echo BUILDING THE $1 KERNEL...
	if [ -n "$1" ]; then
		Config="%{_target_cpu}-$1"
	else
		Config="%{_target_cpu}"
	fi
	KernelVer=%{version}$1

	cp $RPM_SOURCE_DIR/kernel-$Config.config .config

	for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
		sparc32 \
%endif
		%{__make} $target
	done

%ifarch %{ix86}
	%{__make} bzImage EXTRAVERSION="-%{release}"
%endif
%ifarch sparc sparc64 sparcv9 alpha
	sparc32 %{__make} boot EXTRAVERSION="-%{release}"
%endif
%ifarch ppc
	%{__make} vmlinux EXTRAVERSION="-%{release}"
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

%ifarch sparc
	sparc32 \
%endif
	%{__make} modules EXTRAVERSION="-%{release}"
	%{__make} modules_install \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer
	rm -rf $KERNEL_INSTALL_DIR/lib/modules/*/pcmcia
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-build
install -d $KERNEL_INSTALL_DIR

BuildKernel
BuildKernel smp

# BOOT kernel
%if %{?_with_boot:1}0
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-build/%{_libdir}/bootdisk"
install -d $KERNEL_INSTALL_DIR
BuildKernel BOOT
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-build"

cp -a $KERNEL_INSTALL_DIR/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT%{_includedir}/asm

install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config

for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
	sparc32 \
%endif
	%{__make} $target
done

cp -ar . $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" | \
while read file ; do
	mv $file $file.old
sed -e "s|$RPM_BUILD_ROOT\(/usr/src/linux-\)|\1|g" < $file.old > $file
	rm -f $file.old
done

%{__make} clean
rm -f scripts/mkdep
rm -f drivers/net/hamradio/soundmodem/gentbl

%clean
rm -rf $RPM_BUILD_ROOT{,-build}

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

%files pcmcia-cs
%defattr(644,root,root,755)
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/pcmcia
%endif

#%files smp
#%defattr(644,root,root,755)
#%attr(600,root,root) /boot/vmlinuz-%{version}-%{release}smp
#%attr(600,root,root) /boot/System.map-%{version}-%{release}smp
#%dir /lib/modules/%{version}-%{release}smp
#/lib/modules/%{version}-%{release}smp/kernel
#/lib/modules/%{version}-%{release}smp/build
#/lib/modules/%{version}-%{release}smp/modules.dep
#/lib/modules/%{version}-%{release}smp/modules.*map
#/lib/modules/%{version}-%{release}smp/modules.generic_string

#%files -n kernel-smp-pcmcia-cs
#%defattr(644,root,root,755)
#%ifarch %{ix86}
#/lib/modules/%{version}-%{release}smp/pcmcia
#%endif

%if %{?_with_boot:1}0
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
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
/usr/src/linux-%{version}/Documentation

%files source
%defattr(644,root,root,755)
/usr/src/linux-%{version}/arch
/usr/src/linux-%{version}/drivers
/usr/src/linux-%{version}/fs
/usr/src/linux-%{version}/init
/usr/src/linux-%{version}/ipc
/usr/src/linux-%{version}/kernel
/usr/src/linux-%{version}/lib
/usr/src/linux-%{version}/mm
/usr/src/linux-%{version}/net
/usr/src/linux-%{version}/scripts
/usr/src/linux-%{version}/.config
#FIXME: this should be on, but not yet
#/usr/src/linux-%{version}/.depend
#/usr/src/linux-%{version}/.hdepend
/usr/src/linux-%{version}/COPYING
/usr/src/linux-%{version}/CREDITS
/usr/src/linux-%{version}/MAINTAINERS
/usr/src/linux-%{version}/Makefile
/usr/src/linux-%{version}/README
/usr/src/linux-%{version}/REPORTING-BUGS
/usr/src/linux-%{version}/Rules.make
