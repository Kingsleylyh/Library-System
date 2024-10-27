import os
import time
from datetime import datetime

def member_login():
    # Define header format for the member file
    header = "Name: Username: Password"

    # Check if member file exists or is empty, create and initialize it if necessary
    if not os.path.exists('admin/member.txt') or os.path.getsize('admin/member.txt') == 0: 
        with open('admin/member.txt', 'w') as create:
            create.write(f"{header}\n")  # Write header if file is newly created or empty

    # Open the member file in read mode to check for user credentials
    with open("admin/member.txt", 'r') as member:
        lines = member.readlines()  # Read all lines from the file

    # Prompt user for their username
    global username
    username = input("Please enter your username: ").strip()
    found = False  # Flag to check if username exists in file

    # Loop through each line after the header to verify user details
    for line in lines[1:]:
        columns = line.strip().split(":")  # Split line by colon to get individual fields
        name = columns[0].strip()  # Extract name
        saved_username = columns[1].strip()  # Extract username
        saved_password = columns[2].strip()  # Extract password

        # Check if entered username matches any saved username
        if username == saved_username:
            found = True
            count = 0  # Track number of password attempts

            # Allow up to 3 attempts for password entry
            while count < 3:
                password = input("Please enter your password: ").strip()
                if password == saved_password:  # If password matches, grant access
                    print(f"Welcome! {name}.")
                    time.sleep(1)
                    from member.memberpage import library_member_page
                    library_member_page()  # Redirect to library member page
                
                else:
                    count += 1  # Increment attempt count
                    print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")

            # If too many attempts, return to main login page
            print("Too many attempts. Returning to main login page...")
            time.sleep(3)
            from login import user_type
            user_type()  # Redirect to main login page
            return

    # If username not found, inform user and return to main login page
    if not found:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(1)
        user_type()  # Redirect to main login page



def view_loaned_book():
    # Clear the console screen (Windows: 'cls', others: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Use the global username to identify the current user
    current_user = username

    # Check if the loans file exists and is not empty
    if not os.path.exists('librarian/loans.txt'):
        print('Loans file does not exist.')
        return
    elif os.path.getsize('librarian/loans.txt') == 0:
        print('Loans file is empty.')
        return 
    else:
        try:
            # Open the loans file in read mode
            with open('librarian/loans.txt', 'r') as loans:
                lines = loans.readlines()  # Read all lines from the file

            header = lines[0].strip()  # Get and print header line
            print('Loans list:\n')
            print(header)

            # Print a line divider with the length of the longest line in the file
            longest_line = max(lines, key=len)
            print('=' * len(longest_line))

            # Loop through each line in the file (skipping the header) to find books loaned by the current user
            for line in lines[1:]:
                loaned_books_details = line.strip().split(":")
                current_user = loaned_books_details[0]  # Extract current user from line
                
                # If the current user matches the global username, print the loan details
                if current_user == username:
                    print(f"{line.strip()}")

            # Prompt the user with options after viewing the loans
            member_end_choice()

        except Exception as e:
            # Print error message if reading the file fails
            print("Error reading loans file: ", e)



def update_member_information():
    # Clear the console screen (Windows: 'cls', others: 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display update page header
    print("Welcome to update member information page:\n"
          "--------------------------------------------"
          )

    # Check if member files exist and are not empty
    if not os.path.exists('admin/memberdatabase.txt' or 'admin/member.txt'):
        print('Member is not registered.')
        return
    elif os.path.getsize('admin/memberdatabase.txt' or 'admin/member.txt') == 0:
        print('Record is empty.')
        return  
    else:
        try:
            # Initialize variables for user search
            line_index = None
            current_user = username

            # Open member file to find current user's line index
            with open("admin/member.txt","r") as member_file:
                member_lines = member_file.readlines()
                for index, line in enumerate(member_lines):
                    if current_user == line.split(":")[1].strip():
                        line_index = index  # Capture the line index of current user
                        break
            
            # If user is not found, inform and exit
            if line_index is None:
                print("User not found.")
                return

            # Read lines from both member files for updates
            with open("admin/memberdatabase.txt", "r") as member_database_file:
                member_database_lines = member_database_file.readlines()

            member_database_line = member_database_lines[line_index].strip().split(':')
            member_line = member_lines[line_index].strip().split(':')

            # Extract current member details
            stored_name_member_database, stored_age, stored_dob, stored_reg_date, stored_ic = member_database_line         
            stored_name_member, stored_username, stored_password, stored_bookcount = member_line

            # Display current details to user and provide editing options
            print(f"Name: {stored_name_member_database}\nAge: {stored_age}\nDate of Birth: {stored_dob}\n"
                  f"Registration Date: {stored_reg_date}\nIC: {stored_ic}\n")
            print("1. Name")
            print("2. Age")
            print("3. Date of Birth")
            print("4. Registration Date")
            print("5. IC")
            print("6. All\n")

            # Initialize variables to store new input values
            new_name = stored_name_member_database
            new_age = stored_age
            new_dob = stored_dob
            new_reg_date = stored_reg_date
            new_ic = stored_ic

            # Take input for the field to edit
            choice = input("What would you like to edit? ").strip()

            # Based on choice, validate and take new input for each field
            if choice == "1":
                while True:
                    new_name = input("Enter new name: ").strip()
                    if not new_name:
                        print("Name cannot be empty.")
                    elif not all(char.isalpha() or char.isspace() for char in new_name):
                        print("Input cannot contain numbers or special characters.")
                    else:
                        break

            elif choice == "2":
                while True:
                    new_age = input("Enter new age: ").strip()
                    if not new_age:
                        print("Input cannot be empty.")
                    elif not new_age.isdigit():
                        print("Input must only contain numbers.")
                    elif " " in new_age:
                        print("Input cannot contain spaces.")
                    else:
                        break

            elif choice == "3":
                while True:
                    new_dob = input("Enter new date of birth: ").strip()
                    if not new_dob:
                        print("Input cannot be empty.")
                    try:
                        dob_date = datetime.strptime(new_dob, "%Y-%m-%d")
                        if dob_date <= datetime.now(): 
                            break
                        else:
                            print("The date cannot be in the future.")
                    except ValueError:
                        print("Invalid date format. Please enter date as YYYY-MM-DD.")

            elif choice == "4":
                while True:
                    new_reg_date = input("Enter new registration date: ").strip()
                    if not new_reg_date:
                        print("Input cannot be empty.")
                    try:
                        reg_date = datetime.strptime(new_reg_date, "%Y-%m-%d")
                        if reg_date <= datetime.now(): 
                            break
                        else:
                            print("The date cannot be in the future.")
                    except ValueError:
                        print("Invalid date format. Please enter date as YYYY-MM-DD.")

            elif choice == "5":
                while True:
                    new_ic = input("Enter new IC: ").strip()
                    if not new_ic:
                        print("Input cannot be empty.")
                    elif " " in new_ic:
                        print("Input cannot contain spaces.")
                    elif new_ic.isdigit() and len(new_ic) == 12:
                        break
                    else:
                        print("Invalid IC. Please enter a valid numeric value.")

            elif choice == "6":
                # Update all fields if "All" option is selected
                new_name = input("Enter new name: ").strip()
                new_age = input("Enter new age: ").strip()
                new_dob = input("Enter new date of birth: ").strip()
                new_reg_date = input("Enter new registration date: ").strip()
                new_ic = input("Enter new IC: ").strip()

            else:
                print("Invalid option.")
                member_end_choice()

            # Update the lines with new values in both member files
            member_database_lines[line_index] = f"{new_name}:{new_age}:{new_dob}:{new_reg_date}:{new_ic}\n"
            member_lines[line_index] = f"{new_name}:{stored_username}:{stored_password}:{stored_bookcount}\n"

            # Write updated lines back to member files
            with open("admin/memberdatabase.txt", "w") as member_database_file:
                member_database_file.writelines(member_database_lines)              

            with open("admin/member.txt", "w") as member_file:
                member_file.writelines(member_lines) 

            print("Member information updated successfully.")   

            member_end_choice()  # Prompt end options
            return

        except Exception as e:
            print("Error reading member database file: ", e)



def search_catalogue():
    # Check if the catalogue file exists and is not empty
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue does not exist.')
        return
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue is empty.')
        return
    else:
        # Open and read the catalogue file
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines() 

        # Prompt user for a search term and format it for a case-insensitive search
        search_term = input('Please enter your search term: ')
        search_term = search_term.lower().strip()

        found_books = []  # List to store matching books
        
        # Loop through each line in the catalogue (excluding header)
        for line in lines[1:]:
            lower_book_details = line.strip().lower()  # Convert book details to lowercase for matching
            normal_book_details = line.strip()  # Original format for displaying

            # Check if the search term is in the book details
            if search_term in lower_book_details:
                found_books.append(normal_book_details)  # Append original format if match is found
        
        # Return header and list of found books
        return lines[0], found_books



def search_display_catalogue_books():
    # Clear console screen for a clean display
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to search book page:")

    # Call the search_catalogue function to get header and search results
    header, found_books = search_catalogue()
    
    # If matching books are found, display the results
    if found_books:
        print(f'Found {len(found_books)} book(s):')
        print(header.strip())  # Display header line
        print('=' * len(header.strip()))  # Divider line

        # Enumerate through found books, starting index at 1
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")  # Display each found book with index
        
        member_end_choice()  # Option to proceed after displaying results

    else:
        # Inform user if no matches were found
        print("No books found matching your search term.")
        member_end_choice()

    
    
def member_end_choice():
    # Import necessary functions from other modules
    from login import logout
    from member.memberpage import library_member_page

    # Loop to handle the user's end choice
    while True:
        # Prompt user to continue with other functions or log out
        end_choice = input("\nDo you want to carry out other functions? (y/n) ").strip().lower()
        
        if end_choice == 'y':
            # If yes, return to the member's main page
            library_member_page()
        
        elif end_choice == 'n':
            # If no, thank the user and log them out
            print("Thanks for visiting. Hope to see you again!")
            logout()
        
        else:
            # Prompt for valid input if choice is invalid
            print("Invalid choice. Please choose 'y' or 'n'.")



"""def main():
    member_login()
    view_loaned_book()
    update_member_information()
    search_catalogue()
    search_display_catalogue_books()
    member_end_choice()

if __name__ == "__main__":
    main()"""