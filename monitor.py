# About this file:
# Monitor.py is a given program and restars it if it stops running 

# Code explanation for monitor.py

# Takes 2 arguments to program monitor (forever.py)
# and the argument to pass
# Starts the specified program as a subprocess
# Checks the subprocess repeatedly to make sure it's  still running
# if the subprocess is killed, it restarts it automatically
# It also runs the logic in the backend.


import sys
import subprocess
import time

if __name__ == "__main__": #this checks if the script is being run as the main program
    program = sys.argv[1] # Read the first command-line arg and save a 'arg'
    arg = sys.argv # Reads the argument to pass to the moniter program
    process = None # Initialize the process variable as Name
    while True: # starting an infinite loop
        if process is None or process.poll()is not None: #if the process is not running
            print(f"Starting{program}") # prints when starts/restarts
            process = subprocess.Popen(['python3',sys.argv[1]]) # starts suprocess
            time.sleep(1) # waits for 1 sec before checking agian 

# TODO:need to us hashmaps to monitor and restart processses
            # print what forver process are bring printed
            