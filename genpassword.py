#!/usr/bin/python
# -*- coding:utf-8 -*-

import itertools
import sys
from optparse import OptionParser

parser = OptionParser()




parser.add_option("-f", "--file", type="string", dest="pass_file", help="passwords")

(options, args) = parser.parse_args()

if options.pass_file:
    pass
else:
    parser.print_help()
    sys.exit(1)


#f = open(options.pass_file)
#lines = f.readlines()

with open(options.pass_file) as f:
    lines = f.read().splitlines()

res = itertools.permutations(lines,3) # 3 is the length of your result.
for i in res: 
   print ''.join(i)
