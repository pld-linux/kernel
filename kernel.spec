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
# _without_w4l		- don't build Win4Lin support
#

%define		patch_level	4
%define		_rel		6
%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')
%define		no_install_post_strip	1

%define		ipvs_version		1.0.7
%define		freeswan_version	2.00
%define		IPperson_version	20020819-2.4.19
%define		grsec_version		2.0-pre3
%define		jfs_version		1.1.2
%define		lvm_version		1.0.7
%define		evms_version		2.0.0
%define		ntfs_version		2.1.3a
%define		drm_xfree_version	4.3.0
%define		hostap_version		0.0.1
%define		netfilter_snap		20030428
%define		iptables_version	1.2.8
%define		ACL_version		0.8.56
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J�dro Linuxa
Name:		kernel
Version:	2.4.20
%if %{patch_level} !=0
Release:	%{_rel}pl%{patch_level}%{?_without_grsec:_nogrsec}
%else
Release:	%{_rel}%{?_without_grsec:_nogrsec}
%endif
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-141.tar.gz
Source4:	http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
Source5:	linux-2.4.19-netfilter-IMQ.patch.tar.bz2
Source6:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source7:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-2.4-%{jfs_version}.tar.gz
Source8:	http://www.xfree86.org/~alanh/linux-drm-%{drm_xfree_version}-kernelsource.tar.gz
Source9:	http://hostap.epitest.fi/releases/hostap-%{hostap_version}.tar.gz
Source10:	linux-2.4.20-aacraid.tar.bz2

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

##
# Patches
##

Patch0:		%{name}-pldfblogo.patch

## -> Crypto
# from: ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/testing/
Patch1:		patch-int-2.4.20.1.bz2
Patch2:		loop-jari-2.4.20.0.patch

## -> general bugfix.
Patch4:		linux-2.4.20-initrd-close-console.patch
Patch5:		linux-2.4.20-no-FPU.patch
Patch6:		linux-53c7,8xx-build.fix
Patch7:		%{name}-Makefile-include-fix.patch
# support for new chipset ? E820
# from:
Patch8:		linux-2.4.20-e820.patch
# all missing parts
Patch9:		linux-2.4.20.patch

## -> grsecurity and other security 
# from: http://grsecurity.net/grsecurity-%{grsec_version}.patch
Patch15:	grsecurity-%{grsec_version}-%{version}.patch.gz
#made by Qboosh
Patch16:	linux-2.4.20-ptrace.patch
Patch17:	linux-2.4.20-nogrsec.patch
Patch18:	linux-2.4.20-grsecurity-1.9.9e-kmem.patch

## -> Security and network
#from: ftp://ftp.xs4all.nl/pub/crypto/freeswan/freeswan-*
Patch19:	linux-2.4-freeswan-%{freeswan_version}.patch.gz


## -> New filesystems.
# from: ftp://linux-xfs.sgi.com/projects/xfs/download/Release-1.2pre5/kernel_patches/
Patch20:	linux-2.4.20-xfs-1.2.0.patch.gz
# from: http://unc.dl.sourceforge.net/sourceforge/linux-ntfs/
Patch21:	linux-2.4.20-ntfs-%{ntfs_version}.patch.gz
# from: http://dl.sourceforge.net/linux-hfsplus/hfsplus-patch-20020606.patch
Patch22:	hfsplus-20020606.patch.bz2
# from: http://people.sistina.com/~thornber/patches/2.4-stable/2.4.20/2.4.20-dm-10.tar.bz2
Patch23:	linux-2.4.20-dm-10.patch.gz
# EVMS support 
# from: http://www.sourceforge.net/projects/evms/
Patch24:	linux-2.4.20-evms-%{evms_version}.patch.gz
# from MDK kernel
# davfs2-0.2.1.tar.gz
Patch25:	linux-2.4.20-davfs-0.2.4.patch.bz2
# based on FC02_davfs__FUNCTION__.patch and small fix
Patch26:	linux-2.4.20-davfs-fix.patch
# from:
Patch27:	linux-2.4.20-afs.patch.bz2
# from: http://acl.bestbits.at/
Patch28:	linux-2.4.20-ACL-%{ACL_version}.patch.gz
# from:
Patch29:	jfs-2.4.20.patch
# from: http://www-124.ibm.com/developerworks/oss/jfs/
# JFS for Linux [patch ID 399]
Patch30:	linux-2.4.20-jfs-1.1.2-xattr.patch.gz
# from:
Patch31:	linux-2.4.20-squashfs.patch
# from:
# quota for reiserfs
Patch32:	linux-2.4.20-reiserfs-quota.patch.bz2
# from:
Patch33:	linux-2.4.20-ext3.patch
# from: ftp://ftp.sistina.com/pub/LVM/1.0/lvm_%{lvm_version}.tar.gz
# Created from lvm.tgz:LVM/PATCHES by doing make
Patch34:	linux-2.4.20-LVM-%{lvm_version}.patch.bz2
#hpfs fix
Patch35:	linux-2.4.18-hpfs.patch

## -> Preemptive kernel  patch
# from:
Patch40:	ftp://ftp.kernel.org/pub/linux/kernel/people/rml/preempt-kernel/v2.4/preempt-kernel-rml-2.4.20-3.patch


## -> Network
# from: cvs -d :pserver:cvs@pserver.netfilter.org:/cvspublic co netfilter
%if %{netfilter_snap} != 0
Patch45:		linux-2.4.20-netfilter-%{iptables_version}_%{netfilter_snap}.patch.gz
%else
Patch45:		linux-2.4.20-netfilter-%{iptables_version}.patch.gz
%endif
# from:
Patch46:	http://luxik.cdi.cz/~devik/qos/imq-2.4.18.diff-10
# from: http://users.pandora.be/bart.de.schuymer/ebtables/sourcecode.html
#		ebtables_v2.0.003_vs_2.4.20.diff
Patch47:	ebtables-v2.0.003_vs_2.4.20.patch.bz2
#		bridge-nf-0.0.10-against-2.4.20.diff
Patch48:	linux-2.4.20-bridge-nf-0.0.10.patch.gz
# from: http://wipl-wrr.sourceforge.net/tgz-wrr/wrr-021019.tar.gz
Patch49:	wrr-linux-2.4.19.patch.gz
# from: ftp://ftp.samba.org/pub/unpacked/ppp/linux/mppe/
Patch50:	linux-2.4.18-mppe.patch
# from: ftp://ftp.sf.net/pub/sourceforge/lcdpd/lcdp-0.2.3-linux-2.4.18.patch.gz
Patch51:	linux-2.4.20-lcdp-0.2.3.patch.gz

## -> sound
# from: ???
Patch55:	linux-2.4.20-audigy.patch.bz2
# from:
Patch56:	linux-2.4.20-i810_audio.patch

## -> drivers
# from: http://www.promise.com/support/file/driver/promise-patch-2.4.19.gz
Patch60:	linux-2.4.20-promise.patch.bz2
# from: http://www.promise.com/support/file/driver/st6000src_1.30_01_0326.tgz
Patch61:	linux-2.4.20-promise-st6000.patch.bz2
# PC Speaker driver
# from: http://www.geocities.com/stssppnn/pcsn-kernel-2.4.20.diff.gz
Patch62:	linux-2.4.20-pcsp.patch.gz
#usb patches 
# from: ftp://ftp.kernel.org/pub/linux/people/gregkh/usb/*-2.4.20.*
Patch63:	linux-2.4.20-USB.patch.bz2
# from: http://people.freebsd.org/~gibbs/linux/SRC/
#last: aic79xx-linux-2.4-20030424-tar.gz
Patch64:	linux-2.4.20-aic79xx.patch.gz
# from: MDK kernel DV08__i810fb.patch
Patch65:	linux-2.4.20-I810FB.patch.bz2
Patch66:	linux-2.4.20-I810FB_lock_page_fix.patch
Patch67:	linux-2.4.20-radeonfb_clean.patch
Patch68:	linux-2.4.20-agp_uninorth.patch
# rivafb - fix for text background in 16bpp modes
Patch69:	linux-rivafb16.patch
# misc tdfxfb fixes - detailed description inside
Patch70:	linux-tdfxfb-fixes.patch
#support for VIA KT400 chipset in agpgart
Patch71:	linux-2.4.20-kt400.patch
#i2c - version 2.7.0
Patch72:	linux-2.4.20-i2c-2.7.0.patch.gz
# from: http://kernel.bkbits.net/~david-b/gadget24-0331.patch
Patch73:	linux-2.4-USB-gadget-20030331.patch.bz2
# from: ftp://ftp.lsil.com/pub/symchips/scsi/FusionMPT/Linux/2.03.00/mptlinux-2.03.00-src.tar.gz
Patch74:	linux-2.4.20-mptlinux-2.03.00.patch.bz2
## DRM
Patch75:	linux-2.4.20-drm-Makefile.patch
# from http://www.noc.uoa.gr/~avel/page.php?page=nokia&lang=en
Patch76:	linux-2.4.20-Nokia5510.patch
# from:
Patch77:	linux-2.4.20-ecc.patch
# from http://www.holtmann.org/linux/kernel/patch-2.4.20-mh6.gz
Patch78:	linux-2.4.20-mh6.patch.bz2
#fix for DC395
Patch79:	dc395-tab.patch

## Support for CDRW packet writing
Patch100:	%{name}-cdrw-packet.patch
Patch101:	%{name}-cd-mrw-2.patch










#Patch33:	linux-2.4.19-pre8-konicawc.patch
#Patch35:	%{name}-pswscancode.patch
#Patch46:	linux-2.4.19-netmos_pci_parallel_n_serial.patch
#Patch47:	linux-2.4-3com-vlan.patch
#Patch102:	PCI_ISA_bridge.patch
## raid5 xor fix for PIII/P4, should go away shortly
#Patch107:	linux-2.4.0-raid5xor.patch
## disable some networking printk's
#Patch108:	linux-2.4.1-netdebug.patch
#Patch118:	%{name}-2.4.18-SPARC64-PLD.patch
#Patch119:	linux-AXP.patch
#Patch121:	%{name}-2.4.17-netsyms-export-fix.patch
#Patch124:	%{name}-gcc31.patch
#Patch130:	linux-PPC-SMP.patch
#Patch131:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
#Patch132:	ide-EXPORT_SYMBOL.fix
#Patch133:	linux-proc_get_inode.patch
#Patch136:	piix-ide-fix.patch
#Patch138:	http://www.uwsg.indiana.edu/hypermail/linux/kernel/0212.0/att-1445/01-sound.diff
#Patch140:	linux-2.4.20-pwc.patch
#Patch200:	linux-sound_core.patch
#Patch201:	linux-2.4.20-SPARC64.patch
#Patch202:	linux-2.4.20-SPARC-EXPORT_SYMBOL.patch
#Patch203:	linux-2.4.20-AXP-EXPORT_SYMBOL.patch
#Patch204:	linux-2.4.20-AXP-avma1_cs.patch
#Patch205:	linux-2.4.20-PPC-EXPORT_SYMBOL.patch
#Patch903:	linux-2.4-ppc-procesor.patch
#Patch910:	linux-2.4.21-pre4-ac4-via82cxxx_audio.patch.bz2



















# fixed missing MODULE_{AUTHOR,DESCRIPTION,LICENSE}
Patch995:	linux-2.4.20-missing-module.patch
# added missinf EXPORT_SYMBOL
Patch1000:	linux-2.4.20-EXPORT_SYMBOL.patch

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
Provides:	%{name}(cdrw)
Provides:	%{name}(cdmrw)
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
%setup -q -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -n linux-%{version}

## Applayed patches manualy.
# Tekram DC395/315 U/UW SCSI host driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/

# Adaptec AACRaid nev drivers
rm -f drivers/scsi/aacraid/*
cp aacraid/* drivers/scsi/aacraid/

# Fore 200e ATM NIC
patch -p1 -s <linux-2.3.99-pre6-fore200e-0.2f/linux-2.3.99-pre6-fore200e-0.2f.patch

# hostap
patch -p1 -s < hostap-%{hostap_version}/kernel-patches/hostap-linux-%{version}.patch
cp hostap-%{hostap_version}/driver/modules/hostap*.[ch] drivers/net/wireless/

# Changing DRM source ....
cp drm/*.{c,h} drivers/char/drm/

# end of .....

%patch0 -p1

## Crypto
%patch1 -p1
%patch2 -p1

## general bugfix
%patch4 -p1
%patch5 -p1
#fixed to build NCR SCSI driver
%patch6 -p1
#fixed includes
%patch7 -p1
%ifarch %{ix86}
%patch8 -p1
%endif
%patch9 -p1

##grsecurity and other sec.
%patch15 -p1
#ptrace fix by Qboosh
%patch16 -p1
%{?_without_grsec:%patch17 -p1}
# sysctl controll of /dev/mem
%patch18 -p1 

%patch19 -p1


## filesystems
#XFS
%patch20 -p1
#NTFS
%patch21 -p1
#HFS+
%patch22 -p1
#DM
%patch23 -p1
#EVMS
%patch24 -p1
#DavFS
%patch25 -p1
#fix for davfs
%patch26 -p1
#afs
#%patch27 -p1
#ACL
%patch28 -p1
#jfs
%patch29 -p1
#xattr for jfs
%patch30 -p1
#squashfs
%patch31 -p1
#quota for reiserfs
%patch32 -p1
#ext3
%patch33 -p1
#LVM
%patch34 -p1


## Preemptive
%ifnarch sparc sparc64
%patch40 -p1
%endif


## Network
#netfilter
%patch45 -p1
#imq
%patch46 -p1
#ebtable
%patch47 -p1
#bridge-nf
%patch48 -p1
#wrr
%patch49 -p1
#mppe
%patch50 -p1
#lcdp
%patch51 -p1

## Sound
#Audigy
%patch55 -p1
#i810-audio
%patch56 -p1


## Drivers
#promise
%patch60 -p1
#promise ST6000
%patch61 -p1
# PC Speaker
%patch62 -p1
#USB
%patch63 -p1
#AIC79XX
%patch64 -p1
#i810FB
%patch65 -p1
#i810FB fix
%patch66 -p1
#RadeonFB clean
%patch67 -p1
#AGP Uninorth
%patch68 -p1
#RivaFB
%patch69 -p1
#tdfxfb fix
%patch70 -p1
#KT400
%patch71 -p1
#i2c
%patch72 -p1
#USB gadget
%ifnarch ppc
## Or fix ...
%patch73 -p1
%endif
#Fusion MPT
%patch74 -p1
## ->DRM
%patch75 -p1
#Nokia5510 patch
%patch76 -p1
#ecc
%patch77 -p1
#Bluetooth
%patch78 -p1
# fix for DC395
%patch79 -p1

# LAST patch
%patch995 -p1
%patch1000 -p1

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
	cat %{SOURCE1999} >> arch/%{base_arch}/defconfig
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
		echo "# CONFIG_GRKERNSEC is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_CRYPTO is not set" >> arch/%{base_arch}/defconfig
		echo "CONFIG_ROMFS_FS=y" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_IP_NF_MATCH_STEALTH is not set">> arch/%{base_arch}/defconfig
		echo "# CONFIG_NET_SCH_WRR is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_HOSTAP is not set" >> arch/%{base_arch}/defconfig
		echo "# CONFIG_USB_KONICAWC is not set">> arch/%{base_arch}/defconfig
	%ifarch %{ix86}
		echo "# CONFIG_MKI is not set" >> arch/%{base_arch}/defconfig
	%endif
	fi
%ifnarch %{ix86}
#		echo "# CONFIG_IP_NF_MATCH_FUZZY is not set">> arch/%{base_arch}/defconfig
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
cat %{SOURCE1999} >> .config
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
cat %{SOURCE1999} >> .config
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
%ifarch alpha sparc ppc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
%ifnarch sparc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch ppc sparc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/ide/ide-cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%ifnarch sparc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%ifnarch sparc
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

%ifnarch sparc
%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif			# %%{_without_up}
%endif

%if %{?_without_smp:0}%{!?_without_smp:1}
%files smp
%defattr(644,root,root,755)
%ifarch sparc ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
%ifnarch sparc
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch ppc sparc
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/ide/ide-cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/isdn/avmb1/avm_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%ifnarch sparc
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}smp/build
%ghost /lib/modules/%{version}-%{release}smp/modules.*

%ifnarch sparc
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

%ifnarch sparc
%files -n kernel-smp-drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/drm
%endif			# %%{_without_smp}
%endif

%if %{?_without_boot:0}%{!?_without_boot:1}
%ifnarch i586 i686 athlon 		# narch
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc ppc		# arch
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
#%%{_prefix}/src/linux-%{version}/kdb
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
%{_prefix}/src/linux-%{version}/Rules.make
%{_prefix}/src/linux-%{version}/config*
%endif
