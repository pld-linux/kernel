%define		ow_version		2.4.22-ow1

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J╠dro Linuksa
Summary(ru):	Ядро Linux
Summary(uk):	Ядро Linux
Name:		kernel
Version:	2.4.22
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
# Source0-md5:	75dc85149b06ac9432106b8941eb9f7b
Source1:	%{name}-autoconf.h
Source2:        http://www.openwall.com/linux/linux-%{ow_version}.tar.gz
# Source2-md5:	24bfc766280cb46aad1c9ff32a840e3a
Source20:	%{name}-alpha-BOOT.config
Source21:	%{name}-alpha.config
Source22:	%{name}-alpha-smp.config
Source23:	%{name}-athlon.config
Source24:	%{name}-athlon-smp.config
Source25:	%{name}-i386-BOOT.config
Source26:	%{name}-i386.config
Source27:	%{name}-i386-smp.config
Source28:	%{name}-i586.config
Source29:	%{name}-i586-smp.config
Source30:	%{name}-i686.config
Source31:	%{name}-i686-smp.config
Source32:	%{name}-ppc-BOOT.config
Source33:	%{name}-ppc.config
Source34:	%{name}-ppc-smp.config
Source35:	%{name}-sparc64-BOOT.config
Source36:	%{name}-sparc64.config
Source37:	%{name}-sparc64-smp.config
Source38:	%{name}-sparc-BOOT.config
Source39:	%{name}-sparc.config
Source40:	%{name}-sparc-smp.config

Patch0:         %{name}-pldfblogo.patch
Patch1:		linux-2.4.22-owl_remove_extraversion.patch

# bugfixes, found in core
#Patch10:
#Patch11:

# network stuff, such as patch-o-matic, vtun, and others protocols
# with compilation fixes
#
Source100:	http://www.netfilter.org/files/patch-o-matic-20030912.tar.bz2
# Source100-md5:	e6a7c5b00252d9ced0a6b9ab03b032d3

#Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/people/alan/linux-2.4/2.4.21/patch-2.4.21-rc6-ac1.bz2
ExclusiveOS:	Linux
Autoreqprov:	no
URL:		http://www.kernel.org/
BuildRequires:	byacc
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

%package BOOT
Summary:	Kernel kernel_version %{kernel_version} used on the installation boot disks
Summary(de):	Kernel kernel_version %{kernel_version} fЭr Installationsdisketten
Summary(fr):	Kernel kernel_version %{kernel_version} utiliser pour les disquettes d'installation
Summary(pl):	Kernel %{kernel_version} u©ywany na instalacyjnych dyskach startowych
Group:		Base/Kernel
PreReq:		modutils
PreReq:		fileutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down kernel_version of the Linux %{kernel_version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description BOOT -l de
Dieses Paket enthДlt eine verkleinerte kernel_version vom Linux-Kernel
kernel_version %{kernel_version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l fr
Ce package inclut une kernel_version allИgИe du noyau de Linux kernel_version
%{kernel_version}. Ce kernel et utilisИ pour les disquettes de boot
d'installation et ne doivent pas Йtre utilisИes pour un systХme
classique, beaucoup d'options dans le kernel ont Иtaient dИsactivИes a
cause de la contrainte d'espace.

%description BOOT -l pl
Ten pakiet zawiera okrojon╠ wersjЙ kernela %{kernel_version}. U©ywana jest
wyЁ╠cznie na instalacyjnych dyskach startowych i nie powinna byФ
u©ywana na dziaЁaj╠cym systemie, jako ©e wiele opcji jest wyЁ╠czonych
ze wzglЙdu na wymagania rozmiarowe.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nagЁСwkowe j╠dra
Group:		Base/Kernel
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
Provides:	%{name}-doc = %{kernel_version}
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
Requires:	%{name}-headers = %{kernel_version}
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
Provides:	%{name}-pcmcia-cs = %{pcmcia_kernel_version}
Requires(post):	%{name}-up = %{kernel_version}-%{release}
Requires(postun):	%{name}-up = %{kernel_version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_kernel_version}).

%description pcmcia-cs -l pl
ModuЁy PCMCIA-CS (%{pcmcia_kernel_version}).

%prep
%setup -q -a2 -a100 -n linux-%{version}
# 2.4.22 openwall
patch -p1 -s <linux-%{ow_version}/linux-%{ow_version}.diff

%patch0 -p1
%patch1 -p1

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
	KernelVer=%{version}-%{release}$1

	cp $RPM_SOURCE_DIR/kernel-$Config.config .config

	for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
		sparc32 \
%endif
		%{__make} $target
	done

%ifarch %{ix86}
	%{__make} bzImage EXTRAversion="-%{release}"
%endif
%ifarch sparc
	sparc32 %{__make} boot EXTRAversion="-%{release}"
%endif
%ifarch sparc64 sparcv9 alpha
	%{__make} boot EXTRAversion="-%{release}"
%endif
%ifarch ppc
	%{__make} vmlinux EXTRAversion="-%{release}"
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
	%{__make} modules EXTRAversion="-%{release}"
	%{__make} modules_install \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer \
		EXTRAversion="-%{release}"
	rm -rf $KERNEL_INSTALL_DIR/lib/modules/*/{pcmcia,build}
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-build
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

BuildKernel
#BuildKernel smp

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

if [ ! -L /lib/modules/%{version} ] ; then
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

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

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
%ghost /lib/modules/%{version}-%{release}/modules.dep
/lib/modules/%{version}-%{release}/modules.*map
/lib/modules/%{version}-%{release}/modules.generic_string

%if %{?_with_boot:1}0
%files BOOT
%defattr(644,root,root,755)
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.dep
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*map
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.generic_string
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
