# Importing the 'os' module to interact with the operating system (like files and folders)
import os

# Main function where the program starts
def main():
    i = 0  # A counter variable used to create new file names
    path = ""  # The folder path where your files are located (add your folder path here)

    # Loop through all files in the given folder
    for filename in os.listdir(path):
        # Create a new file name like img0.jpg, img1.jpg, img2.jpg, etc.
        my_dest = "img" + str(i) + ".jpg"

        # Full path to the current file
        my_source = path + filename

        # Full path to the new file name
        my_dest = path + my_dest

        # Rename the file from the old name to the new name
        os.rename(my_source, my_dest)

        # Increase the counter for the next file
        i += 1

# Run the main function if this file is being executed
if __name__ == '__main__':
    main()
