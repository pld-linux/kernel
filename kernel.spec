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
%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/')
%define		no_install_post_strip	1
%define		no_install_post_compress_modules	1
#
%define		pre_version		pre1
%define		ipvs_version		1.0.7
%define		freeswan_version	1.97
%define		IPperson_version	20020819-2.4.19
%define		grsec_version		1.9.9c
%define		jfs_version		2.4-1.1.1
%define		lvm_version		1.0.5
%define		evms_version		1.2.0
%define		ntfs_version		2.1.0a
%define		drm_xfree_version	4.2.99
%define		hostap_version		2002-10-12
%define		netfilter_snap		20030306
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J±dro Linuxa
Name:		kernel
Version:	2.4.20
Release:	4.1%{?_with_preemptive:_pr}%{?_without_grsec:_nogrsec}
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-141.tar.gz
Source4:	linux-2.4.20-netfilter-%{netfilter_snap}.tar.gz
Source5:	linux-2.4.19-netfilter-IMQ.patch.tar.bz2
Source6:	http://download.sourceforge.net/ippersonality/ippersonality-%{IPperson_version}.tar.gz
Source7:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-%{jfs_version}.tar.gz
Source8:	http://www.xfree86.org/~alanh/linux-drm-%{drm_xfree_version}-kernelsource.tar.bz2
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
Source1000:	%{name}-addon.config
Source1001:	%{name}-netfilter.config
Source1100:	%{name}-preemptive.config
Source1666:	%{name}-grsec.config
Source2000:	%{name}-win4lin.config

# New features/updates/backports

# Essential stuff

Patch0:		%{name}-pldfblogo.patch
# from ftp://ftp.kerneli.org/pub/linux/kernel/crypto/v2.4/testing/
Patch10:	patch-int-2.4.20.1.bz2
Patch11:	loop-jari-2.4.20.0.patch
# from ftp://ftp.xs4all.nl/pub/crypto/freeswan/freeswan-*
Patch12:	linux-2.4.18-freeswan-%{freeswan_version}.patch.gz
Patch15:	linux-2.4.20-sched-O1.patch
Patch20:	http://dl.sourceforge.net/user-mode-linux/uml-patch-2.4.20-1.bz2
Patch21:	linux-2.4.20-uml-o1.patch
# http://unc.dl.sourceforge.net/sourceforge/user-mode-linux/host-skas3.patch
Patch22:	linux-2.4.20-uml-host-skas3.patch

# New filesystems

# http://linux-xfs.sgi.com/projects/xfs/
Patch25:	linux-2.4.20-core-xfs-1.2.0.patch.bz2
Patch26:	linux-2.4.20-xfs-1.2.0.patch.bz2
# http://acl.bestbits.at/
Patch30:	linux-2.4.20-jfs-xattr.patch
Patch31:	linux-2.4.20-jfs-1.1.1-acl.patch
Patch32:	linux-2.4.20-xattr+acl+trusted-0.8.55.diff.gz
Patch33:	linux-2.4.20-acl-intermezzo-fix.patch
# http://unc.dl.sourceforge.net/sourceforge/linux-ntfs/
Patch40:	linux-2.4.20-ntfs-%{ntfs_version}.patch.bz2
Patch41:	linux-2.4.20-ntfs.patch
# http://dl.sourceforge.net/linux-hfsplus/hfsplus-patch-20020606.patch
Patch45:	hfsplus-20020606.patch.bz2
# FC01_davfs_0.2.4.patch
Patch50:	linux-2.4.20-davfs-0.2.4.patch.bz2
# FC02_davfs__FUNCTION__.patch
Patch55:	linux-2.4.20-davfs-_FUNCTION_.patch
# quota for reiserfs
Patch60:	linux-2.4.20-reiserfs-quota.patch.bz2
# http://dl.sourceforge.net/squashfs/squashfs-1.1b.tar.gz
Patch65:	linux-2.4.20-squashfs.patch
#Patch70:	linux-2.4.20-afs.patch.bz2
#from http://sci.felk.cvut.cz/nwd/linux/nwd-patch-2.4.19
Patch75:	nwd-2.4.20.patch

# Networking

# new version of netfilter.
Patch100:	linux-2.4.20-netfilter-%{netfilter_snap}.patch.gz
# from http://users.pandora.be/bart.de.schuymer/ebtables/sourcecode.html
#	ebtables_v2.0.003_vs_2.4.20.diff
Patch110:	ebtables-v2.0.003_vs_2.4.20.patch.bz2
#	bridge-nf-0.0.10-against-2.4.20.diff
Patch111:	linux-2.4.20-bridge-nf-0.0.10.patch.bz2
# http://www.linuxvirtualserver.org/software/kernel-2.4/linux-2.4.18-ipvs-%{ipvs_version}.patch.gz
Patch115:	linux-2.4.20-ipvs-%{ipvs_version}.patch.bz2
Patch120:	http://luxik.cdi.cz/~devik/qos/imq-2.4.18.diff-10
# ftp://ftp.samba.org/pub/unpacked/ppp/linux/mppe/
Patch125:	linux-2.4.18-mppe.patch

# ATM bugfixes
# Patches by Chas Williams <chas@locutus.cmf.nrl.navy.mil>
Patch150:	atm-00-backport-2.5.patch
Patch151:	atm-01-Makefile.patch
Patch152:	atm-04-min-frame-size.patch
Patch153:	atm-05-multicast-lec.patch
Patch154:	atm-06-skb_pull.patch
Patch155:	atm-07-atm_dev_lock-sem.patch
Patch156:	atm-08-lane-MOD_USE_COUNT.patch
Patch157:	atm-09-suni-MOD_USE_COUNT.patch
Patch158:	atm-10-modular-atm.patch
Patch159:	atm-11-correct-lec-net_device-names.patch
Patch160:	atm-12-br2684-xmit-return.patch
Patch161:	atm-13-atm_vcc-cleanup.patch
Patch162:	atm-14-clip-neigh-lock.patch
Patch180:	atm-20-fore200e-gettimeofday.patch
# http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
# http://christophe.lizzi.free.fr/linux/linux-2.4.0-test9-fore200e-0.3.tar.gz
Patch181:	atm-21-fore200e-0.2f.patch
# Oopses on me - baggins
#Patch191:	atm-21-fore200e-0.3.patch
Patch185:	atm-30-idt77105-cleanup.patch

# New devices/drivers

# from http://people.sistina.com/~thornber/patches/2.4-stable/2.4.20/2.4.20-dm-9.tar.bz2DM-9 patch
Patch200:	linux-2.4.20-dm-9.patch.bz2
# EVMS support (http://www.sourceforge.net/projects/evms/)
Patch201:	linux-2.4.20-evms-1.9.0.patch.bz2
# from http://www.promise.com/support/file/driver/promise-patch-2.4.19.gz
Patch205:	linux-2.4.20-promise.patch.bz2
# from http://www.promise.com/support/file/driver/st6000src_1.30_01_0326.tgz
Patch206:	linux-2.4.20-promise-st6000.patch.bz2

#from http://prdownloads.sourceforge.net/i810fb/linux-2.4.20-i810fb.diff.bz2
Patch210:	linux-2.4.20-I810FB.patch.bz2

# Support for CDRW packet writing
Patch215:	%{name}-cdrw-packet.patch
Patch216:	%{name}-cd-mrw-2.patch
Patch220:	linux-2.4.19-pre8-konicawc.patch
Patch225:	wrr-linux-2.4.9.patch
Patch230:	linux-2.4.20-aic79xx.patch.bz2
Patch235:	linux-2.4.20-audigy.patch.bz2
Patch240:	linux-2.4.20-ecc.patch
Patch245:	linux-2.4.20-01-edd.patch
Patch246:	linux-2.4.20-02-edd-allocate.patch
#i2c - version 2.7.0
Patch255:	linux-2.4.20-i2c-2.7.0.patch.gz
# from ftp://ftp.lsil.com/pub/symchips/scsi/FusionMPT/Linux/2.03.00/mptlinux-2.03.00-src.tar.gz
Patch260:	linux-2.4.20-mptlinux-2.03.00.patch.bz2
Patch265:	linux-2.4.20-e820.patch
# Syntax bug
Patch270:	dc395-tab.patch
# http://www.qlogic.com/
Patch275:	linux-2.4.20-qla2x00-v6.04.00-fo.patch.gz

# The following go last as they touch a lot of code
# and/or are on bcond and/or are ifarch

# from http://grsecurity.net/grsecurity-%{grsec_version}.patch
Patch800:	grsecurity-%{grsec_version}-%{version}.patch.bz2
Patch801:	PPC-grsecurity-pgtable.h.patch
Patch802:	linux-2.4.20-grsecurity-%{grsec_version}-kmem.patch

# Win4Lin
#Patch900:	linux-2.4.20-Win4Lin.PLD.patch.bz2
#Patch991:	linux-2.4.20-Win4Lin-mki-adapter.patch.bz2

# Assorted bugfixes

# jam - http://giga.cps.unizar.es/~magallon/linux/kernel/
Patch1000:	jam-04-clone-detached.patch
Patch1001:	jam-05-module-size-checks.patch
Patch1002:	jam-06-force-inline.patch
Patch1003:	jam-07-scsi-error-tmout.patch
Patch1004:	jam-08-memparam.patch
Patch1005:	jam-09-cache-detection.patch
Patch1006:	jam-10-highpage-init.patch
Patch1007:	jam-11-self_exec_id.patch
Patch1008:	jam-15-fast-csum-D.patch
Patch1009:	jam-21-mem-barriers.patch
Patch1010:	jam-23-config-nr_cpus.patch
Patch1011:	jam-30-smptimers-A0.patch

Patch1100:	linux-2.4.18-lvm-VFSlock.patch
Patch1102:	linux-2.4.20-lvm-updates.patch

# fix lun probing on multilun RAID chassis
Patch1105:	linux-2.4.12-scsi_scan.patch
Patch1106:	linux-scsi-debug-bug.patch

Patch1110:	01-sound.diff
# This patch allows to create more than one sound device using alsa
# and devfs with two or more sound cards
Patch1111:	linux-sound_core.patch
Patch1112:	linux-2.4.21-pre4-ac4-via82cxxx_audio.patch.bz2
Patch1113:	linux-2.4.20-i810_audio.patch

# rivafb - fix for text background in 16bpp modes
Patch1150:	linux-rivafb16.patch
# misc tdfxfb fixes - detailed description inside
Patch1151:	linux-tdfxfb-fixes.patch
Patch1152:	linux-2.4.20-agp_uninorth.patch
Patch1153:	linux-2.4.20-radeonfb_clean.patch
Patch1154:	linux-2.4.20-drm-Makefile.patch
# support for VIA KT400 chipset in agpgart
Patch1155:	linux-2.4.20-kt400.patch

Patch1200:	hpt3xx.patch
Patch1201:	linux-2.4.10-cpqfc.patch
Patch1202:	linux-2.4.20-440gx.patch
Patch1203:	linux-2.4.20-amd-golem.patch
Patch1205:	linux-53c7,8xx-build.fix
Patch1206:	piix-ide-fix.patch
Patch1207:	linux-2.4.20-serverworks.patch
Patch1208:	PCI_ISA_bridge.patch
# this patch adds support for "io" and "irq" options in PCNet32 driver module
Patch1209:	linux-2.4.19-pcnet-parms.patch

# disable some networking printk's
Patch1250:	linux-2.4.1-netdebug.patch
Patch1251:	linux-2.4.2-raw-ip.patch
Patch1252:	linux-2.4.19-netmos_pci_parallel_n_serial.patch
Patch1253:	linux-proc_net_dev-counter-fix.patch
Patch1254:	kernel-2.4.17-netsyms-export-fix.patch
Patch1255:	linux-2.4.20-pre1-nr_frags.patch

Patch1301:	linux-2.4.18-hpfs.patch
Patch1302:	linux-2.4.18-nfs-default-size.patch
Patch1303:	linux-2.4.20-irixnfs.patch
# Tru64 NFS kludge
Patch1304:	linux-2.4.20-tru64nfs.patch
Patch1305:	linux-2.4.20-ext3-updates.patch
Patch1306:	linux-2.4.20-ext3.patch

Patch1350:	linux-2.4.18-nousb.patch
# usb patches from ftp://ftp.kernel.org/pub/linux/people/gregkh/usb/*-2.4.20.*
Patch1351:	linux-2.4.20-USB.patch.bz2
Patch1352:	linux-2.4.20-usb-bugs.patch
# PWC USB Webcam Driver update (only for 2.4.20; 2.4.21 should have this fix)
Patch1353:	linux-2.4.20-pwc.patch
# from http://www.noc.uoa.gr/~avel/page.php?page=nokia&lang=en
Patch1354:	linux-2.4.20-Nokia5510.patch

# raid5 xor fix for PIII/P4, should go away shortly
Patch1400:	linux-2.4.0-raid5xor.patch
Patch1401:	linux-2.4.0-nonintconfig.patch
# Add an ioctl to the block layer so we can be EFI compliant
Patch1402:	linux-2.4.2-blkioctl-sector.patch
Patch1403:	linux-2.4.3-pcipenalty.patch
Patch1404:	linux-2.4.3-rawio.patch
Patch1405:	linux-2.4.7-suspend.patch
Patch1406:	linux-2.4.7-quotareturn.patch
Patch1407:	kernel-Makefile-include-fix.patch
Patch1408:	kernel-pswscancode.patch
Patch1409:	linux-2.4.18-dmi-hall-of-shame.patch
Patch1410:	linux-2.4.18-input-35215.patch
Patch1411:	linux-2.4.18-kiobuf.patch
Patch1412:	linux-2.4.18-sendfile64.patch
Patch1413:	linux-2.4.20-andrea-fix-pausing.patch
Patch1414:	linux-2.4.20-oopsmeharder.patch
Patch1415:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
Patch1416:	linux-2.4.20-no-FPU.patch
Patch1417:	linux-2.4.20-initrd-close-fds.patch

Patch2000:	linux-PPC-SMP.patch
Patch2001:	linux-2.4-ppc-procesor.patch
Patch2002:	kernel-2.4.18-SPARC64-PLD.patch
Patch2003:	linux-2.4.20-AXP-avma1_cs.patch

Patch3000:	linux-2.4.1-compilefailure.patch
Patch3001:	linux-2.4.20-nicupdates.patch
Patch3002:	linux-2.4.20-EXPORT_SYMBOL.patch
Patch3003:	linux-2.4.20-missing-license-tags.patch
Patch3004:	linux-2.4.20-line.patch

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
Provides:	%{name}(netfilter) = 1.2.7a-%{netfilter_snap}
Provides:	%{name}(grsecurity) = %{grsec_version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Provides:	%{name}(cdrw)
Provides:	%{name}(cdmrw)
Provides:	%{name}(hostap)
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
Conflicts:	lvm < 1.0.4
Conflicts:	xfsprogs < 2.1.0
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	e2fsprogs < 1.25
Conflicts:	jfsutils < 1.0.12
Conflicts:	util-linux < 2.10o
Conflicts:	modutils < 2.4.2
Conflicts:	quota < 3.06

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enthält den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist für grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeß-Management, Geräte Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un système d'exploitation Linux. Le noyau traite les
fonctions basiques d'un système d'exploitation: allocation mémoire,
allocation de process, entrée/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j±dro Linuxa niezbêdne do prawid³owego dzia³ania
Twojego komputera. Zawiera w sobie sterowniki do sprzêtu znajduj±cego
siê w komputerze, takich jak karty muzyczne, sterowniki dysków, etc.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} für Multiprozessor-Maschinen
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Group:		Base/Kernel
Provides:	%{name}-smp = %{version}-%{release}
Provides:	module-info
Provides:	i2c = 2.7.0
Provides:	bttv = 0.7.83
Provides:	%{name}(netfilter) = 1.2.7a-%{netfilter_snap}
Provides:	%{name}(grsecurity) = %{grsec_version}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
Provides:	%{name}(cdrw)
Provides:	%{name}(cdmrw)
Provides:	%{name}(hostap)
Prereq:		fileutils
Prereq:		modutils
Prereq:		geninitrd >= 2.21
Autoreqprov:	no
Conflicts:	iptables < 1.2.7a
Conflicts:	lvm < 1.0.4
Conflicts:	xfsprogs < 2.1.0
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	e2fsprogs < 1.25
Conflicts:	jfsutils < 1.0.12
Conflicts:	util-linux < 2.10o
Conflicts:	modutils < 2.4.2
Conflicts:	quota < 3.06

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description -l de smp
Dieses Paket enthält eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird für Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description -l fr smp
Ce package inclu une version SMP du noyau de Linux version {version}.
Il et nécessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand même fonctionner pour les système mono-processeur.

%description -l pl smp
Pakiet zawiera j±dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj±ce dwa lub wiêcej procesorów.
Powinno równie¿ dobrze dzia³aæ na maszynach z jednym procesorem.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} für Installationsdisketten
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
Dieses Paket enthält eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description -l pl BOOT
Pakiet zawiera j±dro Linuksa dedykowane dyskietkom startowym i powinno
byæ u¿ywane jedynie podczas instalacji systemu. Wiele u¿ytecznych
opcji zosta³o wy³±czonych, aby jak najbardziej zmniejszyæ jego
rozmiar.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	Modu³y PCMCIA-CS 
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_version}).

%description -l pl pcmcia-cs
Modu³y PCMCIA-CS (%{pcmcia_version}).

%package smp-pcmcia-cs
Summary:	PCMCIA-CS modules for SMP kernel
Summary(pl):	Modu³y PCMCIA-CS dla maszyn SMP
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_version}
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}

%description smp-pcmcia-cs
PCMCIA-CS modules for SMP kernel (%{pcmcia_version}).

%description -l pl smp-pcmcia-cs
Modu³y PCMCIA-CS dla maszyn SMP (%{pcmcia_version}).

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
Summary(pl):	Pliki nag³ówkowe j±dra
Group:		Base/Kernel
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Provides:	i2c-devel = 2.7.0
Provides:	%{name}(netfilter) = 1.2.7a-%{netfilter_snap}
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nag³ówkowe j±dra, niezbedne do rekompilacji j±dra
oraz niektórych programów.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ¼ród³owy j±dra Linuxa
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
Das Kernel-Source-Paket enthält den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurückgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien können auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description -l fr source
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nécessaires pour compiler la plupart des
programmes C, car il dépend de constantes définies dans le code
source. Les sources peuvent être aussi utilisée pour compiler un noyau
personnalisé pour avoir de meilleures performances sur des matériels
particuliers.

%description source -l pl
Pakiet zawiera kod ¼ród³owy jadra systemu.

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
Pakiet zawiera dokumentacjê j±dra z katalogu
/usr/src/linux/Documentation.

%prep
%setup -q -a3 -a6 -a8 -a9 -n linux-%{version}
# JFS 1.1.1
rm -fr fs/jfs
gzip -dc %{SOURCE7} | tar -xf -
# Adaptec AACRaid new drivers
rm -fr drivers/scsi/aacraid
bzip2 -dc %{SOURCE10} | tar -xf - -C drivers/scsi/
# Changing DRM source ....
cp -f drm/*.{c,h} drivers/char/drm/
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch15 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch25 -p1
%patch26 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch40 -p1
%patch41 -p1
%patch45 -p1
%patch50 -p1
%patch55 -p1
%patch60 -p1
%patch65 -p1
#%patch70 -p1
%patch75 -p1
%patch100 -p1
%patch110 -p1
%patch111 -p1
%patch115 -p1
%patch120 -p1
%patch125 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%patch162 -p0
%patch180 -p1
%patch181 -p1
%patch185 -p1
%patch200 -p1
%patch201 -p1
%patch205 -p1
%patch206 -p1
%patch210 -p1
%patch215 -p1
%patch216 -p1
%patch220 -p1
%patch225 -p1
%patch230 -p1
%patch235 -p1
%patch240 -p1
%patch245 -p1
%patch246 -p1
%patch255 -p1
%patch260 -p1
%patch265 -p1
%patch275 -p1
%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%ifarch %{ix86}
%patch1008 -p1
%patch3004 -p1
%endif
%patch1009 -p1
%patch1010 -p1
%patch1011 -p1
%patch1100 -p1
%patch1102 -p1
%patch1105 -p1
%patch1106 -p0
%patch1110 -p1
%patch1111 -p1
%patch1112 -p1
%patch1113 -p1
%patch1150 -p1
%patch1151 -p1
%patch1152 -p1
%patch1153 -p1
%patch1154 -p1
%patch1155 -p1
%patch1200 -p1
%patch1201 -p1
%patch1202 -p1
%patch1203 -p1
%patch1205 -p1
%patch1206 -p0
%patch1207 -p1
%patch1208 -p0
%patch1209 -p1
%patch1250 -p1
%patch1251 -p1
%patch1252 -p1
%patch1253 -p1
%patch1254 -p0
%patch1255 -p1
%patch1301 -p1
%patch1302 -p1
%patch1303 -p1
%patch1304 -p1
%patch1305 -p1
%patch1306 -p1
%patch1350 -p1
%patch1351 -p1
%patch1352 -p1
%patch1353 -p1
%patch1354 -p1
%patch1400 -p1
%patch1401 -p1
%patch1402 -p1
%patch1403 -p1
%patch1404 -p1
%patch1405 -p1
%patch1406 -p1
%patch1407 -p0
%patch1408 -p1
%patch1409 -p1
%patch1410 -p1
%patch1411 -p1
%patch1412 -p1
%patch1413 -p1
%patch1414 -p1
%patch1415 -p0
%patch1416 -p1
%patch1417 -p1

%patch2000 -p0
%patch2001 -p1
%patch2002 -p1
%patch2003 -p1

%patch3000 -p1
%patch3001 -p1
%patch3002 -p1
%patch3003 -p1

# Tekram DC395/315 U/UW SCSI host driver
echo Adding Tekram DC395/315 driver
patch -p1 -s <dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/
%patch270 -p0

# IP personality
#echo Adding IP Personality 
#patch -p1 -s <ippersonality-%{IPperson_version}/patches/ippersonality-20020819-linux-2.4.19.diff

# hostap
echo Installing Host AP support
patch -p1 -s < hostap-%{hostap_version}/kernel-patches/hostap-linux-2.4.19-rc3.patch
cp hostap-%{hostap_version}/driver/modules/hostap*.[ch] drivers/net/wireless/

# The following go last as they touch a lot of code
# and/or are on bcond and/or are ifarch

%{!?_without_grsec:echo GRSecurity}
%{!?_without_grsec:%patch800 -p1}
%{!?_without_grsec:%patch801 -p1}
%{!?_without_grsec:%patch802 -p1}

#%ifarch %{ix86}
#echo Win4Lin patch ...
#%patch900 -p1
#%patch991 -p1
#%endif

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
	%{?_with_preemptive:cat %{SOURCE1100} >> arch/%{base_arch}/defconfig}
	%{!?_with_preemptive:echo "# CONFIG_PREEMPT is not set" >> arch/%{base_arch}/defconfig}
	cat %{SOURCE1000} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1001} >> arch/%{base_arch}/defconfig
	
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
%ifarch %{ix86}
		cat %{SOURCE2000} >> arch/%{base_arch}/defconfig
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
}

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
%{?_with_preemptive:cat %{SOURCE1100} >> .config}
%{!?_with_preemptive:echo "# CONFIG_PREEMPT is not set" >> .config}
cat %{SOURCE1000} >> .config
cat %{SOURCE1001} >> .config
%{!?_without_grsec:cat %{SOURCE1666} >> .config}

%ifarch %{ix86}
cat %{SOURCE2000} >> .config
%endif

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

%{?_with_preemptive:cat %{SOURCE1100} >> .config}
%{!?_with_preemptive:echo "# CONFIG_PREEMPT is not set" >> .config}
cat %{SOURCE1000} >> .config
cat %{SOURCE1001} >> .config
%{!?_without_grsec:cat %{SOURCE1666} >> .config}

%ifarch %{ix86}
cat %{SOURCE2000} >> .config
%endif

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
rm -rf $RPM_BUILD_DIR/linux-installed

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
#%{_prefix}/src/linux-%{version}/kdb
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
