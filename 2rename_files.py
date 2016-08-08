import os

def rename_files():
	# get files or directories in the path
	file_list = os.listdir("/Users/isaac.yi/udacity/prank")
	print (file_list)
	# get the current working directory (i.e. ~/udacity)
	saved_path = os.getcwd()
	# specify and set the current working directory
	os.chdir("/Users/isaac.yi/udacity/prank")
	# for each file, rename filename
	
	for file_name in file_list:
		print ("Old name: " + file_name)
		print ("New name: " + file_name.translate(None, "0123456789"))
		# using os.rename(old name, new name) and string.translate(translate table, delete characters)
		os.rename(file_name, file_name.translate(None, "0123456789"))
	
	# switch the current directory back to the original saved path
	os.chdir(saved_path)

rename_files()