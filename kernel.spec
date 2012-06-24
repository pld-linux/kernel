#
# If you define the following as 1, only kernel, -headers and -source
# packages will be built
#
# _without_grsec	- build without grsecurity patch
# _with_preemptive	- build with Preemptible patch
# _without_smp		- don't build SMP kernel
# _without_up		- don't build UP kernel
# _without_boot		- don't build BOOT kernel
# _without_source	- don't build source
# _without_doc		- don't build documentation package
#

%define		patch_level	0
%define		_rel		8
%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')
%define		no_install_post_strip	1
#
%define		pre_version		pre1
%define		ipvs_version		1.0.7
%define		freeswan_version	2.00
%define		IPperson_version	20020819-2.4.19
%define		grsec_version		2.0-pre4
%define		jfs_version		1.1.2
%define		lvm_version		1.0.7
%define		evms_version		2.0.0
%define		ntfs_version		2.1.4a
%define		drm_xfree_version	4.3.0
%define		hostap_version		0.0.2
%define		netfilter_snap		20030605
%define		iptables_version	1.2.8
%define		ACL_version		0.8.56
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J�dro Linuxa
Name:		kernel
Version:	2.4.20
%if %{patch_level} !=0
Release:	%{_rel}pl%{patch_level}%{?_with_preemptive:_pr}%{?_without_grsec:_nogrsec}
%else
Release:	%{_rel}%{?_with_preemptive:_pr}%{?_without_grsec:_nogrsec}
%endif
License:	GPL
Group:		Base/Kernel
# Source0-md5:	c439d5c93d7fc9a1480a90842465bb97
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-141.tar.gz
Source4:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
#Source5:	
Source6:	linux-2.4.19-netfilter-IMQ.patch.tar.bz2
Source7:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source8:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-2.4-%{jfs_version}.tar.gz
Source9:	http://www.xfree86.org/~alanh/linux-drm-%{drm_xfree_version}-kernelsource.tar.gz
Source10:	http://hostap.epitest.fi/releases/hostap-%{hostap_version}.tar.gz
#Source11:	
Source12:	linux-2.4.20-aacraid.tar.bz2

Source20:	%{name}-ia32.config
Source21:	%{name}-ia32-smp.config

Source50:	%{name}-sparc.config
Source51:	%{name}-sparc-smp.config

Source60:	%{name}-sparc64.config
Source61:	%{name}-sparc64-smp.config

Source70:	%{name}-alpha.config
Source71:	%{name}-alpha-smp.config

Source73:	%{name}-ppc.config
Source74:	%{name}-ppc-smp.config

#Source1000:
#Source1001:
Source1002:	%{name}-addon.config
Source1003:	%{name}-netfilter.config
Source1004:	%{name}-ipvs.config
Source1005:	%{name}-evms.config
Source1006:	%{name}-cdrw.config
Source1007:	%{name}-acpi.config
Source1008:	%{name}-ebtables.config
Source1009:	%{name}-usb2.config
Source1010:	%{name}-i2c.config
Source1011:	%{name}-promise_st.config
Source1012:	%{name}-i810fb.config
Source1013:	%{name}-davfs.config
Source1666:	%{name}-grsec.config
Source1667:	%{name}-int.config
Source1668:	%{name}-hostap.config
Source1669:	%{name}-konicawc.config
Source1670:	%{name}-wrr.config
Source1671:	%{name}-squashfs.config
Source1672:	%{name}-ACL.config
Source1673:	%{name}-IMQ.config
Source1674:	%{name}-dm.config
Source1675:	%{name}-audigy.config
Source1676:	%{name}-aic79xx.config
Source1677:	%{name}-e820.config
Source1678:	%{name}-ecc.config
Source1679:	%{name}-afs.config
Source1999:	%{name}-preemptive.config

# New features

Patch0:		%{name}-pldfblogo.patch

# from ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/testing/
Patch1:		patch-int-2.4.20.1.bz2

# from ftp://ftp.xs4all.nl/pub/crypto/freeswan/freeswan-*
Patch2:		linux-2.4-freeswan-%{freeswan_version}.patch.gz

# from ftp://linux-xfs.sgi.com/projects/xfs/download/Release-1.2pre5/kernel_patches/
Patch3:		linux-2.4.20-core-xfs-1.2.0.patch.bz2
Patch4:		linux-2.4.20-xfs-1.2.0.patch.bz2

#Patch5:		
# from http://grsecurity.net/grsecurity-%{grsec_version}.patch
Patch6:		grsecurity-%{grsec_version}-%{version}.patch.gz

# Preemptive kernel  patch
Patch7:		ftp://ftp.kernel.org/pub/linux/kernel/people/rml/preempt-kernel/v2.4/preempt-kernel-rml-2.4.20-1.patch

# new version of netfilter.
%if %{netfilter_snap} != 0
Patch8:		linux-2.4.20-netfilter-%{iptables_version}_%{netfilter_snap}.patch.gz
%else
Patch8:		linux-2.4.20-netfilter-%{iptables_version}.patch.gz
%endif

Patch9:		linux-2.4.20-initrd-close-console.patch

#from http://rick.vanrein.org/linux/badram/software/BadRAM-2.4.20.1.patch
Patch10:	linux-2.4.20-badram.patch

# http://www.linuxvirtualserver.org/software/kernel-2.4/linux-2.4.18-ipvs-%{ipvs_version}.patch.gz
Patch11:	linux-2.4.20-ipvs-%{ipvs_version}.patch.bz2

#Patch12:	
Patch13:	http://luxik.cdi.cz/~devik/qos/imq-2.4.18.diff-10

Patch14:	jfs-2.4.20.patch

# http://unc.dl.sourceforge.net/sourceforge/linux-ntfs/
Patch15:	linux-2.4.20-ntfs-%{ntfs_version}.patch.gz

# ftp://ftp.samba.org/pub/unpacked/ppp/linux/mppe/
Patch16:	linux-2.4.18-mppe.patch

#from: 	http://dl.sourceforge.net/linux-hfsplus/hfsplus-patch-20020606.patch
Patch17:	hfsplus-20030507.patch.gz

# from http://people.sistina.com/~thornber/patches/2.4-stable/2.4.20/2.4.20-dm-10.tar.bz2
Patch18:	linux-2.4.20-dm-10.patch.gz
# EVMS support (http://www.sourceforge.net/projects/evms/)
Patch19:	linux-2.4.20-evms-%{evms_version}.patch.gz

# from ???
Patch20:	linux-2.4.20-audigy.patch.bz2

# from http://www.promise.com/support/file/driver/promise-patch-2.4.19.gz
Patch21:	linux-2.4.20-promise.patch.bz2
# from http://www.promise.com/support/file/driver/st6000src_1.30_01_0326.tgz
Patch22:	linux-2.4.20-promise-st6000.patch.bz2

# from ftp://ftp.lsil.com/pub/symchips/scsi/FusionMPT/Linux/2.03.00/mptlinux-2.03.00-src.tar.gz
Patch23:	linux-2.4.20-mptlinux-2.03.00.patch.bz2

# from MDK kernel DV08__i810fb.patch
Patch24:	linux-2.4.20-I810FB.patch.bz2
Patch25:	linux-2.4.20-I810FB_lock_page_fix.patch

# Support for CDRW packet writing
Patch26:	%{name}-cdrw-packet.patch
Patch27:	%{name}-cd-mrw-2.patch

# PC Speaker driver
Patch28:	linux-2.4.20-pcsp.patch.gz

Patch29:	linux-2.4.20-no-FPU.patch

#from http://kernel.bkbits.net/~david-b/gadget24-0331.patch
Patch30:	linux-2.4-USB-gadget-20030331.patch.bz2

# from http://users.pandora.be/bart.de.schuymer/ebtables/sourcecode.html
#		bridge-nf-0.0.10-against-2.4.20.diff
Patch31:	linux-2.4.20-bridge-nf-0.0.10.patch.gz
#		ebtables_v2.0.003_vs_2.4.20.diff
Patch32:	ebtables-v2.0.003_vs_2.4.20.patch.bz2

Patch33:	linux-2.4.19-pre8-konicawc.patch
Patch34:	wrr-linux-2.4.19.patch.gz
Patch35:	%{name}-pswscancode.patch

# from MDK kernel
# FC01_davfs_0.2.4.patch
Patch36:	linux-2.4.20-davfs-0.2.4.patch.bz2
# FC02_davfs__FUNCTION__.patch
Patch37:	linux-2.4.20-davfs-fix.patch

# from http://www.noc.uoa.gr/~avel/page.php?page=nokia&lang=en
Patch38:	linux-2.4.20-Nokia5510.patch

#from http://people.freebsd.org/~gibbs/linux/SRC/
#last: aic79xx-linux-2.4-20030410-tar.gz
Patch39:	linux-2.4.20-aic79xx.patch.bz2
Patch40:	linux-2.4.20-i810_audio.patch
# from : RedHat 2.4.20-13.9
Patch41:	linux-2.4.20-afs.patch
Patch42:	linux-2.4.20-ecc.patch
Patch43:	linux-2.4.20-e820.patch

# from http://www.holtmann.org/linux/kernel/patch-2.4.20-mh6.gz
Patch44:	linux-2.4.20-mh6.patch.bz2
# from http://acl.bestbits.at/
Patch45:	linux-2.4.20-ACL-%{ACL_version}.patch.gz
Patch46:	linux-2.4.19-netmos_pci_parallel_n_serial.patch

Patch47:	linux-2.4-3com-vlan.patch

Patch48:	linux-2.4.20-acpi-EXPORT_SYMBOL.patch
# from : RedHat 2.4.20-13.9
Patch49:	linux-2.4.20-ipmi.patch
Patch50:	linux-2.4.20-irixnfs.patch
Patch51:	linux-2.4.20-odirect.patch
Patch52:	linux-2.4.20-440gx.patch
Patch53:	linux-2.4.20-nforce2.patch

Patch55:	linux-2.4.20-sym53c8xx_2.patch

# from: LKML
Patch56:	linux-2.4.20-new_IO_scheduler.patch

Patch57:	linux-2.4.20-iForce2.patch
Patch58:	linux-2.4.20-iForce2-usb.patch
# Assorted bugfixes

# from LKML
Patch100:	linux-scsi-debug-bug.patch
Patch101:	linux-2.4.2-raw-ip.patch
Patch102:	PCI_ISA_bridge.patch
# from http://www-124.ibm.com/developerworks/oss/jfs/
# JFS for Linux [patch ID 399]
Patch103:	linux-2.4.20-jfs-1.1.2-xattr.patch.gz
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch104:	linux-2.4.19-pcnet-parms.patch
Patch105:	linux-2.4.20-ptrace.patch
Patch106:	linux-2.4.20-lkml-ppp_filter-outbound-fix.patch
# raid5 xor fix for PIII/P4, should go away shortly
Patch107:	linux-2.4.0-raid5xor.patch
# disable some networking printk's
Patch108:	linux-2.4.1-netdebug.patch
# Add an ioctl to the block layer so we can be EFI compliant
Patch109:	linux-2.4.2-blkioctl-sector.patch
# fix lun probing on multilun RAID chassis
Patch110:	linux-2.4.12-scsi_scan.patch
# fix rawio
Patch111:	linux-2.4.3-rawio.patch
Patch112:	linux-2.4.20-nethashfix.patch
Patch113:	linux-2.4.10-cpqfc.patch
# Created from lvm.tgz:LVM/PATCHES by doing make
#from ftp://ftp.sistina.com/pub/LVM/1.0/lvm_%{lvm_version}.tar.gz
Patch114:	linux-2.4.20-LVM-%{lvm_version}.patch.bz2

Patch115:	linux-2.4.20-ioperm.patch
Patch116:	linux-proc_net_dev-counter-fix.patch
Patch117:	01-sigxfs-vs-blkdev.patch
Patch118:	%{name}-2.4.18-SPARC64-PLD.patch
Patch119:	linux-AXP.patch
Patch120:	%{name}-Makefile-include-fix.patch
Patch121:	%{name}-2.4.17-netsyms-export-fix.patch
#Patch122:	
Patch123:	linux-2.4.20-agp_uninorth.patch
Patch124:	%{name}-gcc31.patch
Patch125:	linux-2.4.18-hpfs.patch
Patch126:	linux-2.4.20-crc32.patch
Patch127:	linux-modules-fixed.patch
Patch128:	hpt3xx.patch
Patch129:	linux-53c7,8xx-build.fix
Patch130:	linux-PPC-SMP.patch
Patch131:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
Patch132:	ide-EXPORT_SYMBOL.fix
Patch133:	linux-proc_get_inode.patch

# added support for VIA8237
Patch134:	linux-2.4.20-vt8237.patch

Patch135:	linux-2.4.20-radeonfb_clean.patch
Patch136:	piix-ide-fix.patch
Patch137:	linux-2.4.20-km266-kl266-agp.patch
Patch138:	http://www.uwsg.indiana.edu/hypermail/linux/kernel/0212.0/att-1445/01-sound.diff

# Video 4 Linux 2
#Patch139:	linux-2.4.20-v4l2.patch.bz2 

# PWC USB Webcam Driver update (only for 2.4.20; 2.4.21 should have this fix)
Patch140:	linux-2.4.20-pwc.patch

# rivafb - fix for text background in 16bpp modes
Patch141:	linux-rivafb16.patch

# misc tdfxfb fixes - detailed description inside
Patch142:	linux-tdfxfb-fixes.patch

# quota for reiserfs
Patch143:	linux-2.4.20-reiserfs-quota.patch.bz2

#support for VIA KT400 chipset in agpgart
Patch144:	linux-2.4.20-kt400.patch

#i2c - version 2.7.0
Patch145:	linux-2.4.20-i2c-2.7.0.patch.gz

#usb patches from ftp://ftp.kernel.org/pub/linux/people/gregkh/usb/*-2.4.20.*
Patch146:	linux-2.4.20-USB.patch.bz2

# Patches fixing other patches or 3rd party sources ;)
# This patch allows to create more than one sound device using alsa
# and devfs with two or more sound cards
Patch200:	linux-sound_core.patch
Patch201:	linux-2.4.20-SPARC64.patch
Patch202:	linux-2.4.20-SPARC-EXPORT_SYMBOL.patch
Patch203:	linux-2.4.20-AXP-EXPORT_SYMBOL.patch
Patch204:	linux-2.4.20-AXP-avma1_cs.patch
Patch205:	linux-2.4.20-PPC-EXPORT_SYMBOL.patch

# tweaks for grsecurity, description inside patch
Patch900:	loop-jari-2.4.20.0.patch
Patch901:	dc395-tab.patch
Patch902:	linux-2.4.20-drm-Makefile.patch
Patch903:	linux-2.4-ppc-procesor.patch
Patch904:	linux-2.4.20-gcc33.patch
#Patch905:
#Patch906:	linux-2.4.20-LSM.patch.gz
Patch907:	PPC-grsecurity-pgtable.h.patch
#Patch908:
#Patch909:	
Patch910:	linux-2.4.21-pre4-ac4-via82cxxx_audio.patch.bz2
#Patch911:	
#Patch912:	
#Patch913:	
Patch914:	linux-2.4.20-MODULE_XXX.patch
#Patch915:	linux-2.4.19-usb-digitalcams.patch
#Patch916:	
Patch917:	linux-2.4.20-nogrsec.patch
Patch918:	linux-2.4.20-ext3.patch
Patch919:	linux-2.4.20-ntfs.patch
Patch920:	linux-2.4.20-squashfs.patch
Patch921:	linux-2.4.20-grsecurity-1.9.9e-kmem.patch

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%ifarch sparc64
BuildRequires:	egcs64
#%else
#BuildRequires:	%{kgcc_package}
%endif
BuildRequires:	modutils
Buildrequires:	perl
Provides:	%{name}-up = %{version}-%{release}
Provides:	module-info
Provides:	i2c = 2.7.0
Provides:	bttv = 0.7.83
%if %{netfilter_snap} != 0
Provides:	%{name}(netfilter) = %{iptables_version}-%{netfilter_snap}
%else
Provides:	%{name}(netfilter) = %{iptables_version}
%endif
Provides:	%{name}(grsecurity) = %{grsec_version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Provides:	%{name}(freeswan) = %{freeswan_version}
Provides:	%{name}(cdrw)
Provides:	%{name}(cdmrw)
Provides:	%{name}(hostap) = %{hostap_version}
Provides:	%{name}(evms)
Autoreqprov:	no
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd >= 2.21
Obsoletes:	kernel-modules
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
%ifarch		%{ix86}
BuildRequires:	bin86
%endif
Conflicts:	iptables < 1.2.7a
Conflicts:	lvm < 1.0.7
Conflicts:	xfsprogs < 2.0.0
Conflicts:	quota < 3.06
Conflicts:	jfsutils < %{jfs_version}

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enth�lt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist f�r grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Proze�-Management, Ger�te Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un syst�me d'exploitation Linux. Le noyau traite les
fonctions basiques d'un syst�me d'exploitation: allocation m�moire,
allocation de process, entr�e/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j�dro Linuxa niezb�dne do prawid�owego dzia�ania
Twojego komputera. Zawiera w sobie sterowniki do sprz�tu znajduj�cego
si� w komputerze, takich jak karty muzyczne, sterowniki dysk�w, etc.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} f�r Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Provides:	%{name}-smp = %{version}-%{release}
Provides:	module-info
Provides:	i2c = 2.7.0
Provides:	bttv = 0.7.83
%if %{netfilter_snap} != 0
Provides:	%{name}(netfilter) = %{iptables_version}-%{netfilter_snap}
%else
Provides:	%{name}(netfilter) = %{iptables_version}
%endif
Provides:	%{name}(grsecurity) = %{grsec_version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Provides:	%{name}(freeswan) = %{freeswan_version}
Provides:	%{name}(cdrw)
Provides:	%{name}(cdmrw)
Provides:	%{name}(hostap) = %{hostap_version}
Provides:	%{name}(evms)
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd >= 2.21
Autoreqprov:	no
Conflicts:	iptables < 1.2.7a
Conflicts:	lvm < 1.0.7
Conflicts:	xfsprogs < 2.0.0
Conflicts:	quota < 3.06
Conflicts:	jfsutils < %{jfs_version}

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description -l de smp
Dieses Paket enth�lt eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird f�r Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et n�cessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand m�me fonctionner pour les syst�me mono-processeur.

%description -l pl smp
Pakiet zawiera j�dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj�ce dwa lub wi�cej procesor�w.
Powinno r�wnie� dobrze dzia�a� na maszynach z jednym procesorem.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} f�r Installationsdisketten
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Group:		Base/Kernel
Prereq:		modutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description -l de BOOT
Dieses Paket enth�lt eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description -l pl BOOT
Pakiet zawiera j�dro Linuksa dedykowane dyskietkom startowym i powinno
by� u�ywane jedynie podczas instalacji systemu. Wiele u�ytecznych
opcji zosta�o wy��czonych, aby jak najbardziej zmniejszy� jego
rozmiar.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu�y PCMCIA-CS 
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}
Requires(pre):	%{name}-up = %{version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_version}).

%description -l pl pcmcia-cs
Modu�y PCMCIA-CS (%{pcmcia_version}).

%package smp-pcmcia-cs
Summary:	PCMCIA-CS modules for SMP kernel
Summary(pl):	Modu�y PCMCIA-CS dla maszyn SMP
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}
Requires(pre):	%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description -l pl smp-pcmcia-cs
Modu�y PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
Provides:       %{name}-drm = %{drm_xfree_version}
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}
Requires(pre):	%{name}-up = %{version}-%{release}

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description -l pl drm
Sterowniki DRM (%{drm_xfree_version}).

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
Provides:       %{name}-drm = %{drm_xfree_version}
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}
Requires(pre):	%{name}-smp = %{version}-%{release}

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description -l pl smp-drm
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nag��wkowe j�dra
Group:		Base/Kernel
Provides:	i2c-devel = 2.7.0
Provides:	bttv = 0.7.83
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
%if %{netfilter_snap} != 0
Provides:	%{name}-headers(netfilter) = %{iptables_version}-%{netfilter_snap}
%else
Provides:	%{name}-headers(netfilter) = %{iptables_version}
%endif
Provides:	%{name}-headers(grsecurity) = %{grsec_version}
Provides:	%{name}-headers(freeswan) = %{freeswan_version}
Provides:	%{name}-headers(evms)
Provides:	%{name}-headers(cdrw)
Provides:	%{name}-headers(cdmrw)
Provides:	%{name}-headers(hostap) = %{hostap_version}
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag��wkowe j�dra, niezbedne do rekompilacji j�dra
oraz niekt�rych program�w.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod �r�d�owy j�dra Linuxa
Group:		Base/Kernel
Autoreqprov:	no
Requires:	%{name}-headers = %{version}-%{release}
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
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zur�ckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien k�nnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description -l fr source
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont n�cessaires pour compiler la plupart des
programmes C, car il d�pend de constantes d�finies dans le code
source. Les sources peuvent �tre aussi utilis�e pour compiler un noyau
personnalis� pour avoir de meilleures performances sur des mat�riels
particuliers.

%description source -l pl
Pakiet zawiera kod �r�d�owy jadra systemu.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja do kernela
Group:		Base/Kernel
Provides:	%{name}-doc = %{version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description -l pl doc
Pakiet zawiera dokumentacj� j�dra z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -a3 -a4 -a6 -a7 -a8 -a9 -a10 -a12 -n linux-%{version}
%patch0 -p1
%patch1 -p1
%patch900 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%ifarch ppc
%patch907 -p1
%endif
%patch11 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
echo Added Device-mapper support ...
%patch18 -p1
%patch19 -p1
%patch23 -p1
%patch26 -p1
%patch27 -p1

%patch100 -p0
%patch101 -p1
%patch102 -p0
%patch104 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch113 -p1
%patch116 -p1
%patch117 -p1
%patch120 -p1
%patch121 -p0
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p1
%patch135 -p1
%patch136 -p0
%patch140 -p1
%patch141 -p1
%patch142 -p1

%patch200 -p1

# Tekram DC395/315 U/UW SCSI host driver
echo Adding Tekram DC395/315 driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/
%patch901 -p1

# Adaptec AACRaid nev drivers
echo Updating AAC driver ...
rm -f drivers/scsi/aacraid/*
cp aacraid/* drivers/scsi/aacraid/

# Fore 200e ATM NIC
echo Adding FORE 200e ATM driver
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch

# Netfilter
%patch8 -p1

%patch32 -p1
%patch31 -p1

# hostap
echo Installing Host AP support
patch -p1 -s < hostap-%{hostap_version}/kernel-patches/hostap-linux-%{version}.patch
cp hostap-%{hostap_version}/driver/modules/hostap*.[ch] drivers/net/wireless/

# Konica USB camera support
echo Installing Konica Support
%patch33 -p1

# Changing DRM source ....
echo Installing NEW DRM Source ...
cp drm/*.{c,h} drivers/char/drm/
%patch902 -p1

# WRR
echo Installing WRR Support
%patch34 -p1

# scancode
%patch35 -p1

# added missing MODULE_LICENSE, MODULE_DESCRIPTION, MODULE_AUTHOR
%patch914 -p1

# ACL support
echo Added ACL support
%patch45 -p1

%patch918 -p1
%patch919 -p1

#squashfs
%patch920 -p1

# NetMos support
echo Added NetMos card supprot
%patch46 -p1

%patch138 -p1

# sysctl controll of /dev/mem
echo Sysctl controll access to /dev/kmem 
%patch921 -p1 

%patch143 -p1
%patch145 -p1

# USB patches
%patch146 -p1

# VIA82Cxxx
echo Fixed VIA82Cxxx Audio ...
%patch910 -p1

#promise patch
echo Promise driver patch
%patch21 -p1
%patch22 -p1

#davfs
echo Added davFS support
%patch36 -p1
%patch37 -p1

# Nokia 5510 
echo Added Nokia5510 support
%patch38 -p1

# Audigy
echo Added Audigy SoundBlaster support ...
%patch20 -p1

# AIC79XX
echo Added Adapter AIC79XX controler support ...
%patch39 -p1

# i810 audio
echo Fixed I810 Sound ...
%patch40 -p1

%patch42 -p1
%patch43 -p1

%patch9 -p1

%patch29 -p1

# USB bluesooth
%patch44 -p1

# vlan patch
echo Updated 3Com drivers for VLAN ...
%patch47 -p1

# LVM 1.0.7
echo Added LVM support version %{lvm_version}
%patch114 -p1

# JFS - xattr+acl
echo Added xattr for JFS ...
%patch103 -p1

%patch917 -p1

#ptrace fix by Qboosh
%patch105 -p1

# to fix compile on gcc-3.3
%patch904 -p1

# Hash FiX. Initial by Qboosh, ipdated by me.
%patch112 -p1

# smell cleanup with crc32.
%patch126 -p1

#afs
#%%patch41 -p1

#impmi
%patch49 -p1 

#irixnfs
%patch50 -p1

#odirect
%patch51 -p1

#EXPORT_SYMBOL missing for acpi.
%patch48 -p1
 
# SYM53C8xx old
%patch55 -p1

#new IO scheduler
%patch56 -p1

#iForce joystick
%patch57 -p1
%patch58 -p1

echo Added ARCH specific patches....
%ifarch %{ix86}
echo Ix86 patches ...
# I810FB
echo Added Intel 810 FB support
%patch24 -p1
%patch25 -p1
# KT400
echo Added support for KT400 chipset
%patch144 -p1
#usb gadget
echo Added USB gadget ...
%patch30 -p1
#kt266/kl266 AGP
%patch137 -p1
#VIA8237 support
%patch134 -p1
#ioperm
%patch115 -p1 
#440gx
%patch52 -p1
#nforce2
%patch53 -p1
#EXPORT_SYMBOL for Ix86
%endif

%ifarch ppc
echo PPC patches ...
%patch130 -p0
#EXPORT_SYMBOL for PPC
%patch205 -p1
%patch903 -p1
%endif

%ifarch sparc64
echo SPARC64 patches ...
%patch118 -p1
%patch201 -p1
%endif

%ifarch sparc
echo SPARC patches ...
#EXPORT_SYMBOL for SPARC 
%patch202 -p1
%endif

%ifarch alpha
echo AXP patches ...
%patch119 -p0
#EXPORT_SYBMOL for AXP
%patch203 -p1
%patch204 -p1
%endif

# Remove -g from drivers/atm/Makefile and net/ipsec/Makefile
mv -f drivers/atm/Makefile drivers/atm/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*//g' drivers/atm/Makefile.orig > drivers/atm/Makefile
mv -f net/ipsec/Makefile net/ipsec/Makefile.orig
sed -e 's/EXTRA_CFLAGS.*-g//g' net/ipsec/Makefile.orig > net/ipsec/Makefile

# Fix EXTRAVERSION and CC in main Makefile
mv -f Makefile Makefile.orig
sed -e 's/EXTRAVERSION =.*/EXTRAVERSION =/g' \
%ifarch sparc64
    -e 's/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g' \
%endif
    Makefile.orig >Makefile

%build
BuildKernel() {
	%{?_debug:set -x}
	# is this a special kernel we want to build?
	BOOT=
	smp=
	[ "$1" = "BOOT" -o "$2" = "BOOT" ] && BOOT=yes
	[ "$1" = "smp" -o "$2" = "smp" ] && smp=yes
%ifarch %{ix86}
	if [ "$smp" = "yes" ]; then
		Config="ia32-smp"
	else
		Config="ia32"
	fi
%else
	if [ "$smp" = "yes" ]; then
		Config="%{_target_cpu}-smp"
	else
		Config="%{_target_cpu}"
	fi
%endif
	if [ "$BOOT" = "yes" ]; then
		KernelVer=%{version}-%{release}BOOT
	else
		KernelVer=%{version}-%{release}$1
	fi
	echo "BUILDING THE NORMAL KERNEL $*..."
:> arch/%{base_arch}/defconfig
	cat $RPM_SOURCE_DIR/kernel-$Config.config >> arch/%{base_arch}/defconfig
%ifarch i386
	echo "CONFIG_M386=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch i586
	echo "CONFIG_M586=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch i686
	echo "CONFIG_M686=y" >> arch/%{base_arch}/defconfig
%endif
%ifarch athlon
	echo "CONFIG_MK7=y" >> arch/%{base_arch}/defconfig
%endif
	cat %{SOURCE1002} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1003} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1004} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1005} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1006} >> arch/%{base_arch}/defconfig
	%{?_with_preemptive:cat %{SOURCE1999} >> arch/%{base_arch}/defconfig}
%ifnarch i386 i486
	cat %{SOURCE1007} >> arch/%{base_arch}/defconfig
%endif
	cat %{SOURCE1008} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1009} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1010} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1011} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1012} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1013} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1671} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1672} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1673} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1674} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1675} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1676} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1677} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1678} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1679} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1667} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1668} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1669} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1670} >> arch/%{base_arch}/defconfig
	
	if [ "$BOOT" = "yes" ] ; then
		echo "# CONFIG_MTRR is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_HOTPLUG_PCI is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_PM is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_MTD is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_PARPORT is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_BRIDGE is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IPSEC is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IPV6 is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_KHTTPD is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_PHONE is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_I2O is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_FDDI is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_PPP is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_SLIP is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_HAMRADIO is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_INPUT_GAMEPORT is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_INPUT_SERIO is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_JOYSTICK_IFORCE is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IPMI_HANDLER is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_WATCHDOG is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_AGPGART is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_DRM is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_VIDEO_DEV is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_FB is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_SOUND is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_NF_CONNTRACK is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_NF_QUEUE is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_NF_IPTABLES is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_VS is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_NETFILTER is not set" >> arch/%{base_arch}/defconfig
	
		echo "# CONFIG_GRKERNSEC is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_CRYPTO is not set" >> arch/%{base_arch}/defconfig
		echo "CONFIG_ROMFS_FS=y" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_NF_MATCH_STEALTH is not set">> arch/%{base_arch}/defconfig
		echo "# CONFIG_NET_SCH_WRR is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_HOSTAP is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_USB_KONICAWC is not set">> arch/%{base_arch}/defconfig
	fi

%ifarch sparc64
## Temporay - on SPARC64 can't build SHA suppor
	echo "# CONFIG_SHA1 is not set" >> arch/%{base_arch}/defconfig
	echo "# CONFIG_DIGEST_SHA1 is not set" >> arch/%{base_arch}/defconfig
	echo "# CONFIG_IPSEC_AUTH_HMAC_SHA1 is not set" >> arch/%{base_arch}/defconfig	
%endif

%{?_without_grsec:echo "# CONFIG_GRKERNSEC is not set" >> arch/%{base_arch}/defconfig}
%{?_without_grsec:echo "# CONFIG_IP_NF_MATCH_STEALTH is not set">> arch/%{base_arch}/defconfig}
%{!?_without_grsec:cat %{SOURCE1666} >> arch/%{base_arch}/defconfig}

%ifarch i386
	mv -f arch/%{base_arch}/defconfig arch/%{base_arch}/defconfig.orig
	sed -e 's/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/' \
		arch/%{base_arch}/defconfig.orig > arch/%{base_arch}/defconfig
%endif

	%{__make} mrproper
	ln -sf arch/%{base_arch}/defconfig .config

%ifarch sparc
	sparc32 %{__make} oldconfig
	sparc32 %{__make} dep clean
%else
	%{__make} oldconfig
	%{__make} dep clean
%endif
	%{__make} include/linux/version.h

# making  table for soundmodem.
	(cd drivers/net/hamradio/soundmodem; \
	%{__cc} -o gentbl -lm gentbl.c; \
	./gentbl)	

%ifarch %{ix86}
	%{__make} bzImage
%endif
%ifarch sparc
	sparc32 %{__make} boot
%else
%ifnarch %{ix86}
	%{__make}
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
%ifarch ppc
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinux-$KernelVer
	install vmlinux $KERNEL_INSTALL_DIR/boot/vmlinuz-$KernelVer
%endif
%ifarch sparc
        sparc32 %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
	echo KERNEL RELEASE $KernelVer
%else
        %{__make} modules_install \
     	INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
	KERNELRELEASE=$KernelVer
	echo KERNEL RELEASE $KernelVer
%endif
} # BuildKernel

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# make drivers/scsi/ missing files
#	(cd drivers/scsi; make -f M)

# UP KERNEL
%{!?_without_up:BuildKernel}

# SMP KERNEL
%{!?_without_smp:BuildKernel smp}

# BOOT kernel
%ifnarch i586 i686 athlon
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
%{!?_without_boot:BuildKernel BOOT}
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`

KERNEL_BUILD_INSTALL=no
%{!?_without_up:KERNEL_BUILD_INSTALL=yes}
%{!?_without_smp:KERNEL_BUILD_INSTALL=yes}
[ "$KERNEL_BUILD_INSTALL" = "yes" ] && cp -a $KERNEL_BUILD_DIR-installed/* $RPM_BUILD_ROOT

for i in "" smp ; do
	if [ -e  $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i ] ; then
		rm -f $RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
		ln -sf %{_prefix}/src/linux-%{version} \
			$RPM_BUILD_ROOT/lib/modules/%{version}-%{release}$i/build
	fi
done
ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf linux-%{version} $RPM_BUILD_ROOT%{_prefix}/src/linux

%ifarch sparc sparc64
ln -s /usr/src/linux/include/asm-sparc $RPM_BUILD_ROOT%{_includedir}/asm-sparc
ln -s ../src/linux/include/asm-sparc64 $RPM_BUILD_ROOT%{_includedir}/asm-sparc64
%else
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT/usr/include/asm
%endif

%if %{?_without_source:0}%{!?_without_source:1}
cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}/
%else
cp -a {include,scripts,Makefile,Rules.make,Documentation} $RPM_BUILD_ROOT/usr/src/linux-%{version}/
%endif

%ifarch sparc sparc64
sh %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%endif

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

%if %{?_without_source:0}%{!?_without_source:1}
%{__make} mrproper

find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32.config > .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config
%endif

%ifarch i386
echo "CONFIG_M386=y" >> .config
%endif
%ifarch i586
echo "CONFIG_M586=y" >> .config
%endif
%ifarch i686
echo "CONFIG_M686=y" >> .config
%endif
%ifarch athlon
echo "CONFIG_MK7=y" >> .config
%endif
cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1005} >> .config
cat %{SOURCE1006} >> .config
cat %{SOURCE1666} >> .config
cat %{SOURCE1667} >> .config
%{?_with_preemptive:cat %{SOURCE1999} >> .config}
%ifnarch i386 i486
	cat %{SOURCE1007} >> .config
%endif
cat %{SOURCE1008} >> .config
cat %{SOURCE1009} >> .config
cat %{SOURCE1010} >> .config
cat %{SOURCE1011} >> .config
cat %{SOURCE1012} >> .config
cat %{SOURCE1013} >> .config
cat %{SOURCE1668} >> .config
cat %{SOURCE1669} >> .config
cat %{SOURCE1670} >> .config
cat %{SOURCE1671} >> .config
cat %{SOURCE1672} >> .config
cat %{SOURCE1673} >> .config
cat %{SOURCE1674} >> .config
cat %{SOURCE1675} >> .config
cat %{SOURCE1676} >> .config
cat %{SOURCE1677} >> .config
cat %{SOURCE1678} >> .config
cat %{SOURCE1679} >> .config

%ifarch sparc
sparc32 %{__make} oldconfig
%else
%{__make} oldconfig
%endif

mv include/linux/autoconf.h include/linux/autoconf-up.h
cp .config config-up

%ifarch %{ix86}
cat $RPM_SOURCE_DIR/kernel-ia32-smp.config >> .config
%else
install $RPM_SOURCE_DIR/kernel-%{_target_cpu}-smp.config .config
%endif

%ifarch i386
echo "CONFIG_M386=y" >> .config
%endif
%ifarch i586
echo "CONFIG_M586=y" >> .config
%endif
%ifarch i686
echo "CONFIG_M686=y" >> .config
%endif
%ifarch athlon
echo "CONFIG_MK7=y" >> .config
%endif

cat %{SOURCE1002} >> .config
cat %{SOURCE1003} >> .config
cat %{SOURCE1004} >> .config
cat %{SOURCE1005} >> .config
cat %{SOURCE1006} >> .config
cat %{SOURCE1666} >> .config
cat %{SOURCE1667} >> .config
%{?_with_preemptive:cat %{SOURCE1999} >> .config}
%ifnarch i386 i486
	cat %{SOURCE1007} >> .config
%endif
cat %{SOURCE1008} >> .config
cat %{SOURCE1009} >> .config
cat %{SOURCE1010} >> .config
cat %{SOURCE1011} >> .config
cat %{SOURCE1012} >> .config
cat %{SOURCE1013} >> .config
cat %{SOURCE1668} >> .config
cat %{SOURCE1669} >> .config
cat %{SOURCE1670} >> .config
cat %{SOURCE1671} >> .config
cat %{SOURCE1672} >> .config
cat %{SOURCE1673} >> .config
cat %{SOURCE1674} >> .config
cat %{SOURCE1675} >> .config
cat %{SOURCE1676} >> .config
cat %{SOURCE1677} >> .config
cat %{SOURCE1678} >> .config
cat %{SOURCE1679} >> .config

%ifarch sparc
sparc32 %{__make} oldconfig
%else
%{__make} oldconfig
%endif
mv include/linux/autoconf.h include/linux/autoconf-smp.h
cp .config config-smp
%endif

install %{SOURCE1} $RPM_BUILD_ROOT/usr/src/linux-%{version}/include/linux/autoconf.h

%if %{?_without_source:0}%{!?_without_source:1}
# this generates modversions info which we want to include and we may as
# well include the depends stuff as well
%{__make} symlinks 
%{__make} include/linux/version.h
#%{__make} "`pwd`/include/linux/modversions.h"
%endif
rm -f include/linux/modversions.h
echo "#include <linux/modsetver.h>" > include/linux/modversions.h


# this generates modversions info which we want to include and we may as
# well include the depends stuff as well, after we fix the paths

%if %{?_without_source:0}%{!?_without_source:1}
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
%endif

# BOOT
%if %{?_without_boot:0}%{!?_without_boot:1}
%ifnarch i586 i686 athlon
install -d $RPM_BUILD_ROOT/%{_libdir}/bootdisk
cp -rdp $KERNEL_BUILD_DIR-installed/%{_libdir}/bootdisk/* $RPM_BUILD_ROOT/%{_libdir}/bootdisk
%endif
%endif

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/linux-%{version}-installed

%post
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null 
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release} /boot/vmlinuz
ln -sf System.map-%{version}-%{release} /boot/System.map

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release} /lib/modules/%{version}
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}.gz %{version}-%{release}
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}.gz /boot/initrd

if [ -f %{_prefix}/src/linux-%{version}/config-up ] ; then
	ln -s %{_prefix}/src/linux-%{version}/config-up %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post smp
mv -f /boot/vmlinuz /boot/vmlinuz.old 2> /dev/null > /dev/null
mv -f /boot/System.map /boot/System.map.old 2> /dev/null > /dev/null
ln -sf vmlinuz-%{version}-%{release}smp /boot/vmlinuz
ln -sf System.map-%{version}-%{release}smp /boot/System.map

if [ ! -L /lib/modules/%{version} ] ; then
	mv -f /lib/modules/%{version} /lib/modules/%{version}.rpmsave > /dev/null 2>&1
fi
rm -f /lib/modules/%{version}
ln -snf %{version}-%{release}smp /lib/modules/%{version}
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

/sbin/geninitrd -f --initrdfs=rom /boot/initrd-%{version}-%{release}smp.gz %{version}-%{release}smp
mv -f /boot/initrd /boot/initrd.old
ln -sf initrd-%{version}-%{release}smp.gz /boot/initrd

if [ -f %{_prefix}/src/linux-%{version}/config-smp ] ; then
	ln -s %{_prefix}/src/linux-%{version}/config-smp %{_prefix}/src/linux-%{version}/.config
fi

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post BOOT
if [ ! -L %{_libdir}/bootdisk/lib/modules/%{version} ] ; then
	mv -f %{_libdir}/bootdisk/lib/modules/%{version} %{_libdir}/bootdisk/lib/modules/%{version}.rpmsave
fi
if [ ! -L %{_libdir}/bootdisk/boot/vmlinuz-%{version} ] ; then
	mv -f %{_libdir}/bootdisk/boot/vmlinuz-%{version} %{_libdir}/bootdisk/boot/vmlinuz-%{version}.rpmsave
fi
rm -f %{_libdir}/bootdisk/lib/modules/%{version}
ln -snf %{version}-%{release}BOOT %{_libdir}/bootdisk/lib/modules/%{version}
rm -f %{_libdir}/bootdisk/boot/vmlinuz-%{version}
ln -snf vmlinuz-%{version}-%{release}BOOT %{_libdir}/bootdisk/boot/vmlinuz-%{version}

%postun
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}.gz

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release} > /dev/null 2>&1

%post drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release} > /dev/null 2>&1

%postun smp
if [ -L /lib/modules/%{version} ]; then 
	if [ "`ls -l /lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}smp" ]; then
		if [ "$1" = "0" ]; then
			rm -f /lib/modules/%{version}
		fi
	fi
fi
rm -f /boot/initrd-%{version}-%{release}smp.gz

%post smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp > /dev/null 2>&1

%post smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-drm
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp > /dev/null 2>&1

%postun BOOT
if [ -L %{_libdir}/bootdisk/lib/modules/%{version} ]; then 
	if [ "`ls -l %{_libdir}/bootdisk/lib/modules/%{version} | awk '{ print $11 }'`" = "%{version}-%{release}BOOT" ]; then
		if [ "$1" = "0" ]; then
			rm -f %{_libdir}/bootdisk/lib/modules/%{version}
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

%if %{?_without_up:0}%{!?_without_up:1}
%files
%defattr(644,root,root,755)
%ifarch alpha sparc ppc sparc64
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch ppc sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/ide/ide-cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%ifnarch sparc sparc64
%files pcmcia-cs
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.o*
%ifnarch ppc
/lib/modules/%{version}-%{release}/kernel/drivers/ide/ide-cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%endif

%ifnarch sparc sparc64
%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif			# %%{_without_up}
%endif

%if %{?_without_smp:0}%{!?_without_smp:1}
%files smp
%defattr(644,root,root,755)
%ifarch sparc ppc sparc64
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch ppc sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/ide/ide-cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/avmb1/avm_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*

%ifnarch sparc sparc64
%files -n kernel-smp-pcmcia-cs
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/dtl1_cs.o*
%ifnarch ppc
/lib/modules/%{version}-%{release}smp/kernel/drivers/ide/ide-cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
/lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/avmb1/avm_cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%endif

%ifnarch sparc sparc64
%files -n kernel-smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif			# %%{_without_smp}
%endif

%if %{?_without_boot:0}%{!?_without_boot:1}
%ifnarch i586 i686 athlon 		# narch
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc ppc sparc64		# arch
%{_libdir}/bootdisk/boot/vmlinux-%{version}-%{release}BOOT
%endif				#arch
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/build
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*
%endif				# narch
%endif				# %%{_without_boot}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include
%{_prefix}/src/linux-%{version}/Rules.make
%{_prefix}/src/linux-%{version}/config*
%{_includedir}/asm
%{_includedir}/linux

%if %{?_without_doc:0}%{!?_without_doc:1}
%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
%endif

%if %{?_without_source:0}%{!?_without_source:1}
%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{!?_without_grsec:%{_prefix}/src/linux-%{version}/grsecurity}
%{_prefix}/src/linux-%{version}/init
%{_prefix}/src/linux-%{version}/ipc
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
%endif
