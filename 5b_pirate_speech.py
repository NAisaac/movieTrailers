import urllib

#read the file
def readFile():
	pirateFileObject = open("/Users/isaac.yi/udacity/pirateFile.txt")
	pirateFile = pirateFileObject.read()
	print(pirateFile+'\n')
	pirateFileObject.close()
	speakPirate(pirateFile)

# convert the read file object to Pirate language
def speakPirate(text_to_convert):
	connectionObject = urllib.urlopen("http://isithackday.com/arrpi.php?text="+text_to_convert)
	output = connectionObject.read()
	print(output+'\n')
	connectionObject.close()

readFile()

