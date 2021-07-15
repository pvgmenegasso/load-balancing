"""This module implements a Server along with 
it's capabilites
"""
from load_balancing.server.vm import User, Vm

# each vm costs R$1 to run
COST = 1

class Server():
    """ This class defines a server which contains the
    vms and users. It also implements the load_balancing
    also implements the simulate function which runs a tick

    Attributes
    ----------
    __vms : list[vm]
        A list of vms on the server
    """

    def __init__(self, umax : int, ttask : int):
        """Initialize the server

        Parameters
        ----------
        umax : int
            The umax value 
        ttask : int 
            The ttask value
        __cost : int 
            The total cost for the lifetime of the server
        """
        # Initialize list of vms
        self.__vms : list[Vm]= []
        # Set the parameters for the vm
        Vm.set_params(umax, ttask)
        # The total cost for this Server
        self.__cost : int = 1

    def add_user(self, nUsers : int):
        """Adds a new user to this vm

        Parameters
        ----------
        nUsers : int
            The number of users to add
        """
        Vm.add_users(self.__vms, nUsers)

    def add_cost(self, cost : int):
        """Adds a cost to the total cost of this server

        Parameters
        ----------
        cost : int
            The cost to add
        """
        self.__cost += cost

    def get_cost(self):
        """Return the __cost attribute
        """
        return self.__cost

    def simulate(self):
        """Runs a tick on this server

        Returns
        -------
        list[int] :
            a list with the number of users for each vm
        """
        # Removes empty vms
        self.__vms = [vm for vm in self.__vms if not vm.is_empty()]

        # ticks all vms
        for vm in self.__vms:
            vm.tick()

        # Balances server load
        self.balance_load()

        # Empty list to be returned
        vmUsers : list[int] = []

        # Removes empty vms
        self.__vms = [vm for vm in self.__vms if not vm.is_empty()]

        for vm in self.__vms:
            # each vm costs x per tick
            self.add_cost(COST)

        for vm in self.__vms:
            # Put the values on the list
            vmUsers.append(Server.users_on_vm(vm))


        # returns list of server by users
        return vmUsers

    def balance_load(self):
        """This is where the magic happens ! This method 
        Balances load between multiple vms
        """
        # Remove empty vms
        self.__vms = [vm for vm in self.__vms if not vm.is_empty()]
        # if there is only one vm, no balance is needed
        if len(self.get_vms()) > 1:
            # first we sort vms by number of users in ascending order
            self.__vms.sort(key=Server.users_on_vm)

            # searches for vms with vacant spaces
            vacantVms = [vm for vm in self.__vms if not vm.is_full()]

            # transfer users from vacant vms to other
            # vacant vms untill there are no more than 2 vacant vms
            while len(vacantVms) > 1 :
     
                # get the User from the free vm
                userWithSpace = vacantVms[1].get_users().pop(0)
                # Add the user to a vacant vm
                vacantVms[0].get_users().append(userWithSpace)

                # recalculate vacant vms
                vacantVms = [vm for vm in self.__vms if not vm.is_full()]
        

    def get_vms(self):
        """
        Returns
        -------
        list[Vm] : 
            the vms on this server
        """
        return self.__vms

    def users_on_vm(vm : Vm):
        """
        Parameters
        ----------
        vm : Vm
            Number of users in vm

        Returns
        -------
        int :
            number of users on this vm
        """
        return len(vm.get_users())