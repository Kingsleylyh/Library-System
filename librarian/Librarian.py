import os
from datetime import datetime, timedelta


"""Function to add book into catalogue"""
def add_book_to_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome To Add Book Page:")

    # Define the headers for the catalogue file
    headers = "Title: Author: Publisher: Publication Date: ISBN: Genre: Availability"

    # Create the catalogue file if it doesn't exist or is empty
    if not os.path.exists('librarian/catalogue.txt') or os.path.getsize('librarian/catalogue.txt') == 0: 
        with open('librarian/catalogue.txt', 'w') as catalogue_file:
            # Write headers to the file if it's newly created
            catalogue_file.write(f"{headers}\n")

    # Get book title from user (non-empty input required)
    while True:
        book_title = input("Enter The Book's Title: ").strip()
        # Ensure the book title is not empty or only spaces
        if book_title and not book_title.isspace():
            break
        else:
            print("Please Enter A Valid Book Title.")

    # Get book author from user (alphabetic characters and spaces only)
    while True:
        book_author = input("Enter The Book's Author: ").strip()
        # Ensure the author's name contains only letters or spaces
        if all(x.isalpha() or x.isspace() for x in book_author):
            break
        else:
            print("Please Enter A Valid Book Author.")

    # Get book publisher from user (non-empty input required)
    while True:
        book_publisher = input("Enter The Book's Publisher: ").strip()
        # Ensure the publisher's name is not empty
        if book_publisher and not book_publisher.isspace():
            break
        else:
            print("Please Enter A Valid Book Publisher.")

    # Get publication date from user (must be in YYYY-MM-DD format)
    while True:
        book_publication_date = input("Enter The Book's Publication Date (YYYY-MM-DD): ").strip()
        try:
            # Ensure the input follows the correct date format
            book_date = datetime.strptime(book_publication_date, "%Y-%m-%d") 

            # Check if the date is today or in the past
            if book_date <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
        except ValueError:
            print("Please Enter The Date According To The Format.")

    # Get ISBN from user (must be digits, can include hyphens)
    while True:
        book_isbn = input("Enter The Book ISBN: ").strip()
        # Ensure the ISBN contains only digits or hyphens
        if book_isbn.replace('-', '').isdigit():
            break
        else:
            print("Please Enter A Valid Book ISBN. Avoid Enter Character or Spaces.")

    # Get book genre from user (alphabetic characters and spaces only)
    while True:
        book_genre = input("Enter The Book's Genre:").strip()
        # Ensure the genre contains only letters or spaces
        if book_genre and all(x.isalpha() or x.isspace() for x in book_genre):
            break
        else:
            print("Please Enter A Valid Book Genre.")

    # Set the book's availability status to "Yes"
    availability = 'Yes'

    # Append the new book information to the catalogue file
    with open('librarian/catalogue.txt', 'a') as catalogue_file:
        # Write the book details to the file in the correct format
        catalogue_file.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}:{availability}\n")
    
    # Inform the user that the book has been added successfully
    print("Book Added To Catalogue Successfully!\n")

    # Run end_choice fucntion
    end_choice()
    return


"""Function to view all existing book in catalogue"""
def view_book_in_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')  

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'):
        print('Catalogue Does Not Exist.')
        end_choice()
        return 

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        end_choice() 
        return
    
    else:
        try:
            # Read all lines from the catalogue file
            with open('librarian/catalogue.txt', 'r') as catalogue_file:
                lines = catalogue_file.readlines() # Load all lines into memory

            # Extract and print the header (first line)
            header = lines[0].strip() # Extract and clean the header (removes trailing spaces/newlines)
            print('Catalogue List:\n')
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
            print("Error Reading Catalogue File:", e)
            end_choice() # End function if an error occurs
            return
    
    # Run end_choice function after displaying the catalogue
    end_choice()
    return


"""Function to search books"""
def search_catalogue():
    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue Does Not Exist.')  # Inform the user if the file is missing
        end_choice()  # Navigate back to previous options
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')  # Inform the user if the file is empty
        end_choice()  # Navigate back to previous options
        return
    
    else:
        # Open the catalogue file for reading
        with open('librarian/catalogue.txt', 'r') as catalogue_file:
            catalogue_lines = catalogue_file.readlines()  # Read all lines from the file
            
        keyword = input('Please Enter A Keyword:').lower().strip()  # Prompt user for a search keyword

        found_book = []  # Initialize a list to hold found book details
        index_list = []  # Initialize a list to hold indices of found books
        # Iterate over each line in the catalogue (skipping the header)
        for index, line in enumerate(catalogue_lines[1:]):
            book_details = line.strip()  # Remove any leading/trailing whitespace

            # Check if the keyword is present in the book details (case-insensitive)
            if keyword in book_details.lower():
                found_book.append(book_details)  # Add the book details to the found list
                index_list.append(index + 1)  # Store the index of the found book,exclude header

        # If no books were found, return None and empty lists
        if not found_book:
            return None, [], []
   
    # Return the header, list of found books, and their indices
    return catalogue_lines[0], found_book, index_list



"""Function to display search results"""
def search_display_catalogue_books():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')
   
    print("Welcome To Search Catalogue Page:")

    # Call the search_catalogue function to retrieve the header and found books
    header, found_book, _ = search_catalogue()

    # Check if any books were found during the search
    if found_book:
        print(f'\nFound {len(found_book)} book(s):')  # Display the number of found books
        print(header.strip())  # Print the header (column names)
        print('=' * len(header.strip()))  # Print a separator line based on the header length

        # Enumerate through the found books and display them with their index
        for index, books in enumerate(found_book, start=1):
            print(f"{index}. {books}")  # Print each book with its index
    else:
        print("No Books found matching your search.")  # Inform the user if no books were found
        end_choice()  # Navigate back to previous options
        return
            
    end_choice()  # Navigate back to previous options after displaying the search results
    return



"""Function to edit book information in catalogue"""
def edit_book_information():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Book Page:")

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        end_choice()  # Navigate back to previous options
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        end_choice()  # Navigate back to previous options
        return
    
    else:
        # Search for books and get the search results
        header, found_books, found_books_index = search_catalogue()

        if not found_books:
            print("No books to edit.")
            end_choice()  # Navigate back if no books found
            return
        
        print(f'Found {len(found_books)} book(s):\n')
        print(header.strip())  # Print the header (column names)
        print('=' * len(header.strip()))  # Print a separator line based on the header length

        # Display found books for selection
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")

        # Prompt the user to select a book to edit
        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Book To Edit:')) - 1
                if 0 <= choice_selected < len(found_books):
                    remove_index = found_books_index[choice_selected]  # Get the actual index for removal
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Read the current catalogue entries
        with open('librarian/catalogue.txt', 'r') as catalogue_file:
            catalogue_lines = catalogue_file.readlines()

        # Split the selected book's information into components
        original_catalogue = catalogue_lines[remove_index].strip().split(':')

        # Prompt the user for new title, allowing them to keep the current value
        while True:
            new_title = input('Enter New Title (Press Enter To Keep Current Value): ').strip()
            if new_title == "":  
                break  # Keep current value if input is empty
            if not new_title.isspace():  # Validate input is not just whitespace
                original_catalogue[0] = new_title
                break
            else:
                print("Please Enter A Valid Book Title.")

        # Prompt the user for new author, with validation
        while True:    
            new_author = input('Enter New Author (Press Enter To Keep Current Value): ').strip()
            if new_author == "":  
                break  
            elif all(x.isalpha() or x.isspace() for x in new_author):  # Ensure input consists of letters and spaces
                original_catalogue[1] = new_author
                break
            else:
                print("Please Enter A Valid Book Author.")
                    
        # Prompt the user for new publisher, allowing current value to be kept
        while True:    
            new_publisher = input('Enter New Publisher (Press Enter To Keep Current Value): ').strip() 
            if new_publisher == "":  
                break   
            elif not new_publisher.isspace():  # Validate input is not just whitespace
                original_catalogue[2] = new_publisher
                break  
            else:
                print("Please Enter A Valid Book Publisher.")             

        # Prompt for new publication date with format validation
        while True:
            new_publication_date = input('Enter New Publication Date (Press Enter To Keep Current Value): ').strip()
            if new_publication_date == "":  
                break              # Keep current value if input is empty
            try:
                book_date = datetime.strptime(new_publication_date, "%Y-%m-%d") 
                if book_date <= datetime.now():  # Check if the date is not in the future
                    original_catalogue[3] = new_publication_date
                    break
                else:
                    print("The date cannot be in the future.")
            except ValueError:
                print("Please Enter The Date According To The Format.")

        # Prompt for new ISBN with validation
        while True:
            new_isbn = input('Enter New ISBN (Press Enter To Keep Current Value): ').strip()
            if new_isbn == "":  
                break 
            elif new_isbn.replace('-', '').isdigit():  # Ensure input is numeric, allowing hyphens
                original_catalogue[4] = new_isbn
                break       
            else:
                print("Please Enter A Valid Book ISBN. Avoid Enter Character or Spaces.")

        # Prompt for new genre, ensuring input is valid
        while True:
            new_genre = input('Enter New Genre (Press Enter To Keep Current Value): ').strip()
            if new_genre == "":  
                break 
            elif all(x.isalpha() or x.isspace() for x in new_genre):  # Ensure valid input
                original_catalogue[5] = new_genre 
                break
            else:
                print("Please Enter A Valid Book Genre.")
                   
        # Prompt for new availability status, validating input
        while True:
            new_availability = input('Enter New Availability (Press Enter To Keep Current Value): ').strip()
            if new_availability == "":  
                break 
            elif new_availability in ["yes", "no"]:  # Check for valid availability input
                original_catalogue[6] = new_availability      
                break            
            else:
                print("Please Enter A Valid Availability (yes/no).")

        # Construct the updated catalogue entry and save changes
        updated_original_catalogue = ':'.join(original_catalogue) + '\n'
        catalogue_lines[remove_index] = updated_original_catalogue  # Update the entry in the list

        # Write the updated catalogue back to the file
        with open('librarian/catalogue.txt', 'w') as catalogue_file:
            catalogue_file.writelines(catalogue_lines)
        
        print('Member Information Updated Successfully!')
    
    end_choice()  # Navigate back to previous options
    return



"""Function to remove book in catalogue"""
def remove_book():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Remove Book Page:")

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'):
        print('Catalogue does not exist.')
        end_choice()  # Navigate back to the previous options
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue is empty.')
        end_choice()  # Navigate back to the previous options
        return

    else:
        # Search for books in the catalogue
        header, found_books, found_books_index = search_catalogue()
        
        if not found_books:
            end_choice()  # If no books are found, navigate back
            return

        print(f'Found {len(found_books)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        # Display the found books for selection
        for choice, book in enumerate(found_books, start=1):
            print(f"{choice}. {book}")

        # Prompt the user to select a book to remove
        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Book To Remove: ')) - 1
                if 0 <= choice_selected < len(found_books):
                    remove_index = found_books_index[choice_selected]
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Read the current catalogue entries
        with open('librarian/catalogue.txt', 'r') as catalogue_file:
            catalogue_lines = catalogue_file.readlines()
     
        # Remove the selected book from the list
        catalogue_lines.pop(remove_index)

        # Write the updated catalogue back to the file
        with open('librarian/catalogue.txt', 'w') as catalogue_file:
            catalogue_file.writelines(catalogue_lines)
        
    end_choice()  # Navigate back to the previous options
    return



"""Function to update book availability in catalogue"""
def updated_book_availability(book_title):
    try:
        # Open the catalogue.txt file in read mode to access the current book data
        with open('librarian/catalogue.txt', 'r') as catalogue_file:
            lines = catalogue_file.readlines()  # Read all lines from the file into a list

        updated_lines = []  # Create an empty list to store updated lines
        for index, line in enumerate(lines):
            # Keep the header as it is
            if index == 0:
                updated_lines.append(line)  # Append the header unchanged
                continue
            
            columns = line.strip().split(":")  # Split the line by ':' into columns
            
            # Check if the current line corresponds to the book being updated
            if columns[0].strip().lower() == book_title.lower():
                columns[6] = "No"  # Update availability to "No"
            
            # Append the updated line to the updated_lines list
            updated_lines.append(':'.join(columns) + "\n")

        # Open the catalogue.txt file in write mode to save the updated book data
        with open('librarian/catalogue.txt', 'w') as catalogue_file:
            catalogue_file.writelines(updated_lines)  # Write all updated lines back to the file

    except FileNotFoundError:
        print("Error: catalogue.txt not found.")  # Handle the case where the file does not exist



"""Function to update member's book count in member.txt"""
def updated_book_count(username):
    try:
        # Open the member.txt file in read mode to access the current member data
        with open('admin/member.txt', 'r') as member_file:
            lines = member_file.readlines()  # Read all lines from the file into a list

        # Open the member.txt file in write mode to update the member data
        with open('admin/member.txt', 'w') as member_file:

            # Write the header line back to the file 
            for line in lines:
                if line == lines[0]:  # Check if it's the header line
                    member_file.write(line)  # Write the header line unchanged

            # Loop through the member lines starting from the second line to skip the header
            for line in lines[1:]:
                columns = line.strip().split(":")  # Split the line by ':' into columns

                # Check if the current line corresponds to the user whose count needs to be updated
                if columns[1] == username:
                    count = int(columns[3])  # Get the current book count (4th column)
                    new_count = count + 1  # Increment the count by 1
                    columns[3] = str(new_count)  # Update the count in the columns list

                    updated_line = ":".join(columns) + "\n"  # Join the updated columns back into a string
                    member_file.write(updated_line)  # Write the updated line to the file

                else:
                    member_file.write(line)  # Write unchanged lines back to the file

    except FileNotFoundError:
        print("Error: member.txt not found.")  # Handle the case where the file does not exist



"""Function for book loan process"""
def book_loan(username):
    
    book_found = False  # Flag to check if the book is found in the catalogue
    book_available = False  # Flag to check if the book is available for borrowing

    # Loop to prompt the user until a valid book title is entered and the book is available
    while not book_found:
        book_title = input('Enter the Book Title:')  # Get the book title from the user

        # Open the catalogue.txt file to search for the entered book title
        with open('librarian/catalogue.txt', 'r') as catalogue_file:
            lines = catalogue_file.readlines()  # Read all lines from the catalogue

            # Loop through the catalogue, skipping the header, to search for the book
            for line in lines[1:]:
                columns = line.strip().split(":")  # Split each line by ':' into columns

                # Check if the entered book title matches any book in the catalogue (case-insensitive)
                if columns[0].lower() == book_title.strip().lower():
                    book_found = True  # Mark that the book has been found

                    # Check if the book is available for loan (indicated by "yes")
                    if columns[6].strip().lower() == "yes":
                        book_available = True  # Mark that the book is available

        # If the book is not found in the catalogue, prompt the user to try again
        if not book_found:
            print("The book is not found in the system. Please make sure you key in correctly.")
            end_choice()
            return

        # If the book is found but not available, inform the user and stop the process
        elif not book_available:
            print(f"The book '{book_title}' is currently borrowed.")
            end_choice()
            return
        
    # Get the current date and calculate the due date (14 days from now)
    borrow_date = datetime.now()  # Borrow date is the current date
    due_date = borrow_date + timedelta(days=14)  # Due date is 14 days later

    # Convert the dates to strings in the format "YYYY-MM-DD"
    borrow_date_str = borrow_date.strftime("%Y-%m-%d") 
    due_date_str = due_date.strftime("%Y-%m-%d")

    # Append the new loan information (username, book title, borrow date, due date) to the loans.txt file
    with open('librarian/loans.txt', 'a') as loans_file:
        loans_file.write(f"{username}:{book_title}:{borrow_date_str}:{due_date_str}\n")

    # Call the function to update the user's book count after borrowing
    updated_book_count(username)

    # Call the function to update the book's availability status in the catalogue
    updated_book_availability(book_title.lower())

    print("Successful Book Loan Process.")
    end_choice()
    return
    


"""Function to check overdue fees in loans.txt"""
def check_overdue(username):
    header = "Username: BookTitle: BorrowDate: DueDate"  # Define the header for the loans file

    # Check if loans.txt exists and is not empty. If it's missing or empty, create it with a header
    if not os.path.exists('librarian/loans.txt') or os.path.getsize('librarian/loans.txt') == 0: 
        with open('librarian/loans.txt', 'w') as loans_file:
            loans_file.write(f"{header}\n")  # Write the header to loans.txt

    overdue_fees = []  # List to store overdue fees for each book

    # Open loans.txt in read mode to check the user's loan records
    with open('librarian/loans.txt', 'r') as loans_file:
        lines = loans_file.readlines()  # Read all lines from the file

        # Loop through each loan record, skipping the header
        for line in lines[1:]:
            columns = line.strip().split(':')  # Split each line by ':' into columns

            # Check if the current line corresponds to the given username
            if columns[0] == username:
                book_id = columns[1]  # Get the book ID (or title)
                due_date = datetime.strptime(columns[3], '%Y-%m-%d')  # Parse the borrow date from string format
                current_date = datetime.now()  # Get the current date

                # Calculate the number of overdue days by comparing current date and borrow date
                overdue_days = (current_date - due_date).days 
                overdue_days = max(0, overdue_days)  # Ensure overdue_days is non-negative (no negative overdue)

                # Calculate overdue fee based on the number of overdue days
                if overdue_days == 0:
                    overdue_fees.append(0)  # No fee if overdue is 0 days

                elif overdue_days == 1:
                    overdue_fees.append(2.00)  # Fee for 1 day overdue is RM 2.00

                elif overdue_days == 2:
                    overdue_fees.append(3.00)  # Fee for 2 days overdue is RM 3.00

                elif overdue_days == 3:
                    overdue_fees.append(4.00)  # Fee for 3 days overdue is RM 4.00

                elif overdue_days == 4:
                    overdue_fees.append(5.00)  # Fee for 4 days overdue is RM 5.00

                elif overdue_days == 5:
                    overdue_fees.append(6.00)  # Fee for 5 days overdue is RM 6.00

                else:
                    overdue_fees.append(10.00)  # Flat fee of RM 10.00 for 6 or more overdue days

                # Print the overdue fee for the specific book
                print(f"Overdue fee for Book {book_id}: RM{overdue_fees[-1]:.2f}")

    # Sum up all overdue fees for the user
    total_overdue_fees = sum(overdue_fees)

    # If there are no overdue fees, allow the user to borrow another book
    if total_overdue_fees == 0:
        print(f"{username} has no overdue fees.\n")
        print("Book Loan Process:")
        book_loan(username)  # Call the book_loan function to proceed with borrowing

    # Otherwise, inform the user of their total overdue fees
    else:
        print(f"\nTotal overdue fees for {username} is RM{total_overdue_fees:.2f}")
        print("Please pay all the overdue fees before continue borrowing books.")
        end_choice()
        return

        
                      
"""Function to check username in member.txt"""
def check_username():

    # Clear the console based on the OS (Windows or Unix-based)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Book Loan Process Page:")

    # Ask user to enter their username
    print("Username Verification:")
    username = input('Please Enter Username:')

    try:
         # Open the member.txt file in read mode
        with open('admin/member.txt', 'r') as member_file:
            lines = member_file.readlines() # Read all lines from the file

            # Iterate through the lines starting from the second one (skip header)
            for line in lines[1:]:
                columns = line.strip().split(':') # Split each line into columns by ':'

                # Check if the username matches the input
                if columns[1] == username:
                    print("Username exists.\n") # Confirm that the username exists

                    # Check if the user has borrowed fewer than 5 books
                    if 0 <= int(columns[3]) < 5:
                        print("Overdue Fees Verification:")
                        check_overdue(username) # Call the function to check overdue fees
                        return

                    # If the user has borrowed 5 books, they cannot borrow more
                    else:
                        print("User borrowed 5 books already.")
                        end_choice()
                        return

            # If no matching username is found, inform the user
            print("Username Doesn't Exist.")
            end_choice()
            return

    # Catch the case where the member.txt file is missing and print an error message
    except FileNotFoundError:
        print("Error: member.txt not found.")
        end_choice()
        return



"""Function to prompt the user for their choice to carry out additional functions or to log out""" 
def end_choice():
    # Import necessary functions for navigating the librarian system and logging out
    from librarian.librarianpage import librarian_page
    from login import logout
    
    while True:
        # Prompt the librarian for whether they want to perform more actions
        end_choice = input("\nDo you want to carry out other functions? (y/n): ")
        
        if end_choice.lower() == 'y':
            # If yes, redirect to the librarian page
            librarian_page()
            break
        elif end_choice.lower() == 'n':
            # If no, log out and end the session
            logout()
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please choose y or n.")