#!/bin/sh
INCPATH=${1:-/usr/include}
cd $INCPATH
if [ ! -d asm-sparc -o ! -d asm-sparc64 ] ; then
	echo You must create $INCPATH/asm-sparc* symlinks first.
	exit 1
fi
if [ ! -d asm ]; then mkdir asm; fi
cd asm
for I in `( ls ../asm-sparc; ls ../asm-sparc64 ) | grep '\.h$' | sort -u`; do
	J=`echo $I | tr a-z. A-Z_`
	cat > $I << EOF
#ifndef __SPARCSTUB__${J}__
#define __SPARCSTUB__${J}__
EOF
	if [ -f ../asm-sparc/$I -a -f ../asm-sparc64/$I ]; then
		cat >> $I <<EOF
#ifdef __sparc_v9__
#include <asm-sparc64/$I>
#else
#include <asm-sparc/$I>
#endif
#endif
EOF
	elif [ -f ../asm-sparc/$I ]; then
		cat >> $I <<EOF
#ifndef __sparc_v9__
#include <asm-sparc/$I>
#endif
#endif
EOF
	else
		cat >> $I <<EOF
#ifdef __sparc_v9__
#include <asm-sparc64/$I>
#endif
#endif
EOF
	fi
done
