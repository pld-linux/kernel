Summary:     Generic linux kernel
Name:        kernel
Version:     2.0.36
Release:     1
Copyright:   GPL
Group:       Base/Kernel
Source0:     ftp://ftp.kernel.org/pub/linux/kernel/v2.0/linux-%{version}.tar.bz2
Source2:     kernel-i386.config
Source6:     kernel-alpha.config
Source8:     installkernel
Patch0:      kernel-make.patch
Patch1:      ftp://ftp.redhat.com/sound/patches-current/2.0.36-modular-1.test.patch.gz
Requires:    initscripts >= 3.64
ExclusiveOS: Linux
BuildRoot:   /tmp/%{name}-%{version}-root
Autoreqprov: no
Obsoletes:   kernel-modules
ExclusiveArch: i386

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%package source
Summary:     Kernel source tree
Group:       Base/Kernel
Requires:    %{name}-headers = %{version}, bin86

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%package headers
Summary:     Header files for the Linux kernel.
Group:       Base/Kernel

%description headers
These are the C header files for the Linux kernel, which define structures
and constants that are needed when building most standard programs under
Linux, as well as to rebuild the kernel.

%prep
%setup -q -n linux
%patch0 -p1
%patch1 -p1

%ifarch i386
install $RPM_SOURCE_DIR/kernel-i386.config arch/i386/defconfig
%endif
%ifarch alpha
install $RPM_SOURCE_DIR/kernel-alpha.config arch/alpha/defconfig
%endif

%build
export SMP=0
make oldconfig
make dep
make include/linux/version.h
make boot modules

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{boot,sbin,lib/modules} \
	 $RPM_BUILD_ROOT/usr/{include,src/linux-%{version}}

ln -s ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
ln -s ../src/linux/include/linux $RPM_BUILD_ROOT/usr/include/linux
ln -s ../src/linux/include/scsi $RPM_BUILD_ROOT/usr/include/scsi

install System.map $RPM_BUILD_ROOT/boot/System.map-%{version}-%{release}

install $RPM_SOURCE_DIR/installkernel $RPM_BUILD_ROOT/sbin/

%ifarch i386
cp arch/i386/boot/zImage $RPM_BUILD_ROOT/boot/vmlinuz-%{version}-%{release}
%endif

make PREFIX=$RPM_BUILD_ROOT modules_install

mv $RPM_BUILD_ROOT/lib/modules/%{version} \
       $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}
ln -sf %{version}-%{release} $RPM_BUILD_ROOT/lib/modules/%{version}

ln -sf linux-%{version} $RPM_BUILD_ROOT/usr/src/linux

make mrproper

cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}
%ifarch i386
install $RPM_SOURCE_DIR/kernel-i386.config \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/arch/i386/defconfig
%endif
%ifarch alpha
install $RPM_SOURCE_DIR/kernel-alpha.config \
	$RPM_BUILD_ROOT/usr/src/linux-%{version}/arch/alpha/defconfig
%endif

# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
make oldconfig -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
make symlinks -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
make include/linux/version.h -C $RPM_BUILD_ROOT/usr/src/linux-%{version}

#this generates modversions info which we want to include and we may as
#well include the depends stuff as well, after we fix the paths
make depend -C $RPM_BUILD_ROOT/usr/src/linux-%{version}
find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" | \
while read file ; do
    mv $file $file.old
    sed -e "s|[^ ]*\(/usr/src/linux\)|\1|g" < $file.old > $file
    rm -f $file.old
done

%clean
rm -rf $RPM_BUILD_ROOT

# do this for upgrades...in case the old modules get removed we have
# loopback in the kernel so that mkinitrd will work.
%pre
/sbin/modprobe loop 2> /dev/null > /dev/null
exit 0

%post
ln -sf vmlinuz-%{version}-%{release} /bootvmlinuz
ln -sf System.map-%version}-%{release} /boot/System.map

if [ -x /sbin/lilo -a -f /etc/lilo.conf ]; then
	/sbin/lilo > /dev/null 2>&1 || :
fi

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L /usr/src/linux ]; then 
    if [ `ls -l /usr/src/linux | awk '{ print $11 }'` = "linux-%{version}" ]; then
	 [ $1 = 0 ] && rm -f /usr/src/linux
    fi
fi

%files
%defattr(644, root, root, 755)
/boot/vmlinuz-*
/boot/System.map-*
/sbin/installkernel
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/scsi
/lib/modules/%{version}-%{release}/net
/lib/modules/%{version}-%{release}/block
/lib/modules/%{version}-%{release}/cdrom
/lib/modules/%{version}-%{release}/fs
/lib/modules/%{version}-%{release}/misc
/lib/modules/%{version}-%{release}/ipv4

%files source
%defattr(644, root, root, 755)
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/COPYING
/usr/src/linux-%{version}/CREDITS
/usr/src/linux-%{version}/Documentation
/usr/src/linux-%{version}/MAINTAINERS
/usr/src/linux-%{version}/Makefile
/usr/src/linux-%{version}/README
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

%files headers
%defattr(644, root, root, 755)
%defverify(not mtime)
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/include/asm
/usr/src/linux-%{version}/include/asm-generic
/usr/src/linux-%{version}/include/linux
/usr/src/linux-%{version}/include/net
/usr/src/linux-%{version}/include/scsi
/usr/src/linux-%{version}/include/asm-%{buildarch}
/usr/include/asm
/usr/include/linux
/usr/include/scsi

%changelog
* Mon Nov 16 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.36-1]
- first release kernel package for PLD (based on RH kernel spec).
