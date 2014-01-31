MAKE_OPTS :=
TARGETOBJ ?= $(patsubst %.mk,%,$(wildcard *.mk))

include $(TARGETOBJ).mk

all := $(filter-out all Makefile,$(MAKECMDGOALS))

all $(all):
	$(MAKE) -C $(KERNELSRC) O=$(KERNELOUTPUT) $(MAKE_OPTS) $(all)

# vim:ft=make
