import os
import time
from datetime import datetime, timedelta

def member_login():
    h2 = "Name: Username: Password"
    if not os.path.exists('admin/member.txt') or os.path.getsize('admin/member.txt') == 0: 
        with open('admin/member.txt', 'w') as create:
            create.write(f"{h2}\n")    

    with open("admin/member.txt", 'r') as member:
        lines = member.readlines()

    global username
    username = input("Please enter your username: ").strip()
    found = False

    for index, line in enumerate(lines[1:]):
        columns = line.strip().split(":")
        name = columns[0].strip()
        saved_username = columns[1].strip()
        saved_password = columns[2].strip()

        if username == saved_username:
            found = True
            count = 0
            line_index = index  # Store the index of the line where the username is found

            while count < 3:
                password = input("Please enter your password: ").strip()
                if password == saved_password:
                    print(f"Welcome! {name}.")
                    time.sleep(1)
                    from member.memberpage import library_member_page
                    library_member_page()
                    
                else:
                    count += 1
                    print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")

            print("Too many attempts. Returning to main login page...")
            time.sleep(1)
            from login import user_type
            user_type()
            return

    if not found:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(1)
        user_type()

    return line_index

def view_loaned_book():

    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')
    
    current_user = username

    # Check if the loans file exists
    if not os.path.exists('librarian/loans.txt'):
        print('Loans file does not exist.')
        return

    # Check if the loans file is empty
    elif os.path.getsize('librarian/loans.txt') == 0:
        print('Loans file is empty.')
        return 
    
    else:
        try:
            # Read all lines from the loans file
            with open('librarian/loans.txt', 'r') as loans:
                lines = loans.readlines() # Load all lines into memory

            # Extract and print the header (first line)
            header = lines[0].strip() # Extract and clean the header (removes trailing spaces/newlines)
            print('Loans list:\n')
            print(header) # Print the header as the title of the loans

            # Print a separator line based on the longest line in the file
            longest_line = max(lines, key=len) # Find the longest line in the file to create a consistent separator
            print('=' * len(longest_line)) # Print the separator (equal sign) based on longest line length

            for line in lines[1:]:  # Skip the header line
                loaned_books_details = line.strip().split(":")
                current_user = loaned_books_details[0]
                if current_user == username:
                    print(f"{line.strip()}")

                    member_end_choice()

        except Exception as e:
            # Handle any errors during file reading
            print("Error reading loans file: ", e)


# Update member information
def update_member_information():
    # Clear terminal history
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to update member information page:")

    # Check if the file exists
    if not os.path.exists('admin/member.txt'):
        print('Member is not registered.')
        member_end_choice()
        return

    # Check if the file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        member_end_choice()
        return
    
    else:
        line_index = member_login()

        try:
            with open("admin/memberdatabase.txt", "r") as member_database_file:
                member_database_lines = member_database_file.readlines()

            with open('admin/member.txt', 'r') as member_file:
                member_lines = member_file.readlines()

            member_database_line = member_database_lines[line_index].strip().split(':')
            member_line = member_lines[line_index].strip().split(':')
            

            for index, line in enumerate(member_database_lines):
                # Keep the header as it is
                if index == 0:
                    edited_profile_memberdatabase.append(line)  # Append the header unchanged
                    continue  # Skip to the next iteration

            for index, line in enumerate(member_lines):
                # Keep the header as it is
                if index == 0:
                    edited_profile_member.append(line)  # Append the header unchanged
                    continue  # Skip to the next iteration

                edited_profile_memberdatabase = []
                edited_profile_member = []
            for memberdatabase_credentials in member_database_lines[1:]:
                stored_name_member_database, stored_age, stored_dob, stored_reg_date, stored_ic = memberdatabase_credentials.strip().split(":")
            
            for member_credentials in member_lines[1:]:
                stored_name_member, stored_username, stored_password, stored_bookcount = member_credentials.strip().split(":")
                
                print(f"Name: {stored_name_member_database}\nAge: {stored_age}\nDate of Birth: {stored_dob}\nRegistration Date: {stored_reg_date}\nIC: {stored_ic}\n")
                print("1. Name")
                print("2. Age")
                print("3. Date of Birth")
                print("4. Registration Date")
                print("5. IC")
                print("6. All\n")
                choice = input("What would you like to edit? ").strip()

                new_name = stored_name_member_database
                new_name = stored_name_member
                new_age = stored_age
                new_dob = stored_dob
                new_reg_date = stored_reg_date
                new_ic = stored_ic

                if choice == "1":
                    while True:
                        new_name = input("Enter new name: ").strip()                          
                        # Ensure the name is not empty, contains no spaces, and only consists of alphabets.
                        if not new_name:
                            print("Input cannot be empty.")
                        elif not new_name.isalpha():
                            print("Input can only contain alphabets.")
                        elif " " in new_name:
                            print("Input cannot contain spaces.")
                            break

                elif choice == "2":
                    while True:
                        new_age = input("Enter new age: ").strip()                                                                       
                        # Ensure the age is not empty, contains no spaces, and only consists of numbers
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
                        # Ensure the date of birth is not empty, contains no spaces, and only consists of digits and hyphens
                        if not new_dob:
                            print("Input cannot be empty.")
                        elif " " in new_dob:
                            print("Input cannot contain spaces.")
                        elif not new_dob.replace('-', '').isdigit():
                            print("Input must only contain numbers and hyphens.")
                        else:
                            break

                elif choice == "4":
                    while True:
                        new_reg_date = input("Enter new registration date: ").strip()                                               
                        # Ensure the registration date is not empty, contains no spaces, and only consists of digits and hyphens
                        if not new_reg_date:
                            print("Input cannot be empty.")
                        elif " " in new_reg_date:
                            print("Input cannot contain spaces.")
                        elif not new_reg_date.replace('-', '').isdigit():
                            print("Input must only contain numbers and hyphens.")
                        else:
                            break

                elif choice == "5":
                    while True:
                        new_ic = input("Enter new ic: ").strip()                    
                        # Ensure the ic is not empty, contains no spaces, and only consists of numbers
                        if not new_ic:
                            print("Input cannot be empty.")
                        elif not new_ic.isdigit():
                            print("Input must only contain numbers.")
                        elif " " in new_ic:
                            print("Input cannot contain spaces.")
                        else:
                            break

                elif choice == "6":
                    new_name = input("Enter new name: ").strip()
                    new_age = input("Enter new age: ").strip()
                    new_dob = input("Enter new dob: ").strip()
                    new_reg_date = input("Enter new registration date: ").strip()
                    new_ic = input("Enter new ic: ").strip()

                else:
                    print("Invalid option.")
                    # continue

                edited_profile_memberdatabase.append(f"{new_name}:{new_age}:{new_dob}:{new_reg_date}:{new_ic}\n")
                edited_profile_member.append(f"{new_name}:{stored_username}:{stored_password}:{stored_bookcount}\n")
                print("Member information updated succesfully.")

                with open("admin/memberdatabase.txt", "w") as member_database_file:
                    member_database_file.writelines(edited_profile_memberdatabase)              

                with open("admin/member.txt", "w") as member_file:
                    member_file.writelines(edited_profile_member)    

            member_end_choice()
            return

        except Exception as e:
            print("Error reading memberdatabase file: ", e)

# Search book
def search_catalogue():
    # Check if catalogue file exists 
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue does not exist.')
        return
    
    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue is empty.')
        return

    else:
        # Read all lines from the catalogue file
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines() 

        # Get search term from user input and normalize it (convert to lowercase and remove extra spaces)
        search_term = input('Please enter your search term: ')
        search_term = search_term.lower().strip()

        # Initialize a list to store the found books
        found_books = []
        
        # Loop through the catalogue lines (skip the first line, which is the header)
        for line in lines[1:]:
            lower_book_details = line.strip().lower()  # Convert book details to lowercase for case-insensitive search
            normal_book_details = line.strip()  # Keep the original format for display

            # Check if the search term is found in the book details
            if search_term in lower_book_details:
                found_books.append(normal_book_details)  # Add the book to the found_book list
        
        return lines[0], found_books

# Display search book result
def search_display_catalogue_books():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    # Welcome message for the search book page
    print("Welcome to search book page:")

    # Call the search_catalogue function to get the header and found books
    header, found_books = search_catalogue()
    
    # Check if any books were found
    if found_books:
        # Print the number of books found
        print(f'Found {len(found_books)} book(s):')

        # Print the header for the book list
        print(header.strip())
        # Print a separator line based on the length of the header
        print('=' * len(header.strip()))

        # Enumerate through the found books and print them with an index
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")
    
            member_end_choice()

    else:
        # If no books were found, inform the user
        print("No books found matching your search term.")
    
    



def member_end_choice():
    from login import logout
    from member.memberpage import library_member_page
    while True:
        end_choice = input("\nDo you want carry out other functions ? (y/n)")
        if end_choice.lower() == 'y':
            library_member_page()
        elif end_choice.lower() == 'n':
            print("Thanks for visiting. Hope to see you again!")
            logout()
        else:
            print("Invalid choice. Please choose y or n.")


def main():
    member_login()
    view_loaned_book(username)
    update_member_information()
    search_display_catalogue_books()
    member_end_choice()

if __name__ == "__main__":
    main()