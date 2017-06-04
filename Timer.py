#!/usr/bin/python3

#The Above code was to make the file an executable one

#FOLLOWING IS A BREAK REMINDER WHICH REMINDES YOU TO TAKE BREAK AFTER A GIVENTIME. 
#YOU CAN LISTEN SONGS OR PLAY A VIDEO ON YOUTUBE. PROGRAM USES EASYGUI FOR GRAPHIC INTERFACE.
#MAKE SURE U HAVE IT INSTALLED TO COMFORTABLY RUN THE PROGRAM.

#importing various modules
from easygui import *
import time
import subprocess
import webbrowser

#to pop up a dialogue box displaying the msg below
msgbox("This reminds you to take breaks after every N miniutes", title = "BREAK REMINDER")

msg = "DO YOU WISH TO CONTINUE?"
if ccbox(msg):     # show a Continue/Cancel dialog and if continue
	work_time = integerbox( msg = "How long you want to work?(min):",  upperbound = 1440) * 60
	time_on_break = integerbox( msg = "Time on each break?(min)",  upperbound = 1440)  * 60 
	break_after = integerbox( msg = "You want break after ? (min)",  upperbound = 1440)  * 60
	
else:  # user chose Cancel
	quit()

#if user cancels work time none is reurned
#hence set worktime and break_after to avoide aritmetical errors
if work_time is None or break_after is None: 
	work_time = 0
	break_after = 1

#initilaizing
temp = time_on_break
breaks_consumed = 0

#divide the total time interval by the time you want your break to get no of breaks 
total_breaks_allowed = int (work_time / break_after)

#main code of program
while (total_breaks_allowed > breaks_consumed):
	#sleep for those many seconds and then run the further code
	time.sleep(break_after)
	msgbox("TIME FOR A BREAK")

	msg = "Wanna hear a song or YouTube?"
	choices = ["MUSIC", "YouTube", "Cancel"]
	# show a Continue/Cancel dialog 
	reply = buttonbox(msg, choices=choices)


	if reply is "MUSIC": 
		#path to my music directory you can put yours
		subprocess.Popen( ["xdg-open", '/home/prathamesh/Music/']) 
	elif reply is "YouTube":
		#open youtube website  u can specify ur custom url too
		webbrowser.open("https://www.youtube.com") 
	else:
		pass
		

	while time_on_break > 0:
		#timer to count time left to finish the break
		time.sleep(0.99)
		time_on_break = time_on_break - 1

	msgbox("BREAK OVER BACK TO WORK")

	#reset time for break
	time_on_break = temp 
	#increase the break counter
	breaks_consumed  = breaks_consumed +1	
	
#end the program peacefully!!
quit()






