#
%define		_netfilter_snap		20040518
%define		_cset			20040524_0509
%define		_rc			rc1
%define		no_install_post_strip	1
#
Summary:	The Linux kernel (the core of the Linux operating system)
Name:		kernel
Version:	2.6.7
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-2.6.6.tar.bz2
# Source0-md5:	5218790bc3db41e77a7422969639a9ad
Source1:	%{name}-config-nondist
Patch0:		ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/patch-2.6.7-%{_rc}.bz2
Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/cset/cset-%{_cset}.txt.gz
#Patch2:		grsecurity-2.0-2.6.6-unofficial.patch
Patch3:		linux-kbuild-extmod.patch
Patch4:		2.6.0-t6-usb-irq.patch
Patch5:		2.6.0-t7-memleak-lkml.patch
Patch6:		2.6.0-t7-memleak2-lkml.patch
Patch7:		2.6.0-t8-swap-include-lkml.patch
Patch8:		2.6.0-t9-acpi_osl-lkml.patch
Patch9:		2.6.6-squashfs2.0.patch
Patch10:	2.6.6-pramfs.patch
Patch11:	2.6.6-kfree-calls-cleanup-lkml.patch

Patch20:	2.6.4-esfq.patch
Patch21:	2.6.4-imq.patch
Patch22:	2.6.4-imq-nat.patch
Patch23:	2.6.4-wrr.patch
Patch30:	2.6.6-pom-ng-%{_netfilter_snap}.patch
Patch31:	2.6.5-pom-ng-fixes.patch
# http://www.barbara.eu.org/~quaker/ipt_account/
Patch32:	2.6.6-ipt_account.patch
URL:		http://www.kernel.org/
BuildRequires:	binutils >= 2.14.90.0.7
BuildRequires:	module-init-tools
BuildRequires:	sed >= 4.0
PreReq:		coreutils
PreReq:		module-init-tools >= 0.9.9
Provides:	module-info
Provides:	kernel(netfilter) = %{_netfilter_snap}
Obsoletes:	kernel-modules
Conflicts:	PPP < 2.4.0
Conflicts:	e2fsprogs < 1.29
Conflicts:	isdn4k-utils < 3.1pre1
Conflicts:	jfsutils < 1.1.3
Conflicts:	module-init-tool < 0.9.10
Conflicts:	nfs-utils < 1.0.5
Conflicts:	oprofile < 0.5.3
Conflicts:	procps < 3.1.13
Conflicts:	quota-tools < 3.09
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	util-linux < 2.10o
Conflicts:	xfsprogs < 2.1.0
Autoreqprov:	no
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%package doc
Summary:	Kernel documentation
Group:		Base/Kernel
Requires:	kernel-headers = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%package headers
Summary:	Header files for the Linux kernel
Group:		Base/Kernel
Provides:	kernel-headers(agpgart) = %{version}
Provides:	kernel-headers(reiserfs) = %{version}
Provides:	kernel-headers(bridging) = %{version}
Provides:	kernel-i2c-devel
Provides:	kernel-headers(netfilter) = %{_netfilter_snap}
Provides:	kernel-headers(alsa-drivers)
Obsoletes:	kernel-i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%package module-build
Summary:	Development files for building kernel modules
Group:		Base/Kernel
Requires:	kernel-headers = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description module-build
Development files from kernel source tree needed to build Linux kernel
modules from external packages.

%package source
Summary:	Kernel source tree
Group:		Base/Kernel
Requires:	kernel-module-build = %{epoch}:%{version}-%{release}
Autoreqprov:	no

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%prep
%setup -q -n linux-2.6.6
%if "%{_cset}" != "0"
%patch0 -p1
%endif
%if "%{_rc}" != "0"
%patch1 -p1
%endif
#patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%patch30 -p1
%patch31 -p1
%patch32 -p1

%build
sed -i 's:EXTRAVERSION =.*:EXTRAVERSION =:gi' Makefile
find include/ -type d -maxdepth 1 -name "asm-*" ! -name asm-i386 ! -name asm-generic | xargs rm -rf
mv arch/{x86_64,i386}/kernel/early_printk.c
find arch/* -type d -maxdepth 0 ! -name i386 | xargs rm -rf
find -name '*.orig' | xargs rm -rf

cat << EOF > regen-autoconf.sh
#!/bin/sh
if [ -r "config-nondist" ]; then
    cp config-nondist .config
    make include/linux/autoconf.h
    mv include/linux/autoconf{,-nondist}.h
    make mrproper
    ln -sf asm-i386 include/asm
else
    echo "regen-autoconf.sh: config-nondist - file not found!"
fi
EOF
chmod 744 regen-autoconf.sh

cat << EOF > regen-version.sh
#!/bin/sh
if [ -r "config-nondist" ]; then
    cp config-nondist .config
    make include/linux/version.h
    chmod 644 include/linux/version.h
    rm .config
else
    echo "regen-version.sh: config-nondist - file not found!"
fi
EOF
chmod 744 regen-version.sh

install %{SOURCE1} config-nondist
./regen-autoconf.sh
./regen-version.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}
cp -R . $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post headers
rm -f %{_kernelsrcdir}
ln -snf linux-%{version} %{_kernelsrcdir}
touch %{_kernelsrcdir}/config-nondist
touch %{_kernelsrcdir}/include/linux/autoconf-nondist.h

%postun headers
if [ -L %{_kernelsrcdir} ]; then
    if [ "`ls -l %{_kernelsrcdir} | awk '{ print $10 }'`" = "linux-%{version}" ]; then
	if [ "$1" = "0" ]; then
	    rm -f %{_kernelsrcdir}
	fi
    fi
fi

%preun source
CWD=`pwd`
cd %{_kernelsrcdir}
make mrproper
./regen-autoconf.sh
./regen-version.sh
cd $CWD

%files doc
%defattr(644,root,root,755)
%{_kernelsrcdir}-%{version}/Documentation

%files headers
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}-%{version}
%{_kernelsrcdir}-%{version}/include
%{_kernelsrcdir}-%{version}/config-nondist

%files module-build
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}-%{version}/arch
%dir %{_kernelsrcdir}-%{version}/arch/i386
%dir %{_kernelsrcdir}-%{version}/arch/i386/kernel
%{_kernelsrcdir}-%{version}/arch/i386/Makefile
%{_kernelsrcdir}-%{version}/arch/i386/kernel/Makefile
%{_kernelsrcdir}-%{version}/arch/i386/kernel/asm-offsets.c
%{_kernelsrcdir}-%{version}/arch/i386/kernel/sigframe.h
%dir %{_kernelsrcdir}-%{version}/scripts
%{_kernelsrcdir}-%{version}/scripts/Makefile
%{_kernelsrcdir}-%{version}/scripts/Makefile.*
%{_kernelsrcdir}-%{version}/scripts/basic
%{_kernelsrcdir}-%{version}/scripts/*.c
%{_kernelsrcdir}-%{version}/scripts/*.h
%{_kernelsrcdir}-%{version}/scripts/*.sh
%{_kernelsrcdir}-%{version}/Makefile
%attr(744,root,root) %{_kernelsrcdir}-%{version}/regen-version.sh

%files source
%defattr(644,root,root,755)
%{_kernelsrcdir}-%{version}/arch/i386/[!Mk]*
%{_kernelsrcdir}-%{version}/arch/i386/kernel/[!M]*
%exclude %{_kernelsrcdir}-%{version}/arch/i386/kernel/asm-offsets.c
%exclude %{_kernelsrcdir}-%{version}/arch/i386/kernel/sigframe.h
%{_kernelsrcdir}-%{version}/crypto
%{_kernelsrcdir}-%{version}/drivers
%{_kernelsrcdir}-%{version}/fs
#%{_kernelsrcdir}-%{version}/grsecurity
%{_kernelsrcdir}-%{version}/init
%{_kernelsrcdir}-%{version}/ipc
%{_kernelsrcdir}-%{version}/kernel
%{_kernelsrcdir}-%{version}/lib
%{_kernelsrcdir}-%{version}/mm
%{_kernelsrcdir}-%{version}/net
%{_kernelsrcdir}-%{version}/scripts/*
%exclude %{_kernelsrcdir}-%{version}/scripts/Makefile
%exclude %{_kernelsrcdir}-%{version}/scripts/Makefile.*
%exclude %{_kernelsrcdir}-%{version}/scripts/basic
%exclude %{_kernelsrcdir}-%{version}/scripts/*.c
%exclude %{_kernelsrcdir}-%{version}/scripts/*.h
%exclude %{_kernelsrcdir}-%{version}/scripts/*.sh
%{_kernelsrcdir}-%{version}/sound
%{_kernelsrcdir}-%{version}/security
%{_kernelsrcdir}-%{version}/usr
%{_kernelsrcdir}-%{version}/COPYING
%{_kernelsrcdir}-%{version}/CREDITS
%{_kernelsrcdir}-%{version}/MAINTAINERS
%{_kernelsrcdir}-%{version}/README
%{_kernelsrcdir}-%{version}/REPORTING-BUGS
%attr(744,root,root) %{_kernelsrcdir}-%{version}/regen-autoconf.sh
