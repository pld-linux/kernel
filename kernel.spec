%define		ow_ver	2.2.14-ow2
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J�dro Linuxa
Name:		kernel
Version:	2.2.14
Release:	3
Copyright:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
Source1:	kernel-autoconf.h
Source10:	kernel-i386.config
#Source11:	kernel-i386-fb.config
Source12:	kernel-i386-BOOT.config
Source13:	kernel-i586.config
#Source14:	kernel-i586-fb.config
Source15:	kernel-i586-smp.config
#Source16:	kernel-i586-smp-fb.config
Source17:	kernel-i686.config
#Source18:	kernel-i686-fb.config
Source19:	kernel-i686-smp.config
#Source20:	kernel-i686-smp-fb.config
Source21:	kernel-sparc.config
Source22:	kernel-sparc-smp.config
Source23:	kernel-sparc-BOOT.config
#Source24:	kernel-sparc64.config
#Source25:	kernel-sparc64-smp.config
#Source26:	kernel-sparc64-BOOT.config
#Source27:	kernel-alpha.config
#Source28:	kernel-alpha-smp.config
#Source29:	kernel-alpha-BOOT.config
Source30:	ftp://ftp.openwall.com/linux/linux-%{ow_ver}.tar.gz
Source31:	http://www.garloff.de/kurt/linux/dc395/dc395-124.tar.gz
Source32:	kernel-BuildASM.sh
Patch0:		ftp://ftp.kerneli.org/pub/kerneli/v2.2/patch-int-2.2.13.3.gz
Patch1:		ftp://ftp.botik.ru/rented/namesys/ftp/pub/linux+reiserfs/linux-2.2.14-reiserfs-3.5.20-pre1-patch.gz
Patch2:		linux-2.2.14-atm-0.59-fore200e-0.1e.patch.gz
Patch3:		linux-tasks.patch
Patch4:		raid-2.2.14-B1.gz
Patch5:		kernel-cpqarray-raid090.patch
Patch6:		ftp://ftp.kernel.org/pub/linux/kernel/people/hedrick/ide.2.2.14.20000124.patch.gz
Patch7:		%{name}-pldfblogo.patch
Patch8:		linux-%{version}-freeswan-1.3.patch
ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	module-info
Autoreqprov:	no
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha
%ifarch		%{ix86}
BuildRequires:	bin86
%endif

%description
This package contains the Linux kernel that is used to boot and run your
system. It contains few device drivers for specific hardware. Most hardware
is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enth�lt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist f�r grundliegende Systemfunktionen
verantwortlich: Speicherreservierung, Proze�-Management, Ger�te Ein- und
Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie centrale d'un
syst�me d'exploitation Linux. Le noyau traite les fonctions basiques d'un
syst�me d'exploitation: allocation m�moire, allocation de process,
entr�e/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j�dro Linuxa niezb�dne do prawid�owego dzia�ania Twojego
komputera.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} f�r Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Provides:	%{name} %{version}
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It is
required only on machines with two or more CPUs, although it should work
fine on single-CPU boxes.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}. Il et
n�cessaire seulement pour les machine avec deux processeurs ou plus, il peut
quand m�me fonctionner pour les syst�me mono-processeur.

%description -l de smp
Dieses Paket enth�lt eine SMP (Multiprozessor)-Version von Linux-Kernel
%{version}. Es wird f�r Maschinen mit zwei oder mehr Prozessoren gebraucht,
sollte aber auch auf Computern mit nur einer CPU laufen.

%package fb
Summary:	Kernel version %{version} with framebuffer support
Summary(de):	Kernel version %{version} mit Framebuffer-Support
Summary(fr):	Kernel version %{version} avec framebuffer
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Provides:	%{name} %{version}
Autoreqprov:	no

%description fb
This package includes a version of the Linux %{version} kernel
with framebuffer support.

%description -l fr fb
Ce package inclu une version de Linux version %{version} avec framebuffer.

%description -l de fb
Dieses Paket enth�lt eine Version von Linux-Kernel %{version} mit
framebuffer-Support.

%package smp-fb
Summary:	Kernel version %{version} compiled for SMP machines with fb
Summary(de):	Kernel version %{version} f�r Multiprozessor-Maschinen mit framebuffer
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur avec fb
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Provides:	%{name} %{version}
Autoreqprov:	no

%description smp-fb
This package includes a SMP version of the Linux %{version} kernel. It is
required only on machines with two or more CPUs, although it should work
fine on single-CPU boxes.
It also contains support for framebuffer (graphical console) devices.

%description -l fr smp-fb
Ce package inclu une version SMP du noyau de Linux version
%{version} avec framebuffer. Il et n�cessaire seulement pour les machine
avec deux processeurs ou plus, il peut quand m�me fonctionner pour les
syst�me mono-processeur.

%description -l de smp-fb
Dieses Paket enth�lt eine SMP (Multiprozessor)-Version von Linux-Kernel
%{version}. Es wird f�r Maschinen mit zwei oder mehr Prozessoren gebraucht,
sollte aber auch auf Computern mit nur einer CPU laufen. Au�erdem ist
Support f�r Framebuffer-Devices (Console im Grafikmodus) enthalten.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} f�r Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version} kernel.
This kernel is used on the installation boot disks only and should not be
used for an installed system, as many features in this kernel are turned off
because of the size constraints.

%description -l fr BOOT
Ce package inclut une version all�g�e du noyau de Linux version %{version}.
Ce kernel et utilis� pour les disquettes de boot
d'installation et ne doivent pas �tre utilis�es pour un syst�me
classique, beaucoup d'options dans le kernel ont �taient d�sactiv�es a
cause de la contrainte d'espace.

%description -l de BOOT
Dieses Paket enth�lt eine verkleinerte Version vom Linux-Kernel version
%{version}.
Dieser Kernel wird auf den Installations-Bootdisketten benutzt und sollte
nicht auf einem installierten System verwendet werden, da viele Funktionen
wegen der Platzprobleme abgeschaltet sind.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag��wkowe j�dra
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define structures
and constants that are needed when building most standard programs under
Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag��wkowe j�dra, niezbedne do rekompilacji j�dra
oraz niekt�rych program�w.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod �r�d�owy j�dra Linuxa
Group:		Base/Kernel
Group(pl):	Podstawowe/J�dro
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
Das Kernel-Source-Paket enth�lt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele C-Programme zu
compilieren, da sie auf Konstanten zur�ckgreifen, die im Kernel-Source
definiert sind. Die Source-Dateien k�nnen auch benutzt werden, um einen
Kernel zu compilieren, der besser auf Ihre Hardware ausgerichtet ist.

%description -l fr source
Le package pour le kernel-source contient le code source pour le noyau linux.
Ces sources sont n�cessaires pour compiler la plupart des programmes C, car il
d�pend de constantes d�finies dans le code source. Les sources peuvent �tre
aussi utilis�e pour compiler un noyau personnalis� pour avoir de meilleures
performances sur des mat�riels particuliers. 

%description source -l pl
Pakiet zawiera kod �r�d�owy jadra systemu.

%prep
%setup -q -a30 -a31 -n linux
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%ifarch %{ix86}
%patch6 -p1
%patch7 -p1
%endif
%patch8 -p1

patch -p1 -s <linux-%{ow_ver}/linux-%{ow_ver}.diff
# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s <dc395/dc395-integ22.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

%build
BuildKernel() {
    # is this a special kernel we want to build?
    if [ -n "$1" ] ; then
	if [ "%{_target_cpu}" = "i586" -o "%{_target_cpu}" = "i686" ] ; then
	    Config="%{_target_cpu}"-$1
	else
	    Config=$RPM_ARCH-$1
	fi
	KernelVer=%{version}-%{release}$1
	echo BUILDING A KERNEL FOR $1...
    else
	if [ "%{_target_cpu}" = "i586" -o "%{_target_cpu}" = "i686" ] ; then
	    Config="%{_target_cpu}"
	else
	    Config=$RPM_ARCH
	fi
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
    make mrproper
    ln -sf arch/$RPM_ARCH/defconfig .config

    make oldconfig
    make dep 
    make include/linux/version.h 
%ifarch %{ix86}
    make bzImage EXTRAVERSION="-%{release}"
%else
    make boot EXTRAVERSION="-%{release}"
%endif
    make modules EXTRAVERSION="-%{release}"
    mkdir -p $RPM_BUILD_ROOT/boot
    install System.map $RPM_BUILD_ROOT/boot/System.map-$KernelVer
%ifarch %{ix86}
     cp arch/i386/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-$KernelVer
%endif
%ifarch alpha sparc
     gzip -cfv vmlinux > vmlinuz
     install vmlinux $RPM_BUILD_ROOT/boot/vmlinux-$KernelVer
     install vmlinuz $RPM_BUILD_ROOT/boot/vmlinuz-$KernelVer
%endif
     make INSTALL_MOD_PATH=$RPM_BUILD_ROOT modules_install KERNELRELEASE=$KernelVer
}

rm -rf $RPM_BUILD_ROOT

# NORMAL KERNEL
BuildKernel

# FB-ENABLED KERNEL
#BuildKernel fb

# SMP-ENABLED KERNEL
%ifnarch i386
BuildKernel smp
%endif

# SMP and FB-ENABLED KERNEL
#BuildKernel smp-fb

# BOOT kernel
%ifnarch i586 i686
BuildKernel BOOT
%endif

%install
rm -rf $RPM_BUILD_ROOT/usr
install -d $RPM_BUILD_ROOT/usr/{include,src}

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT/usr/include/linux

%ifarch sparc
ln -s ../src/linux/include/asm-sparc $RPM_BUILD_ROOT/usr/include/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT/usr/include/asm-sparc64
mkdir $RPM_BUILD_ROOT/usr/include/asm
cp -a $RPM_SOURCE_DIR/kernel-BuildASM.sh $RPM_BUILD_ROOT/usr/include/asm/BuildASM
$RPM_BUILD_ROOT/usr/include/asm/BuildASM $RPM_BUILD_ROOT/usr/include
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

tar Ixf %{SOURCE0} -C $RPM_BUILD_ROOT/usr/src/
mv -f $RPM_BUILD_ROOT/usr/src/linux $RPM_BUILD_ROOT/usr/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

gzip -dc %{PATCH0} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH1} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH2} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH4} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
%ifarch %{ix86}
gzip -dc %{PATCH6} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
%endif
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH3}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < %{PATCH5}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < linux-%{ow_ver}/linux-%{ow_ver}.diff

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}

make mrproper
find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f

%ifarch %{ix86}
install $RPM_SOURCE_DIR/kernel-i586.config .config
%else
install $RPM_SOURCE_DIR/kernel-$RPM_ARCH.config .config
%endif
make oldconfig
mv include/linux/autoconf.h include/linux/autoconf-up.h
%ifarch %{ix86}
install $RPM_SOURCE_DIR/kernel-i586-smp.config .config
%else
install $RPM_SOURCE_DIR/kernel-$RPM_ARCH-smp.config .config
%endif
make oldconfig
mv include/linux/autoconf.h include/linux/autoconf-smp.h

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux/autoconf.h

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
make symlinks 
make include/linux/version.h
make "`pwd`/include/linux/modversions.h"

#this generates modversions info which we want to include and we may as
#well include the depends stuff as well, after we fix the paths

make depend 
find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" | \
while read file ; do
	mv $file $file.old
	sed -e "s|[^ ]*\(/usr/src/linux\)|\1|g" < $file.old > $file
	rm -f $file.old
done

make clean
rm -f scripts/mkdep

%clean
rm -rf $RPM_BUILD_ROOT

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
		[ $1 = 0 ] && rm -f /lib/modules/%{version}
	fi
fi

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		[ $1 = 0 ] && rm -f /lib/modules/%{version}
	fi
fi

%postun BOOT
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}BOOT" ]; then
		[ $1 = 0 ] && rm -f /lib/modules/%{version}
	fi
fi

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L /usr/src/linux ]; then 
	if [ "`ls -l /usr/src/linux | awk '{ print $11 }'`" = "linux-%{version}" ]; then
		[ $1 = 0 ] && rm -f /usr/src/linux
	fi
fi

%files
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/atm
/lib/modules/%{version}-%{release}/block
/lib/modules/%{version}-%{release}/cdrom
/lib/modules/%{version}-%{release}/fs
/lib/modules/%{version}-%{release}/ipv4
/lib/modules/%{version}-%{release}/ipv6
/lib/modules/%{version}-%{release}/misc
/lib/modules/%{version}-%{release}/net
/lib/modules/%{version}-%{release}/scsi
%ifarch %{ix86}
/lib/modules/%{version}-%{release}/video
#/lib/modules/%{version}-%{release}/pcmcia
%endif

%ifnarch i386
%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/atm
/lib/modules/%{version}-%{release}smp/block
/lib/modules/%{version}-%{release}smp/cdrom
/lib/modules/%{version}-%{release}smp/fs
/lib/modules/%{version}-%{release}smp/ipv4
/lib/modules/%{version}-%{release}smp/ipv6
/lib/modules/%{version}-%{release}smp/misc
/lib/modules/%{version}-%{release}smp/net
/lib/modules/%{version}-%{release}smp/scsi
%ifarch %{ix86}
/lib/modules/%{version}-%{release}smp/video
#/lib/modules/%{version}-%{release}smp/pcmcia
%endif
%endif

%ifnarch i586 i686
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}BOOT
%endif
/boot/vmlinuz-%{version}-%{release}BOOT
/boot/System.map-%{version}-%{release}BOOT
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}BOOT
#/lib/modules/%{version}-%{release}BOOT/atm
/lib/modules/%{version}-%{release}BOOT/block
/lib/modules/%{version}-%{release}BOOT/cdrom
/lib/modules/%{version}-%{release}BOOT/fs
/lib/modules/%{version}-%{release}BOOT/ipv4
#/lib/modules/%{version}-%{release}BOOT/ipv6
/lib/modules/%{version}-%{release}BOOT/misc
/lib/modules/%{version}-%{release}BOOT/net
/lib/modules/%{version}-%{release}BOOT/scsi
#%ifarch i386
#/lib/modules/%{version}-%{release}BOOT/video
#/lib/modules/%{version}-%{release}BOOT/pcmcia
#%endif
%endif

%files headers
%defattr(644,root,root,755)
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files source
%defattr(644,root,root,755)
/usr/src/linux-%{version}/Documentation
/usr/src/linux-%{version}/arch
/usr/src/linux-%{version}/crypto
/usr/src/linux-%{version}/drivers
/usr/src/linux-%{version}/fs
/usr/src/linux-%{version}/init
/usr/src/linux-%{version}/ipc
/usr/src/linux-%{version}/kernel
/usr/src/linux-%{version}/lib
/usr/src/linux-%{version}/mm
/usr/src/linux-%{version}/modules
/usr/src/linux-%{version}/net
/usr/src/linux-%{version}/scripts
/usr/src/linux-%{version}/security
/usr/src/linux-%{version}/.config
/usr/src/linux-%{version}/.depend
/usr/src/linux-%{version}/.hdepend
/usr/src/linux-%{version}/COPYING
/usr/src/linux-%{version}/CREDITS
/usr/src/linux-%{version}/MAINTAINERS
/usr/src/linux-%{version}/Makefile
/usr/src/linux-%{version}/README
/usr/src/linux-%{version}/REPORTING-BUGS
/usr/src/linux-%{version}/Rules.make
