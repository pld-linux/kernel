%define		ow_ver	2.2.14-ow2
Summary:	The Linux kernel (the core of the Linux operating system).
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems).
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.2.14
Release:	1
Copyright:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
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
#Source21:	kernel-sparc.config
#Source22:	kernel-sparc-smp.config
#Source23:	kernel-sparc-BOOT.config
#Source24:	kernel-sparc64.config
#Source25:	kernel-sparc64-smp.config
#Source26:	kernel-sparc64-BOOT.config
#Source27:	kernel-alpha.config
#Source28:	kernel-alpha-smp.config
#Source29:	kernel-alpha-BOOT.config
Source30:	ftp://ftp.openwall.com/linux/linux-%{ow_ver}.tar.gz
Patch0:		ftp://ftp.kerneli.org/pub/kerneli/v2.2/patch-int-2.2.13.3.gz
Patch1:		ftp://ftp.botik.ru/rented/namesys/ftp/pub/linux+reiserfs/linux-2.2.14-reiserfs-3.5.16-patch.gz
Patch2:		linux-2.2.14-atm-0.59-fore200e-0.1e.patch.gz
Patch3:		linux-tasks.patch
Patch4:		raid-2.2.14-B1.gz
Patch5:		ftp://ftp.kernel.org/pub/linux/kernel/people/hedrick/ide.2.2.14.20000124.patch.gz
ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	/tmp/%{name}-%{version}-root
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
Das Kernel-Paket enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende Systemfunktionen
verantwortlich: Speicherreservierung, Prozeß-Management, Geräte Ein- und
Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie centrale d'un
système d'exploitation Linux. Le noyau traite les fonctions basiques d'un
système d'exploitation: allocation mémoire, allocation de process,
entrée/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j±dro Linuxa niezbêdne do prawid³owego dzia³ania Twojego
komputera.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines.
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen.
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur.
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no

%description smp
This package includes a SMP version of the Linux %{version} kernel. It is
required only on machines with two or more CPUs, although it should work
fine on single-CPU boxes.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}. Il et
nécessaire seulement pour les machine avec deux processeurs ou plus, il peut
quand même fonctionner pour les système mono-processeur.

%description -l de smp
Dieses Paket enthält eine SMP (Multiprozessor)-Version von Linux-Kernel
%{version}. Es wird für Maschinen mit zwei oder mehr Prozessoren gebraucht,
sollte aber auch auf Computern mit nur einer CPU laufen.

%package fb
Summary:	Kernel version %{version} with framebuffer support
Summary(de):	Kernel version %{version} mit Framebuffer-Support
Summary(fr):	Kernel version %{version} avec framebuffer.
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no

%description fb
This package includes a version of the Linux %{version} kernel
with framebuffer support.

%description -l fr fb
Ce package inclu une version de Linux version %{version} avec framebuffer.

%description -l de fb
Dieses Paket enthält eine Version von Linux-Kernel %{version} mit
framebuffer-Support.

%package smp-fb
Summary:	Kernel version %{version} compiled for SMP machines with fb.
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen mit framebuffer.
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur avec fb.
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no

%description smp-fb
This package includes a SMP version of the Linux %{version} kernel. It is
required only on machines with two or more CPUs, although it should work
fine on single-CPU boxes.
It also contains support for framebuffer (graphical console) devices.

%description -l fr smp-fb
Ce package inclu une version SMP du noyau de Linux version
%{version} avec framebuffer. Il et nécessaire seulement pour les machine
avec deux processeurs ou plus, il peut quand même fonctionner pour les
système mono-processeur.

%description -l de smp-fb
Dieses Paket enthält eine SMP (Multiprozessor)-Version von Linux-Kernel
%{version}. Es wird für Maschinen mit zwei oder mehr Prozessoren gebraucht,
sollte aber auch auf Computern mit nur einer CPU laufen. Außerdem ist
Support für Framebuffer-Devices (Console im Grafikmodus) enthalten.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks.
Summary(de):	Kernel version %{version} für Installationsdisketten.
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation.
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version} kernel.
This kernel is used on the installation boot disks only and should not be
used for an installed system, as many features in this kernel are turned off
because of the size constraints.

%description -l fr BOOT
Ce package inclut une version allégée du noyau de Linux version %{version}.
Ce kernel et utilisé pour les disquettes de boot
d'installation et ne doivent pas être utilisées pour un système
classique, beaucoup d'options dans le kernel ont étaient désactivées a
cause de la contrainte d'espace.

%description -l de BOOT
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel version
%{version}.
Dieser Kernel wird auf den Installations-Bootdisketten benutzt und sollte
nicht auf einem installierten System verwendet werden, da viele Funktionen
wegen der Platzprobleme abgeschaltet sind.

%package headers
Summary:	Header files for the Linux kernel.
Summary(pl):	Pliki nag³owkowe j±dra
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define structures
and constants that are needed when building most standard programs under
Linux, as well as to rebuild the kernel.

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
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele C-Programme zu
compilieren, da sie auf Konstanten zurückgreifen, die im Kernel-Source
definiert sind. Die Source-Dateien können auch benutzt werden, um einen
Kernel zu compilieren, der besser auf Ihre Hardware ausgerichtet ist.

%description -l fr source
Le package pour le kernel-source contient le code source pour le noyau linux.
Ces sources sont nécessaires pour compiler la plupart des programmes C, car il
dépend de constantes définies dans le code source. Les sources peuvent être
aussi utilisée pour compiler un noyau personnalisé pour avoir de meilleures
performances sur des matériels particuliers. 

%description source -l pl
Pakiet zawiera kod ¼ród³owy jadra systemu.

%prep
%setup -q -a30 -n linux
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
patch -p1 -s <linux-%{ow_ver}/linux-%{ow_ver}.diff

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
    # make sure EXTRAVERSION says what we want it to say
    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = -%{release}$1/" Makefile
    perl -p -i -e "s/-m386//" arch/i386/Makefile
    perl -p -i -e "s/-m486//" arch/i386/Makefile
    if [ "$1" = "BOOT" ]; then
#	SIZE_OPT_FLAGS=`echo "$RPM_OPT_FLAGS" | sed -e s/-O[0-9]//`
#	SIZE_OPT_FLAGS="$SIZE_OPT_FLAGS -g0 -O -Os -fomit-frame-pointer -fno-exceptions -fno-rtti -s -funroll-all-loops"
# Due to the RISC core nature of recent CPUs, optimized binaries are generally
# a bit larger than non-optimized ones. Therefore, we completely ignore
# RPM_OPT_FLAGS settings for the boot kernel, and replace them with the ones
# known to produce the smallest binaries.
	SIZE_OPT_FLAGS="-g0 -O -fomit-frame-pointer -fno-exceptions -fno-rtti -funroll-all-loops -ffast-math -m386 -march=i386 -pipe -s -Os"
        perl -p -i -e "s/^HOSTCFLAGS.*/HOSTCFLAGS = $SIZE_OPT_FLAGS/" Makefile
        perl -p -i -e "s/^CFLAGS_NSR.*/CFLAGS_NSR := $SIZE_OPT_FLAGS/" arch/i386/Makefile
#	Doesn't seem to work well: perl -p -i -e "s/-malign-loops=2 -malign-jumps=2 -malign-functions=2/-malign-loops=0 -malign-jumps=0 -malign-functions=0/" arch/i386/Makefile
    else
        perl -p -i -e "s/^HOSTCFLAGS.*/HOSTCFLAGS = $RPM_OPT_FLAGS/" Makefile
        perl -p -i -e "s/^CFLAGS_NSR.*/CFLAGS_NSR := $RPM_OPT_FLAGS/" arch/i386/Makefile
	# undo damage from BOOT 
#	perl -p -i -e "s/-malign-loops=0 -malign-jumps=0 -malign-functions=0/-malign-loops=2 -malign-jumps=2 -malign-functions=2/" arch/i386/Makefile
   fi
    rm -f .config
    make mrproper
    ln -s arch/$RPM_ARCH/defconfig .config

    export CFLAGS="$RPM_OPT_FLAGS"
    export CXXFLAGS="$RPM_OPT_FLAGS"
    make oldconfig
    make dep 
    make include/linux/version.h 
%ifarch %{ix86}
    make bzImage
%else
    make boot
%endif
    make modules 
    mkdir -p $RPM_BUILD_ROOT/boot
    install -m 644 System.map $RPM_BUILD_ROOT/boot/System.map-$KernelVer
%ifarch %{ix86}
     cp arch/i386/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-$KernelVer
%endif
%ifarch alpha sparc
     gzip -cfv vmlinux > vmlinuz
     install -m 755 vmlinux $RPM_BUILD_ROOT/boot/vmlinux-$KernelVer
     install -m 644 vmlinuz $RPM_BUILD_ROOT/boot/vmlinuz-$KernelVer
%endif
     mkdir -p $RPM_BUILD_ROOT/lib/modules/$KernelVer/{block,cdrom,fs,ipv4,misc,net,scsi}
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
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm

tar Ixf %{SOURCE0} -C $RPM_BUILD_ROOT/usr/src/
mv -f $RPM_BUILD_ROOT/usr/src/linux $RPM_BUILD_ROOT/usr/src/linux-%{version}
ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux
gzip -dc %{PATCH0} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH1} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH2} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH3} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH4} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
gzip -dc %{PATCH5} | patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version}
patch -s -p1 -d $RPM_BUILD_ROOT/usr/src/linux-%{version} < linux-%{ow_ver}/linux-%{ow_ver}.diff

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}

find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f

install %{SOURCE10} .config

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
make oldconfig 
make symlinks 
make include/linux/version.h

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
mv -f /boot/vmlinuz /boot/vmlinuz.old
mv -f /boot/System.map /boot/System.map.old
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old
mv -f /boot/System.map /boot/System.map.old
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo 1>&2 || :
fi

rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}

%post BOOT
mv -f /boot/vmlinuz /boot/vmlinuz.old
mv -f /boot/System.map /boot/System.map.old
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
