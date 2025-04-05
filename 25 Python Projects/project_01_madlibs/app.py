# Define a function named madlib
def madlib():
    # Ask the user to input a body part (e.g., eyes, hands)
    body_part = input("Body Part: ")
    
    # Ask the user to input a verb (an action word like run, build)
    verb = input("Verb: ")
    
    # Ask the user to input 5 adjectives (describing words like smart, fast)
    adj1 = input("Adjective: ")
    adj2 = input("Adjective: ")
    adj3 = input("Adjective: ")
    adj4 = input("Adjective: ")
    adj5 = input("Adjective: ")
    
    # Ask the user to input 2 nouns (naming words like computer, idea)
    noun1 = input("Noun: ")
    noun2 = input("Noun: ")
    
    # Ask the user to input 2 plural nouns (more than one, like apps, ideas)
    noun_plural_1 = input("Noun (plural): ")
    noun_plural_2 = input("Noun (plural): ")

    # Create the madlib paragraph using the user's inputs
    madlib = f"Stepping into Quarter 3 at GIAIC is an exciting and {adj1} milestone in my learning journey. \
With a vision in my {body_part} and an eagerness to {verb}, I am ready to embrace new challenges and opportunities. \
This phase is not just about gaining knowledge but about transforming ideas into {noun_plural_1}. \
By developing a {adj2} mindset, I aim to master cutting-edge technologies, enhance my {adj3} problem-solving skills, \
and contribute meaningfully to the digital world. From building {adj4} applications to exploring {noun1} and {noun2}, \
each step will bring me closer to my goals. The path ahead is {adj5}, and I am prepared to navigate it with passion and perseverance."

    # Print the final madlib story
    print(madlib)

# Call the function to run the madlib program
madlib()
