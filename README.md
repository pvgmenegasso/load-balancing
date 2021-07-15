# load-balancing

This package simulates a load-balancing environment in python

# running

Execute the script ./test.sh to activate python venv and run tests

# Project Structure:

* .venv  
    Python3 virtual environment
* load_balancing  
    Main project folder
    * main.py  
        Main code for the module
    * io  
        Directory that contains I/O related code and files
        * input.py  
            Process input file
        * output.py  
            Parses result into file
        * input.txt  
            File containing input example
        * output.txt
            File containing output example
    * server  
        Directory containing code implementing a vm, a user and a server with load balancing capabilities
        * vm.py  
            Implements the User and Vm classes
        * load_balancer.py  
            Implements the Server class along with it's functions
    * tests  
        Directory containing tests
        * test_vm.py  
            Tests for the vm.py file
        * test_load_balancing.py  
            Tests for the load_balancer file
        * test_input.py
            Tests file input
        * test main.py
            Try tu run the full project
    * requirements.txt  
        Project requirements
* test.sh  
    Activate virtual environment, install packages and run tests
  
