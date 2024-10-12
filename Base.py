# PAGE TO CHOOSE USER TYPE
import os
def user_type():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print(
        "Welcome to Brickfields Kuala Lumpur Community Library login page:\n"
        "Please Select A User Type:\n"
        "   1. System Administrator\n"
        "   2. Librarian\n"
        "   3. Library Member"
    )
    while True:
        try:
            user_choice = int(input("Enter your user type (1/2/3):")) # REQUEST INPUT FROM USER
            if user_choice == 1:
                admin_login()
            elif user_choice == 2:
                librarian_login()
            elif user_choice == 3:
                member_login()
            else:
                print("Please choose 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

import time
from admin.adminpage import system_admin_page
def admin_login():
    with open("admin.txt", 'r') as info:
        lines = info.readlines()

        if len(lines) >= 4:
            name_line = lines[1].strip()
            username_line = lines[2].strip()
            password_line = lines[3].strip()
        else:
            return

        saved_username = username_line[16:]
        saved_password = password_line[10:]

    username = input("Please enter your username: ").strip()

    # Check if the entered credentials match the registered info
    if username == saved_username:
        count = 0
        while True:
            password = input("Please enter your password: ").strip()
            if password == saved_password and count < 3:
                print(f"Welcome!{name_line[11:]}.")
                system_admin_page()
            elif count >= 3:
                print("Too many attempts. Returning to main login page...")
                time.sleep(3)
                user_type()
            else:
                count +=1
                print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")
    else:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(3)
        user_type()



import time
from admin.adminpage import system_admin_page
def admin_login():
    with open("admin.txt", 'r') as admin:
        lines = admin.readlines()

        if len(lines) >= 4:
            name_line = lines[1].strip()
            username_line = lines[2].strip()
            password_line = lines[3].strip()
        else:
            return

        saved_username = username_line[16:]
        saved_password = password_line[10:]

    username = input("Please enter your username: ").strip()

    # Check if the entered credentials match the registered info
    if username == saved_username:
        count = 0
        while True:
            password = input("Please enter your password: ").strip()
            if password == saved_password and count < 3:
                print(f"Welcome!{name_line[11:]}.")
                system_admin_page()
            elif count >= 3:
                print("Too many attempts. Returning to main login page...")
                time.sleep(3)
                user_type()
            else:
                count +=1
                print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")
    else:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(3)
        user_type()


from librarian.librarianpage import librarian_page
def librarian_login():
    with open("librarian.txt", 'r') as librarian:
        lines = librarian.readlines()

        if len(lines) >= 4:
            name_line = lines[1].strip()
            username_line = lines[2].strip()
            password_line = lines[3].strip()
        else:
            return

        saved_username = username_line[16:]
        saved_password = password_line[10:]

    username = input("Please enter your username: ").strip()

    # Check if the entered credentials match the registered info
    if username == saved_username:
        count = 0
        while True:
            password = input("Please enter your password: ").strip()
            if password == saved_password and count < 3:
                print(f"Welcome!{name_line[11:]}.")
                librarian_page()
            elif count >= 3:
                print("Too many attempts. Returning to main login page...")
                time.sleep(3)
                user_type()
            else:
                count +=1
                print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")
    else:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(3)
        user_type()


def member_login():
    with open('member.txt', 'r') as member:
        lines = member.readlines()



def main():
    user_type()

if __name__ == "__main__":
    main()