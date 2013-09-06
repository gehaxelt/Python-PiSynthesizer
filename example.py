#!/usr/bin/python2.7
from PiSynthesizer import PiSynthesizer
Synth = PiSynthesizer(18);

tones= [(40,1), #c
	(42,1), #d
	(44,1), #e
	(45,1), #f
	(47,1), #g
	(47,1), #g
	(49,1), #a
	(49,1), #a
	(49,1), #a
	(49,1), #a
	(47,1), #g
	(49,1), #a
	(49,1), #a
	(49,1), #a 
	(49,1), #a
	(47,1), #g
	(47,1), #g
	(45,1), #f
	(45,1), #f
	(45,1), #f
	(45,1), #f	
	(45,1), #f
	(44,2), #e
	(44,2), #e
	(40,4)] #c


Synth.setNotes(tones)
Synth.playSounds()


