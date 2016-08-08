import urllib

def read_text():
	# open the file; returns a File type object. File class is a built-in class in Python
	# open is a built-in function that creates a File object with File class's __init__ function
	rawFileObject = open("/Users/isaac.yi/udacity/movie_quotes.txt")
	# read the file
	contentOfFile = rawFileObject.read()
	# print out the file
	print(contentOfFile+'\n')
	# good convention to close the opened file
	rawFile.close()
	# now let's check for profanity
	check_profanity(contentOfFile)

def check_profanity(text_to_check):
	# urllib is a module that helps get data from the internet
	# urlopen opens a connection to the URL and creates an object
	# http://www.wdylike.appspot.com outputs true/false on any text data
	connectionObject = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connectionObject.read()
	print(output+'\n')
	connectionObject.close()

read_text()