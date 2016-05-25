#!/usr/bin/env python
import os # only used to get the hostname
import argparse

import templates.bashrc # contained within this repository
import templates.screenrc
import templates.vimrc


parser = argparse.ArgumentParser(description='This program will create my environment files.')
parser.add_argument('--method', required = True, help = 'Value of { write | symlink }')
parser.add_argument('--target', help = 'Value of { linux | osx }')
a = parser.parse_args()

m, t = a.method, a.target
host = os.uname()[1].split('.')[0]

# filenames
fname_bash = '.bashrc'
fname_vim = '.vimrc'
fname_screen = '.screenrc'

# create contents of each file based upon the target architecture

# bash
content_bash = ""
content_bash += templates.bashrc.header
if t == 'linux':
	content_bash += templates.bashrc.grep_linux
	content_bash += templates.bashrc.ls_linux
if t == 'osx':
	content_bash += templates.bashrc.grep_osx
	content_bash += templates.bashrc.ls_osx
content_bash += templates.bashrc.per_host_aliases(host) # host is defined above
content_bash += templates.bashrc.functions

# vim
content_vim = ""
content_vim += templates.vimrc.header
# nothing more implemented / segregated at this time

# screen
content_screen = ""
content_screen += templates.screenrc.header
# nothing more implemented / segregated at this time


# if the method is "write", then write the files directly into my home.
# if the method is "symlink", then write the files in CWD and create symlinks from home.
if m == 'write':
	with open(fname_bash, 'w') as f:
		f.write(content_bash)
	with open(fname_vim, 'w') as f:
		f.write(content_vim)
	with open(fname_screen, 'w') as f:
		f.write(content_screen)
# if m == 'symlink':
	# TODO: implement this...

