from vm import *
from os import environ
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
    pass