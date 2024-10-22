# PAGE TO CHOOSE USER TYPE
import os
import time
from admin.adminpage import system_admin_page
from librarian.librarianpage import librarian_page

"""Menu to choose the role"""
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
            user_choice = int(input("Enter your user type (1/2/3): ")) # REQUEST INPUT FROM USER
            if user_choice == 1:
                admin_login()
                break

            elif user_choice == 2:
                librarian_login()
                break

            elif user_choice == 3:
                from member.Member import member_login
                member_login()
                break

            else:
                print("Please choose 1, 2 or 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")



"""Admin login function"""
def admin_login():
    
    with open("admin/admin.txt", 'r') as admin:
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



"""Admin login function"""
def librarian_login():
    h1 = "LibrarianID: Name: Username: Password"

    # Create the librarian file if it doesn't exist or is empty
    if not os.path.exists('admin/librarian.txt') or os.path.getsize('admin/librarian.txt') == 0: 
        with open('admin/librarian.txt', 'w') as create:
            # Write headers to the file if it's newly created
            create.write(f"{h1}\n")
    with open("admin/librarian.txt", 'r') as librarian:
        lines = librarian.readlines()

    username = input("Please enter your username: ").strip()
    found = False

    for line in lines[1:]:
        columns = line.strip().split(":")
        name = columns[1].strip()
        saved_username = columns[2].strip()
        saved_password = columns[3].strip()

        if username == saved_username:
            found = True
            count = 0

            while count < 3:
                password = input("Please enter your password: ").strip()
                if password == saved_password:
                    print(f"Welcome! {name}.")
                    librarian_page()
                    return
                    
                else:
                    count += 1
                    print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")

            print("Too many attempts. Returning to main login page...")
            time.sleep(3)
            user_type()

    if not found:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(3)
        user_type()






"""Logout function"""
def logout():
    print("Logging out...")
    time.sleep(2) 
    user_type()