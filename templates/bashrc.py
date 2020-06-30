def per_host_aliases(hname):
	fname = "~/.bash_aliases_" + hname
	to_return = "# aliases specific to this host\n"
	to_return += "if [ -f " + fname + " ]\n"
	to_return += "then\n"
	to_return += "\t. " + fname + "\n"
	to_return += "fi\n\n"
	return to_return


header = r"""
# this should work across everything...
export CLICOLOR=1
export EDITOR=/usr/bin/vim

# default user, blue @, default hostname, blue cwd, cyan $
PS1='\[\033[0;39m\]\u\[\033[0;34m\]@\[\033[0;39m\]\h \[\033[0;34m\]\W\[\033[0;36m\]\$ \[\033[0m\]'
# PS1='\u@\h \W \$ ' # non-colored template

# generally useful aliases
if [ -f ~/.bash_aliases ]
then
	. ~/.bash_aliases
fi

"""

grep_osx = r"""
alias grep='grep --color=auto'

"""

grep_linux =''

ls_osx = ''

ls_linux = r"""
alias ls='ls --color=auto'

"""


macports_path = r"""
# this is to support macports. leave commented on most systems.
# export PATH=$PATH:/opt/local/bin:/opt/local/sbin

"""


functions = r"""
################
# functions
################
# vim modeline injector
modeline.python ()
{
        echo "# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4"
}

modeline.yaml ()
{
        echo "# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2"
}

modeline.js ()
{
        echo -e "/*\n# vim: tabstop=2 expandtab shiftwidth=2 softtabstop=2\n*/"
}

# sleep.verbose accepts an integer sleep time, gives periodic updates on time remaining.
sleep.verbose () {

        # no arguments? probably looking for usage...
        if [[ -z $1 ]]; then
                echo "Usage: sleep.verbose <integer seconds>"
                return
        else
                local sleeptime=$1
        fi

        # change output interval here...
        local interval=10

        # sleep in intervals, giving periodic updates
        while [ $sleeptime -gt 0 ]
        do
                if [ $sleeptime -le $interval ]; then
                        echo "Remaining time: $sleeptime"
                        sleep $sleeptime
                        return
                else
                        echo "Remaining time: $sleeptime"
                        sleep $interval
                        let sleeptime-=interval
                fi
        done
}

"""

