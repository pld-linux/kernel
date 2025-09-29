#!/bin/sh
set -xe

#BRANCH=aufs6.16
BRANCH=aufs6.x-rcN

# aufs6
[ -d aufs-standalone ] || git clone https://github.com/sfjro/aufs-standalone.git
cd aufs-standalone
git checkout -b ${BRANCH} origin/${BRANCH} || git switch ${BRANCH}
git pull
rm -rf linux && mkdir linux
cp -a Documentation fs include linux
diff -urN /usr/share/empty linux | filterdiff -x linux/include/uapi/linux/Kbuild > ../kernel-aufs.patch
cat aufs6-kbuild.patch aufs6-base.patch aufs6-mmap.patch aufs6-standalone.patch aufs6-loopback.patch >> ../kernel-aufs.patch

# other
