#include <linux/config.h>

#ifdef CONFIG_SMP
#include <linux/version-smp.h>
#else
#include <linux/version-up.h>
#endif
