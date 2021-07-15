""" This module outputs a list of servers available at the end of each tick, on a file
and the total cost at the end

Line standard:

for each tick:
    (*,)^n
at the end:
x


Where:
* = the server represented by the number of users
n = the number of servers
x = the total cost 

Example:

1,                          2
^                           ^                                   
a server with 1 user        a server with 2 users               

2
^
R$1 for 1 tick of the first vm + R$1 for 1 tick of the second vm = R$2 total.

"""