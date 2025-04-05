# Importing the time module to use the sleep function
import time

# This function starts a countdown from the given time in seconds
def countdown(t):
    # Loop will keep running until t becomes 0
    while t:
        # divmod() breaks time into minutes and seconds
        mins, secs = divmod(t, 60)

        # Format time as MM:SS (e.g., 01:30 for 1 min 30 secs)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)

        # Print the timer on the same line (end='\r' rewrites the line)
        print(timeformat, end='\r')

        # Wait for 1 second
        time.sleep(1)

        # Decrease time by 1 second
        t -= 1

    # After the countdown ends, print this message
    print('Timer completed!')

# Ask user to enter time in seconds
t = input('Enter the time in seconds: ')

# Convert the input to integer and start the countdown
countdown(int(t))
