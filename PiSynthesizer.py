#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time
import math

class PiSynthesizer(object):
	__GPIOPIN=-1 #Pin not set
	__NOTEPAUSE=0.1 #Wait 0.1 between all notes - default
	__TACT=1.0/4.0 #Default tact multiplikator
	__NOTES=[] #Empty array

	#Initialize GPIOPin
	def __init__(self,GPIOPIN):
		self.__GPIOPIN=GPIOPIN
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__GPIOPIN, GPIO.OUT)

	#Play a note in a specific frequency and duration
	def __playSound(self,hz,secs):
	    	SLEEPDELAY=1.0/hz

		hcount=hz*secs/2
	    	while (hcount>0):
        		GPIO.output(self.__GPIOPIN,True)
        		time.sleep(SLEEPDELAY) 
        		GPIO.output(self.__GPIOPIN, False)
        		time.sleep(SLEEPDELAY)
			hcount=hcount-1

	#Pause the sound between every note
	def __notePause(self):
    		time.sleep(self.__NOTEPAUSE)
	

	#Plays every note in the NOTES-Array 
	def playSounds(self):
    		for aNote in self.__NOTES:
			note, duration = aNote
			self.__playSound( self.__calcToneFromKeyCode(note) ,duration/(1.0/self.__TACT))
			self.__notePause()

	#Calculates the frequency of every note
	def __calcToneFromKeyCode(self,keyCode):
    		return 440*2.0**((keyCode-49)/12.0) #Default Hz-formula (Src: Wikipedia)

	#Getter and Setter Methods
	#
	#
	def setTact(self,tact):
		self.__TACT=tact

	def getTact(self):
		return self.__TACT

	def setGPIOPin(self,gpiopin):
		self.__GPIOPIN=gpiopin
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__GPIOPIN, GPIO.OUT)


	def getGPIOPin(self):
		return self.__GPIOPIN

	def setNotePause(self,duration):
		self.__NOTEPAUSE=duration

	def getNotePause(self):
		return self.__NOTEPAUSE

	def setNotes(self,notes):
		self.__NOTES=notes
	
	def getNotes(self):
		return self.__NOTES
