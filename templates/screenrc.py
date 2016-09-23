header = r"""
# .screenrc

# termcapinfo xterm* ti@:te@
vbell off

# this is just for silly messages. seriously.
nethack on

hardstatus alwayslastline 
# blue hostname, blue pipe, cyan time, blue pipe, cyan window list (current window yellow)
hardstatus string "%{bk}H: %H | %{ck}%c%{bk} | %{ck}%-w%{yk}%n %t%{ck}%+w "

# default windows
screen -t L 0 bash
"""

