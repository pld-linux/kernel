#
%define		_netfilter_snap		20040429
%define		_cset			20040515_0809
%define		no_install_post_strip	1
#
Summary:	The Linux kernel (the core of the Linux operating system)
Name:		kernel
%define		_ver	2.6.6
Version:	%{_ver}+grsec
Release:	1.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{_ver}.tar.bz2
# Source0-md5:	5218790bc3db41e77a7422969639a9ad
Source1:	grsecurity-2.0-2.6.6-unofficial.patch
Source2:	%{name}-config-nondist
%if "%{_cset}" != "0"
Patch0:		ftp://ftp.kernel.org/pub/linux/kernel/v2.6/testing/cset/cset-%{_cset}.txt.gz
%endif
Patch1:		2.6.0-t6-usb-irq.patch
Patch2:		2.6.0-t7-memleak-lkml.patch
Patch3:		2.6.0-t7-memleak2-lkml.patch
Patch4:		2.6.0-t8-swap-include-lkml.patch
Patch5:		2.6.0-t9-acpi_osl-lkml.patch
Patch6:		2.6.1-squashfs1.3r3.patch
Patch7:		2.6.6-pramfs.patch
Patch8:		linux-kbuild-extmod.patch

Patch10:	2.6.4-esfq.patch
Patch11:	2.6.4-imq.patch
Patch12:	2.6.4-imq-nat.patch
Patch13:	2.6.4-wrr.patch
Patch14:	2.6.6-pom-ng-%{_netfilter_snap}.patch
Patch15:	2.6.5-pom-ng-fixes.patch
URL:		http://www.kernel.org/
BuildRequires:	binutils >= 2.14.90.0.7
BuildRequires:	module-init-tools
BuildRequires:	sed >= 4.0
Autoreqprov:	no
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
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%package headers
Summary:	Header files for the Linux kernel
Group:		Base/Kernel
Provides:	kernel-headers(agpgart) = %{_ver}
Provides:	kernel-headers(reiserfs) = %{_ver}
Provides:	kernel-headers(bridging) = %{_ver}
Provides:	kernel-i2c-devel
Provides:	kernel-headers(netfilter) = %{_netfilter_snap}
Provides:	kernel-headers(alsa-drivers)
Obsoletes:	kernel-i2c-devel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when rebuilding the kernel or
building kernel modules.

%package source
Summary:	Kernel source tree
Group:		Base/Kernel
Autoreqprov:	no
Requires:	kernel-headers = %{version}-%{release}
Provides:	kernel-module-build

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%prep
%setup -q -n linux-%{_ver}
%if "%{_cset}" != "0"
%patch0 -p1
%endif
%{__patch} -p1 < %{SOURCE1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
find include/ -type d -maxdepth 1 -name "asm-*" ! -name asm-i386 ! -name asm-generic | xargs rm -rf
mv arch/{x86_64,i386}/kernel/early_printk.c
find arch/* -type d -maxdepth 0 ! -name i386 | xargs rm -rf
make mrproper

cat << EOF > cleanup-nondist-kernel.sh
#!/bin/sh
CWD=\`pwd\`
cd %{_kernelsrcdir}
if [ -r ".config" ]; then
    mv .config config-nondist
fi
if [ -r "config-nondist" ]; then
    cp config-nondist .config
    make include/linux/autoconf.h
    mv include/linux/autoconf{,-nondist}.h
    make mrproper
    cd include/linux
    ln -sf autoconf{-nondist,}.h
    cd ..
    ln -sf asm-i386 asm
    cd ..
    cp config-nondist .config
    make include/linux/version.h
    chmod 644 include/linux/version.h
    rm .config
else
    echo "error: %{_kernelsrcdir}/(.config or config-nondist) - file not found!"
fi
cd \$CWD
EOF

%install
rm -rf $RPM_BUILD_ROOT
umask 022
install -d $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}
cp -R . $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}/
install %{SOURCE2} $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}/config-nondist

%clean
rm -rf $RPM_BUILD_ROOT

%post headers
rm -f %{_kernelsrcdir}
ln -snf linux-%{version} %{_kernelsrcdir}

%postun headers
if [ -L %{_kernelsrcdir} ]; then
	if [ "`ls -l %{_kernelsrcdir} | awk '{ print $10 }'`" = "linux-%{version}" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_kernelsrcdir}
		fi
	fi
fi

%preun source
cd %{_kernelsrcdir}
make mrproper
rm -f config-nondist include/linux/autoconf-nondist.h

%post source
echo
echo "You need to configure your kernel now."
echo

%files headers
%defattr(644,root,root,755)
%dir %{_kernelsrcdir}-%{version}
%{_kernelsrcdir}-%{version}/include

%files source
%defattr(644,root,root,755)
%{_kernelsrcdir}-%{version}/Documentation
%{_kernelsrcdir}-%{version}/arch
%{_kernelsrcdir}-%{version}/crypto
%{_kernelsrcdir}-%{version}/drivers
%{_kernelsrcdir}-%{version}/fs
%{_kernelsrcdir}-%{version}/grsecurity
%{_kernelsrcdir}-%{version}/init
%{_kernelsrcdir}-%{version}/ipc
%{_kernelsrcdir}-%{version}/kernel
%{_kernelsrcdir}-%{version}/lib
%{_kernelsrcdir}-%{version}/mm
%{_kernelsrcdir}-%{version}/net
%{_kernelsrcdir}-%{version}/scripts
%{_kernelsrcdir}-%{version}/sound
%{_kernelsrcdir}-%{version}/security
%{_kernelsrcdir}-%{version}/usr
%{_kernelsrcdir}-%{version}/Makefile
%{_kernelsrcdir}-%{version}/COPYING
%{_kernelsrcdir}-%{version}/CREDITS
%{_kernelsrcdir}-%{version}/MAINTAINERS
%{_kernelsrcdir}-%{version}/README
%{_kernelsrcdir}-%{version}/REPORTING-BUGS
%attr(744,root,root) %{_kernelsrcdir}-%{version}/cleanup-nondist-kernel.sh
%{_kernelsrcdir}-%{version}/config-nondist
