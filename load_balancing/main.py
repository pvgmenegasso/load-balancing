"""Tests the example given by files input.txt and output.txt
"""

from load_balancing.io import input
from load_balancing.server.load_balancer import Server
from load_balancing.server.vm import User, Vm


def main(file : str):
    """Simulate the load balancer
    """

    # Get from file
    (ttask, umax, usersPerTick) = input.parse_input(file)

    # Create a server
    server = Server(umax, ttask)

    # Create an empty output
    output : list[list[int]] = []

    # Counts current tick
    row = 1

    # Since we are using pop, this list needs to be reversed
    usersPerTick.reverse()

    # While there are entries to process, do:
    while len(usersPerTick) > 0:
        # prints header
        print("Simulation ================="+str(row))
        # gets the number of users to add on this tick
        nUsers = usersPerTick.pop()
        # are there users to add ?      
        if nUsers > 0:
            # add them
            server.add_user(nUsers)
        # simulate a tick and append the result
        output.append(server.simulate())
        # print the vms
        for vm in server.get_vms():
            print(" VM  ")
            vm.print()
        # next row !
        row += 1

    # Continue simulating while there are vms with pending processes
    while len([vm for vm in server.get_vms() if len(vm.get_users()) > 0]):
        # the same logic as before
        print("Simulation ================="+str(row))
        output.append(server.simulate())
        for vm in server.get_vms():
            print("VM ")
            vm.print()
        row += 1

    print(server.get_cost())

    output.append(server.get_cost())

    return output

