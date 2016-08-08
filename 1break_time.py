import time
import webbrowser

### This program opens up a URL every 2 hours from the start of the program; 3 times in total

total_breaks = 3
break_count = 0

# ctime gives us the current time
print ("This program started on " + time.ctime() + "and will run every 2 hrs")

while (break_count < total_break): 
	# sleep pauses the function in inputted seconds, which is 2 hours
	time.sleep(2*60*60)
	# opens the inputted URL 
	webbrowser.open("http://www.youtube.com")
	break_count += 1