import os
import re

FILE_NAME = "users.txt"

def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def username_exists(username):
    if not os.path.exists(FILE_NAME):
        return False

    with open(FILE_NAME, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")

            if username == stored_username:
                return True

    return False

def register():
    print("\n===== USER REGISTRATION =====")

    username = input("Enter Username: ")

    if username_exists(username):
        print("Username already exists!")
        return

    password = input("Enter Password: ")

    strength = password_strength(password)

    print("Password Strength:", strength)

    if strength == "Weak":
        print("Please choose a stronger password.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration Successful!")

def login():
    print("\n===== USER LOGIN =====")

    if not os.path.exists(FILE_NAME):
        print("No registered users found.")
        return

    attempts = 3

    while attempts > 0:

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        success = False

        with open(FILE_NAME, "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")

                if username == stored_username and password == stored_password:
                    success = True
                    break

        if success:
            print("\nLogin Successful!")
            print("Welcome,", username)
            return

        attempts -= 1

        print("Invalid Username or Password!")
        print("Remaining Attempts:", attempts)

    print("Account Locked. Too many failed attempts.")

def view_users():
    print("\n===== REGISTERED USERS =====")

    if not os.path.exists(FILE_NAME):
        print("No users found.")
        return

    with open(FILE_NAME, "r") as file:
        users = file.readlines()

    if len(users) == 0:
        print("No users registered.")
        return

    count = 1

    for user in users:
        username = user.strip().split(",")[0]
        print(count, ".", username)
        count += 1

def main():

    while True:

        print("\n==============================")
        print("   ADVANCED LOGIN SYSTEM")
        print("==============================")
        print("1. Register")
        print("2. Login")
        print("3. View Registered Users")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            view_users()

        elif choice == "4":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid Choice! Please try again.")

main()