import os
import time

def view_loaned_book():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')  

    # Check if the catalogue file exists
    if not os.path.exists('librarian/loans.txt'):
        print('Loaned book file does not exist.')
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/loans.txt') == 0:
        print('Loaned book file is empty.')
        return 
    
    else:
        try:
            # Read all lines from the catalogue file
            with open('librarian/loans.txt', 'r') as catalogue:
                lines = catalogue.readlines() # Load all lines into memory

            # Extract and print the header (first line)
            header = lines[0].strip() # Extract and clean the header (removes trailing spaces/newlines)
            print('Loaned book list:\n')
            print(header) # Print the header as the title of the catalogue

            # Print a separator line based on the longest line in the file
            longest_line = max(lines, key=len) # Find the longest line in the file to create a consistent separator
            print('=' * len(longest_line)) # Print the separator (equal sign) based on longest line length

            # Sort books by genre (last field in each line)
            sorted_books = sorted(lines[1:], key=lambda x: x.strip().split(":")[5].lower()) # Sort alphabetically by genre
            
            # Initialize a variable to track the current genre for grouping books
            current_genre = ""
            for line in sorted_books:
                book_details = line.strip() # Clean the book details from extra spaces/newlines
                genre = book_details.split(':')[5] # Extract the genre from the 6th field of each line
                genre_lower = genre.lower() # Convert genre to lowercase for comparison

                # If a new genre is encountered, print it as a header
                if genre_lower != current_genre:
                    current_genre = genre_lower # Update the current genre to the new one
                    print(f"\n{genre}:") # Print the genre as a section header
                
                # Print the book details under the current genre
                print(f"{book_details}")

        except Exception as e:
            # Handle any errors during file reading
            print("Error reading loans file: ", e)

# Update member information
def update_member_information():
    # Clear terminal history
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the file exists
    if not os.path.exists('admin/memberdatabase.txt'):
        print('Member is not registered.')
        return

    # Check if the file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        return
    
    else:
        try:
            username = input("Enter Name: ")
            edited_profile = []
            with open("admin/memberdatabase.txt", "r") as memberfile:
                members = memberfile.readlines()
            
            for credentials in members:
                stored_username, stored_userage, stored_dob, stored_regdate, stored_ic = credentials.strip().split(":")
                if stored_username == username:
                    print(f"ID: {stored_username}\nName: {stored_userage}\nPassword: {stored_dob}\nRole: {stored_regdate}\nIC: {stored_ic}")
                    print("1. ID")
                    print("2. Name")
                    print("3. Password")
                    print("4. Role")
                    print("5. IC")
                    print("6. All")
                    choice = input("What would you like to edit?").strip()

                    new_username = stored_username
                    new_userage = stored_userage
                    new_dob = stored_dob
                    new_regdate = stored_regdate
                    new_ic = stored_ic

                    if choice == "1":
                        new_username = input("Enter new id: ")
                    elif choice == "2":
                        new_userage = input("Enter new name: ")
                    elif choice == "3":
                        new_dob = input("Enter new password: ")
                    elif choice == "4":
                        new_regdate = input("Enter new role: ")
                    elif choice == "5":
                        new_ic = input("Enter new ic: ")
                    elif choice == "6":
                        new_username = input("Enter new id: ")
                        new_userage = input("Enter new name: ")
                        new_dob = input("Enter new password: ")
                        new_regdate = input("Enter new role: ")
                        new_ic = input("Enter new ic: ")
                    else:
                        print("Invalid option.")
                        continue

                    edited_profile.append(f"{new_username}:{new_userage}:{new_dob}:{new_regdate}:{new_ic}\n")
                    print("Member information edited.")
                else:
                    edited_profile.append(credentials)

            with open("admin/memberdatabase.txt", "w") as memberfile:
                memberfile.writelines(edited_profile)

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
        

    else:
        # If no books were found, inform the user
        print("No books found matching your search term.")
    
    member_end_choice()

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
    search_display_catalogue_books()

if __name__ == "__main__":
    main()