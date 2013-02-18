#! /usr/bin/env python

import webbrowser
import os
import time


NE = 1
hour = raw_input("Enter Hour: ")
minute = raw_input("Enter Minute: ")

while(NE):
	dt = list(time.localtime())
	ahour = dt[3]
	amin = dt[4]
	if (ahour == int(hour)) and (amin == int(minute)):
	
		webbrowser.open("http://www.youtube.com/watch?v=H2g0Pk3gBzI", new=1, autoraise=1)
		NE = 0

