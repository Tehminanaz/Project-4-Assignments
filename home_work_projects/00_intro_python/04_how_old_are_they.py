def main():
    anton = 21  # Anton's age is 21
    beth = anton + 6  # Beth is 6 years older than Anton
    chen = beth + 20  # Chen is 20 years older than Beth
    drew = chen + anton  # Drew is Chen's age plus Anton's age
    ethan = chen  # Ethan is the same age as Chen

    # Printing their names and ages
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
