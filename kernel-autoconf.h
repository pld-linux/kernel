#ifndef __pld_kernel_autoconf_h__
#define __pld_kernel_autoconf_h__

/*
 * Define some nasty macros o we can construct the file names
 * we want to include
 */

#if defined(__pld_autoconf_included_file__)
#undef __pld_autoconf_included_file__
#endif /* __pld_autoconf_included_file__ */

#if defined(__KERNEL_SMP)
#include <linux/autoconf-smp.h>
#define __pld_autoconf_included_file__ 1
#endif /* __KERNEL_SMP */

#if !defined(__pld_autoconf_included_file__)
#include <linux/autoconf-up.h>
#else
#undef __pld_autoconf_included_file__
#endif /* __pld_autoconf_included_file__ */

#endif /* __pld_kernel_autoconf_h__ */
