
DEST = $(if $(DESTDIR),$(DESTDIR),unspecified)

INSTALL = install -D
MKDIR = install -d

boot_LIBS += of1275/lib.a
boot_LIBS += common/lib.a
boot_LIBS += lib/lib.a

boot_LIBS += openfirmware/dummy.o

boot_LIBS += openfirmware/start.o
boot_LIBS += openfirmware/misc.o
boot_LIBS += openfirmware/common.o
	
boot_LIBS += openfirmware/crt0.o
boot_LIBS += openfirmware/coffcrt0.o
boot_LIBS += openfirmware/coffmain.o
boot_LIBS += openfirmware/newworldmain.o
boot_LIBS += openfirmware/chrpmain.o

boot_LIBS += simple/head.o
boot_LIBS += simple/relocate.o
boot_LIBS += simple/prepmap.o
boot_LIBS += simple/misc.o
boot_LIBS += simple/misc-prep.o
boot_LIBS += simple/mpc10x_memory.o

kernel_LIBS += lib.a

UTILS += addnote
UTILS += hack-coff
UTILS += mkbugboot
UTILS += mknote
UTILS += mkprep


all: $(addprefix arch/ppc/boot/,$(boot_LIBS)) \
	$(addprefix lib/,$(kernel_LIBS)) \
	$(addprefix arch/ppc/boot/utils/,$(UTILS))


$(DESTDIR)/kernel/%: $(DEST) lib/%
	$(INSTALL) lib/$* $@

$(DESTDIR)/utils/%: $(DEST) arch/ppc/boot/utils/%
	$(INSTALL) arch/ppc/boot/utils/$* $@

$(DESTDIR)/%: $(DEST) arch/ppc/boot/%
	$(INSTALL) arch/ppc/boot/$* $@

install: all \
	$(addprefix $(DESTDIR)/,$(boot_LIBS)) \
	$(addprefix $(DESTDIR)/kernel/,$(kernel_LIBS)) \
	$(addprefix $(DESTDIR)/utils/,$(UTILS))
	
$(DESTDIR):
	$(MKDIR) $@

unspecified:
	@echo "DESTDIR must be specified"
	@exit 10

#vim:syntax=make
