import os
"""Function to search books"""
def search_catalogue():
    if not os.path.exists('librarian/catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        return

    # Check if the catalogue file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
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
    header, found_books = search_catalogue()
    if found_books:
        print(f'Found {len(found_books)} book(s):')

        print(header.strip())
        print('=' * len(header.strip()))

        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book}")

    else:
        print("No books found matching your search.")
    
    #end_choice()
    
search_display_catalogue_books()