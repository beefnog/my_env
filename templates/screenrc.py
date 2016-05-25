header = r"""
# .screenrc

# termcapinfo xterm* ti@:te@
vbell off

# this is just for silly messages. seriously.
nethack on

hardstatus alwayslastline 
# blue hostname, blue pipe, cyan time, blue pipe, cyan window list (current window magenta)
hardstatus string "%{bk}H: %H | %{ck}%c%{bk} | %{ck}%-w%{mk}%n %t%{ck}%+w "

# default windows
screen -t L 0 bash
"""

