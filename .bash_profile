# Robby Stahl - .bashrc / .bash_profile
# 20140810

# this should work across everything...
export CLICOLOR=1

# default user, blue @, default hostname, blue cwd, cyan $
PS1='\[\033[0;37m\]\u\[\033[0;34m\]@\[\033[0;37m\]\h \[\033[0;34m\]\w\[\033[0;36m\]\$ \[\033[0m\]'
# PS1='\u@\h \w \$ ' # non-colored template

# this is to support macports. leave commented on most systems.
# export PATH=$PATH:/opt/local/bin:/opt/local/sbin

# core command aliases
# alias grep='grep --color=auto' # uncomment for os x / bsd
alias ls='ls --color=auto' # comment for os x and some funky BSDs

# generally useful aliases
if [ -f ~/.bash_aliases ]
then
	. ~/.bash_aliases
fi
# aliases specific to this host from .bash_aliases_{hostname}
if [ -f ~/.bash_aliases_beeftop ]
then
	. ~/.bash_aliases_beeftop
fi

################
# functions
################
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

