Summary:	The Linux kernel (the core of the Linux operating system).
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems).
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.2.10
Release:	1
Copyright:	GPL
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
URL:		http://www.kernel.org/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
Source1:	kernel-i386.config
Source20:	kernel-2.2-i386.config
Source21:	kernel-2.2-i386-smp.config
Source22:	kernel-2.2-i386-BOOT.config
Source23:	kernel-2.2-alpha.config
Source24:	kernel-2.2-alpha-smp.config
Source25:	kernel-2.2-sparc.config
Source26:	kernel-2.2-sparc-smp.config
Source27:	kernel-2.2-sparc64.config
Source28:	kernel-2.2-sparc64-smp.config
Source29:	kernel-2.2-i686.config
Source30:	kernel-2.2-i686-smp.config
Source31:	kernel-2.2-alpha-BOOT.config
Source32:	kernel-2.2-sparc-BOOT.config
Source33:	kernel-2.2-sparc64-BOOT.config
Source34:	kernel-2.2-i586.config
Source35:	kernel-2.2-i586-smp.config
Source36:	kernel-2.2-i386-fb.config
Source37:	kernel-2.2-i386-smp-fb.config
Source38:	kernel-2.2-i586-fb.config
Source39:	kernel-2.2-i586-smp-fb.config
Source40:	kernel-2.2-i686-fb.config
Source41:	kernel-2.2-i686-smp-fb.config
#Requires:	rc-scripts
ExclusiveOS:	Linux
BuildRoot:	/tmp/%{name}-%{version}-root
BuildPrereq:	bin86
Autoreqprov:	no
#Obsoletes:	kernel-modules
ExclusiveArch:	i386

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

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuxa
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro
Requires:	%{name}-headers = %{version}
%ifarch i386 i486 i586 i686
Requires:	bin86
%endif

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l pl
Pakiet zawiera kod ¼ród³owy jadra systemu.

%package headers
Summary:	Header files for the Linux kernel.
Summary(pl):	Pliki nag³owkowe j±dra
Group:		Base/Kernel
Group(pl):	Podstawowe/J±dro

%description headers
These are the C header files for the Linux kernel, which define structures
and constants that are needed when building most standard programs under
Linux, as well as to rebuild the kernel.

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

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbedne do rekompilacji j±dra
oraz niektórych programów.

%prep
%setup -q -n linux

install %{SOURCE1} .config



%build
make oldconfig
make dep

make bzImage modules

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{boot,sbin,lib/modules} \
	 $RPM_BUILD_ROOT/usr/{include,src/linux-%{version}}

install System.map $RPM_BUILD_ROOT/boot/System.map-%{version}-%{release}

cp arch/i386/boot/bzImage $RPM_BUILD_ROOT/boot/vmlinuz-%{version}-%{release}

make INSTALL_MOD_PATH=$RPM_BUILD_ROOT modules_install

mv $RPM_BUILD_ROOT/lib/modules/%{version} \
       $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}

ln -sf %{version}-%{release} $RPM_BUILD_ROOT/lib/modules/%{version}

ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

ln -sf vmlinuz-%{version}-%{release} $RPM_BUILD_ROOT/boot/vmlinuz
ln -sf System.map-%{version}-%{release} $RPM_BUILD_ROOT/boot/System.map

make mrproper

cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}

cd $RPM_BUILD_ROOT/usr/src/linux-%{version}

install %{SOURCE1} .config

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

%clean
rm -rf $RPM_BUILD_ROOT

# do this for upgrades...in case the old modules get removed we have
# loopback in the kernel so that mkinitrd will work.
#%pre modules
%pre
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

#%post modules 
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}

#%postun modules
%postun
if [ -L /lib/modules/%{version} ]; then 
    if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
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
%ifarch alpha sparc
/boot/vmlinux-%{version}
%endif
/boot/vmlinuz-%{version}
/boot/System.map-%{version}
/boot/module-info-%{version}
/sbin/installkernel
%dir /lib/modules
%dir /lib/modules/%{version}
/lib/modules/%{version}/.rhkmvtag
/lib/modules/%{version}/block
/lib/modules/%{version}/cdrom
/lib/modules/%{version}/fs
/lib/modules/%{version}/ipv4
/lib/modules/%{version}/misc
/lib/modules/%{version}/net
/lib/modules/%{version}/scsi
%ifarch i386
/lib/modules/%{version}/video
/lib/modules/%{version}/pcmcia
%endif

%files fb
%ifarch alpha sparc
/boot/vmlinux-%{version}fb
%endif
/boot/vmlinuz-%{version}fb
/boot/System.map-%{version}fb
/boot/module-info-%{version}
/sbin/installkernel
%dir /lib/modules
%dir /lib/modules/%{version}fb
/lib/modules/%{version}fb/.rhkmvtag
/lib/modules/%{version}fb/block
/lib/modules/%{version}fb/cdrom
/lib/modules/%{version}fb/fs
/lib/modules/%{version}fb/ipv4
/lib/modules/%{version}fb/misc
/lib/modules/%{version}fb/net
/lib/modules/%{version}fb/scsi
%ifarch i386
/lib/modules/%{version}fb/video
/lib/modules/%{version}fb/pcmcia
%endif

%files source
/usr/src/linux-%{kversion}/COPYING
/usr/src/linux-%{kversion}/CREDITS
/usr/src/linux-%{kversion}/Documentation
/usr/src/linux-%{kversion}/MAINTAINERS
/usr/src/linux-%{kversion}/Makefile
/usr/src/linux-%{kversion}/README
/usr/src/linux-%{kversion}/Rules.make
/usr/src/linux-%{kversion}/arch/%{_target_cpu}
/usr/src/linux-%{kversion}/drivers
/usr/src/linux-%{kversion}/fs
/usr/src/linux-%{kversion}/init
/usr/src/linux-%{kversion}/ipc
/usr/src/linux-%{kversion}/kernel
/usr/src/linux-%{kversion}/lib
/usr/src/linux-%{kversion}/mm
/usr/src/linux-%{kversion}/modules
/usr/src/linux-%{kversion}/net
/usr/src/linux-%{kversion}/scripts

%changelog
* Mon Jan 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.2.0-pre7-2d]
- updated to 2.2.0-pre7,
- SCSI cards are now kompiled into the kernel
  (we still wait for installer for PLD Linux ...)
- added linux-tasks.patch,
  by Micha³ Zalewski <lcamtuf@ids.pl>
- added linux-icmp.patch

* Wed Dec  9 1998 Krzysztof G. Baranowski <kgb@knm.org.pl>
  [2.1.131-1d]
- updated for 2.1.131
  by Wojtek Slusarczyk <wojtek@shadow.eu.org>
- removed symlinks in %{_includedir},
- minor changes in linux-config file.
  
* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.36-2]
- adedd secure-linux-2.0.36.diff from 
  ftp://ftp.false.com/pub/security/linux/secure-linux-06.tar.gz.

* Mon Nov 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.36-1]
- first release kernel package for PLD (based on RH kernel spec).
