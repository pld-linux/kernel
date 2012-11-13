MAKE_OPTS :=
SUB_DIR :=
OSUB_DIR :=

include $(TARGETOBJ).mk

all := $(filter-out all Makefile,$(MAKECMDGOALS))

all $(all):
	$(MAKE) -C $(KERNELSRC)/$(SUB_DIR) O=$(KERNELOUTPUT)/$(OSUB_DIR) $(MAKE_OPTS) $(all)

# vim:ft=make
