#!/bin/sh
set -xe

#BRANCH=aufs5.x-rcN
BRANCH=aufs5.10.82

# aufs5
[ -d aufs5-standalone ] || git clone git://github.com/sfjro/aufs5-standalone.git
cd aufs5-standalone
git checkout -b ${BRANCH} origin/${BRANCH}
git pull
cat aufs5-kbuild.patch aufs5-base.patch aufs5-mmap.patch aufs5-standalone.patch > ../kernel-aufs5.patch
rm -rf linux && mkdir linux
cp -a Documentation fs include linux
diff -urN /usr/share/empty linux | filterdiff -x linux/include/uapi/linux/Kbuild >> ../kernel-aufs5.patch
cat aufs5-loopback.patch >> ../kernel-aufs5.patch

# other
