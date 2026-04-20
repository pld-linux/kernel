#!/bin/sh
set -xe

BRANCH=aufs7.0
#BRANCH=aufs7.x-rcN

# aufs7
[ -d aufs-standalone ] || git clone https://github.com/sfjro/aufs-standalone.git
cd aufs-standalone
git checkout -b ${BRANCH} origin/${BRANCH} || git switch ${BRANCH}
git pull
rm -rf linux && mkdir linux
cp -a Documentation fs include linux
diff -urN /usr/share/empty linux | filterdiff -x linux/include/uapi/linux/Kbuild > ../kernel-aufs.patch
cat aufs7-kbuild.patch aufs7-base.patch aufs7-mmap.patch aufs7-standalone.patch aufs7-loopback.patch >> ../kernel-aufs.patch

# other
