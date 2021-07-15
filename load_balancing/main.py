"""
Blank Lines

Surround top-level function and class definitions with two blank lines.

Method definitions inside a class are surrounded by a single blank line.

Extra blank lines may be used (sparingly) to separate groups of related functions.
Blank lines may be omitted between a bunch of related one-liners 
(e.g. a set of dummy implementations).

Use blank lines in functions, sparingly, to indicate logical sections.

Python accepts the control-L (i.e. ^L) form feed character as whitespace; 
Many tools treat these characters as page separators, so you may use them 
to separate pages of related sections of your file. Note, some editors and
web-based code viewers may not recognize control-L as a form feed and will
show another glyph in its place.
"""

from load_balancing.io import input
from load_balancing.server.load_balancer import Server
from load_balancing.server.vm import User, Vm
def main(file : str):

    # Get from file
    (ttask, umax, usersPerTick) = input.parse_input(file)

    server = Server(umax, ttask)

    output : list[list[int]] = []

    row = 0

    while len(usersPerTick) > 0:
        print("Simulation ================="+str(row))
        server.add_user(usersPerTick.pop())
        output.append(server.simulate())
        for vm in server.get_vms():
            print(" VM ----------------")
            vm.to_str()
        row += 1

    while len([vm for vm in server.get_vms() if len(vm.get_users()) > 0]):
        print("Simulation ================="+str(row))
        output.append(server.simulate())
        for vm in server.get_vms():
            print("VM ----------------")
            vm.to_str()
        row += 1

    return output

