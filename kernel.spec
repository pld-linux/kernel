%define		ow_version		2.4.23-ow1

Summary:	The Linux kernel (the core of the Linux operating system)
Summary(de):	Der Linux-Kernel (Kern des Linux-Betriebssystems)
Summary(fr):	Le Kernel-Linux (La partie centrale du systeme)
Summary(pl):	J╠dro Linuksa
Summary(ru):	Ядро Linux
Summary(uk):	Ядро Linux
Name:		kernel
Version:	2.4.23
Release:	0.1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/v2.4/linux-%{version}.tar.bz2
# Source0-md5:	75dc85149b06ac9432106b8941eb9f7b
Source1:	%{name}-autoconf.h
Source2:        http://www.openwall.com/linux/linux-%{ow_version}.tar.gz
# Source2-md5:	24bfc766280cb46aad1c9ff32a840e3a
Source20:	%{name}-alpha-BOOT.config
Source21:	%{name}-alpha.config
Source22:	%{name}-alpha-smp.config
Source23:	%{name}-athlon.config
Source24:	%{name}-athlon-smp.config
Source25:	%{name}-i386-BOOT.config
Source26:	%{name}-i386.config
Source27:	%{name}-i386-smp.config
Source28:	%{name}-i586.config
Source29:	%{name}-i586-smp.config
Source30:	%{name}-i686.config
Source31:	%{name}-i686-smp.config
Source32:	%{name}-ppc-BOOT.config
Source33:	%{name}-ppc.config
Source34:	%{name}-ppc-smp.config
Source35:	%{name}-sparc64-BOOT.config
Source36:	%{name}-sparc64.config
Source37:	%{name}-sparc64-smp.config
Source38:	%{name}-sparc-BOOT.config
Source39:	%{name}-sparc.config
Source40:	%{name}-sparc-smp.config

Patch1:		00_3.5G-address-space-5
Patch2:		00_VM_IO-4
Patch3:		00_alpha-numa-VALID_PAGE-1
Patch4:		00_athlon-smp-ctx-switch-gdt-1
Patch5:		00_backout-gcc-3_0-patch-1
Patch6:		00_backout-pre9-list_t-removal-1
Patch7:		00_backout-set_cpus_allowed-1
Patch8:		00_bdflush-tuning-1
Patch9:		00_binfmt-elf-checks-4
Patch10:	00_cdrom_root_table-procfs-1
Patch11:	00_clean-inode-fix-1
Patch12:	00_close-root-fd-1
Patch13:	00_coherent-oops-locking-1
Patch14:	00_comx-driver-compile-1
Patch15:	00_cpu-affinity-syscall-rml-5
Patch16:	00_crc-makefile-clean-1
Patch17:	00_csum-trail-1
Patch18:	00_dcache-inline-1
Patch19:	00_dirty-inode-3
Patch20:	00_drop-broken-flock-account-1
Patch21:	00_drop-inetpeer-cache-6.gz
Patch22:	00_e-nodev-1
Patch23:	00_elevator-lowlatency-1
Patch24:	00_ext3-register-filesystem-lifo-2
Patch25:	00_extraversion-33
Patch26:	00_fcntl-dupfd-unsigned-long-cleanups-1
Patch27:	00_fcntl_getfl-largefile-1
Patch28:	00_fix-end_kio_request-race-1
Patch29:	00_flush-inode-reschedule-2
Patch30:	00_free_pages-lru-no_irq-1
Patch31:	00_gcc-30-volatile-xtime-1
Patch32:	00_generic_file_write_nolock-3
Patch33:	00_get_request_wait-race-1
Patch34:	00_global-irq-race-2
Patch35:	00_i8k-compile-1
Patch36:	00_ia64-dma-3
Patch37:	00_intermezzo-tcgets-1
Patch38:	00_invlpg-386-1
Patch39:	00_ip_conntrack-ack-seq-1
Patch40:	00_irda-compile-1
Patch41:	00_isofs-options-elseif-1
Patch42:	00_jfs-locking-fix-1
Patch43:	00_ksoftirqd-max-loop-networking-2
Patch44:	00_ll_rw_block-sync-race-1
Patch45:	00_log-buf-len-dynamic-1
Patch46:	00_loop-IV-API-hvr-1
Patch47:	00_mark-inode-dirty-smp-race-1
Patch48:	00_max-mp-busses-1
Patch49:	00_max-threads-pid-nr-1
Patch50:	00_max_bytes-6
Patch51:	00_module-gfp-7
Patch52:	00_module-locking-fix-3
Patch53:	00_nanosleep-6
Patch54:	00_negative-dentry-waste-ram-1
Patch55:	00_netconsole-2.4.10-C2-4.gz
Patch56:	00_netconsole-3c59x-1
Patch57:	00_nfs-dcache-parent-optimize-1
Patch58:	00_nfs_mtime-change-if-invalid-1
Patch59:	00_nfs_writeback-2
Patch60:	00_nfsd-reply-cache-smp-1
Patch61:	00_o_direct-blkdev-2
Patch62:	00_one_highpage_init-cleanup-1
Patch63:	00_ordered-freeing-2
Patch64:	00_osync-lock-1
Patch65:	00_panic-export-2
Patch66:	00_parport-multi-io-pci-1
Patch67:	00_parport_pc-compile-1
Patch68:	00_partition-pagemap-include-1
Patch69:	00_poll-nfds-3
Patch70:	00_poll-smp-races-1
Patch71:	00_posix-lock-overflow-1
Patch72:	00_rbtree-cleanups-1
Patch73:	00_readahead-got-broken-somewhere-3
Patch74:	00_readahead-last-page-1
Patch75:	00_relax-timer-sync-1
Patch76:	00_rwsem-fair-39
Patch77:	00_rwsem-fair-39-recursive-8
Patch78:	00_sched-O1-aa-2.4.19rc3-18.gz
Patch79:	00_scsi-scan-new-devices-2
Patch80:	00_sctp-compile-1
Patch81:	00_semop-timeout-3
Patch82:	00_setfl-race-fix-3
Patch83:	00_shm_destroy-deadlock-2
Patch84:	00_silent-stack-overflow-20
Patch85:	00_sis-fpu-bugs-1
Patch86:	00_skb-frag-1
Patch87:	00_small-vma-1
Patch88:	00_smp-timers-not-deadlocking-6
Patch89:	00_spinlock-no-egcs-3
Patch90:	00_sync-buffer-scale-1
Patch91:	00_tcp-spurious-dupack-winup-streamers-1
Patch92:	00_tcp-syn-rst-fin-1
Patch93:	00_thinkpad-2.gz
Patch94:	00_umount-against-unused-dirty-inodes-race-2
Patch95:	00_vm-cleanups-3
Patch96:	00_vm_raend-race-1
Patch97:	00_vma-file-merge-3
Patch98:	00_vmalloc-cache-flush-1
Patch99:	00_watchdog-1
Patch100:	00_writeoute_one_page-b_flushtime-1
Patch101:	00_x86-optimize-apic-irq-and-cacheline-3
Patch102:	00_x86-sa_interrupt-1
Patch103:	01_softirq-nowait-1
Patch104:	05_vm_00_anon-lru-race-better-fix-1
Patch105:	05_vm_02-execve-mm-fast-path-safe-1
Patch106:	05_vm_08_try_to_free_pages_nozone-4
Patch107:	05_vm_10_read_write_tweaks-3
Patch108:	05_vm_13_activate_page_cleanup-1
Patch109:	05_vm_15_active_page_swapout-1
Patch110:	05_vm_18_buffer-page-uptodate-1
Patch111:	05_vm_21_rt-alloc-1
Patch112:	05_vm_22_vm-anon-lru-3
Patch113:	05_vm_23_per-cpu-pages-4
Patch114:	05_vm_25_try_to_free_buffers-invariant-1
Patch115:	05_vm_26-rest-2
Patch116:	05_vm_27-pte-dirty-bit-in-hardware-1
Patch117:	07_cpqarray-sard-1
Patch118:	07_cpqfc-compile-1
Patch119:	07_qlogicfc-5.gz
Patch120:	08_qlogicfc-template-aa-6
Patch121:	09_qlogic-link-3
Patch122:	10_ext3-o_direct-3
Patch123:	10_get_pid-no-deadlock-and-boosted-4
Patch124:	10_inode-highmem-3
Patch125:	10_lvm-snapshot-check-4
Patch126:	10_o_direct-open-check-4
Patch127:	10_rawio-vary-io-21
Patch128:	10_sched-o1-bluetooth-2
Patch129:	10_sched-o1-hyperthreading-4
Patch130:	10_x86-fast-pte-2
Patch131:	20_highmem-debug-11
Patch132:	20_keventd-rt-1
Patch133:	20_numa-mm-7
Patch134:	20_pte-highmem-32.gz
Patch135:	20_rcu-poll-10
Patch136:	20_reduce-module-races-1
Patch137:	20_sched-o1-fixes-10
Patch138:	21_o1-A4-aa-1
Patch139:	21_ppc64-aa-3
Patch140:	21_pte-highmem-24-sparc64
Patch141:	21_pte-highmem-mremap-smp-scale-1
Patch142:	21_sched-o1-yield-rt-1
Patch143:	22_sched-deadlock-mmdrop-1
Patch144:	30_00_posix-race-1
Patch145:	30_02_fix-commit-1
Patch146:	30_03_fix-osx-1
Patch147:	30_04_soft2-1
Patch148:	30_05_seekdir-2
Patch149:	30_06_cto2-1
Patch150:	30_07_access-1
Patch151:	30_08_rdplus-2
Patch152:	30_09_fix-unlink-1
Patch153:	30_10-sock-disconnect-1
Patch154:	30_105_seekdir-fix-1
Patch155:	30_12-lockd3-2
Patch156:	30_14-pathconf-3
Patch157:	30_16_rpciod-lock-1
Patch158:	30_17-mmap-fix-1
Patch159:	30_19-nfs-kill-unlock-1
Patch160:	30_irq-balance-16
Patch161:	30_p3-p4-optimize-2
Patch162:	50_uml-patch-2.4.20-5-3.bz2
Patch164:	51_uml-aa-14
Patch165:	51_uml-o1-5
Patch166:	52_alloc_pages-1
Patch167:	52_uml-sys-read-write-5
Patch168:	53_uml-cache-shift-1
Patch169:	54_uml-sa_interrupt-1
Patch170:	55_uml-highmem-1
Patch171:	56_uml-pte-highmem-7
Patch172:	57_uml-kernel-thread-1
Patch173:	60_atomic-alloc-8
Patch174:	60_atomic-lookup-6
Patch175:	60_net-exports-4
Patch176:	60_pagecache-atomic-8
Patch177:	60_tux-2.4.18-final-A3.gz
Patch178:	60_tux-config-stuff-2
Patch179:	60_tux-create_child-1
Patch180:	60_tux-data-1
Patch181:	60_tux-dprintk-3
Patch182:	60_tux-exports-8
Patch183:	60_tux-kstat-5
Patch184:	60_tux-o1-1
Patch185:	60_tux-process-1
Patch186:	60_tux-syscall-6
Patch187:	60_tux-sysctl-4
Patch188:	60_tux-vfs-5
Patch189:	61_tux-alpha-compile-1
Patch190:	61_tux-exports-gcc-3_1-compile-2
Patch191:	62_tux-dump-stack-1
Patch192:	62_tux-generic-file-read-2
Patch193:	62_tux-invalidate_inode_pages2-1
Patch194:	62_tux-uml-2
Patch195:	63_tux-notuxnostat-1
Patch196:	64_tux-reduce-1
Patch197:	70_PF_FSTRANS-1
Patch198:	70_delalloc-3
Patch199:	70_dmapi-stuff-2
Patch200:	70_iget-2
Patch201:	70_intermezzo-junk-2
Patch202:	70_qsort-1
Patch203:	70_xfs-1.3-3.gz
Patch204:	70_xfs-config-stuff-4
Patch205:	70_xfs-exports-3
Patch206:	70_xfs13pre-final-1.gz
Patch207:	71_posix_acl-3
Patch208:	71_xfs-aa-5
Patch209:	71_xfs-fixup-1
Patch210:	71_xfs-infrastructure-1
Patch211:	71_xfs-mmap-1
Patch212:	71_xfs-qsort-1
Patch213:	72_22pre7-broke-the-vmap-api-1
Patch214:	90_buddyinfo-4
Patch215:	90_module-oops-tracking-3
Patch216:	90_proc-mapped-base-6
Patch217:	90_s390-aa-4
Patch218:	90_s390x-aa-3
Patch219:	91_zone_start_pfn-8
Patch220:	92_core-dump-seek-unmapped-1
Patch221:	93_NUMAQ-16
Patch222:	94_discontigmem-meminfo-6
Patch223:	96_inode_read_write-atomic-9
Patch224:	97_i_size-corruption-fixes-5
Patch225:	98_prepare-write-fixes-3-1
Patch226:	9900_aio-25.bz2
Patch228:	9901_aio-blkdev-1
Patch229:	9903_aio-22-ppc-2
Patch230:	9910_shm-largepage-18.bz2
Patch232:	9920_kgdb-13.bz2
Patch234:	9925_kmsgdump-0.4.4-5.bz2
Patch236:	9930_io_request_scale-6
Patch237:	9931_io_request_scale-drivers-3
Patch238:	9940_ocfs-3.gz
Patch239:	9941_ocfs-direct-1
Patch240:	9941_ocfs-warnings-1
Patch241:	9942_ocfs-o_direct-API-1
Patch242:	9950_futex-6.gz
Patch243:	9980_fix-pausing-7
Patch244:	9985_blk-atomic-13
Patch245:	9990_hack-drop-x86-fast-pte-2
Patch246:	9995_frlock-gettimeofday-7
Patch247:	9996_kiobuf-slab-2
Patch248:	9997_rawio-readv-writev-1
Patch249:	9998_lowlatency-fixes-13
Patch250:	9998_lowlatency-reiserfs-1
Patch251:	9999900_BH_Sync-remove-1
Patch252:	9999900_aio-rawio-varyio-2
Patch253:	9999900_blkdev-inode-times-pagecache-1
Patch254:	9999900_distributed-shared-memory-hook-1
Patch255:	9999900_ecc-20030225-2.gz
Patch256:	9999900_epoll-common-2
Patch257:	9999900_ikd-4.gz
Patch258:	9999900_ipc-rcu-2
Patch259:	9999900_monitor-mwait-2
Patch260:	9999900_q-full-2
Patch261:	9999900_rcu-helpers-1
Patch262:	9999900_scsi-error-handler-new-1
Patch263:	9999900_soft-float-1
Patch264:	9999900_x86-movsl-copy-user-1
Patch265:	9999901_aio-poll-2
Patch266:	9999901_scsi-softirq-3
Patch267:	9999_00_x86_64-suse-1
Patch268:	9999_00_x86_64-sys-1
Patch269:	9999_00_x86_64-tsc-c0-bandaid-1
Patch270:	9999_00_x86_64-warning-1
Patch271:	9999_00_x86_64-zone-startpfn-1
Patch272:	9999_01_x86_64-aio-bigpages-1
Patch273:	9999_01_x86_64-aio-export-1
Patch274:	9999_01_x86_64-bitops-1
Patch275:	9999_01_x86_64-discontig-pmd-1
Patch276:	9999_01_x86_64-epoll-1
Patch277:	9999_01_x86_64-kgdb-1
Patch278:	9999_01_x86_64-lvm32-no-checks-1
Patch279:	9999_athlon-errata-prefetch-1
Patch280:	9999_dm-3.gz
Patch281:	9999_gcc-3.3-7
Patch282:	9999_ia64-__clear_bit-1
Patch283:	9999_mmap-cache-3
Patch284:	9999_sched_yield_scale-9
Patch285:	9999_truncate-nopage-race-3
Patch286:	9999_zz-dynamic-timeslice-1
Patch287:	9999_zzz-dynamic-hz-4.bz2
Patch288:	9999_zzzz-stackoverflow-1

Patch300:	%{name}-pldfblogo.patch
Patch301:	linux-2.4.22-owl_remove_extraversion.patch


# bugfixes, found in core
#Patch10:
#Patch11:

# network stuff, such as patch-o-matic, vtun, and others protocols
# with compilation fixes
#
Source100:	http://www.netfilter.org/files/patch-o-matic-20030912.tar.bz2
# Source100-md5:	e6a7c5b00252d9ced0a6b9ab03b032d3

#Patch1:		ftp://ftp.kernel.org/pub/linux/kernel/people/alan/linux-2.4/2.4.21/patch-2.4.21-rc6-ac1.bz2
ExclusiveOS:	Linux
Autoreqprov:	no
URL:		http://www.kernel.org/
BuildRequires:	byacc
%ifarch sparc
BuildRequires:	sparc32
%endif
Provides:	%{name}-up = %{version}-%{release}
Autoreqprov:	no
PreReq:		modutils
PreReq:		fileutils
PreReq:		geninitrd
#Prereq:	rc-boot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kernel-modules

%define		no_install_post_strip                   yes
%define		no_install_post_compress_modules        yes
%ifarch i386 sparc sparcv9 sparcv9 alpha
%define		_with_boot				1
%endif

%description
This package contains the Linux kernel that is used to boot and run
your system. It contains few device drivers for specific hardware.
Most hardware is instead supported by modules loaded after booting.

%description -l de
Das Kernel-Paket enthДlt den Linux-Kernel (vmlinuz), den Kern des
Linux-Betriebssystems. Der Kernel ist fЭr grundliegende
Systemfunktionen verantwortlich: Speicherreservierung,
Prozeъ-Management, GerДte Ein- und Ausgaben, usw.

%description -l fr
Le package kernel contient le kernel linux (vmlinuz), la partie
centrale d'un systХme d'exploitation Linux. Le noyau traite les
fonctions basiques d'un systХme d'exploitation: allocation mИmoire,
allocation de process, entrИe/sortie de peripheriques, etc.

%description -l pl
Pakiet zawiera j╠dro Linuksa niezbЙdne do prawidЁowego dziaЁania
Twojego komputera.

%description -l ru
Этот пакет содержит ядро Linux, которое необходимо для того, чтобы
система загрузилась и работала. Набор драйверов устройств, включенных
в ядро, ограничен до минимума. Большинство устройств поддерживаются
при помощи модулей, загружаемых после загрузки ядра.

Также этот пакет содержит модули, обеспечивающие поддержку всех
устройств, поддерживаемых в Linux на сегодняшний день.

%description -l uk
Цей пакет м╕стить ядро Linux, яке необх╕дне для того, щоб система
загрузилася ╕ працювала. К╕льк╕сть драйвер╕в перифер╕йних пристро╖в,
вбудованих в ядро, обмежена до м╕н╕мума. Б╕льш╕сть пристро╕в
п╕дтримуються за допомогою модул╕в, що загружаються п╕сля загрузки
ядра.

Також цей пакет м╕стить модул╕, що забезпечують п╕дтримку вс╕х
перифер╕йних пристро╕в, як╕ Linux п╕дтриму╓ на сьогодняшн╕й день.

%package BOOT
Summary:	Kernel kernel_version %{kernel_version} used on the installation boot disks
Summary(de):	Kernel kernel_version %{kernel_version} fЭr Installationsdisketten
Summary(fr):	Kernel kernel_version %{kernel_version} utiliser pour les disquettes d'installation
Summary(pl):	Kernel %{kernel_version} u©ywany na instalacyjnych dyskach startowych
Group:		Base/Kernel
PreReq:		modutils
PreReq:		fileutils
Autoreqprov:	no

%description BOOT
This package includes a trimmed down kernel_version of the Linux %{kernel_version}
kernel. This kernel is used on the installation boot disks only and
should not be used for an installed system, as many features in this
kernel are turned off because of the size constraints.

%description BOOT -l de
Dieses Paket enthДlt eine verkleinerte kernel_version vom Linux-Kernel
kernel_version %{kernel_version}. Dieser Kernel wird auf den
Installations-Bootdisketten benutzt und sollte nicht auf einem
installierten System verwendet werden, da viele Funktionen wegen der
Platzprobleme abgeschaltet sind.

%description BOOT -l fr
Ce package inclut une kernel_version allИgИe du noyau de Linux kernel_version
%{kernel_version}. Ce kernel et utilisИ pour les disquettes de boot
d'installation et ne doivent pas Йtre utilisИes pour un systХme
classique, beaucoup d'options dans le kernel ont Иtaient dИsactivИes a
cause de la contrainte d'espace.

%description BOOT -l pl
Ten pakiet zawiera okrojon╠ wersjЙ kernela %{kernel_version}. U©ywana jest
wyЁ╠cznie na instalacyjnych dyskach startowych i nie powinna byФ
u©ywana na dziaЁaj╠cym systemie, jako ©e wiele opcji jest wyЁ╠czonych
ze wzglЙdu na wymagania rozmiarowe.

%package headers
Summary:	Header files for the Linux kernel
Summary(pl):	Pliki nagЁСwkowe j╠dra
Group:		Base/Kernel
Autoreqprov:	no

%description headers
These are the C header files for the Linux kernel, which define
structures and constants that are needed when building most standard
programs under Linux, as well as to rebuild the kernel.

%description headers -l pl
Pakiet zawiera pliki nagЁСwkowe j╠dra, niezbedne do rekompilacji j╠dra
oraz niektСrych programСw.

%package doc
Summary:	Kernel documentation
Summary(pl):	Dokumentacja j╠dra
Group:		Base/Kernel
Provides:	%{name}-doc = %{kernel_version}
Autoreqprov:	no

%description doc
This is the documentation for the Linux kernel, as found in
/usr/src/linux/Documentation directory.

%description doc -l pl
Pakiet zawiera dokumentacjЙ j╠dra z katalogu
/usr/src/linux/Documentation.

%package source
Summary:	Kernel source tree
Summary(pl):	Kod ╪rСdЁowy j╠dra Linuksa
Summary(ru):	Исходные тексты ядра Linux
Summary(uk):	Вих╕дн╕ тексти ядра Linux
Group:		Base/Kernel
Autoreqprov:	no
Requires:	%{name}-headers = %{kernel_version}
%ifarch %{ix86}
Requires:	bin86
%endif

%description source
This is the source code for the Linux kernel. It is required to build
most C programs as they depend on constants defined in here. You can
also build a custom kernel that is better tuned to your particular
hardware.

%description source -l de
Das Kernel-Source-Paket enthДlt den source code (C/Assembler-Code) des
Linux-Kernels. Die Source-Dateien werden gebraucht, um viele
C-Programme zu compilieren, da sie auf Konstanten zurЭckgreifen, die
im Kernel-Source definiert sind. Die Source-Dateien kЖnnen auch
benutzt werden, um einen Kernel zu compilieren, der besser auf Ihre
Hardware ausgerichtet ist.

%description source -l fr
Le package pour le kernel-source contient le code source pour le noyau
linux. Ces sources sont nИcessaires pour compiler la plupart des
programmes C, car il dИpend de constantes dИfinies dans le code
source. Les sources peuvent Йtre aussi utilisИe pour compiler un noyau
personnalisИ pour avoir de meilleures performances sur des matИriels
particuliers.

%description source -l pl
Pakiet zawiera kod ╪rСdЁowy jadra systemu. Jest wymagany do budowania
wiЙkszo╤ci programСw C, jako ©e s╠ one zale©ne od staЁych tutaj
zawartych. Mo©esz rСwnie© skompilowaФ wЁasne j╠dro, lepiej dopasowane
do twojego sprzЙtu.

%description source -l ru
Это исходные тексты ядра Linux. Используя их, вы можете построить свое
ядро, которое лучше настроено на ваш набор устройств.

%description source -l uk
Це вих╕дн╕ тексти ядра Linux. Використовуючи ╖х ви можете побудувати
ваше власне ядро, яке краще настро╓но на конф╕гурац╕ю вашо╖ машини.

%package pcmcia-cs
Summary:	PCMCIA-CS modules
Summary(pl):	ModuЁy PCMCIA-CS
Group:		Base/Kernel
Provides:	%{name}-pcmcia-cs = %{pcmcia_kernel_version}
Requires(post):	%{name}-up = %{kernel_version}-%{release}
Requires(postun):	%{name}-up = %{kernel_version}-%{release}

%description pcmcia-cs
PCMCIA-CS modules (%{pcmcia_kernel_version}).

%description pcmcia-cs -l pl
ModuЁy PCMCIA-CS (%{pcmcia_kernel_version}).

%prep
%setup -q -a2 -a100 -n linux-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
# remove extraversion
#%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
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
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
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
%patch162 -p1
#%patch163 -p1
%patch164 -p1
%patch165 -p1
%patch166 -p1
%patch167 -p1
%patch168 -p1
%patch169 -p1
%patch170 -p1
%patch171 -p1
%patch172 -p1
%patch173 -p1
%patch174 -p1
%patch175 -p1
%patch176 -p1
%patch177 -p1
%patch178 -p1
%patch179 -p1
%patch180 -p1
%patch181 -p1
%patch182 -p1
%patch183 -p1
%patch184 -p1
%patch185 -p1
%patch186 -p1
%patch187 -p1
%patch188 -p1
%patch189 -p1
%patch190 -p1
%patch191 -p1
%patch192 -p1
%patch193 -p1
%patch194 -p1
%patch195 -p1
%patch196 -p1
%patch197 -p1
%patch198 -p1
%patch199 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%patch214 -p1
%patch215 -p1
%patch216 -p1
%patch217 -p1
%patch218 -p1
%patch219 -p1
%patch220 -p1
%patch221 -p1
%patch222 -p1
%patch223 -p1
%patch224 -p1
%patch225 -p1
%patch226 -p1
#%patch227 -p1
%patch228 -p1
%patch229 -p1
%patch230 -p1
#%patch231 -p1
%patch232 -p1
#%patch233 -p1
%patch234 -p1
#%patch235 -p1
%patch236 -p1
%patch237 -p1
%patch238 -p1
%patch239 -p1
%patch240 -p1
%patch241 -p1
%patch242 -p1
%patch243 -p1
%patch244 -p1
%patch245 -p1
%patch246 -p1
%patch247 -p1
%patch248 -p1
%patch249 -p1
%patch250 -p1
%patch251 -p1
%patch252 -p1
%patch253 -p1
%patch254 -p1
%patch255 -p1
%patch256 -p1
%patch257 -p1
%patch258 -p1
%patch259 -p1
%patch260 -p1
%patch261 -p1
%patch262 -p1
%patch263 -p1
%patch264 -p1
%patch265 -p1
%patch266 -p1
%patch267 -p1
%patch268 -p1
%patch269 -p1
%patch270 -p1
%patch271 -p1
%patch272 -p1
%patch273 -p1
%patch274 -p1
%patch275 -p1
%patch276 -p1
%patch277 -p1
%patch278 -p1
%patch279 -p1
%patch280 -p1
%patch281 -p1
%patch282 -p1
%patch283 -p1
%patch284 -p1
%patch285 -p1
%patch286 -p1
%patch287 -p1
%patch288 -p1

# 2.4.22 openwall
#patch -p1 -s <linux-%{ow_version}/linux-%{ow_version}.diff

find  -name "*~" -print | xargs rm -f
find  -name "*.orig" -print | xargs rm -f
%ifarch %{ix86}
	perl -p -i -e "s/-m486//" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=486/-m486 -DCPU=486/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=586/-mpentium -DCPU=586/" arch/i386/Makefile
	perl -p -i -e "s/-DCPU=686/-mpentiumpro -DCPU=686/" arch/i386/Makefile
%endif

%build
BuildKernel() {
	%{?verbose:set -x}
	# is this a special kernel we want to build?
	echo BUILDING THE $1 KERNEL...
	if [ -n "$1" ]; then
		Config="%{_target_cpu}-$1"
	else
		Config="%{_target_cpu}"
	fi
	KernelVer=%{version}-%{release}$1

	cp $RPM_SOURCE_DIR/kernel-$Config.config .config

	for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
		sparc32 \
%endif
		%{__make} $target
	done

%ifarch %{ix86}
	%{__make} bzImage EXTRAversion="-%{release}"
%endif
%ifarch sparc
	sparc32 %{__make} boot EXTRAversion="-%{release}"
%endif
%ifarch sparc64 sparcv9 alpha
	%{__make} boot EXTRAversion="-%{release}"
%endif
%ifarch ppc
	%{__make} vmlinux EXTRAversion="-%{release}"
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
	sparc32 \
%endif
	%{__make} modules EXTRAversion="-%{release}"
	%{__make} modules_install \
		INSTALL_MOD_PATH=$KERNEL_INSTALL_DIR \
		KERNELRELEASE=$KernelVer \
		EXTRAversion="-%{release}"
	rm -rf $KERNEL_INSTALL_DIR/lib/modules/*/{pcmcia,build}
}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR=$KERNEL_BUILD_DIR-build
rm -rf $KERNEL_INSTALL_DIR
install -d $KERNEL_INSTALL_DIR

BuildKernel
#BuildKernel smp

# BOOT kernel
%if %{?_with_boot:1}0
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-build/%{_libdir}/bootdisk"
install -d $KERNEL_INSTALL_DIR
BuildKernel BOOT
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{include,src/linux-%{version}}

KERNEL_BUILD_DIR=`pwd`
KERNEL_INSTALL_DIR="$KERNEL_BUILD_DIR-build"

cp -a $KERNEL_INSTALL_DIR/* $RPM_BUILD_ROOT

ln -sf ../src/linux/include/linux $RPM_BUILD_ROOT%{_includedir}/linux
ln -sf ../src/linux/include/asm $RPM_BUILD_ROOT%{_includedir}/asm

install $RPM_SOURCE_DIR/kernel-%{_target_cpu}.config .config

for target in clean oldconfig dep include/linux/version.h; do
%ifarch sparc
	sparc32 \
%endif
	%{__make} $target
done

cp -ar . $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

cd $RPM_BUILD_ROOT%{_prefix}/src/linux-%{version}

find $RPM_BUILD_ROOT/usr/src/linux-%{version} -name ".*depend" | \
while read file ; do
	mv $file $file.old
sed -e "s|$RPM_BUILD_ROOT\(/usr/src/linux-\)|\1|g" < $file.old > $file
	rm -f $file.old
done

%{__make} clean
rm -f scripts/mkdep
rm -f drivers/net/hamradio/soundmodem/gentbl

%clean
rm -rf $RPM_BUILD_ROOT{,-build}

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

if [ -x /sbin/rc-boot ] ; then
	/sbin/rc-boot 1>&2 || :
fi

%post pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

%postun pcmcia-cs
/sbin/depmod -a -F /boot/System.map-%{version}-%{release} %{version}-%{release}

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

%files
%defattr(644,root,root,755)
%ifarch alpha sparc
/boot/vmlinux-%{version}-%{release}
%endif
/boot/vmlinuz-%{version}-%{release}
/boot/System.map-%{version}-%{release}
%dir /lib/modules/%{version}-%{release}
/lib/modules/%{version}-%{release}/kernel
%ghost /lib/modules/%{version}-%{release}/modules.dep
/lib/modules/%{version}-%{release}/modules.*map
/lib/modules/%{version}-%{release}/modules.generic_string

%if %{?_with_boot:1}0
%files BOOT
%defattr(644,root,root,755)
%{_libdir}/bootdisk/boot/vmlinuz-%{version}-%{release}BOOT
%{_libdir}/bootdisk/boot/System.map-%{version}-%{release}BOOT
%dir %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/kernel
%ghost %{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.dep
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.*map
%{_libdir}/bootdisk/lib/modules/%{version}-%{release}BOOT/modules.generic_string
%endif

%files headers
%defattr(644,root,root,755)
%dir /usr/src/linux-%{version}
/usr/src/linux-%{version}/include
%{_includedir}/asm
%{_includedir}/linux

%files doc
%defattr(644,root,root,755)
/usr/src/linux-%{version}/Documentation

%files source
%defattr(644,root,root,755)
/usr/src/linux-%{version}/arch
/usr/src/linux-%{version}/drivers
/usr/src/linux-%{version}/fs
/usr/src/linux-%{version}/init
/usr/src/linux-%{version}/ipc
/usr/src/linux-%{version}/kernel
/usr/src/linux-%{version}/lib
/usr/src/linux-%{version}/mm
/usr/src/linux-%{version}/net
/usr/src/linux-%{version}/scripts
/usr/src/linux-%{version}/.config
#FIXME: this should be on, but not yet
#/usr/src/linux-%{version}/.depend
#/usr/src/linux-%{version}/.hdepend
/usr/src/linux-%{version}/COPYING
/usr/src/linux-%{version}/CREDITS
/usr/src/linux-%{version}/MAINTAINERS
/usr/src/linux-%{version}/Makefile
/usr/src/linux-%{version}/README
/usr/src/linux-%{version}/REPORTING-BUGS
/usr/src/linux-%{version}/Rules.make
