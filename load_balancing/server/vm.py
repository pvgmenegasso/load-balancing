"""This module defines a VM for usage in the simulation environment"""

from os import environ
import math
# Check DEBUG environment variable and assign it
if environ.get('DEBUG') == "True":
    DEBUG = True
else:
    DEBUG = False


class User():
    """Defines a User object which represents a client connected
    to a Vm on the cloud

    Class Attributes
    ----------------
    ttask : int
        Number of ticks per task

    Attributes
    ----------
    __ticksLeft : int
        Number of ticks left for the user
    
    Methods
    -------
    tick() : None 
        Passes time by one tick for this User
    isOver() bool
        Returns true if the process has finished
    """

    __ttask : int

    def __init__(self):
        """Creates a new User"""
        # The number of ticks left is essentially the number of ticks at first
        self.__ticksLeft = User.__ttask

    def set_ttask(ttask : int):
        """Set value for class variable ttask
        
        Parameters
        ----------
        ttask : int
            cost of ticks per task
        """

        # ttask cannot be lesser or equal than 0
        if ttask <= 0:          
            # is debug mode set ?
            if DEBUG:
                print("Value for ttask invalid Lesser than 0 !")
                raise ValueError
            raise ValueError

        if ttask >10:
            if DEBUG:
                print("Value for ttask greater than 10 !")
                raise ValueError
            raise ValueError

        # everything checks, we can set the task
        User.__ttask = ttask

    def tick(self):
        """Passes time by one tick"""
        if self.__ticksLeft == 0:
            if DEBUG:
                print("Cannot tick this user !!")
                raise ValueError
            raise ValueError
        # Decreases number of ticks left
        self.__ticksLeft = self.__ticksLeft - 1

    def isOver(self):
        """Looks to see if the task is over

        Returns
        -------
        True : The task is over
        False : Task still running

        raises
        -------
        RuntimeError : Invalid value for number of ticks left, check logic
        """
        # Does the process has still ticks to do ?
        if self.__ticksLeft == 0:
            return True
        # So it's not over
        if self.__ticksLeft <0 or self.__ticksLeft > User.__ttask:
            # Oops, something wrong happened !
            # Is DEBUG environment variable enabled ?
            if DEBUG:
                # Prints debug info
                print(" Wrong value for Ticks left on user")
                print(" ticksLeft =" +str(self.__ticksLeft))
                raise RuntimeError
            raise RuntimeError
        # Everything seems fine, task not over !
        return False

    def ticksPassed(self):
        """Return quantity of ticks passed since the
        User was created

        Returns
        -------
        int :
            The number of ticks passed
        """
        return User.__ttask - self.__ticksLeft
    

class Vm():
    """Defines a Vm object which simulates a virtual server in a 
    cloud environment

    Class Attributes
    ----------
    __umax : int
        Maximum number of users per Vm

    Class Methods
    -------------
    add_users(list, int):
        adds int users to a given list of vms

    Attributes
    ----------
    users : list[User]
        A list of users on the Vm
    __ticks : int
        The total lifetime counter of this server
    """

    __umax : int

    def add_users(vms : list, number : int):
        """Add users to a list of vms
        create another vm if needed
        vms : list[Vm]
            The vms to add to
        number : int
            how many users to add
        """
        users = 0
        while users < number :

            # get all not full vms
            vmsWithSpace = [
                vm for vm in vms if not vm.is_full()]

            # check to see if there are not full vms
            if len(vmsWithSpace) > 0:
                # add users to them
                for vm in vmsWithSpace:
                    vm.add_user()
                    users += 1
            else:
                # There are no vms with space, add another
                vms.append(Vm())

    def __init__(self):
        """Creates a new instance of a vm"""
        # Vm starts with 0 ticks
        self.__ticks = 0
        # Initiates an empty list of Users
        self.__users : list[User] = []

    def set_params(umax : int, ttask : int):
        """Set the class attribute umax

        Parameters
        ----------
        umax : int
            The max number of users per Vm
        ttask : int
            The cost of each task
        """

        # umax cannot be 0 or less
        if umax <= 0:
            if DEBUG:
                print("Umax cannot be lesser than 1!")
                raise ValueError
            raise ValueError

        # nor greater than 10
        if umax > 10:
            if DEBUG:
                print("Umax cannot be more than 10!")
                raise ValueError
            raise ValueError

        # umax is a valid value, assign it
        Vm.__umax = umax
        User.set_ttask(ttask)

    def is_full(self):
        """Checks if this vm is full

        Returns
        -------
        True :
            if this Vm is full
        False "
            if this Vm is not full
        """

        if len(self.__users) == Vm.__umax:
            return True
        return False

    def is_empty(self):
        """Checks if this vm is empty

        Returns
        -------
        True : 
            if this Vm is empty
        False :
            if this Vm is not empty
        """

        if len(self.__users) == 0:
            return True
        return False

    def add_user(self):
        """Adds a new user to this vm"""

        # Checks if the Vm is full before adding
        if self.is_full():
            # is the debug environment variable enabled ?
            if DEBUG:
                print(" Cannot Add another User !!!")
                raise IndexError
            raise IndexError
        # Everything seems fine ! Add user
        self.__users.append(User())

    def remove_user(self, user : User):
        """Removes a user from this machine

        Parameters
        ----------
        user : User
            The user to be removed
        """

        # Checks if there is an user to remove
        if self.is_empty():
            # is the debug environment variable enabled ?
            if DEBUG:
                print(" Cannot remove User ! Server already empty")
                raise ValueError
            raise ValueError
        # User seems removable
        self.__users.remove(user)

    def tick(self):
        """Passes a unit of time on this machine"""

        # Don't even tick if Vm is empty
        if self.is_empty():
            if DEBUG:
                print(" Oh ! Vm is empty, can't tick !")
                raise RuntimeError
            raise RuntimeError

        # get all finished users
        users = [user for user in self.__users if user.isOver()]

        # remove all processes that have been finished:
        for user in users:
            self.remove_user(user)

        # goes through all users for that machine
        for user in self.__users:
            # if the user process is not over, do it !
            if not user.isOver():
                user.tick()

        # all the user processes are done ! Tick completed !
        self.__ticks += 1
        return

    def get_ticks(self):
        return self.__ticks

    def get_users(self):
        return self.__users

    def print(self):
        """Prints the vm in a more elegant format"""
        nUsers = len(self.get_users())
        print("----", end = "")
        for user in self.__users:
            print("----", end = "")
        print("")
        print("| ", end = " ")
        for user in self.__users:
            print(str(user.ticksPassed()), end = " | ")
        print("")
        print("----", end = "")
        for user in self.__users:
            print("----", end = "")
        print("")