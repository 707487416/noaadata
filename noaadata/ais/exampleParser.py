#!/usr/bin/env python

__version__ = '$Revision: 4791 $'.split()[1]
__date__ = '$Date: 2006-10-18 $'.split()[1]
__author__ = 'xmlbinmsg'

__doc__='''

Autogenerated python functions to serialize/deserialize binary messages.

WRITTEN BY HAND.  THIS VERSION IS FOR ME TO WRITE THE CODE BEFORE
HAND.  Then I can create the code generator.


Generated by: ./xmlbinmsg.py

Need to then wrap these functions with the outer AIS packet and then
convert the whole binary blob to a NMEA string.  Those functions are
not currently provided in this file.

serialize: python to ais binary
deserialize: ais binary to python

The generated code uses translators.py, binary.py, and aisstring.py
which should be packaged with the resulting files.


@requires: U{epydoc<http://epydoc.sourceforge.net/>} > 3.0alpha3
@requires: U{BitVector<http://cheeseshop.python.org/pypi/BitVector>}

@author: '''+__author__+'''
@version: ''' + __version__ +'''
@var __date__: Date of last svn commit
@undocumented: __version__ __author__ __doc__ myparser
@status: under development
@license: Generated code has no license
'''

import sys
from decimal import Decimal
from BitVector import BitVector

import binary
def waterlevelEncode(*aDict, **params):
	'''Serializer for the waterlevel binary message
	
	Keywords and types:

	  - dac:  uint
	  - unavail_uint:  uint
	  - uint:  uint
	FIX: generate CORRECT doctest string that does all the defaults

	The default message:

	>>> print waterlevelEncode()
	1011011101100

	@param aDict: for passing in a dictionary of keyword and values.
	@param params: keyword dictionary or if a dict is passed, it will use that dict
	@note: only use one of aDict or params
	'''

	if len(aDict) > 1:
		assert(False and 'Illegal call to with more than one param')
	if len(aDict) == 1:
		if not isinstance(dict,aDict):
			assert(False and 'a single parameter must be a dictionary of key values')
		if len(params)>0:
			assert(False and 'Must not specify both a lookup table and keyvalues')
		params=aDict

	bvList = []
	

	### FIELD: dac (type=uint)   REQUIRED CONSTANT FIELD
	bvList.append(binary.setBitVectorSize(BitVector(intVal=366)))

	### FIELD: unavail_uint (type=uint)
	if 'unavail_uint' in params: 		bvList.append(binary.setBitVectorSize(BitVector(intVal=param[unavail_uint]),2))
	else: bvList.append(binary.setBitVectorSize(BitVector(intVal=3),2))

	### FIELD: uint (type=uint)
	if 'uint' in params: 		bvList.append(binary.setBitVectorSize(BitVector(intVal=param[uint]),2))
	else: bvList.append(BitVector(size=2))
	return binary.joinBV(bvList)

############################################################
if __name__=='__main__':
    print waterlevelEncode()
    from optparse import OptionParser
    myparser = OptionParser(usage="%prog [options]",
			    version="%prog "+__version__)

    #sys.exit('EARLY EXIT - FIX: remove')
    myparser.add_option('--doc-test',dest='doctest',default=False,action='store_true',
                        help='run the documentation tests')
    myparser.add_option('--unit-test',dest='unittest',default=False,action='store_true',
                        help='run the unit tests')
    myparser.add_option('-v','--verbose',dest='verbose',default=False,action='store_true',
                        help='Make the test output verbose')

    (options,args) = myparser.parse_args()
    success=True

    if options.doctest:
	import os; print os.path.basename(sys.argv[0]), 'doctests ...',
	sys.argv= [sys.argv[0]]
	if options.verbose: sys.argv+='-v'
	import doctest
	numfail,numtests=doctest.testmod()
	if numfail==0: print 'ok'
	else:
	    print 'FAILED'
	    success=False

    if not success:
	sys.exit('Something Failed')

    del success # Hide success from epydoc


    if options.unittest:
	sys.argv = [sys.argv[0]]
	if options.verbose: sys.argv+='-v'
        print 'Currently no unit tests'
	#unittest.main()