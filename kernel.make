MAKE_OPTS :=

include $(TARGETOBJ).mk

all := $(filter-out all Makefile,$(MAKECMDGOALS))

all:
	$(MAKE) -C $(KERNELSRC) O=$(KERNELOUTPUT) $(MAKE_OPTS) $(all)

# vim:ft=make
