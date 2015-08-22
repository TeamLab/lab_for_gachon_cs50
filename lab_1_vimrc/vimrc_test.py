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

if __name__ == '__main__':
	vimrc_contents = get_vimrc_contents()
	print (vimrc_contents)
