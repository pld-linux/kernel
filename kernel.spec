#
# Programs required by kernel to work.
%define		_binutils_ver		2.12
%define		_util_linux_ver		2.10o
%define		_module_init_tool_ver	0.9.10
%define		_e2fsprogs_ver		1.29
%define		_jfsutils_ver		1.1.3
%define		_reiserfsprogs_ver	3.6.3
%define		_xfsprogs_ver		2.1.0
%define		_pcmcia_cs_ver		3.1.21
%define		_quota_tools_ver	3.09
%define		_PPP_ver		2.4.0
%define		_isdn4k_utils_ver	3.1pre1
%define		_nfs_utils_ver		1.0.5
%define		_procps_ver		3.1.13
%define		_oprofile_ver		0.5.3
# Netfilter snap.
%define		_netfilter_snap		20040429
#
%define		no_install_post_strip	1
#
Summary:	The Linux kernel (the core of the Linux operating system)
Name:		kernel
%define		_ver	2.6.6
Version:	%{_ver}+grsec
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.6/linux-%{_ver}.tar.bz2
# Source0-md5:	5218790bc3db41e77a7422969639a9ad
Source1:	grsecurity-2.0-2.6.6-unofficial.patch
# Source1-md5:	be087f7e902801ff6368f1cb88d7bbe7
Source2:	%{name}-config-nondist
Patch0:		2.6.0-t6-usb-irq.patch
Patch1:		2.6.0-t7-memleak-lkml.patch
Patch2:		2.6.0-t7-memleak2-lkml.patch
Patch3:		2.6.0-t8-swap-include-lkml.patch
Patch4:		2.6.0-t9-acpi_osl-lkml.patch
Patch5:		2.6.1-squashfs1.3r3.patch
Patch6:		2.6.6-pramfs.patch
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
Conflicts:	util-linux < %{_util_linux_ver}
Conflicts:	module-init-tool < %{_module_init_tool_ver}
Conflicts:	e2fsprogs < %{_e2fsprogs_ver}
Conflicts:	jfsutils < %{_jfsutils_ver}
Conflicts:	reiserfsprogs < %{_reiserfsprogs_ver}
Conflicts:	xfsprogs < %{_xfsprogs_ver}
Conflicts:	quota-tools < %{_quota_tools_ver}
Conflicts:	PPP < %{_PPP_ver}
Conflicts:	isdn4k-utils < %{_isdn4k_utils_ver}
Conflicts:	nfs-utils < %{_nfs_utils_ver}
Conflicts:	procps < %{_procps_ver}
Conflicts:	oprofile < %{_oprofile_ver}
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
%{__patch} -p1 < %{SOURCE1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
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
    cd ../..
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
cd $RPM_BUILD_ROOT%{_kernelsrcdir}-%{version}
find include/ -type d -maxdepth 1 -name "asm-*" ! -name asm-i386 ! -name asm-generic | xargs rm -rf
%{__make} mrproper
install %{SOURCE2} config-nondist

%clean
rm -rf $RPM_BUILD_ROOT

%post headers
rm -f /usr/src/linux
ln -snf linux-%{version} /usr/src/linux

%postun headers
if [ -L %{_prefix}/src/linux ]; then
	if [ "`ls -l %{_prefix}/src/linux | awk '{ print $10 }'`" = "linux-%{version}" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_prefix}/src/linux
		fi
	fi
fi

%preun source
cd /usr/src/linux
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
%{_kernelsrcdir}-%{version}%{_prefix}
%{_kernelsrcdir}-%{version}/Makefile
%{_kernelsrcdir}-%{version}/COPYING
%{_kernelsrcdir}-%{version}/CREDITS
%{_kernelsrcdir}-%{version}/MAINTAINERS
%{_kernelsrcdir}-%{version}/README
%{_kernelsrcdir}-%{version}/REPORTING-BUGS
%attr(744,root,root) %{_kernelsrcdir}-%{version}/cleanup-nondist-kernel.sh
%{_kernelsrcdir}-%{version}/config-nondist
