PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
  
    user_input = input(f"{PROMPT}: ")
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()





# def main():
#     # 👇 Prompt using f-string, simple input
#     prompt = "What do you want? "
    
#     # 👇 Variables for demonstration
#     attendee_name = "Tehmina"
#     course = "MCP 2025"
#     version = 3.14159
#     users = 1200000
#     accuracy = 0.97654
#     completed_modules = 7
#     total_modules = 10

#     # 👇 Joke string with multiple f-string formatting and expressions
#     joke = f"""
# Hey {attendee_name}! 👩‍💻

# Here's a joke for you:

# At {course}, a student built an agent using the OpenAI SDK v{version:.2f}.
# It became so smart, it helped {users:,} developers — with {accuracy:.1%} accuracy!

# Student: "Agent, I just wanted a print statement!"
# Agent: "Relax... I’ve already submitted your assignment, emailed your instructor, 
# and enrolled you in {total_modules - completed_modules} more modules 😄"

# Keep up the great work, {attendee_name}! You're {completed_modules / total_modules:.0%} done!
# """

#     # 👇 If not asking for joke
#     sorry = "Sorry, I only tell jokes. Try asking for a 'joke' 😅"

#     # 👇 Input with .strip() & .lower() for clean comparison
#     user_input = input(prompt).strip().lower()

#     # 👇 Check if user said "joke"
#     if "joke" in user_input:
#         print(joke)
#     else:
#         print(sorry)

# if __name__ == "__main__":
#     main()






