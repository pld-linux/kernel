%define		ow_version		2.2.18-ow1
%define		pcmcia_version		3.1.23
%define		freeswan_version	1.8
%define		reiserfs_version	3.5.29
%define		i2c_version		2.5.4
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.2.18
Release:	8
License:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	ftp://ftp.openwall.com/linux/linux-%{ow_version}.tar.gz
Source4:	http://www.garloff.de/kurt/linux/dc395/dc395-132.tar.gz
Source5:	ftp://projects.sourceforge.net/pub/pcmcia-cs/pcmcia-cs-%{pcmcia_version}.tar.gz
Source6:	ftp://ftp.tux.org/pub/people/gerard-roudier/drivers/linux/stable/sym-1.7.2-ncr-3.4.2.tar.gz
Source7:	http://www2.lm-sensors.nu/~lm78/archive/i2c-%{i2c_version}.tar.gz
Source20:	%{name}-i386.config
Source21:	%{name}-i386-smp.config
Source22:	%{name}-i386-BOOT.config
Source31:	%{name}-i586.config
Source32:	%{name}-i586-smp.config
Source41:	%{name}-i686.config
Source42:	%{name}-i686-smp.config
Source51:	%{name}-sparc.config
Source52:	%{name}-sparc-smp.config
Source63:	%{name}-sparc-BOOT.config
Source71:	%{name}-sparc64.config
Source72:	%{name}-sparc64-smp.config
Source73:	%{name}-sparc64-BOOT.config
Source81:	%{name}-alpha.config
Source82:	%{name}-alpha-smp.config
Source83:	%{name}-alpha-BOOT.config
Patch0:		%{name}-pldfblogo.patch
Patch1:		linux-2.2.18-freeswan-%{freeswan_version}.patch
Patch2:		wanrouter-v2215.patch.gz
Patch3:		linux-ipv6-addrconf.patch
Patch4:		%{name}-3c90x.patch
Patch5:		linux-ipv6-glibc2.2.patch
Patch6:		http://milosch.net/pub/beos/2.2.18-pre2-beos09032000.patch
Patch7:		kernel-autoraidraid.patch
Patch8:		ftp://ftp.reiserfs.org/linux-%{version}-reiserfs-%{reiserfs_version}-patch.gz
Patch9: 	ftp://ftp.kernel.org/pub/linux/kernel/people/hedrick/ide-2.2.18/ide.2.2.18.1221.patch.gz
Patch10:	http://www.math.leidenuniv.nl/~buytenh/bridge/patches/bridge-0.0.9-against-2.2.18.diff
Patch11:	http://download.sourceforge.net/linux1394/ieee1394-2.2.18-20001223.gz
Patch12:	ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.2/patch-int-2.2.18.3.gz
Patch13:	linux-2.2.18-atm-0.59-fore200e-0.1f.patch.gz
Patch14:	linux-tasks.patch
# Linux Virtual Server: http://www.linuxvirtualserver.org/software/
Patch15:	%{name}-ipvs-1.0.3-2.2.18.patch
# based on ftp://ftp.kernel.org/pub/linux/kernel/people/sct/raw-io/kiobuf-2.2.18pre24.tar.gz
Patch16:	linux-raw.patch
Patch17:	linux-i815-support.patch
Patch18:	kernel-ide-geometry.patch
#Patch:		linux-2.2.18pre21.ext3.diff

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
%ifarch %{x86}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(i2c) = %{i2c_version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Autoreqprov:	no
Prereq:		modutils
Prereq:		fileutils
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
Twojego komputera.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
%ifarch %{x86}
Provides:	%{name}(reiserfs) = %{version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Prereq:		modutils
Prereq:		fileutils
Prereq:		geninitrd
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

%package fb
Summary:	Kernel version %{version} with framebuffer support
Summary(de):	Kernel version %{version} mit Framebuffer-Support
Summary(fr):	Kernel version %{version} avec framebuffer
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
%ifarch %{x86}
Provides:	%{name}(reiserfs) = %{version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Prereq:		modutils
Prereq:		fileutils
Prereq:		geninitrd
Autoreqprov:	no

%description fb
This package includes a version of the Linux %{version} kernel with
framebuffer support.

%description -l fr fb
Ce package inclu une version de Linux version %{version} avec
framebuffer.

%description -l de fb
Dieses Paket enthält eine Version von Linux-Kernel %{version} mit
framebuffer-Support.

%package smp-fb
Summary:	Kernel version %{version} compiled for SMP machines with fb
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen mit framebuffer
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur avec fb
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Provides:	%{name} = %{version}
%ifarch %{x86}
Provides:	%{name}(reiserfs) = %{version}
%endif
Provides:	%{name}(ipvs) = %{version}
Provides:	%{name}(rawio) = %{version}
Prereq:		modutils
Prereq:		fileutils
Prereq:		geninitrd
Autoreqprov:	no

%description smp-fb
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes. It also contains support for
framebuffer (graphical console) devices.

%description -l fr smp-fb
Ce package inclu une version SMP du noyau de Linux version %{version}
avec framebuffer. Il et nécessaire seulement pour les machine avec
deux processeurs ou plus, il peut quand même fonctionner pour les
système mono-processeur.

%description -l de smp-fb
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen. Außerdem ist Support für Framebuffer-Devices (Console im
Grafikmodus) enthalten.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
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
Group(pl):	Podstawowe/J±dro
%ifarch %{x86}
Provides:	%{name}-headers(reiserfs) = %{version}
%endif
Provides:	%{name}-headers(ipvs) = %{version}
Provides:	%{name}-headers(rawio) = %{version}
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
%setup -q -a3 -a4 -a5 -a6 -n linux
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
#%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch18 -p1
%ifarch %{ix86}
cd ..
rm -rf i2c-%{i2c_version}
tar xfz %{SOURCE7}

cd i2c-%{i2c_version}
mkpatch/mkpatch.pl . ../linux | (cd ../linux; patch -p1 -s)
cd ../linux
%endif

patch -p1 -s <linux-%{ow_version}/linux-%{ow_version}.diff
# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s <dc395/dc395-integ22.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# move symbios drivers to proper place
mv sym-1.7.2-ncr-3.4.2/*.{c,h} drivers/scsi
mv sym-1.7.2-ncr-3.4.2/{README,ChangeLog}.* Documentation
rm -rf sym-1.7.2-ncr-3.4.2

%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a special kernel we want to build?
	if [ -n "$1" ] ; then
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
     %{__make} INSTALL_MOD_PATH=$KERNEL_BUILD_DIR-installed modules_install KERNELRELEASE=$KernelVer
}

BuildPCMCIA() {
if [ -n "$1" ] ; then
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
	--target=$KERNEL_BUILD_DIR-installed

mv config.mk config.mk.bak
mv Makefile Makefile.bak
mv clients/Makefile clients/Makefile.bak
sed "s/^MODDIR=.*/MODDIR=\/lib\/modules\/$KernelVer/" config.mk.bak > config.mk
sed "s/^DIRS =.*//" Makefile.bak > Makefile
sed "s/.*= 8390\..$//" clients/Makefile.bak > clients/Makefile

%{__make} all \
	CC=egcs \
	CFLAGS="$RPM_OPT_FLAGS -Wall -Wstrict-prototypes -pipe" \
	XFLAGS="$RPM_OPT_FLAGS -O -pipe -I../include -I$KERNEL_BUILD_DIR/include -D__KERNEL__ -DEXPORT_SYMTAB"

%{__make} PREFIX=$KERNEL_BUILD_DIR-installed install
cd ..
}

KERNEL_BUILD_DIR=`pwd`
rm -rf $KERNEL_BUILD_DIR-installed
install -d $KERNEL_BUILD_DIR-installed

# NORMAL KERNEL
BuildKernel
%ifarch %{ix86}
BuildPCMCIA
%endif

# FB-ENABLED KERNEL
#BuildKernel fb

# SMP-ENABLED KERNEL
BuildKernel smp
%ifarch %{ix86}
BuildPCMCIA smp
%endif

# BOOT kernel
%ifnarch i586 i686
BuildKernel BOOT
%ifarch %{ix86}
BuildPCMCIA BOOT
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src}

KERNEL_BUILD_DIR=`pwd`
cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux

bzip2 -dc %{SOURCE0} | tar -xf - -C $RPM_BUILD_ROOT/usr/src/
mv -f $RPM_BUILD_ROOT/usr/src/linux $RPM_BUILD_ROOT/usr/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH0}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH1}
gzip -dc %{PATCH2} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH3}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH4}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH5}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH6}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH7}
gzip -dc %{PATCH8} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH9} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
#patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH10}
gzip -dc %{PATCH11} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH12} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH13} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}

patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH14}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH15}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH16}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH18}

patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} <linux-%{ow_version}/linux-%{ow_version}.diff

# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s -d $RPM_BUILD_ROOT/usr/src/linux-%{version} <dc395/dc395-integ22.diff
install dc395/dc395x_trm.? dc395/README.dc395x $RPM_BUILD_ROOT/usr/src/linux-%{version}/drivers/scsi/

# symbios drivers
tar zxf %{SOURCE6}
mv sym-1.7.2-ncr-3.4.2/*.{c,h} drivers/scsi
mv sym-1.7.2-ncr-3.4.2/{README,ChangeLog}.* Documentation
rm -rf sym-1.7.2-ncr-3.4.2

%ifarch sparc sparc64
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT%{_includedir}/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT%{_includedir}/asm-sparc64
sh $RPM_SOURCE_DIR/kernel-BuildASM.sh $RPM_BUILD_ROOT%{_includedir}
cp -a $RPM_SOURCE_DIR/kernel-BuildASM.sh $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

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

geninitrd /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

geninitrd /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}

%post BOOT
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}BOOT /boot/vmlinuz
ln -sf System.map-%{version}-%{release}BOOT /boot/System.map

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
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

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

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
#/lib/modules/%{version}-%{release}/atm
/lib/modules/%{version}-%{release}/block
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}/cdrom
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

%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
#/lib/modules/%{version}-%{release}smp/atm
/lib/modules/%{version}-%{release}smp/block
%ifnarch sparc sparc64
/lib/modules/%{version}-%{release}smp/cdrom
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

%ifnarch i586 i686
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}BOOT
%endif
/boot/vmlinuz-%{version}-%{release}BOOT
/boot/System.map-%{version}-%{release}BOOT
%dir /lib/modules/%{version}-%{release}BOOT
#/lib/modules/%{version}-%{release}BOOT/atm
/lib/modules/%{version}-%{release}BOOT/block
%ifnarch sparc sparc64 alpha
/lib/modules/%{version}-%{release}BOOT/cdrom
%endif
/lib/modules/%{version}-%{release}BOOT/fs
#/lib/modules/%{version}-%{release}BOOT/ipv4
#/lib/modules/%{version}-%{release}BOOT/ipv6
/lib/modules/%{version}-%{release}BOOT/misc
/lib/modules/%{version}-%{release}BOOT/net
/lib/modules/%{version}-%{release}BOOT/scsi
%ifarch %{ix86} 
/lib/modules/%{version}-%{release}/usb
/lib/modules/%{version}-%{release}/video
%endif
%ifarch i386
/lib/modules/%{version}-%{release}BOOT/pcmcia
%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_includedir}/asm
%ifarch sparc sparc64
%{_includedir}/asm-sparc*
%endif
%{_includedir}/linux

%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
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
