import time  # Importing the time module to use time.sleep for delay

def countdown(t):
    while t:  # While the time left is greater than 0
        mins, secs = divmod(t, 60)  # Convert total seconds into minutes and seconds
        timeformat = '{:02d}:{:02d}'.format(mins, secs)  # Format the time as MM:SS
        print(timeformat, end='\r')  # Print the time in the same line (using \r to overwrite)
        time.sleep(1)  # Wait for 1 second
        t -= 1  # Decrease the time by 1 second

    print('Timer completed!')  # Once time is up, print the completion message

t = input('Enter the time in seconds: ')  # Ask user to input the countdown time in seconds
countdown(int(t))  # Call the countdown function with the inputted time
