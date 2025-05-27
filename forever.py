# About this File:
# forver takes an argument and starts the process that runs forever in the background

# Code explanation for forever.py

# Takes a singe argument
# Prints message indicating it started
# Runs an infinite loop,-> a long running background process

# issue : the process does't keep running in the backgrund the process is terminated 
# as soon as we start the process 
# resolution syntax fixed on line 15

import sys  # Import sys to access command-line arguments
import time  # Import time for sleep calls

if __name__ == "__main__":  # Ensure this block runs only when the script is executed directly
    # Check if an argument is provided, use it; otherwise, use a default value

    if len(sys.argv) > 1:  # Check if there's at least one argument after the script name
        arg = sys.argv[1]  # Get the first command-line argument and assign to 'arg'

    else:  # If no argument provided
        arg = "default"  # Assign 'default' as the fallback value

    print(f"Started forever with argument: {arg}")  # Print a message with the argument used
    
    while True:  # Begin an infinite loop to keep the program running
        time.sleep(1)  # Sleep for 1 second in each iteration to minimize CPU usage



