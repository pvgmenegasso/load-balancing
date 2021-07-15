""" This module parses input in the following format:
1st line     = ttask value
2nd line     = umax
3rd-nth line = new users per tick

Where:
ttask = the number of ticks for each task
umax  = max number of simultaneous users 
tick  = basic time unit for the simulation
"""

def parse_input(file : str):
    """
    Returns
    -------
    ttask, umax, usersPerTick : int, int, list[int]
    """

    stream = open(file)

    ttask = int(stream.readline().strip())
    umax = int(stream.readline().strip())

    usersPerTick : list[int]= []

    for line in stream.readlines():
        usersPerTick.append(int(line.strip(" ")))

    stream.close()

    return ttask, umax, usersPerTick