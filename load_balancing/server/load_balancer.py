from load_balancing.server.vm import User, Vm


class Server():

    def __init__(self, umax : int, ttask : int):

        self.__vms : list[Vm]= []
        Vm.set_umax(umax)
        User.set_ttask(ttask)

    def add_user(self, nUsers : int):
        Vm.add_users(self.__vms, nUsers)

    def simulate(self):
        
        # ticks all vms
        for vm in self.__vms:
            vm.tick()

        self.balance_load()

        vmUsers : list[int] = []

        for vm in self.__vms:
            vmUsers.append(Server.users_on_vm(vm))

        # returns list of server by users
        return vmUsers

    def balance_load(self):
        """This is where the magic happens !
        """
        # first we sort vms by number of users in ascending order
        self.__vms.sort(key=Server.users_on_vm)

        # searches for vms with vacant spaces
        vacantVms = [vm for vm in self.__vms if not vm.is_full()]

        # transfer users from vacant vms to other
        # vacant vms untill there are no more than 2 vacant vms
        while len(vacantVms) > 1 :
            
            vmWithSpace = vacantVms[1].get_users().pop(0)

            vacantVms[0].get_users().append(vmWithSpace)

            # recalculate vacant vms
            vacantVms = [vm for vm in self.__vms if not vm.is_full()]

        self.__vms = [vm for vm in self.__vms if not vm.is_empty()]

    def get_vms(self):
        return self.__vms

    def users_on_vm(vm : Vm):
        return len(vm.get_users())