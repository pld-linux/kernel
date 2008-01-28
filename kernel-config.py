#!/usr/bin/python

# Generate kernel .config file based on special kernel.conf rules file.
# arekm@pld-linux.org

import sys
import re

if len(sys.argv) != 5:
    print "Usage: %s target_arch kernel.conf input-config output-config" % sys.argv[0]
    sys.exit(1)

arch = sys.argv[1]
kernelconfig = sys.argv[2]
inconfig = sys.argv[3]
outconfig = sys.argv[4]

from UserDict import UserDict

# odict from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/107747
class odict(UserDict):
    def __init__(self, dict = None):
        self._keys = []
        UserDict.__init__(self, dict)

    def __delitem__(self, key):
        UserDict.__delitem__(self, key)
        self._keys.remove(key)

    def __setitem__(self, key, item):
        UserDict.__setitem__(self, key, item)
        if key not in self._keys: self._keys.append(key)

    def clear(self):
        UserDict.clear(self)
        self._keys = []

    def copy(self):
        dict = UserDict.copy(self)
        dict._keys = self._keys[:]
        return dict

    def items(self):
        return zip(self._keys, self.values())

    def keys(self):
        return self._keys

    def popitem(self):
        try:
            key = self._keys[-1]
        except IndexError:
            raise KeyError('dictionary is empty')

        val = self[key]
        del self[key]

        return (key, val)

    def setdefault(self, key, failobj = None):
        UserDict.setdefault(self, key, failobj)
        if key not in self._keys: self._keys.append(key)

    def update(self, dict):
        UserDict.update(self, dict)
        for key in dict.keys():
            if key not in self._keys: self._keys.append(key)

    def values(self):
        return map(self.get, self._keys)

dict = odict()

rc = 0
f = open(kernelconfig, 'r')
for l in f:
    if l[:6] == 'CONFIG_':
        print "Omit CONFIG_ when specifing symbol name: %s" % l
        rc = 1
        continue

    if re.match('^#', l) or re.match('^\s*$', l):
        continue

    if not re.match('^[0-9A-Z]+', l):
        print "Unknown line: %s" % l
        rc = 1
        continue

    c = l.strip().split()
    symbol = c[0]
    if dict.has_key(symbol):
        print "Duplicate symbol %s!" % symbol
        rc = 1
        continue

    par = False
    for i in c[1:]:
        par = True
        i = i.split('=')
        key = i[0]
        if key != arch and key != "all": 
            continue

        try:
            val = i[1]
        except IndexError:
            print "Invalid line: %s" % l.strip()
            continue

        dict[symbol] = val
    if not par:
        print "Unknown line: %s" % l
        rc = 1
        continue

f.close()

if not rc == 0:
    sys.exit(1)

f = open(inconfig, 'r')
cfg = f.read()
f.close()

cfg += '\n# PLD configs\n'
for symbol in dict.items():
    (key, val) = symbol

    # strip contents
    rp = re.compile("^CONFIG_%s=.*$" % key, re.MULTILINE)
    cfg = rp.sub("", cfg)
    rp = re.compile("^# CONFIG_%s is not set$" % key, re.MULTILINE)
    cfg = rp.sub("", cfg)
    
    if val == "y":
        cfg += "CONFIG_%s=y\n" % key
    elif val == "m":
        cfg += "CONFIG_%s=m\n" % key
    elif val == "n":
        cfg += "# CONFIG_%s is not set\n" % key
    elif re.compile('^[a-zA-Z0-9"\_\/\-]+$').match(val):
        cfg += "CONFIG_%s=%s\n" % (key, val)
    else:
        print "Unknown value [%s] for key: %s" % (val, key)
        sys.exit(1)

f = open(outconfig, 'w')
f.write(cfg)
f.close()
