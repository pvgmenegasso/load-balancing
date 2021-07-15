from vm import *
import pytest

# First we verify the ttask and umax limits

def test_invalid_constants():
    with pytest.raises(Exception):
        User.set_ttask(0)
    with pytest.raises(Exception):
        User.set_ttask(11)
    with pytest.raises(Exception):
        Vm.set_umax(0)
    with pytest.raises(Exception):
        Vm.set_umax(11)

# Can we remove things or add when we shouldn't ?
def test_out_of_bounds():
    with pytest.raises(Exception):
        User.set_ttask(1)
        Vm.set_umax(1)
        # can we create a vm ?
        newVm = Vm()
        # can we add a user ? We should
        newVm.add_user()
        # can we add another ? We shouldn't be able to
        newVm.add_user()
    with pytest.raises(Exception):
        User.set_ttask(1)
        Vm.set_umax(1)
        newVm = Vm()
        newVm.add_user()
        newVm.tick()
        # This tick should be impossible
        newVm.tick()
    

# Now we execute a simple test
def test_simple_use():
    # Simulate ttask 4 and umax 2
    Vm.set_umax(2)
    User.set_ttask(4)
    # Now we simulate 6 ticks and check states

    # First tick
    vms : list[Vm] = []
    # Create a new Vm
    vms.append(Vm())
    vms[0].add_user()
    vms[0].tick()

    # we should now have a vm with 1 user and 1 tick
    assert vms[0].get_ticks() == 1
    assert len(vms[0].get_users()) == 1

    # Second tick
    # Add 3 users
    Vm.add_users(vms, 3)


    # now we tick the vms
    for vm in vms:
        vm.tick()

    # we should now have 2 vms with 2 users
    for vm in vms:
        assert len(vm.get_users()) == 2
    # first vm should have 2 ticks and second should have one
    assert vms[0].get_ticks() == 2
    assert vms[1].get_ticks() == 1

    # Third tick
    for vm in vms:
        vm.tick()

    # we should now have 3 ticks on first vm and 2 on second
    assert vms[0].get_ticks() == 3
    assert vms[1].get_ticks() == 2

    # Third tick
    for vm in vms:
        vm.tick()

    # same as the old one +1
    assert vms[0].get_ticks() == 4
    assert vms[1].get_ticks() == 3

    for vm in vms:
        vm.tick()
    # same thing as before, but now vms[0] should have only one user    
    assert vms[0].get_ticks() == 5
    assert vms[1].get_ticks() == 4
    assert len(vms[0].get_users()) == 1

