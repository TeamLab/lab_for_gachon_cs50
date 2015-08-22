def get_vimrc_contents():
	vimrc_contents = ""

	with open('~/.vimrc', 'r') as f:
	     vimrc_contents = f.read()

    return vimrc_contents

if __name__ == '__main__':
	vimrc_contents = get_vimrc_contents()
	print (vimrc_contents)