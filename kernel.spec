Summary:	Generic linux kernel
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.2.6
Release:	1_i386
Copyright:	GPL
Group:		Base/Kernel
Group(pl):	Podstawy/J±dro
URL:		http://www.kernel.org/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.2/linux-%{version}.tar.bz2
Source1:	kernel-i386.config
#Patch0:		linux-icmp.patch
#Patch1:		linux-tasks.patch
#Patch2:		soundcore-%{version}.patch
#Requires:	rc-scripts
ExclusiveOS:	Linux
BuildRoot:	/tmp/%{name}-%{version}-root
BuildPrereq:	bin86
Autoreqprov:	no
#Obsoletes:	kernel-modules
ExclusiveArch:	i386

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l pl
Pakiet zawiera j±dro Linuxa niezbêdne do prawid³owego dzia³ania Twojego
komputera.

%package	source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuxa
Group:		Base/Kernel
Group(pl):	Podstawy/J±dro
Requires:	%{name}-headers = %{version}
#Requires:	bin86

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l pl
Pakiet zawiera kod ¼ród³owy jadra systemu.

%package	headers
Summary:	Header files for the Linux kernel.
Summary(pl):	Pliki nag³owkowe j±dra
Group:		Base/Kernel
Group(pl):	Podstawy/J±dro

%description headers
These are the C header files for the Linux kernel, which define structures
and constants that are needed when building most standard programs under
Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbedne do rekompilacji j±dra
oraz niektórych programów.

%prep
%setup -q -n linux
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

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
%defattr(644,root,root,755)
/boot/vmlinuz-*
/boot/System.map-*
%ghost /boot/vmlinuz
%ghost /boot/System.map

#%files modules
#%defattr(644,root,root,755)
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}
%ghost /lib/modules/%{version}
/lib/modules/%{version}-%{release}/scsi
/lib/modules/%{version}-%{release}/net
/lib/modules/%{version}-%{release}/block
#/lib/modules/%{version}-%{release}/cdrom
/lib/modules/%{version}-%{release}/fs
/lib/modules/%{version}-%{release}/misc
/lib/modules/%{version}-%{release}/ipv4
/lib/modules/%{version}-%{release}/ipv6

%files source
%defattr(644,root,root,755)

#%dir /usr/src/linux-%{version}
%doc /usr/src/linux-%{version}/COPYING
%doc /usr/src/linux-%{version}/CREDITS
%doc /usr/src/linux-%{version}/Documentation
%doc /usr/src/linux-%{version}/MAINTAINERS
%doc /usr/src/linux-%{version}/README
/usr/src/linux-%{version}/Makefile
/usr/src/linux-%{version}/Rules.make
/usr/src/linux-%{version}/arch
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
/usr/src/linux-%{version}/.config

%files headers
%defattr(644,root,root,755)
%defverify(not mtime)
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/include/asm
/usr/src/linux-%{version}/include/asm-generic
/usr/src/linux-%{version}/include/linux
/usr/src/linux-%{version}/include/net
/usr/src/linux-%{version}/include/scsi
/usr/src/linux-%{version}/include/video
/usr/src/linux-%{version}/include/asm-%{_target_cpu}

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
- removed symlinks in /usr/include,
- minor changes in linux-config file.
  
* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.36-2]
- adedd secure-linux-2.0.36.diff from 
  ftp://ftp.false.com/pub/security/linux/secure-linux-06.tar.gz.

* Mon Nov 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.36-1]
- first release kernel package for PLD (based on RH kernel spec).
