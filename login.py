import os
import time
from admin.adminpage import system_admin_page
from librarian.librarianpage import librarian_page

"""Menu to choose the role"""
def user_type():
    # Clear the terminal screen for better visibility of the login page
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)  # Pause for a moment before displaying the login options

    # Display the welcome message and user type selection options
    print(
        "Welcome to Brickfields Kuala Lumpur Community Library login page:\n"
        "Please Select A User Type:\n"
        "   1. System Administrator\n"
        "   2. Librarian\n"
        "   3. Library Member"
    )

    while True:
        try:
            # Prompt the user to enter their user type
            user_choice = int(input("Enter your user type (1/2/3): "))  # REQUEST INPUT FROM USER
            
            # Handle the selection of the System Administrator
            if user_choice == 1:
                admin_login()  # Call the admin login function
                break  # Exit the loop after processing the login

            # Handle the selection of the Librarian
            elif user_choice == 2:
                librarian_login()  # Call the librarian login function
                break  # Exit the loop after processing the login

            # Handle the selection of the Library Member
            elif user_choice == 3:
                from member.Member import member_login  # Import member login function
                member_login()  # Call the member login function
                break  # Exit the loop after processing the login

            # Handle invalid choices
            else:
                print("Please choose 1, 2 or 3.")  # Prompt user to select a valid option

        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-integer inputs



"""Admin login function"""
def admin_login():
    # Open the admin file to read admin credentials
    with open("admin/admin.txt", 'r') as admin:
        lines = admin.readlines()  # Read all lines from the admin file

        # Check if there are enough lines in the file to extract credentials
        if len(lines) >= 4:
            name_line = lines[1].strip()  # Get the name line and strip whitespace
            username_line = lines[2].strip()  # Get the username line
            password_line = lines[3].strip()  # Get the password line
        else:
            return  # Exit the function if the file does not have sufficient data

        # Extract the saved username and password from the lines
        saved_username = username_line[16:]  # Extract username starting from the 17th character
        saved_password = password_line[10:]  # Extract password starting from the 11th character

    username = input("Please enter your username: ").strip()  # Prompt for username input

    # Check if the entered username matches the registered username
    if username == saved_username:
        count = 0  # Initialize counter for password attempts
        while True:
            password = input("Please enter your password: ").strip()  # Prompt for password input
            # Check if the entered password is correct
            if password == saved_password and count < 3:
                print(f"Welcome! {name_line[11:]}.")  # Welcome message for the admin
                system_admin_page()  # Navigate to the admin page
                return  # Exit the function after successful login

            elif count >= 3:
                print("Too many attempts. Returning to main login page...")  # Notify of too many attempts
                time.sleep(3)  # Wait before returning to the main login page
                user_type()  # Navigate back to user type selection
                return  # Exit the function

            else:
                count += 1  # Increment the failed attempt counter
                print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")  # Notify user of remaining attempts

    else:
        print("User doesn't exist. Returning to main login page...")  # Notify if the username does not exist
        time.sleep(3)  # Wait before returning to the main login page
        user_type()  # Navigate back to user type selection



"""Admin login function"""
def librarian_login():
    # Header for librarian information in the format: LibrarianID: Name: Username: Password
    h1 = "LibrarianID: Name: Username: Password"

    # Check if the librarian file exists or is empty; if so, create it
    if not os.path.exists('admin/librarian.txt') or os.path.getsize('admin/librarian.txt') == 0: 
        with open('admin/librarian.txt', 'w') as create:
            # Write the header line to the file upon creation
            create.write(f"{h1}\n")

    # Open the librarian file for reading
    with open("admin/librarian.txt", 'r') as librarian:
        lines = librarian.readlines()  # Read all lines from the file

    username = input("Please enter your username: ").strip()  # Prompt user for username
    found = False  # Flag to check if the username exists

    # Iterate through each line of the file to find the matching username
    for line in lines[1:]:  # Skip the header line
        columns = line.strip().split(":")  # Split the line into components
        name = columns[1].strip()  # Extract the librarian's name
        saved_username = columns[2].strip()  # Extract the saved username
        saved_password = columns[3].strip()  # Extract the saved password

        if username == saved_username:  # Check if the entered username matches
            found = True  # Set found flag to true
            count = 0  # Initialize password attempt counter

            # Allow up to 3 attempts to enter the correct password
            while count < 3:
                password = input("Please enter your password: ").strip()  # Prompt for password
                if password == saved_password:  # Check if the entered password is correct
                    print(f"Welcome! {name}.")  # Welcome message for the librarian
                    librarian_page()  # Navigate to the librarian's page
                    return  # Exit the function after successful login
                    
                else:
                    count += 1  # Increment the count of failed attempts
                    print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")

            print("Too many attempts. Returning to main login page...")  # Notify user of too many attempts
            time.sleep(3)  # Wait before returning to the main login page
            user_type()  # Navigate back to user type selection

    # If the username was not found in the file
    if not found:
        print("User doesn't exist. Returning to main login page...")  # Notify user
        time.sleep(3)  # Wait before returning to the main login page
        user_type()  # Navigate back to user type selection



"""Logout function"""
def logout():
    print("Logging out...")
    time.sleep(2) 
    user_type()