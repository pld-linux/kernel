%define		is_pre		yes

%define		kernel_stable	2.4.21
%define		kernel_pre	2.4.22-pre8

%{!?_is_pre:%define	_kernel_version		%(echo %{kernel_pre} | sed s/-//g)}
%{?_is_pre:%define	_kernel_version		%{kernel_stable}}
%{!?_is_pre:%define	kernel_version		%{kernel_pre}}
%{?_is_pre:%define	kernel_version		%{kernel_stable}}

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J�dro Linuksa
Summary(ru):	���� Linux
Summary(uk):	���� Linux
Name:		kernel
Version:	%{_kernel_version}
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{kernel_stable}.tar.bz2
# Source0-md5:	f51e12efa18bb828cf57d9d4a81b2fb1
Source1:	%{name}-alpha-BOOT.config
Source2:	%{name}-alpha.config
Source3:	%{name}-alpha-smp.config
Source4:	%{name}-athlon.config
Source5:	%{name}-athlon-smp.config
Source6:	%{name}-i386-BOOT.config
Source7:	%{name}-i386.config
Source8:	%{name}-i386-smp.config
Source9:	%{name}-i586.config
Source10:	%{name}-i586-smp.config
Source11:	%{name}-i686.config
Source12:	%{name}-i686-smp.config
Source13:	%{name}-ppc-BOOT.config
Source14:	%{name}-ppc.config
Source15:	%{name}-ppc-smp.config
Source16:	%{name}-sparc64-BOOT.config
Source17:	%{name}-sparc64.config
Source18:	%{name}-sparc64-smp.config
Source19:	%{name}-sparc-BOOT.config
Source20:	%{name}-sparc.config
Source21:	%{name}-sparc-smp.config
Source22:	%{name}-autoconf.h
%{!?_is_pre:Patch0:		ftp://ftp.kernel.org/pub/linux/kernel/v2.4/testing/patch-%{kernel_pre}.bz2}
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
Das Kernel-Paket enth�lt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist f�r grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Proze�-Management, Ger�te Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un syst�me d'exploitation Linux. Le noyau traite les
fonctions basiques d'un syst�me d'exploitation: allocation m�moire,
allocation de process, entr�e/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j�dro Linuksa niezb�dne do prawid�owego dzia�ania
Twojego komputera.

%description -l ru
���� ����� �������� ���� Linux, ������� ���������� ��� ����, �����
������� ����������� � ��������. ����� ��������� ���������, ����������
� ����, ��������� �� ��������. ����������� ��������� ��������������
��� ������ �������, ����������� ����� �������� ����.

����� ���� ����� �������� ������, �������������� ��������� ����
���������, �������������� � Linux �� ����������� ����.

%description -l uk
��� ����� ͦ����� ���� Linux, ��� ����Ȧ��� ��� ����, ��� �������
����������� � ���������. ���˦��� ������Ҧ� ������Ҧ���� ������ϧ�,
���������� � ����, �������� �� ͦΦ����. ���ۦ��� ������Ϧ�
Ц����������� �� ��������� ����̦�, �� ������������ Ц��� ��������
����.

����� ��� ����� ͦ����� ����̦, �� ������������ Ц������� �Ӧ�
������Ҧ���� ������Ϧ�, �˦ Linux Ц�����դ �� ���������Φ� ����.

%package BOOT
Summary:	Kernel kernel_version %{kernel_version} used on the installation boot disks
Summary(de):	Kernel kernel_version %{kernel_version} f�r Installationsdisketten
Summary(fr):	Kernel kernel_version %{kernel_version} utiliser pour les disquettes d'installation
Summary(pl):	Kernel %{kernel_version} u�ywany na instalacyjnych dyskach startowych
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
Dieses Paket enth�lt eine verkleinerte kernel_version vom Linux-Kernel
kernel_version %{kernel_version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l fr
Ce package inclut une kernel_version all�g�e du noyau de Linux kernel_version
%{kernel_version}. Ce kernel et utilis� pour les disquettes de boot
d'installation et ne doivent pas �tre utilis�es pour un syst�me
classique, beaucoup d'options dans le kernel ont �taient d�sactiv�es a
cause de la contrainte d'espace.

%description BOOT -l pl
Ten pakiet zawiera okrojon� wersj� kernela %{kernel_version}. U�ywana jest
wy��cznie na instalacyjnych dyskach startowych i nie powinna by�
u�ywana na dzia�aj�cym systemie, jako �e wiele opcji jest wy��czonych
ze wzgl�du na wymagania rozmiarowe.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag��wkowe j�dra
Group:		Base/Kernel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag��wkowe j�dra, niezbedne do rekompilacji j�dra
oraz niekt�rych program�w.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja j�dra
Group:		Base/Kernel
Provides:	%{name}-doc = %{kernel_version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacj� j�dra z katalogu
/usr/src/linux/Documentation.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod �r�d�owy j�dra Linuksa
Summary(ru):	�������� ������ ���� Linux
Summary(uk):	��Ȧ�Φ ������ ���� Linux
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
Das Kernel-Source-Paket enth�lt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zur�ckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien k�nnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont n�cessaires pour compiler la plupart des
programmes C, car il d�pend de constantes d�finies dans le code
source. Les sources peuvent �tre aussi utilis�e pour compiler un noyau
personnalis� pour avoir de meilleures performances sur des mat�riels
particuliers.

%description source -l pl
Pakiet zawiera kod �r�d�owy jadra systemu. Jest wymagany do budowania
wi�kszo�ci program�w C, jako �e s� one zale�ne od sta�ych tutaj
zawartych. Mo�esz r�wnie� skompilowa� w�asne j�dro, lepiej dopasowane
do twojego sprz�tu.

%description source -l ru
��� �������� ������ ���� Linux. ��������� ��, �� ������ ��������� ����
����, ������� ����� ��������� �� ��� ����� ���������.

%description source -l uk
�� ��Ȧ�Φ ������ ���� Linux. �������������� �� �� ������ ����������
���� ������ ����, ��� ����� �����Ϥ�� �� ���Ʀ����æ� ���ϧ ������.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu�y PCMCIA-CS
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_kernel_version}
Requires(post):	%{name}-up = %{kernel_version}-%{release}
Requires(postun):	%{name}-up = %{kernel_version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_kernel_version}).

%description pcmcia-cs -l pl
Modu�y PCMCIA-CS (%{pcmcia_kernel_version}).

%prep
%setup -q -n linux-%{kernel_stable}
%{!?_is_pre:%patch0 -p1}
#%patch1 -p1

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
	KernelVer=%{kernel_version}-%{release}$1

	cp $RPM_SOURCE_DIR/kernel-$Config.config .config

	for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
		sparc32 \
%endif
		%{__make} $target
	done

%ifarch %{ix86}
	%{__make} bzImage EXTRAkernel_version="-%{release}"
%endif
%ifarch sparc
	sparc32 %{__make} boot EXTRAkernel_version="-%{release}"
%endif
%ifarch sparc64 sparcv9 alpha
	%{__make} boot EXTRAkernel_version="-%{release}"
%endif
%ifarch ppc
	%{__make} vmlinux EXTRAkernel_version="-%{release}"
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
	%{__make} modules EXTRAkernel_version="-%{release}"
	%{__make} modules_install \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer \
		EXTRAkernel_version="-%{release}"
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
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{kernel_version}}

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

cp -ar . $RPM_BUILD_ROOT%{_prefix}/src/linux-%{kernel_version}

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{kernel_version}

find $RPM_BUILD_ROOT/usr/src/linux-%{kernel_version} -name ".*depend" | \
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
ln -sf vmlinuz-%{kernel_version}-%{release} /boot/vmlinuz
ln -sf System.map-%{kernel_version}-%{release} /boot/System.map

depmod -a -F /boot/System.map-%{kernel_version}-%{release} %{kernel_version}-%{release}
geninitrd -f --fs=rom /boot/initrd-%{kernel_version}-%{release}.gz %{kernel_version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{kernel_version}-%{release}.gz /boot/initrd

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

if [ ! -L /lib/modules/%{kernel_version} ] ; then
	mv -f /lib/modules/%{kernel_version} /lib/modules/%{kernel_version}.rpmsave
fi
rm -f /lib/modules/%{kernel_version}
ln -snf %{kernel_version}-%{release} /lib/modules/%{kernel_version}

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{kernel_version}-%{release} %{kernel_version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{kernel_version}-%{release} %{kernel_version}-%{release}

%post headers
rm -f /usr/src/linux
ln -snf linux-%{kernel_version} /usr/src/linux

%postun headers
if [ -L /usr/src/linux ]; then
	if [ "`ls -l /usr/src/linux | awk '{ print $11 }'`" = "linux-%{kernel_version}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /usr/src/linux
		fi
	fi
fi

%files
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{kernel_version}-%{release}
%endif
/boot/vmlinuz-%{kernel_version}-%{release}
/boot/System.map-%{kernel_version}-%{release}
%dir /lib/modules/%{kernel_version}-%{release}
/lib/modules/%{kernel_version}-%{release}/kernel
%ghost /lib/modules/%{kernel_version}-%{release}/modules.dep
/lib/modules/%{kernel_version}-%{release}/modules.*map
/lib/modules/%{kernel_version}-%{release}/modules.generic_string

%if %{?_with_boot:1}0
%files BOOT
%defattr(644,root,root,755)
%{_libdir}/bootdisk/boot/vmlinuz-%{kernel_version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{kernel_version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{kernel_version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{kernel_version}-%{release}BOOT/kernel
%ghost %{_libdir}/bootdisk/lib/modules/%{kernel_version}-%{release}BOOT/modules.dep
%{_libdir}/bootdisk/lib/modules/%{kernel_version}-%{release}BOOT/modules.*map
%{_libdir}/bootdisk/lib/modules/%{kernel_version}-%{release}BOOT/modules.generic_string
%endif

%files headers
%defattr(644,root,root,755)
%dir /usr/src/linux-%{kernel_version}
/usr/src/linux-%{kernel_version}/include
%{_includedir}/asm
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
/usr/src/linux-%{kernel_version}/Documentation

%files source
%defattr(644,root,root,755)
/usr/src/linux-%{kernel_version}/arch
/usr/src/linux-%{kernel_version}/drivers
/usr/src/linux-%{kernel_version}/fs
/usr/src/linux-%{kernel_version}/init
/usr/src/linux-%{kernel_version}/ipc
/usr/src/linux-%{kernel_version}/kernel
/usr/src/linux-%{kernel_version}/lib
/usr/src/linux-%{kernel_version}/mm
/usr/src/linux-%{kernel_version}/net
/usr/src/linux-%{kernel_version}/scripts
/usr/src/linux-%{kernel_version}/.config
#FIXME: this should be on, but not yet
#/usr/src/linux-%{kernel_version}/.depend
#/usr/src/linux-%{kernel_version}/.hdepend
/usr/src/linux-%{kernel_version}/COPYING
/usr/src/linux-%{kernel_version}/CREDITS
/usr/src/linux-%{kernel_version}/MAINTAINERS
/usr/src/linux-%{kernel_version}/Makefile
/usr/src/linux-%{kernel_version}/README
/usr/src/linux-%{kernel_version}/REPORTING-BUGS
/usr/src/linux-%{kernel_version}/Rules.make
