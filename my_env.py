#!/usr/bin/env python3
import os # used to get hostname, home directory
import argparse

import templates.bashrc # contained within this repository
import templates.screenrc
import templates.vimrc


parser = argparse.ArgumentParser(description='This program will create my environment files.')
parser.add_argument('--target', help = 'Value of { linux | osx }', default = "linux")
a = parser.parse_args()

t = a.target
host = os.uname()[1].split('.')[0]

# filenames
home = os.environ['HOME']
fname_bash = home + '/.bashrc'
fname_vim = home + '/.vimrc'
fname_screen = home + '/.screenrc'

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


with open(fname_bash, 'w') as f:
	f.write(content_bash)
with open(fname_vim, 'w') as f:
	f.write(content_vim)
with open(fname_screen, 'w') as f:
	f.write(content_screen)

