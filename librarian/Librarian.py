import os
import time
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
        with open('librarian/catalogue.txt', 'w') as catalogue:
            # Write headers to the file if it's newly created
            catalogue.write(f"{headers}\n")

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
    with open('librarian/catalogue.txt', 'a') as catalogue:
        # Write the book details to the file in the correct format
        catalogue.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}:{availability}\n")
    
    # Inform the user that the book has been added successfully
    print("Book Added To Catalogue Successfully!\n")

    # Run end_choice fucntion
    end_choice()


"""Function to view all existing book in catalogue"""
def view_book_in_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')  

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'):
        print('Catalogue Does Not Exist.')
        end_choice() 

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        end_choice() 
    
    else:
        try:
            # Read all lines from the catalogue file
            with open('librarian/catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines() # Load all lines into memory

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
    
    # Run end_choice function after displaying the catalogue
    end_choice()


"""Function to search books"""
def search_catalogue():

    # Check if catalogue file exists 
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        end_choice()

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        end_choice() 
    
    else:
        # Read all lines from the catalogue file
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines() 

        # Get search term from user input and normalize it (convert to lowercase and remove extra spaces)
        search_term = input('Please Enter Your Search Term:')
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


"""Function to display search results"""
def search_display_catalogue_books():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    # Welcome message for the search book page
    print("Welcome To Search Book Page:")

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
        print("No books found matching your search.")
        # Call end_choice function to handle end of the operation
        end_choice()
    
    # Call end_choice function to finish the search operation
    end_choice()


"""Function to edit book information in catalogue"""
def edit_book_information():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Book Page:")

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        end_choice()

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        end_choice()
    
    else:
        # Search for books and get the search results
        header, found_books = search_catalogue()

        if not found_books:
            print("No books to edit.")
            end_choice()
        
        print(f'Found {len(found_books)} book(s):\n')
        print(header.strip())  # Print the header (column names)
        print('=' * len(header.strip()))  # Print a separator line based on the header length

        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")

        # Get the index of the book the user wants to edit
        while True:
            try:
                # Prompt user to enter the index of the book to edit
                edit_index = int(input('\nPlease Enter The Index Of Book To Edit:'))
                book_id = edit_index - 1  # Adjust for 0-based index

                # Ensure the entered index is within the valid range
                if 0 <= book_id < len(found_books):
                    break  # Exit the loop if the index is valid

                else:
                    print("Invalid Index. Please Try Again.")  # Error for out-of-range index

            except ValueError:
                print("Invalid Input. Please Enter a Number.")  # Handle non-integer input

        # Read all lines from the catalogue file
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        # Get the original book details based on the selected index
        original_book = found_books[book_id]
        book_details = original_book.split(':')  # Split the book details by colon
        line_index = lines.index(original_book + '\n')  # Get the line index for replacement

        # Define the fields that can be edited
        fields = ['title', 'author', 'publisher', 'publication date', 'ISBN', 'genre', 'availability']
        new_details = []

        for i, field in enumerate(fields):
            if field == 'title':
                while True:
                    new_title = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_title:
                        # Ensure the book title is not empty or only spaces
                        if not new_title.isspace():
                            new_details.append(new_title)
                            break
                        else:
                            print("Please Enter A Valid Book Title.")
                    else:
                        new_details.append(book_details[i].strip())
                        break

            elif field == 'author':
                while True:
                    new_author = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_author:

                        # Ensure the author's name contains only letters or spaces
                        if all(x.isalpha() or x.isspace() for x in new_author):
                            new_details.append(new_author)
                            break
                        else:
                            print("Please Enter A Valid Book Author.")
                    else:
                        new_details.append(book_details[i].strip())
                        break

            elif field == 'publisher':
                # Get book publisher from user (non-empty input required)
                while True:
                    new_publisher = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_publisher:
                        # Ensure the publisher's name is not empty
                        if not new_publisher.isspace():
                            new_details.append(new_publisher)
                            break
                        else:
                            print("Please Enter A Valid Book Publisher.")
                    else:
                        new_details.append(book_details[i].strip())
                        break

            elif field == 'publication date':
                # Get publication date from user (must be in YYYY-MM-DD format and cannot over current date)
                while True:
                    new_publication_date = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_publication_date:
                        try:
                            # Ensure the input follows the correct date format
                            book_date = datetime.strptime(new_publication_date, "%Y-%m-%d") 

                            # Check if the date is today or in the past
                            if book_date <= datetime.now(): 
                                new_details.append(new_publication_date)
                                break
                            else:
                                print("The date cannot be in the future. Please enter a past or current date.")

                        except ValueError:
                            print("Please Enter The Date According To The Format.")

                    else:
                        new_details.append(book_details[i].strip())
                        break

            elif field == 'ISBN':
                # Get ISBN from user (must be digits, can include hyphens)
                while True:
                    new_isbn = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_isbn:
                        # Ensure the ISBN contains only digits or hyphens
                        if new_isbn.replace('-', '').isdigit():
                            new_details.append(new_isbn)
                            break
                        else:
                            print("Please Enter A Valid Book ISBN. Avoid Enter Character or Spaces.")
                    else:
                        new_details.append(book_details[i].strip())
                        break
        
            elif field == 'genre':
                # Get book genre from user (alphabetic characters and spaces only)
                while True:
                    new_genre = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_genre:
                        # Ensure the genre contains only letters or spaces
                        if all(x.isalpha() or x.isspace() for x in new_genre):
                            new_details.append(new_genre)
                            break
                        else:
                            print("Please Enter A Valid Book Genre.")
                    else:
                        new_details.append(book_details[i].strip())
                        break
            
            else:
                while True:
                    new_availability = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_availability:
                        if new_availability == "yes" or new_availability == "no":
                            new_details.append(new_availability)
                            break
                        else:
                            print("Please Enter A Valid Availability (yes/no).")
                    else:
                        new_details.append(book_details[i].strip())
                        break

        # Create an updated book entry by joining the new details
        updated_book = ':'.join(new_details) + '\n'
        
        # Replace the original book entry with the updated one
        lines[line_index] = updated_book

        # Write the updated lines back to the catalogue file
        with open('librarian/catalogue.txt', 'w') as catalogue:
            catalogue.writelines(lines)

        # Notify the user that the book information has been updated successfully
        print('\nBook Information Updated Successfully.')

    # Run end_choice fucntion
    end_choice()


"""Function to remove book in catalogue"""
def remove_book():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Remove Book Page:")

    # Check if the catalogue file exists
    if not os.path.exists('librarian/catalogue.txt'):
        print('Catalogue does not exist.')
        end_choice()

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue is empty.')
        end_choice()

    else:
        # Search for books in the catalogue and get the search results
        header, found_books = search_catalogue()

        if not found_books:
            print("No books to remove.")
            end_choice()
        
        print(f'Found {len(found_books)} book(s):\n')
        print(header.strip())  # Print the header (column names)
        print('=' * len(header.strip()))  # Print a separator line based on the header length

        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")

        # Prompt the user to enter the index of the book they wish to remove
        while True:
            try:
                # Ask user for the index of the book to remove
                remove_index = int(input('\nPlease Enter The Index Of Book To Remove: '))
                book_id = remove_index - 1  # Adjust index to be 0-based

                # Validate the index to ensure it's within range
                if 0 <= book_id < len(found_books):
                    break  # Exit loop if valid index is provided
                else:
                    print("Invalid Index. Please Try Again.")  # Prompt again for out-of-range index

            except ValueError:
                print("Invalid Input. Please Enter a Number.")  # Handle invalid input (non-integer)

        # Store the book details to be removed
        book_to_remove = found_books[book_id]

        # Read all lines from the catalogue file
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        # Remove the selected book from the catalogue by filtering out the matching line
        filter_lines = [line for line in lines if line.strip() != book_to_remove]

        # Write the updated content back to the catalogue file
        with open('librarian/catalogue.txt', 'w') as catalogue:
            catalogue.writelines(filter_lines)

        # Inform the user that the selected book has been removed
        print(f"Book '{book_to_remove.split(':')[0]}' has been removed from the catalogue.")

    # Run end_choice fucntion
    end_choice()


"""Function to update book availability in catalogue"""
def updated_book_availability(book_title):
    try:
        # Open the catalogue.txt file in read mode to access the current book data
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()  # Read all lines from the file into a list

        updated_lines = []  # Create an empty list to store updated lines
        for index, line in enumerate(lines):
            # Keep the header as it is
            if index == 0:
                updated_lines.append(line)  # Append the header unchanged
                continue  # Skip to the next iteration
            
            columns = line.strip().split(":")  # Split the line by ':' into columns
            
            # Check if the current line corresponds to the book being updated
            if columns[0].strip().lower() == book_title.lower():
                columns[6] = "No"  # Update availability to "No"
            
            # Append the updated line to the updated_lines list
            updated_lines.append(':'.join(columns) + "\n")

        # Open the catalogue.txt file in write mode to save the updated book data
        with open('librarian/catalogue.txt', 'w') as catalogue:
            catalogue.writelines(updated_lines)  # Write all updated lines back to the file

    except FileNotFoundError:
        print("Error: catalogue.txt not found.")  # Handle the case where the file does not exist


"""Function to update member's book count in member.txt"""
def updated_book_count(username):
    try:
        # Open the member.txt file in read mode to access the current member data
        with open('admin/member.txt', 'r') as member:
            lines = member.readlines()  # Read all lines from the file into a list

        # Open the member.txt file in write mode to update the member data
        with open('admin/member.txt', 'w') as member:

            # Write the header line back to the file 
            for line in lines:
                if line == lines[0]:  # Check if it's the header line
                    member.write(line)  # Write the header line unchanged

            # Loop through the member lines starting from the second line to skip the header
            for line in lines[1:]:
                columns = line.strip().split(":")  # Split the line by ':' into columns

                # Check if the current line corresponds to the user whose count needs to be updated
                if columns[1] == username:
                    count = int(columns[3])  # Get the current book count (4th column)
                    new_count = count + 1  # Increment the count by 1
                    columns[3] = str(new_count)  # Update the count in the columns list

                    updated_line = ":".join(columns) + "\n"  # Join the updated columns back into a string
                    member.write(updated_line)  # Write the updated line to the file

                else:
                    member.write(line)  # Write unchanged lines back to the file

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
        with open('librarian/catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()  # Read all lines from the catalogue

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

        # If the book is found but not available, inform the user and stop the process
        elif not book_available:
            print(f"The book '{book_title}' is currently borrowed.")
            end_choice()
        
    # Get the current date and calculate the due date (14 days from now)
    borrow_date = datetime.now()  # Borrow date is the current date
    due_date = borrow_date + timedelta(days=14)  # Due date is 14 days later

    # Convert the dates to strings in the format "YYYY-MM-DD"
    borrow_date_str = borrow_date.strftime("%Y-%m-%d") 
    due_date_str = due_date.strftime("%Y-%m-%d")

    # Append the new loan information (username, book title, borrow date, due date) to the loans.txt file
    with open('librarian/loans.txt', 'a') as loans:
        loans.write(f"{username}:{book_title}:{borrow_date_str}:{due_date_str}\n")

    # Call the function to update the user's book count after borrowing
    updated_book_count(username)

    # Call the function to update the book's availability status in the catalogue
    updated_book_availability(book_title.lower())

    print("Successful Book Loan Process.")
    end_choice()
    

"""Function to check overdue fees in loans.txt"""
def check_overdue(username):
    header = "Username: BookTitle: BorrowDate: DueDate"  # Define the header for the loans file

    # Check if loans.txt exists and is not empty. If it's missing or empty, create it with a header
    if not os.path.exists('librarian/loans.txt') or os.path.getsize('librarian/loans.txt') == 0: 
        with open('librarian/loans.txt', 'w') as loans:
            loans.write(f"{header}\n")  # Write the header to loans.txt

    overdue_fees = []  # List to store overdue fees for each book

    # Open loans.txt in read mode to check the user's loan records
    with open('librarian/loans.txt', 'r') as loans:
        lines = loans.readlines()  # Read all lines from the file

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
        with open('admin/member.txt', 'r') as member:
            lines = member.readlines() # Read all lines from the file

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

            # If no matching username is found, inform the user
            print("Username Doesn't Exist.")
            end_choice()

    # Catch the case where the member.txt file is missing and print an error message
    except FileNotFoundError:
        print("Error: member.txt not found.")
        end_choice()

    return username


"""Function to prompt the user for their choice to carry out additional functions or to log out""" 
def end_choice():
    while True:
        end_choice = input("\nDo you want carry out other functions ? (y/n)")
        if end_choice.lower() == 'y':
            from librarian.librarianpage import librarian_page
            librarian_page()
            break
        elif end_choice.lower() == 'n':
            from Base import logout
            logout()
            break
        else:
            print("Invalid choice. Please choose y or n.")


def main():
    add_book_to_catalogue()
    view_book_in_catalogue()
    search_display_catalogue_books()
    edit_book_information()
    remove_book()
    check_username()

if "__name__" == "__main__":
    main()