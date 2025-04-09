def madlib():
    # Ask the user for various inputs to fill in the blanks
    body_part = input("Body Part: ")  # User inputs a body part (e.g., 'head')
    verb = input("Verb: ")  # User inputs a verb (e.g., 'run')
    adj1 = input("Adjective: ")  # User inputs an adjective (e.g., 'exciting')
    adj2 = input("Adjective: ")  # User inputs an adjective (e.g., 'innovative')
    adj3 = input("Adjective: ")  # User inputs an adjective (e.g., 'creative')
    adj4 = input("Adjective: ")  # User inputs an adjective (e.g., 'functional')
    adj5 = input("Adjective: ")  # User inputs an adjective (e.g., 'challenging')
    noun1 = input("Noun: ")  # User inputs a noun (e.g., 'project')
    noun2 = input("Noun: ")  # User inputs a noun (e.g., 'team')
    noun_plural_1 = input("Noun (plural): ")  # User inputs a plural noun (e.g., 'ideas')
    noun_plural_2 = input("Noun (plural): ")  # User inputs another plural noun (e.g., 'skills')

    # Creating a fun madlib using the inputs provided by the user
    madlib = f"Stepping into Quarter 3 at GIAIC is an exciting and {adj1} milestone in my learning journey. \
With a vision in my {body_part} and an eagerness to {verb}, I am ready to embrace new challenges and opportunities. \
This phase is not just about gaining knowledge but about transforming ideas into {noun_plural_1}. \
By developing a {adj2} mindset, I aim to master cutting-edge technologies, enhance my {adj3} problem-solving skills, \
and contribute meaningfully to the digital world. From building {adj4} applications to exploring {noun1} and {noun2}, \
each step will bring me closer to my goals. The path ahead is {adj5}, and I am prepared to navigate it with passion and perseverance."

    # Print the madlib result
    print(madlib)

# Call the function to run the madlib game
madlib()
