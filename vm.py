"""This module defines a VM for usage in the simulation environment"""

from os import environ

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
    

class Vm():
    """Defines a Vm object which simulates a virtual server in a 
    cloud environment

    Class Attributes
    ----------
    __umax : int
        Maximum number of users per Vm

    Attributes
    ----------
    users : list[User]
        A list of users on the Vm
    __ticks : int
        The total lifetime counter of this server


    Methods
    ------- 
    tick():
        Run a tick on this machine
    add_user():
        Adds a user on this machine
    remove_user(User):
        Remove a user on this machine
    is_full() : bool
        Returns true if this vm is full
    is_empty() : bool, int
        Returns true if this Vm has no users
        Also returns ticks used
    """

    __umax : int

    def __init__(self):
        """Creates a new instance of a vm"""
        # Vm starts with 0 ticks
        self.__ticks = 0
        # Initiates an empty list of Users
        self.__users : list[User] = []

    def set_umax(umax : int):
        """Set the class attribute umax

        Parameters
        ----------
        umax : int
            The max number of users per Vm
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

    def is_full(self):
        """Checks if this vm is full

        Returns
        -------
        True
            if this Vm is full
        False
            if this Vm is not full
        """
        if len(self.__users) == Vm.__umax:
            return True
        return False

    def is_empty(self):
        """Checks if this vm is empty

        Returns
        -------
        True, int : Number of ticks
            if this Vm is empty
        False
            if this Vm is not empty
        """
        print(self.__users)
        if len(self.__users) == 0:
            return True, self.__ticks
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
        new = User()
        self.__users.append(new)

    def remove_user(self, user : int):
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
        self.__users.remove(self.__users.pop(user))

    def tick(self):
        """Passes a unit of time on this machine"""

        # Don't even tick if server is empty
        if self.is_empty():
            if DEBUG:
                print(" Oh ! Server is empty, can't tick !")
                raise RuntimeError
            raise RuntimeError

        userIndexes = []

        # goes through all users for that machine
        for user in self.__users:
            # if the user process is not over, do it !
            if not user.isOver():
                user.tick()
            else:
                # The user process is over Save it's index
                userIndexes.append(self.__users.index(user))

        # remove all processes that have been finished:
        for index in userIndexes:
            self.remove_user(index)

        # all the user processes are done ! Tick completed !

        self.__ticks += 1
        return