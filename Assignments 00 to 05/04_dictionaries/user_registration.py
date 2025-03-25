from hashlib import sha256
import os

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def register_user(file_path):
    email = input("Enter your email to register: ").strip()
    password = input("Enter your password: ").strip()
    hashed_pw = hash_password(password)

    # Check if email already exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                stored_email, _ = line.strip().split(",")
                if stored_email == email:
                    print("This email is already registered.")
                    return

    with open(file_path, "a") as f:
        f.write(f"{email},{hashed_pw}\n")
    print("Registration successful!")

def load_logins(file_path):
    stored_logins = {}
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            for line in f:
                email, pw_hash = line.strip().split(",")
                stored_logins[email] = pw_hash
    return stored_logins

def login(file_path):
    stored_logins = load_logins(file_path)
    email = input("Enter your email: ").strip()
    password_to_check = input("Enter your password: ").strip()

    if email in stored_logins and stored_logins[email] == hash_password(password_to_check):
        print("Login successful!")
    else:
        print("Login failed! Incorrect email or password.")

def main():
    file_path = "logins.txt"
    while True:
        print("\nSelect an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            register_user(file_path)
        elif choice == "2":
            login(file_path)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == '__main__':
    main()


#  How it works:
# All user data (email and hashed passwords) is stored in logins.txt.

# On registration, it appends new email-password hash lines to this file.

# On login, it reads the file and checks if the hashed password matches.

