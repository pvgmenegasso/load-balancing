from load_balancer import *

def test_simple():
    # Simulate ttask 4 and umax 2
    server = Server(2, 4)

    # Now we simulate 4 ticks and check states

    # First tick

    # add a new user
    server.add_user(1)

    # we should now have a vm with 1 user and 1 tick
    assert server.simulate() == [1]

    # Second tick
    # Add 3 users
    server.add_user(3)
    assert server.simulate() == [2, 2]
    # we should now have 2 vms with 2 users
    for vm in server.get_vms():
        assert len(vm.get_users()) == 2

    # Third tick
    server.add_user(1)
    server.simulate()


    # fourth tick
    assert server.simulate() == [1, 2, 2]


    # fifth tick
    # same thing as before, but now rebalance should occur 
    assert server.simulate() == [2, 2]
      

    