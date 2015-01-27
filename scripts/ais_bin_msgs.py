#!/usr/bin/env python
"""Summarize AIS binary messages (6 and 8) in files."""

import datetime
from decimal import Decimal
import exceptions
import StringIO
import sys
import traceback

from aisutils.BitVector import BitVector
from aisutils import binary
from aisutils.uscg import uscg_ais_nmea_regex


def parse_msgs(infile, verbose=False):
    for line in infile:
        line = line.strip()

        try:
            match = uscg_ais_nmea_regex.search(line).groupdict()
        except AttributeError:
            continue

        msg_type = match['body'][0]
        if msg_type not in ('6', '8'):
            continue

        if msg_type == '6' and len(match['body']) < 15:
            continue
        if msg_type == '8' and len(match['body']) < 10:
            continue

        try:
            bv = binary.ais6tobitvec(match['body'][:15])
        except ValueError:
            sys.stderr.write('bad msg: %s\n' % line.strip())
            continue

        r = {}
        r['MessageID']=int(bv[0:6])
        r['UserID']=int(bv[8:38])

        if '6' == msg_type:
            dac = int(bv[72:82])
            fi = int(bv[82:88])
        elif '8' == msg_type:
            dac = int(bv[40:50])
            fi = int(bv[50:56])
        elif verbose:
            print 'not a bbm:', line

        if verbose:
            print msg_type, dac, fi, r['UserID'], line.rstrip()
        else:
            print msg_type, dac, fi, r['UserID'], match['station']


def main():
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] file1.ais [file2.ais ...]")

    parser.add_option('-v','--verbose',default=False,action='store_true',
                      help='Make program output more verbose info as it runs')

    (options,args) = parser.parse_args()
    for filename in args:
        parse_msgs(open(filename), verbose = options.verbose)

if __name__=='__main__':
    main()
