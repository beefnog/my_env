header = r"""
# .screenrc

term xterm-256color
vbell off

# this is just for silly messages. seriously.
nethack on

hardstatus alwayslastline 
# blue hostname, yellow session name, blue pipe, cyan time, blue pipe, cyan window list (current window yellow)
hardstatus string "%{bk}H: %H,%{yk}%S%{bk} | %{ck}%c%{bk} | %{ck}%-w%{yk}%n %t%{ck}%+w "

# USE THIS ONE for screen v5.x
# hardstatus string "%{4}H: %H,%{3}%S%{4} | %{6}%c%{4} | %{6}%-w%{3}%n %t%{6}%+w "


# default windows
screen -t L 0 bash
"""

