# -*- makefile -*-
# Simple makefile so I don't have to remember how to run this stuff
GEN:=../scripts/aisxmlbinmsg2py.py

AISXMLFILES:=
AISXMLFILES += ais_msg_1.xml # position, Class A
AISXMLFILES += ais_msg_2.xml # position, Class A
AISXMLFILES += ais_msg_3.xml # position, Class A
AISXMLFILES += ais_msg_4.xml # base station report
AISXMLFILES += ais_msg_5.xml # ship and cargo
AISXMLFILES += ais_msg_6.xml # Addressed binary message
AISXMLFILES += ais_msg_7.xml # ACK for address binary message
AISXMLFILES += ais_msg_8.xml # binary message
AISXMLFILES += ais_msg_9.xml # SAR position
AISXMLFILES += ais_msg_10.xml # utcquery
AISXMLFILES += ais_msg_11.xml # 
AISXMLFILES += ais_msg_12.xml # asrm
#AISXMLFILES += ais_msg_13.xml # 
AISXMLFILES += ais_msg_14.xml # srbm
AISXMLFILES += ais_msg_15.xml # Interrogation
#AISXMLFILES += ais_msg_16.xml # 
AISXMLFILES += ais_msg_17.xml # A - GNSS differential corrections
AISXMLFILES += ais_msg_18.xml # Class B position report
AISXMLFILES += ais_msg_19.xml # Class B extended position and ship type report
AISXMLFILES += ais_msg_20.xml # Data Link management
AISXMLFILES += ais_msg_21.xml # AidsToNavReport
AISXMLFILES += ais_msg_22.xml
AISXMLFILES += ais_msg_23.xml # GroupAssignmentCommand
#AISXMLFILES += ais_msg_24.xml # StaticDataReport
#AISXMLFILES += ais_msg_25.xml # SingleSlotBinaryMessage - addressed or broadcast
#AISXMLFILES += ais_msg_26.xml # Multi slot binary message with comm state

# FIX: move to an IMO or IALA subdir
AISXMLFILES += imo_001_11.xml
AISXMLFILES += imo_001_13.xml
AISXMLFILES += imo_001_14.xml

# Move to a prototypes subdir
AISXMLFILES += waterlevel2.xml
AISXMLFILES += whalenotice.xml
AISXMLFILES += whalenotice1.xml
AISXMLFILES += whalenotice2.xml
AISXMLFILES += timed_circular_notice.xml # Whale notice for J. Arroyo

AISXMLFILES += allaistypes.xml

AISPYFILES := ${AISXMLFILES:.xml=.py} ais_msg_2_handcoded.py
AISHTMLFILES := ${AISXMLFILES:.xml=.html}

default: ${AISHTMLFILES} ${AISPYFILES}

py: ${AISPYFILES}
html: ${AISHTMLFILES}

clean:
	rm -f *expanded*.{xml,html}
	-rm -f *.pyc
	-rm -f out-ais.xml
	-rm -f ?.html
	-rm -f a.out foo* blah*
	-rm -rf html
	-rm -f *_exp.xml *.html


%.html: %.xml
	./expandais.py -i $< -o $<.expanded
	xsltproc ais.xsl $<.expanded > $@
	rm $<.expanded

test:
	echo 'nop'
