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

    for line in lines[1:]:
        columns = line.strip().split(":")
        name = columns[0].strip()
        saved_username = columns[1].strip()
        saved_password = columns[2].strip()

        if username == saved_username:
            found = True
            count = 0

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
            from Base import user_type
            user_type()
            return

    if not found:
        print("User doesn't exist. Returning to main login page...")
        time.sleep(1)
        user_type()

    return username

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

    stored_username = username

    # Check if the file exists
    if not os.path.exists('admin/member.txt'):
        print('Member is not registered.')
        return

    # Check if the file is empty
    elif os.path.getsize('admin/member.txt') == 0:
        print('Record is empty.')
        return
    
    else:
        try:
            with open("admin/member.txt", "r") as memberfile:
                lines = memberfile.readlines()
            
            edited_profile = []
            for index, line in enumerate(lines):
                # Keep the header as it is
                if index == 0:
                    edited_profile.append(line)  # Append the header unchanged
                    continue  # Skip to the next iteration

            for credentials in lines[1:]:
                # if stored_username == username:                
                    stored_name, stored_username, stored_password, stored_bookcount = credentials.strip().split(":")
                    print(stored_username, username, stored_username == username)
                    if stored_username != username:
                        continue
                    print(f"Name: {stored_name}\nUsername: {stored_username}\nPassword: {stored_password}\nBookCount: {stored_bookcount}\n")
                    print("1. Username")
                    print("2. Password")
                    print("3. Both\n")
                    choice = input("What would you like to edit? ").strip()

                    new_username = stored_username
                    new_password = stored_password

                    if choice == "1":
                        while True:
                            new_username = input("Enter new username: ").strip()
                            # Ensure the username is not empty or only spaces
                            if new_username == "":
                                print("Input cannot be empty.")
                                continue
                            break

                    elif choice == "2":
                        while True:
                            new_password = input("Enter new password: ").strip()                                               
                            # Ensure the password is not empty or only spaces
                            if new_password == "":
                                print("Input cannot be empty.")
                                continue
                            break

                    elif choice == "3":
                        new_username = input("Enter new username: ").strip()
                        new_password = input("Enter new password: ").strip()
                    else:
                        print("Invalid option.")
                        continue

                    edited_profile.append(f"{stored_name}:{new_username}:{new_password}:{stored_bookcount}\n")
                    print("Member information edited.")

                    with open("admin/member.txt", "w") as memberfile:
                        memberfile.writelines(edited_profile)

                    member_end_choice()
                    return

        except Exception as e:
            print("Error reading member file: ", e)

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
    while True:
        end_choice = input("\nDo you want carry out other functions ? (y/n)")
        if end_choice.lower() == 'y':
            from member.memberpage import library_member_page
            library_member_page()
        elif end_choice.lower() == 'n':
            member_logout()
        else:
            print("Invalid choice. Please choose y or n.")
    

def member_logout():
    print("Thanks for visiting. Hope to see you again!")
    print("Logging out ...")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    from Base import user_type
    user_type()

def main():
    member_login()
    view_loaned_book(username)
    update_member_information()
    search_display_catalogue_books()
    member_end_choice()
    member_logout()

if __name__ == "__main__":
    main()