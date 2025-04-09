# Gravity constants for different planets
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Ask the user to input their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Ask the user to input the name of a planet
    planet = input("Enter a planet: ")

    # Check the planet entered by the user and assign the corresponding gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        # If the planet entered is not found above, it must be Neptune
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant

    # Round the planetary weight to 2 decimal places
    rounded_planetary_weight = round(planetary_weight, 2)

    # Display the equivalent weight on the selected planet
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))

# Call the main function when the script is executed
if __name__ == '__main__':
    main()
