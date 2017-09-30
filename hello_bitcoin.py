#!/usr/bin/env python

from bitcoin import *

pk1 = random_key()
pk2 = random_key()
pk3 = random_key()

pbk1 = privtopub(pk1)
pbk2 = privtopub(pk2)
pbk3 = privtopub(pk3)

multi_sig = mk_multisig_script(pbk1, pbk2, pbk3, 2, 3)
multi_address = scriptaddr(multi_sig)
print "multi_address: {}".format(multi_address)
print "multi_sig: {}".format(multi_sig)
