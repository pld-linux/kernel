#
# Conditional build:
%bcond_without	smp		# don't build SMP kernel
%bcond_without	up		# don't build UP kernel
%bcond_without	boot		# don't build BOOT kernel
%bcond_without	source		# don't build source
%bcond_without	doc		# don't build documentation package
%bcond_without	grsec		# don't apply grsecurity patch
%bcond_with	win4lin		# apply the Win4lin patches
#
%define		base_arch %(echo %{_target_cpu} | sed 's/i.86/i386/;s/athlon/i386/;s/amd64/x86_64/')
%define		no_install_post_strip	1
%define		no_install_post_compress_modules	1
#
%define		pre_version		%{nil}
%define		netfilter_snap		20031209
%define		i2c_version		2.8.3
Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(es):	N�cleo (Kernel) linux gen�rico
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(ja):	Linux �����ͥ� (Linux ���ڥ졼�ƥ��󥰥����ƥ�ο�¡��ʬ)
Summary(pl):	J�dro Linuksa
Summary(pt_BR):	Kernel Linux (a parte central do sistema operacional Linux)
Name:		kernel
Version:	2.4.25
Release:	0.3
License:	GPL v2
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-2.4.24.tar.bz2
# Source0-md5:	1e055c42921b2396a559d84df4c3d9aa
Source1:	%{name}-autoconf.h
Source2:	%{name}-BuildASM.sh
Source3:	http://www.garloff.de/kurt/linux/dc395/dc395-141.tar.gz
# Source3-md5:	8ed492197244b6a772270417c66214d3
Source7:	http://www10.software.ibm.com/developer/opensource/jfs/project/pub/jfs-2.4-1.1.4.tar.gz
# Source7-md5:	ea33c28ca1d3afa448b20f337b615b48
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
Source1002:	%{name}-grsec.config
Source2000:	%{name}-win4lin.config

# New features/updates/backports

# Essential stuff

Patch0:		patch-2.4.25-pre8.bz2

Patch1:		%{name}-pldfblogo.patch

# from ftp://ftp.kernel.org/pub/linux/kernel/people/hvr/testing/
Patch10:	patch-cryptoloop-jari-2.4.22-rc2.0
# from ftp://ftp.xs4all.nl/pub/crypto/freeswan/freeswan-*
Patch12:	linux-2.4.23-freeswan-2.04.patch.gz
Patch15:	linux-2.4.25-sched-O1.patch
# http://dl.sourceforge.net/user-mode-linux/uml-patch-2.4.20-6.bz2
Patch20:	uml-patch-2.4.20-6-21.bz2
Patch21:	linux-2.4.21-uml-o1.patch
# http://dl.sourceforge.net/user-mode-linux/host-skas3.patch
Patch22:	linux-2.4.20-uml-host-skas3.patch
# http://www.kernel.org/pub/linux/kernel/people/jgarzik/libata/
Patch23:	2.4.25-pre4-libata1.patch.bz2
# missing <linux/mm.h> include in libata-core.c (needed on alpha)
Patch24:	linux-2.4.23-libata1-include.patch

# New filesystems

# http://acl.bestbits.at/
Patch31:	linux-2.4.21-jfs-acl.patch
Patch32:	linux-2.4.25-ea-acl-nfsacl-2.4.23-0.8.65.diff.gz
# http://dl.sourceforge.net/linux-ntfs/
Patch40:	linux-2.4.24-ntfs-2.1.6a.patch.bz2
# FC01_davfs_0.2.4.patch
Patch50:	linux-2.4.20-davfs-0.2.4.patch.bz2
# FC02_davfs__FUNCTION__.patch
Patch55:	linux-2.4.20-davfs-_FUNCTION_.patch
# ftp://ftp.suse.com/pub/people/mason/patches/data-logging/2.4.23/
# ftp://ftp.suse.com/pub/people/jeffm/reiserfs/aclea/2.4.23/
Patch56:	01-reiserfs-free-blocks.diff.gz
Patch57:	02-akpm-b_journal_head-1.diff.gz
Patch58:	03-reiserfs-sync_fs-5.diff.gz
Patch59:	04-data-logging-40.diff.gz
Patch60:	05-reiserfs-quota-28.diff.gz
Patch61:	06-kinoded-9.diff.gz
Patch62:	06-write_times.diff.gz
Patch63:	01-reiserfs-xattrs-2.4.23+datalogging+quota-03
Patch64:	02-reiserfs-acl-2.4.23+datalogging+quota-03
# http://dl.sourceforge.net/squashfs/
Patch65:	squashfs1.3r3-2.4.25.patch
#from http://sci.felk.cvut.cz/nwd/linux/nwd-patch-2.4.19
Patch70:	nwd-2.4.21.patch
Patch80:	linux-2.4.25-intermezzo-acl.patch

# Networking

# ALWAYS use released patchomatic tarball (don't use CVS)
# DO NOT include patches from patch-o-matic/userspace since they cause iptables incompatibilities
Patch100:	linux-2.4.23-netfilter-pom-%{netfilter_snap}.patch.gz
Patch101:	linux-2.4.23-netfilter-IMQ-target.patch
# http://rnvs.informatik.uni-leipzig.de/ipp2p/index_en.html
# http://rnvs.informatik.uni-leipzig.de/ipp2p/downloads/ipp2p-0.5a_vs_2.4.22.diff.gz
Patch102:	ipp2p-0.5a_vs_2.4.22.diff.gz

# http://ebtables.sourceforge.net/
Patch110:	ebtables-brnf-3_vs_2.4.22.diff.gz
# http://trash.net/~kaber/imq/
Patch120:	linux-2.4.21-imq-1.diff
# ftp://ftp.samba.org/pub/unpacked/ppp/linux/mppe/
Patch125:	linux-2.4.18-mppe.patch
Patch130:	linux-2.4.22-tun-new-style.patch

# ATM bugfixes
# Patches by Chas Williams <chas@locutus.cmf.nrl.navy.mil>
# Included in Chas patch:
# http://tulipe.cnam.fr/personne/lizzi/linux/linux-2.3.99-pre6-fore200e-0.2f.tar.gz
# http://christophe.lizzi.free.fr/linux/linux-2.4.0-test9-fore200e-0.3.tar.gz
# ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/
Patch150:	linux-2.4.21-atm_diffs.patch
Patch151:	ftp://ftp.cmf.nrl.navy.mil/pub/chas/linux-atm/vbr/vbr-kernel-diffs
Patch152:	linux-2.4.22-fore200e-0.2f.patch

# New devices/drivers

# http://people.sistina.com/~thornber/patches/2.4-stable/
Patch200:	linux-2.4.25-dm-3.patch

# EVMS additional patches (http://www.sourceforge.net/projects/evms/)
Patch205:	linux-2.4.25-evms-2.2.1.patch

#from http://dl.sourceforge.net/i810fb/linux-2.4.20-i810fb.diff.bz2
Patch210:	linux-2.4.21-I810FB.patch.gz

# Support for CDRW packet writing
Patch215:	%{name}-cdrw-packet.patch
Patch216:	%{name}-cd-mrw-2.patch
Patch225:	wrr-linux-2.4.9.patch
Patch226:	linux-2.4.18-esfq.diff
# http://l7-filter.sourceforge.net/
Patch227:	layer7-kernel2.4patch-v0.4.1a.patch.gz

Patch235:	linux-2.4.20-audigy.patch.bz2
Patch240:	linux-2.4.20-ecc.patch
# i2c - http://secure.netroedge.com/~lm78/
Patch255:	linux-2.4.25-i2c-%{i2c_version}-1.patch
Patch256:	linux-2.4.21-i2c-headers.patch
Patch257:	linux-2.4.21-i2c-sparc64.patch
Patch265:	linux-2.4.20-e820.patch
# Syntax bug
Patch270:	dc395-tab.patch
# http://www.qlogic.com/
Patch275:	linux-2.4.20-qla2x00-v6.04.00-fo.patch.gz

# TV stuff from http://bytesex.org/
Patch301:	20_v4l2-2.4.23-pre7.diff.gz
Patch302:	30_bt832-2.4.23-pre7.diff
Patch303:	30_btaudio-2.4.23-pre7.diff

# AIC7XXX
# based on http://people.freebsd.org/~gibbs/linux/SRC/aic79xx-linux-2.4-20031222-tar.gz
Patch350:	linux-2.4.24-aic79xxx-20031222.patch

# I18N stuff
# Adds a sysctl for controlling the default iocharset
Patch400:	%{name}-nls_default.patch

# ftp://ftp.suse.com/pub/people/stepan/bootsplash/kernel/
Patch450:	bootsplash-3.0.7-2.4.25.patch

# The following go last as they touch a lot of code
# and/or are on bcond and/or are ifarch

# Win4Lin
Patch900:	linux-2.4.20-Win4Lin.PLD.patch.bz2
Patch901:	linux-2.4.20-Win4Lin-mki-adapter.patch.bz2

# http://openipmi.sourceforge.net/
Patch950:	linux-2.4.23-ipmi-v28.patch

# Assorted bugfixes

# jam - http://giga.cps.unizar.es/~magallon/linux/kernel/
Patch1000:	jam-04-clone-detached.patch
Patch1002:	jam-06-force-inline.patch
Patch1003:	jam-07-scsi-error-tmout.patch
Patch1006:	jam-10-highpage-init.patch
Patch1007:	jam-11-self_exec_id.patch
Patch1008:	jam-15-fast-csum-D.patch
Patch1009:	jam-21-mem-barriers.patch
Patch1010:	jam-30-smptimers-A0.patch

Patch1102:	linux-2.4.20-lvm-updates.patch

# IrDA patch for broken IBM Latpops
Patch1104:	linux-2.4.21-irda-ibm.patch

# fix lun probing on multilun RAID chassis
Patch1105:	linux-2.4.12-scsi_scan.patch
Patch1106:	linux-scsi-debug-bug.patch

# This patch allows to create more than one sound device using alsa
# and devfs with two or more sound cards
Patch1111:	linux-sound_core.patch

# rivafb - fix for text background in 16bpp modes
Patch1150:	linux-rivafb16.patch
Patch1152:	linux-2.4.20-agp_uninorth.patch

Patch1201:	linux-2.4.21-cpqfc.patch
Patch1203:	linux-2.4.20-amd-golem.patch
Patch1205:	linux-53c7,8xx-build.fix
Patch1207:	linux-2.4.20-serverworks.patch
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
Patch1304:	linux-2.4.21-tru64nfs.patch
Patch1305:	linux-2.4.21-nfs-silly-rename.patch

Patch1350:	linux-2.4.21-nousb.patch
# from http://www.noc.uoa.gr/~avel/page.php?page=nokia&lang=en
Patch1354:	linux-2.4.20-Nokia5510.patch

# raid5 xor fix for PIII/P4, should go away shortly
Patch1400:	linux-2.4.0-raid5xor.patch
Patch1401:	linux-2.4.0-nonintconfig.patch
# Add an ioctl to the block layer so we can be EFI compliant
Patch1402:	linux-2.4.2-blkioctl-sector.patch
Patch1403:	linux-2.4.3-pcipenalty.patch
Patch1405:	linux-2.4.7-suspend.patch
Patch1407:	kernel-Makefile-include-fix.patch
Patch1408:	kernel-pswscancode.patch
Patch1410:	linux-2.4.18-input-35215.patch
Patch1411:	linux-2.4.18-kiobuf.patch
Patch1413:	linux-2.4.22-andrea-9980_fix-pausing-6.patch
Patch1414:	linux-2.4.21-oopsmeharder.patch
Patch1415:	linux-mtd-missing-include-fix-2.4.7-pre6.patch
Patch1416:	linux-2.4.21-no-FPU.patch
Patch1418:	linux-2.4.21-hpt372-chicken-egg-hack.patch
Patch1419:	linux-2.4.21-agp-num_of_masks.patch
# fix spare disk counting for raid 5
Patch1420:	linux-raid5-spare-counting.patch
Patch1421:	linux-2.4.21-bttv-typo.patch

Patch2000:	linux-PPC-SMP.patch
Patch2001:	linux-2.4-ppc-procesor.patch
Patch2002:	kernel-2.4.18-SPARC64-PLD.patch
Patch2003:	linux-2.4.20-AXP-avma1_cs.patch
Patch2004:	linux-2.4.22-ppc-amd8111e.patch

Patch3000:	linux-2.4.1-compilefailure.patch
Patch3002:	linux-2.4.20-EXPORT_SYMBOL.patch
Patch3003:	linux-2.4.20-missing-license-tags.patch
Patch3004:	linux-2.4.20-sym53c8xx_old.patch
Patch3008:	linux-drm-4.2.0-force-cmpxchg.patch
Patch3010:	linux-2.4.21-ipsec-sparc64.patch
Patch3011:	linux-2.4.22-gcc33-inline.patch
Patch3012:	linux-2.4.22-gcc-ext3.patch
Patch3013:	linux-2.4.23-ppc-symbols.patch

# Security patches/fixes

# modified http://www.hardrock.org/kernel/current-updates/linux-2.4.23-updates.patch
# since we already have some of these fixes applied
#Patch3500:	http://www.hardrock.org/kernel/current-updates/linux-2.4.24-updates.patch
Patch3600:	linux-2.4-sysctl-empty.patch
Patch4000:	grsecurity-2.0-rc4-2.4.25-O1.patch

ExclusiveOS:	Linux
URL:		http://www.kernel.org/
%ifarch		%{ix86}
BuildRequires:	bin86
%endif
#BuildRequires:	%{kgcc_package}
BuildRequires:	modutils
BuildRequires:	ed
PreReq:		modutils
PreReq:		geninitrd >= 1354
Requires(post,postun):	fileutils
Requires(postun):	awk
Provides:	%{name}-up = %{version}-%{release}
Provides:	module-info
Provides:	i2c = %{i2c_version}
Provides:	bttv = 0.7.83
Provides:	%{name}(netfilter) = 1.2.9-%{netfilter_snap}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
#Provides:	%{name}(cdrw)
#Provides:	%{name}(cdmrw)
AutoReqProv:	no
Obsoletes:	kernel-modules
Conflicts:	iptables < 1.2.9
Conflicts:	lvm < 1.0.4
Conflicts:	xfsprogs < 2.1.0
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	e2fsprogs < 1.25
Conflicts:	jfsutils < 1.0.12
Conflicts:	util-linux < 2.10o
Conflicts:	modutils < 2.4.2
Conflicts:	quota < 3.06
Conflicts:	linux-atm < 2.4.1
Conflicts:	device-mapper < 1.00.05
ExclusiveArch:	%{ix86} sparc sparc64 alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enth�lt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist f�r grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Proze�-Management, Ger�te Ein- und Ausgaben, usw.

%description -l es
Este paquete contiene n�cleo (kernel) Linux que se usa para arranque y
funcionamiento de tu sistema. Contiene soporte a pocos hardwares
espec�ficos. La mayor�a de los hardwares son soportados, v�a m�dulos
que se cargan despu�s del arranque.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un syst�me d'exploitation Linux. Le noyau traite les
fonctions basiques d'un syst�me d'exploitation: allocation m�moire,
allocation de process, entr�e/sortie de peripheriques, etc.

%description -l ja
kernel �ѥå������ˤϡ�Red Hat Linux ���ڥ졼�ƥ��󥰥����ƥ�ο�¡��ʬ
�Ȥ������ Linux �����ͥ� (vmlinuz) ���ޤޤ�Ƥ��ޤ���
�����ͥ�ϡ�����������ץ������������ǥХ������������������ڥ졼�ƥ���
�����ƥ�δ���Ū����ʬ��ʤ�ޤ���

%description -l pl
Pakiet zawiera j�dro Linuksa niezb�dne do prawid�owego dzia�ania
Twojego komputera. Zawiera w sobie sterowniki do sprz�tu znajduj�cego
si� w komputerze, takich jak karty muzyczne, sterowniki dysk�w, etc.

%description -l pt_BR
Este pacote cont�m o kernel Linux que � usado para inicializa��o
e funcionamento de seu sistema. Cont�m suporte a poucos hardwares
espec�ficos. A maioria dos hardwares s�o suportados via m�dulos
que s�o carregados ap�s a inicializa��o.

%package smp
Summary:	Kernel version %{version} compiled for SMP machines
Summary(de):	Kernel version %{version} f�r Multiprozessor-Maschinen
Summary(es):	N�cleo (kernel) compilado para m�quinas SMP
Summary(fr):	Kernel version %{version} compiler pour les machine Multi-Processeur
Summary(ja):	SMP (�оΥޥ���ץ����å���) �б� Linux �����ͥ�
Summary(pl):	J�dro Linuksa %{version} skompilowane dla maszyn wieloprocesorowych
Summary(pt_BR):	Kernel compilado para m�quinas SMP
Group:		Base/Kernel
PreReq:		modutils
PreReq:		geninitrd >= 2.21
Requires(post,postun):	fileutils
Requires(postun):	awk
Provides:	%{name}-smp = %{version}-%{release}
Provides:	module-info
Provides:	i2c = %{i2c_version}
Provides:	bttv = 0.7.83
Provides:	%{name}(netfilter) = 1.2.9-%{netfilter_snap}
Provides:	%{name}(reiserfs) = %{version}
Provides:	%{name}(agpgart) = %{version}
#Provides:	%{name}(cdrw)
#Provides:	%{name}(cdmrw)
AutoReqProv:	no
Conflicts:	iptables < 1.2.9
Conflicts:	lvm < 1.0.4
Conflicts:	xfsprogs < 2.1.0
Conflicts:	reiserfsprogs < 3.6.3
Conflicts:	e2fsprogs < 1.25
Conflicts:	jfsutils < 1.0.12
Conflicts:	util-linux < 2.10o
Conflicts:	modutils < 2.4.2
Conflicts:	quota < 3.06
Conflicts:	linux-atm < 2.4.1
Conflicts:	device-mapper < 1.00.05

%description smp
This package includes a SMP version of the Linux %{version} kernel. It
is required only on machines with two or more CPUs, although it should
work fine on single-CPU boxes.

%description smp -l de
Dieses Paket enth�lt eine SMP (Multiprozessor)-Version von
Linux-Kernel %{version}. Es wird f�r Maschinen mit zwei oder mehr
Prozessoren gebraucht, sollte aber auch auf Computern mit nur einer
CPU laufen.

%description smp -l es
N�cleo (kernel) compilado para m�quinas SMP

%description smp -l fr
Ce package inclu une version SMP du noyau de Linux version %{version}.
Il et n�cessaire seulement pour les machine avec deux processeurs ou
plus, il peut quand m�me fonctionner pour les syst�me mono-processeur.

%description smp -l ja
���Υѥå������ˤ� SMP �Ǥ� Linux �����ͥ뤬������Ƥ��ޤ���
���Υ����ͥ�� 2�İʾ�� CPU ����ܤ����ޥ���ˤΤ�ɬ�פȤʤ�ޤ�����
1CPU �Υޥ���Ǥ�����ʤ�ư��ޤ���

���ʤ��Υޥ��� 2�İʾ�� CPU ����ܤ��Ƥ������
kernel-smp �ѥå������򥤥󥹥ȡ��뤷�Ƥ���������

%description smp -l pl
Pakiet zawiera j�dro SMP Linuksa w wersji %{version}. Jest ono
wymagane przez komputery zawieraj�ce dwa lub wi�cej procesor�w.
Powinno r�wnie� dobrze dzia�a� na maszynach z jednym procesorem.

%description smp -l pt_BR
Este pacote inclui uma vers�o SMP do kernel Linux vers�o %{version}.
Ele deve ser utilizado apenas em m�quinas com dois ou mais processadores,
apesar de trabalhar perfeitamente em m�quinas com apenas um processador.

%package BOOT
Summary:	Kernel version %{version} used on the installation boot disks
Summary(de):	Kernel version %{version} f�r Installationsdisketten
Summary(es):	N�cleo (kernel) de Linux, utilizado en el disco de instalaci�n
Summary(fr):	Kernel version %{version} utiliser pour les disquettes d'installation
Summary(ja):	���󥹥ȡ��鵯ư�ǥ������ǻȤ��� Linux �����ͥ�
Summary(pl):	J�dro Linuksa %{version} dla bootkietek instalacyjnych
Summary(pt_BR):	Kernel Linux utilizado no disco de instala��o
Group:		Base/Kernel
PreReq:		modutils
Requires(post,postun):	fileutils
Requires(postun):	awk
AutoReqProv:	no

%description BOOT
This package includes a trimmed down version of the Linux %{version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description BOOT -l de
Dieses Paket enth�lt eine verkleinerte Version vom Linux-Kernel
version %{version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l es
N�cleo (kernel) de Linux, utilizado en el disco de instalaci�n

%description BOOT -l ja
���Υѥå������ˤ�;ʬ�ʵ�ǽ������ƥ������򾮤�������
Linux �����ͥ뤬������Ƥ��ޤ������Υ����ͥ�ϥ��󥹥ȡ���
��ư�ǥ������˻Ȥ����Τǡ����˥��󥹥ȡ��뤬���ä������ƥ���
�Ȥ��٤Τ�ΤǤ���ޤ��󡥥������򾮤�������٤�¿���ε�ǽ��
����Ƥ��뤫��Ǥ���

%description BOOT -l pl
Pakiet zawiera j�dro Linuksa dedykowane dyskietkom startowym i powinno
by� u�ywane jedynie podczas instalacji systemu. Wiele u�ytecznych
opcji zosta�o wy��czonych, aby jak najbardziej zmniejszy� jego
rozmiar.

%description BOOT -l pt_BR
Este pacote inclui uma vers�o minimizada do kernel Linux, criada para
ser utilizada *apenas* no disco de instala��o, e n�o deve ser utilizada
em m�quinas j� instaladas, pois v�rias caracter�sticas do kernel
s�o desabilitadas para diminuir o tamanho final do kernel a ser utilizado.

%package pcmcia
Summary:	PCMCIA modules
Summary(pl):	Modu�y PCMCIA
Group:		Base/Kernel
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}
Provides:	kernel(pcmcia)

%description pcmcia
Kernel PCMCIA modules.

%description pcmcia -l pl
Modu�y PCMCIA z kernela.

%package smp-pcmcia
Summary:	PCMCIA modules for SMP kernel
Summary(pl):	Modu�y PCMCIA dla maszyn SMP
Group:		Base/Kernel
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}
Provides:	kernel(pcmcia)

%description smp-pcmcia
Kernel PCMCIA modules for SMP kernel.

%description smp-pcmcia -l pl
Modu�y PCMCIA z kernela dla maszyn SMP.

%package drm
Summary:	DRM kernel modules
Summary(pl):	Sterowniki DRM
Group:		Base/Kernel
PreReq:		%{name}-up = %{version}-%{release}
Requires(postun):	%{name}-up = %{version}-%{release}
Provides:	%{name}-drm = %{drm_xfree_version}

%description drm
DRM kernel modules (%{drm_xfree_version}).

%description drm -l pl
Sterowniki DRM (%{drm_xfree_version}).

%package smp-drm
Summary:	DRM SMP kernel modules
Summary(pl):	Sterowniki DRM dla maszyn wieloprocesorowych
Group:		Base/Kernel
PreReq:		%{name}-smp = %{version}-%{release}
Requires(postun):	%{name}-smp = %{version}-%{release}
Provides:	%{name}-drm = %{drm_xfree_version}

%description smp-drm
DRM SMP kernel modules (%{drm_xfree_version}).

%description smp-drm -l pl
Sterowniki DRM dla maszyn wieloprocesorowych (%{drm_xfree_version}).

%package headers
Summary:	Header files for the Linux kernel
Summary(es):	Archivos de inclusi�n para n�cleo (kernel) Linux.
Summary(ja):	Linux �����ͥ�Υإå��ե�����
Summary(pl):	Pliki nag��wkowe j�dra
Summary(pt_BR):	Arquivos de inclus�o para o kernel Linux.
Group:		Base/Kernel
Requires(post,postun):	fileutils
Requires(postun):	awk
Provides:	%{name}-headers(agpgart) = %{version}
Provides:	%{name}-headers(reiserfs) = %{version}
Provides:	%{name}-headers(bridging) = %{version}
Provides:	kernel-i2c-devel = %{i2c_version}
Provides:	%{name}-headers(netfilter) = 1.2.9-%{netfilter_snap}
Obsoletes:	kernel-i2c-devel
AutoReqProv:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l es
Estos son los archivos de inclusi�n C para n�cleo (kernel) Linux, que define
estructuras y constantes que son necesarias a la construcci�n de la
mayor�a de los programas en el Linux, como tambi�n para reconstruir
el n�cleo (kernel).

%description headers -l ja
kernel-headers �ѥå������ˤ� Linux �����ͥ�� C �إå��ե����뤬
������Ƥ��ޤ����إå��ե�����ˤϡ�¿���Υץ������򥳥�ѥ���
����ݡ������ϥ����ͥ��ƹ��ۤ���Τ�ɬ�פʹ�¤�������������Ƥ��ޤ���

%description headers -l pl
Pakiet zawiera pliki nag��wkowe j�dra, niezb�dne do rekompilacji j�dra
oraz niekt�rych program�w.

%description headers -l pt_BR
Estes s�o os arquivos de inclus�o C para o kernel Linux, os
quais definem estruturas e constantes que s�o necess�rias para
a constru��o da maioria dos programas no Linux, bem como para
reconstruir o pr�prio kernel.

%package source
Summary:	Kernel source tree
Summary(es):	Fuentes del n�cleo (kernel) Linux
Summary(ja):	Linux �����ͥ�Υ�����������
Summary(pl):	Kod �r�d�owy j�dra Linuksa
Summary(pt_BR):	Fontes do kernel Linux
Group:		Base/Kernel
Requires:	%{name}-headers = %{version}-%{release}
%ifarch %{ix86}
Requires:	bin86
%endif
AutoReqProv:	no

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l de
Das Kernel-Source-Paket enth�lt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zur�ckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien k�nnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l es
Este es el fuente para el n�cleo (kernel) Linux. Se necesita para la
construcci�n de la mayor�a de los programas C, pues dependen de
constantes definidas en �l. Tu puedes tambi�n construir un n�cleo (kernel)
personalizado que ser� lo mejor configurado para tu hardware en
particular.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont n�cessaires pour compiler la plupart des
programmes C, car il d�pend de constantes d�finies dans le code
source. Les sources peuvent �tre aussi utilis�e pour compiler un noyau
personnalis� pour avoir de meilleures performances sur des mat�riels
particuliers.

%description source -l ja
kernel-source �ѥå������ˤ� Linux �����ͥ�Υ����������ɤ��ޤޤ��
���ޤ��������ͥ�Υ����������ɤ�¿���� C �ץ������κ�����ɬ�פǤ���
�����ͥ�Υ����������ɤ��������Ƥ������¤˰�¸���뤳�Ȥ����뤫��Ǥ���
���Υ����������ɤ�Ȥäơ����ʤ��Υ����ƥ�����˥��塼�󥢥åפ���
�������५���ͥ��������뤳�Ȥ�Ǥ��ޤ���

%description source -l pl
Pakiet zawiera kod �r�d�owy j�dra systemu.

%description source -l pt_BR
Este � o fonte para o kernel Linux. � necess�rio para a
constru��o da maioria dos programas C, pois eles dependem de
constantes definidas nele. Voc� tamb�m pode construir um kernel
personalizado que ser� melhor configurado para seu hardware particular.

%package doc
Summary:	Kernel documentation
Summary(es):	Documentaci�n para los archivos fuente del n�cleo (kernel) de Linux
Summary(ja):	�����ͥ륽�����˴ޤޤ���͡��ʥɥ������
Summary(pl):	Dokumentacja do j�dra Linuksa
Summary(pt_BR):	Documenta��o para os arquivos fontes do kernel Linux
Group:		Base/Kernel
Provides:	%{name}-doc = %{version}
AutoReqProv:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l es
Documentaci�n para los archivos fuente del n�cleo (kernel) de Linux

%description doc -l ja
���Υѥå������ˤϥ����ͥ륽�����˴ޤޤ�Ƥ���ɥ�����Ȥ�
������Ƥ��ޤ���Linux �����ͥ��ǥХ����ɥ饤�Ф˴ؤ����͡���
���󤬤��Υɥ�����Ȥˤϵ�����Ƥ��ޤ���

Linux �����ͥ�⥸�塼����ɤ߹���ݤΰ�����Ĵ�٤����������
���Υѥå������򥤥󥹥ȡ��뤹����ɤ��Ǥ��礦��

%description doc -l pl
Pakiet zawiera dokumentacj� j�dra z katalogu
/usr/src/linux/Documentation.

%description doc -l pt_BR
Este pacote cont�m documenta��o para o kernel Linux.

%prep
%setup -q -a3 -n linux-2.4.24
# new JFS
rm -fr fs/jfs
gzip -dc %{SOURCE7} | tar -xf -
%patch0 -p1
%patch1 -p1
%patch10 -p1
%patch12 -p1
%patch15 -p1
%patch20 -p1
%patch21 -p1
# drop it?
#%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch32 -p1
# XXX: TODO - update patch?
#%patch31 -p1
%patch40 -p1
%patch50 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch70 -p1
%patch80 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch110 -p1
%patch120 -p1
%patch125 -p1
%patch130 -p1
# ???
#%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch200 -p1
%patch205 -p1
%patch210 -p1
# mtrainer, problematic with some LG cdroms
#%patch215 -p1
#%patch216 -p1
%patch225 -p1
%patch226 -p1
%patch227 -p1
%patch235 -p1
%patch240 -p1
%patch255 -p1
%patch256 -p1
%patch257 -p1
%patch265 -p1
%patch275 -p1
%patch301 -p1
%patch302 -p1
%patch303 -p1
%patch350 -p1
%patch400 -p1
%patch950 -p1
%patch1000 -p1
%patch1002 -p1
%patch1003 -p1
%patch1006 -p1
%patch1007 -p1
# broken on SMP machines!
#%patch1008 -p1
%patch1009 -p1
%patch1010 -p1
%patch1102 -p1
%patch1104 -p0
%patch1105 -p1
%patch1106 -p0
%patch1111 -p1
%patch1150 -p1
%patch1152 -p1
%patch1201 -p1
%patch1203 -p1
%patch1205 -p1
%patch1207 -p1
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
%patch1350 -p1
%patch1354 -p1
%patch1400 -p1
%patch1401 -p1
%patch1402 -p1
%patch1403 -p1
%patch1405 -p1
%patch1407 -p1
%patch1408 -p1
%patch1410 -p1
%patch1411 -p1
%patch1413 -p1
%patch1414 -p1
%patch1415 -p0
%patch1416 -p1
%patch1418 -p1
%patch1419 -p1
%patch1420 -p1
%patch1421 -p1

%patch2000 -p0
%patch2001 -p1
%patch2002 -p1
%patch2003 -p1
%ifarch ppc
%patch2004 -p1
%endif

%patch3000 -p1
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1
cd drivers/char/drm
%patch3008 -p1
cd ../../..

%ifarch sparc64
%patch3010 -p1
%endif

%patch3011 -p1
#???
#%patch3012 -p1
%patch3013 -p1

# left for future updates
#%patch3500 -p1
%patch3600 -p1
%{?with_grsec:%patch4000 -p1}

mv -f drivers/scsi/sym53c8xx.c drivers/scsi/sym53c8xx_old.c

# Tekram DC395/315 U/UW SCSI host driver
echo Adding Tekram DC395/315 driver
patch -p1 -s < dc395/dc395-integ24.diff
install dc395/dc395x_trm.? dc395/README.dc395x drivers/scsi/
%patch270 -p1

%patch450 -p1

# The following go last as they touch a lot of code
# and/or are on bcond and/or are ifarch

%ifarch %{ix86}
%if %{with win4lin}
echo Win4Lin patch ...
%patch900 -p1
%patch901 -p1
%endif
%endif

# Remove -g from drivers/atm/Makefile and net/ipsec/Makefile
echo -e ',s/EXTRA_CFLAGS.*-g//g\n,w' | ed net/ipsec/Makefile

# Fix EXTRAVERSION and CC in main Makefile
echo -e ',s/EXTRAVERSION =.*/EXTRAVERSION =/g\n,w' | ed Makefile
%ifarch sparc64
echo -e ',s/CC.*$(CROSS_COMPILE)gcc/CC		= sparc64-linux-gcc/g\n,w' | ed Makefile
%endif

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
	cat %{SOURCE1000} >> arch/%{base_arch}/defconfig
	cat %{SOURCE1001} >> arch/%{base_arch}/defconfig

%ifarch sparc64
	echo -e ',s/^CONFIG_FB_I810=.*/# CONFIG_FB_I810 is not set/g\n,w' | \
		ed arch/%{base_arch}/defconfig
	echo -e ',s/CONFIG_IPSEC_AUTH_HMAC_SHA1=y/# CONFIG_IPSEC_AUTH_HMAC_SHA1 is not set/g\n,w' | \
		ed arch/%{base_arch}/defconfig
%endif

	if [ "$BOOT" = "yes" ] ; then
		echo "# CONFIG_GRKERNSEC is not set" >> arch/%{base_arch}/defconfig
	else
		:;
%if %{with grsec}
		echo -e ',s/CONFIG_CRYPTO_SHA256=m/CONFIG_CRYPTO_SHA256=y/g\n,w' | \
			ed arch/%{base_arch}/defconfig
		cat %{SOURCE1002} >> arch/%{base_arch}/defconfig
%endif
	fi
%ifarch %{ix86}
	cat %{SOURCE2000} >> arch/%{base_arch}/defconfig
%endif

%ifarch i386
	echo -e ',s/# CONFIG_MATH_EMULATION is not set/CONFIG_MATH_EMULATION=y/g\n,w' | \
		ed arch/%{base_arch}/defconfig
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
	cd drivers/net/hamradio/soundmodem
	%{__cc} -o gentbl -lm gentbl.c
	./gentbl
	cd ../../../..

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
	echo "CHECKING DEPENDENCIES FOR KERNEL MODULES"
	/sbin/depmod --basedir $KERNEL_INSTALL_DIR -ae -F $KERNEL_INSTALL_DIR/boot/System.map-$KernelVer -r $KernelVer || echo
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-installed
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

# make drivers/scsi/ missing files
#	(cd drivers/scsi; make -f M)

# UP KERNEL
%{?with_up:BuildKernel}

# SMP KERNEL
%{?with_smp:BuildKernel smp}

%if ! %{with up} && ! %{with smp}
# We need include/asm created somewhere
make symlinks
%endif

# BOOT kernel
%ifnarch i586 i686 athlon
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-installed%{_libdir}/bootdisk"
rm -rf $KERNEL_INSTALL_DIR
%{?with_boot:BuildKernel BOOT}
%endif

%install
rm -rf $RPM_BUILD_ROOT
umask 022

install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`

KERNEL_BUILD_INSTALL=no
%{?with_up:KERNEL_BUILD_INSTALL=yes}
%{?with_smp:KERNEL_BUILD_INSTALL=yes}
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

%if %{with source}
cp -a . $RPM_BUILD_ROOT/usr/src/linux-%{version}
%else
cp -a {include,scripts,Makefile,Rules.make,Documentation} $RPM_BUILD_ROOT/usr/src/linux-%{version}
%endif

%ifarch sparc sparc64
sh %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_includedir}/asm/BuildASM
%endif

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

# remove foreign architecture files
cd include
mkdir _asm_keep
mv asm-generic _asm_keep
%ifarch sparc sparc64
	mv asm-sparc* _asm_keep
%else
	mv `resolvesymlink asm 2> /dev/null || readlink asm 2> /dev/null` _asm_keep
%endif
rm -rf asm-*
mv _asm_keep/* .
rmdir _asm_keep
cd ..

%if %{with source}
MYARCH=%{_arch}
%ifarch %{ix86}
MYARCH=i386
%endif
%ifarch sparc sparc64
MYARCH="sparc sparc64"
%endif
cd arch
mv $MYARCH ..
cd ..
rm -rf arch/*
mv $MYARCH arch
%endif

%if %{with source}
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
cat %{SOURCE1000} >> .config
cat %{SOURCE1001} >> .config
%{?with_grsec:cat %{SOURCE1002} >> .config}

%ifarch sparc64
	echo -e ',s/^CONFIG_FB_I810=.*/# CONFIG_FB_I810 is not set/g\n,w' | \
		ed .config
	echo -e ',s/CONFIG_IPSEC_AUTH_HMAC_SHA1=y/# CONFIG_IPSEC_AUTH_HMAC_SHA1 is not set/g\n,w' | \
		ed .config
%endif

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

cat %{SOURCE1000} >> .config
cat %{SOURCE1001} >> .config
%{?with_grsec:cat %{SOURCE1002} >> .config}

%ifarch sparc64
	echo -e ',s/^CONFIG_FB_I810=.*/# CONFIG_FB_I810 is not set/g\n,w' | \
		ed .config
	echo -e ',s/CONFIG_IPSEC_AUTH_HMAC_SHA1=y/# CONFIG_IPSEC_AUTH_HMAC_SHA1 is not set/g\n,w' | \
		ed .config
%endif

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

%if %{with source}
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

%if %{with source}
%{__make} depend
find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" \
	-exec /bin/sh -c "echo -e \",s|$RPM_BUILD_ROOT||g\n,w\" | ed {}" \;

%{__make} clean
rm -f scripts/mkdep
rm -f drivers/net/hamradio/soundmodem/gentbl
%endif

# BOOT
%if %{with boot}
%ifnarch i586 i686 athlon
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk
cp -rdp $KERNEL_BUILD_DIR-installed%{_libdir}/bootdisk/* $RPM_BUILD_ROOT%{_libdir}/bootdisk
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

%post pcmcia
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia
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

%post smp-pcmcia
/sbin/depmod -a -F /boot/System.map-%{version}-%{release}smp %{version}-%{release}smp

%postun smp-pcmcia
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

%if %{with up}
%files
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/ide/legacy/*-cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/mtd/maps/pcmcia*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o*
%ifnarch ppc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%endif
%ifnarch sparc
%exclude /lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif
/lib/modules/%{version}-%{release}/build
%ghost /lib/modules/%{version}-%{release}/modules.*

%ifnarch sparc sparc64
%files pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/ide/legacy/*-cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/mtd/maps/pcmcia*
/lib/modules/%{version}-%{release}/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}/kernel/drivers/net/wireless/*_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/parport/*_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/bluetooth/*_cs.o*
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/hisax/*_cs.o*
%ifnarch alpha
/lib/modules/%{version}-%{release}/kernel/drivers/isdn/avmb1/avm_cs.o*
%ifnarch ppc
/lib/modules/%{version}-%{release}/kernel/drivers/telephony/*_pcmcia.o*
%endif
%endif
%endif

%ifnarch sparc
%files drm
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}/kernel/drivers/char/drm
%endif			# %%{with up}
%endif

%if %{with smp}
%files smp
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc
/boot/vmlinux-%{version}-%{release}smp
%endif
/boot/vmlinuz-%{version}-%{release}smp
/boot/System.map-%{version}-%{release}smp
%dir /lib/modules/%{version}-%{release}smp
/lib/modules/%{version}-%{release}smp/kernel
%ifnarch sparc sparc64
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/ide/legacy/*-cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/mtd/maps/pcmcia*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o*
%exclude /lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/*_cs.o*
%endif
%ifnarch ppc sparc sparc64
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

%ifnarch sparc sparc64
%files -n kernel-smp-pcmcia
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}smp/kernel/drivers/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/ide/legacy/*-cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/mtd/maps/pcmcia*
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/scsi/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/char/pcmcia
/lib/modules/%{version}-%{release}smp/kernel/drivers/net/wireless/*_cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/parport/*_cs.o*
/lib/modules/%{version}-%{release}smp/kernel/drivers/bluetooth/dtl1_cs.o*
%ifnarch ppc
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
%endif			# %%{with smp}
%endif

%if %{with boot}
%ifnarch i586 i686 athlon 		# narch
%files BOOT
%defattr(644,root,root,755)
%ifarch alpha sparc sparc64 ppc		# arch
%{_libdir}/bootdisk/boot/vmlinux-%{version}-%{release}BOOT
%endif				#arch
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/build
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*
%endif				# narch
%endif				# %%{with boot}

%files headers
%defattr(644,root,root,755)
%dir %{_prefix}/src/linux-%{version}
%{_prefix}/src/linux-%{version}/include

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/Documentation
%endif

%if %{with source}
%files source
%defattr(644,root,root,755)
%{_prefix}/src/linux-%{version}/arch
%{_prefix}/src/linux-%{version}/crypto
%{_prefix}/src/linux-%{version}/drivers
%{_prefix}/src/linux-%{version}/fs
%{_prefix}/src/linux-%{version}/init
%{?with_grsec:%{_prefix}/src/linux-%{version}/grsecurity}
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
