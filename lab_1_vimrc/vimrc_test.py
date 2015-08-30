from os.path import expanduser
import os

def get_vimrc_contents():
	home = expanduser("~")
	vimrc_contents = ""
	home_vimrc = os.path.join(home, ".vimrc")

	if not os.path.exists(home_vimrc):
		print ("NOT exists: .vimrc")
		return vimrc_contents

	with open(home_vimrc, 'r') as f:
		vimrc_contents = f.read()
	
	return vimrc_contents

def send_vimrc_file():
	data = ''' ''' 
	return data

def find(l, s):
	for i in range(len(l)):
		if l[i].find(s)!=-1:
			return i
	return None # Or -1

def remake_vimrc_test_file(vimrc_contenets):
	with open("vimrc_test.py", "r") as f:
		vimrc_test_contents = f.readlines()
	
	target_index = find(vimrc_test_contents, 'data = ' )
	vimrc_contenets = vimrc_contenets.replace("\n", " ")
	vimrc_test_contents[target_index] =	"\tdata = '''%s'''\n" % vimrc_contenets
	with open("vimrc_test.py", "w") as w:
		for line in vimrc_test_contents:
			w.write(line)

if __name__ == '__main__':
	vimrc_contents = get_vimrc_contents()
	print ("===The contents of your vimrc file=====")
	print (vimrc_contents)
	remake_vimrc_test_file(vimrc_contents)
	print ("=====> Your vimrc_test.py is changed")
