#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# _without_smp		- don't build SMP kernel
#
%define		test_build		0
#
# Kernel vannilized
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.5.8
Release:	0.1
License:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.5/linux-%{version}.tar.bz2
Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-i386-BOOT.config
Source23:	%{name}-i586.config
Source24:	%{name}-i586-smp.config
Source25:	%{name}-i686.config
Source26:	%{name}-i686-smp.config
Source50:	%{name}-sparc.config
Source51:	%{name}-sparc-smp.config
Source52:	%{name}-sparc-BOOT.config
Source60:	%{name}-sparc64.config
Source61:	%{name}-sparc64-smp.config
Source62:	%{name}-sparc64-BOOT.config
Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config
Source72:	%{name}-alpha-BOOT.config
Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config

Patch1:		%{name}-net_divert.patch
Patch2:		linux-setup_per_cpus.patch

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
%else
BuildRequires:	egcs
%endif
BuildRequires:	modutils
Buildrequires:	perl
Provides:	%{name}-up = %{version}
Provides:	module-info
Provides:	i2c = 2.6.1
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
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

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	i2c-devel = 2.6.1
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
%setup -q -n linux-%{version}
%patch1 -p1
%patch2 -p1

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
	# is this a special kernel we want to build?
	BOOT=
	if [ -n "$1" ] ; then
		if [ "$1" = "BOOT" ] ; then
			BOOT=yes
		fi
%ifarch %{ix86}
		Config="i386"-$1
%else
		Config="%{_target_cpu}"-$1
%endif
		KernelVer=%{version}-%{release}$1
		echo BUILDING A KERNEL FOR $1...
		shift
	else
		Config="%{_target_cpu}"
		KernelVer=%{version}-%{release}
		echo BUILDING THE NORMAL KERNEL...
	fi
	rm -Rf arch/$RPM_ARCH/defconfig
	:> arch/$RPM_ARCH/defconfig
	cat $RPM_SOURCE_DIR/kernel-$Config.config >> arch/$RPM_ARCH/defconfig
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
%ifarch ppc
	%{__make}
%else
	%{__make} boot
%endif
%endif
%endif
%ifarch sparc
	sparc32 %{__make} modules
%else
	%{__make} modules
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
     %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# UP KERNEL
BuildKernel 


%install
umask 022
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

%ifarch sparc sparc64
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT%{_includedir}/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT%{_includedir}/asm-sparc64
sh %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

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



# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
#%{__make} symlinks 
#%{__make} include/linux/version.h
#%{__make} "`pwd`/include/linux/modversions.h"

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
rm -f drivers/net/hamradio/soundmodem/gentbl

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-installed

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
#%ifarch %{ix86}
#/lib/modules/%{version}-%{release}/pcmcia
#%endif
/lib/modules/%{version}-%{release}/kernel
/lib/modules/%{version}-%{release}/build
/lib/modules/%{version}-%{release}/modules.dep
/lib/modules/%{version}-%{release}/modules.*map
/lib/modules/%{version}-%{release}/modules.generic_string


%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files source
%defattr(-,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
%{_prefix}/src/linux-%{version}/abi
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/grsecurity
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
%{_prefix}/src/linux-%{version}/kdb
%{_prefix}/src/linux-%{version}/kernel
%{_prefix}/src/linux-%{version}/lib
%{_prefix}/src/linux-%{version}/mm
%{_prefix}/src/linux-%{version}/net
%{_prefix}/src/linux-%{version}/scripts
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
