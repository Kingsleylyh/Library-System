import os
from datetime import datetime
# ADD BOOK FUCNTION()
def add_book_to_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display a header for the book entry process
    print('Please Enter The Book Details:')
    print('='*40)

    # Define the headers for the catalogue file
    headers = "Title: Author: Publisher: Publication Date: ISBN: Genre"

    # Create the catalogue file if it doesn't exist or is empty
    if not os.path.exists('catalogue.txt') or os.path.getsize('catalogue.txt') == 0: 
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.write(f"{headers}\n")

    # Get book title from user (non-empty input required)
    while True:
        book_title = input("Enter The Book's Title: ").strip()
        if book_title and not book_title.isspace():
            break
        else:
            print("Please Enter A Valid Book Title.")

    # Get book author from user (alphabetic characters and spaces only)
    while True:
        book_author = input("Enter The Book's Author: ").strip()
        if all(x.isalpha() or x.isspace() for x in book_author):
            break
        else:
            print("Please Enter A Valid Book Author.")

    # Get book publisher from user (non-empty input required)
    while True:
        book_publisher = input("Enter The Book's Publisher: ").strip()
        if book_publisher and not book_publisher.isspace():
            break
        else:
            print("Please Enter A Valid Book Publisher.")

    # Get publication date from user (must be in YYYY-MM-DD format)
    while True:
        book_publication_date = input("Enter The Book's Publication Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(book_publication_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please Enter The Date According To The Format.")

    # Get ISBN from user (must be digits, can include hyphens)
    while True:
        book_isbn = input("Enter The Book ISBN: ").strip()
        if book_isbn.replace('-', '').isdigit():
            break
        else:
            print("Please Enter A Valid Book ISBN. Avoid Enter Character or Spaces.")

    # Get book genre from user (alphabetic characters and spaces only)
    while True:
        book_genre = input("Enter The Book's Genre : ").strip()
        if book_genre and all(x.isalpha() or x.isspace() for x in book_genre):
            break
        else:
            print("Please Enter A Valid Book Genre.")

    # Append the new book information to the catalogue file
    with open('catalogue.txt', 'a') as catalogue:
        catalogue.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}\n")
    
    # Inform the user that the book has been added successfully
    print("Book Added To Catalogue Successfully!")

add_book_to_catalogue()





import os
# VIEW ALL EXISTING BOOKS IN CATALOGUE
def view_book_in_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the catalogue file exists
    if not os.path.exists('catalogue.txt'):
        print('Catalogue Does Not Exist.')
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        try:
            # Read all lines from the catalogue file
            with open('catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()

            # Extract and print the header (first line)
            header = lines[0].strip()
            print('Catalogue List:\n')
            print(header)

            # Print a separator line based on the longest line in the file
            longest_line = max(lines, key=len)
            print('=' * len(longest_line))

            # Sort books by genre (last field in each line)
            sorted_books = sorted(lines[1:], key=lambda x: x.strip().split(":")[-1].lower())
            
            # Print sorted books
            current_genre = ""
            for line in sorted_books:
                book_details = line.strip()
                genre = book_details.split(':')[-1]

                # Print genre name if it's a new genre
                if genre != current_genre:
                    current_genre = genre
                    print(f"\n{genre}:")
                
                # Print book details
                print(f"{book_details}")

        except Exception as e:
            print("Error Reading Catalogue File:", e)
    
# Call the function to view the catalogue
view_book_in_catalogue()





import os
# SEARCH BOOK FROM CATALOGUE
def search_book_from_catalogue():
    # Clear the terminal screen for better visibility
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the catalogue file exists
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        # Read all lines from the catalogue file
        with open('catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()
        
        # Get search term from user and normalize it
        search_term = input('Please Enter Your Search Term:')
        search_term = search_term.lower().strip()

        # Search for books matching the search term
        found_book = []
        for line in lines[1:]:  # Skip the header line
            lower_book_details = line.strip().lower()
            normal_book_details = line.strip()
            if search_term in lower_book_details:
                found_book.append(normal_book_details)
        
        # Display search results
        print(f'\nFound {len(found_book)} Result(s):')

        # Print header
        headers = lines[0].strip()
        print(headers)
        print('=' * len(headers))

        # Print found books with index numbers
        for index, book in enumerate(found_book, start=1):
            print(f"{index}. {book}")

        return found_book
    
# Call the search function
search_book_from_catalogue()




def edit_book_information():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the catalogue file exists
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        # Search for books and get the results
        found_book = search_book_from_catalogue() 

        # Get the index of the book to edit
        while True:
            try:
                edit_index = int(input('\nPlease Enter The Index Of Book To Edit:'))
                book_id = edit_index - 1

                if 0 <= book_id < len(found_book):
                        break
                
                else:
                    print("Invalid Index. Please Try Again.")

            except ValueError:
                print("Invalid Input. Please Enter a Number.")


        # Read all lines from the catalogue
        with open('catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        # Get the original book details
        original_book = found_book[book_id]
        book_details = original_book.split(':')
        line_index = lines.index(original_book + '\n')

        # Define fields for editing
        fields = ['title', 'author', 'publisher', 'publication date', 'ISBN', 'genre']
        new_details = []

        # Get new values for each field
        for i, field in enumerate(fields):
            new_value = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
            if new_value:
                new_details.append(new_value)
            else:
                new_details.append(book_details[i].strip())

        # Create updated book entry
        updated_book = ':'.join(new_details) + '\n'
        lines[line_index] = updated_book

        # Write back the updated lines to the catalogue
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.writelines(lines)

        print('Book Information Updated Successfully.')

edit_book_information()





def remove_book():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('catalogue.txt'): 
        print('Catalogue does not exist.')
        return

    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
        return
    
    else:
        found_book = search_book_from_catalogue()

        while True:
            try:
                remove_index = int(input('\nPlease Enter The Index Of Book To Remove: '))
                book_id = remove_index - 1

                if 0 <= book_id < len(found_book):
                    break
                
                else:
                    print("Invalid Index. Please Try Again.")

            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        book_to_remove = found_book[book_id]

        with open('catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        # Remove the selected book
        lines = [line for line in lines if line.strip() != book_to_remove]

        # Write the updated content back to the file
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.writelines(lines)

        print(f"Book '{book_to_remove.split(':')[0]}' has been removed from the catalogue.")