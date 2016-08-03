from sys import argv

def usage():
	print ("Usage: python %s <arg1> <arg2> <arg3>" % argv[0])

if len(argv) != 4:
	usage()
	exit()

script, first, second, third = argv

name = input ("Now tell me your name:")
print ("Hello, %s" % name)
print ("The number of arg is:", len(argv))
print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
