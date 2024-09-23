import os
# ADD BOOK FUCNTION()
def add_book_to_catalogue():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # PRINT SENTENCES  
    print('Please Enter the Book Details:')
<<<<<<< HEAD
    print('-'*40)

    # HEADER SETTINGS
    headers = ['Title', 'Author', 'Publisher', 'Publication Date', 'ISBN', 'Genre'] # DEFINE COLUMN HEADERS
    header_line = ':'.join(headers) # JOIN HEADER WITH ":"
=======
    print('='*40)

    # HEADER SETTINGS
    headers = ("Title: Author: Publisher: Publication Date: ISBN: Genre") # DEFINE COLUMN HEADERS
>>>>>>> origin/YongHeng

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('catalogue.txt') or os.path.getsize('catalogue.txt') == 0: 
        with open('catalogue.txt', 'w') as catalogue:
<<<<<<< HEAD
            catalogue.write(header_line + '\n')
=======
            catalogue.write(f"{headers}\n")

>>>>>>> origin/YongHeng

    # GET BOOK DETAILS FROM USERS
    book_title = input("Enter the book's title: ").strip()
    book_author = input("Enter the book's author: ").strip()
    book_publisher = input("Enter the book's publisher: ").strip()
    book_publication_date = input("Enter the book's publication date (YYYY-MM-DD): ").strip()
    book_isbn = input("Enter the book's ISBN: ").strip()
    book_genre = input("Enter the book's genre: ").strip()

<<<<<<< HEAD
    # JOIN BOOK DETAILS WITH ":"
    book_line = ':'.join([book_title,
                          book_author,
                          book_publisher,
                          book_publication_date,
                          book_isbn,
                          book_genre])

    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('catalogue.txt','a') as catalogue:
        catalogue.write(book_line + "\n") 
=======
    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('catalogue.txt','a') as catalogue:
        catalogue.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}\n")
>>>>>>> origin/YongHeng
    
    print("Book added to catalogue successfully!")

add_book_to_catalogue()



import os
# VIEW ALL EXISTING BOOK IN CATALOGUE
def view_book_in_catalogue():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('catalogue.txt'):
        print('Catalogue does not exist.')
        return

    #CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
        return
    
    else:
        try:
            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()
                
<<<<<<< HEAD
                headers = lines[0].strip().split(':')
                print("|".join(headers))
                print("-"*50)

                # SORT BOOKS BY GENRE
                sorted_book = sorted(lines[1:], key = lambda x: x.strip().split(':')[-1].lower())
                current_genre = ""
                for line in sorted_book:
                    book_details = line.strip().split(':')
                    genre = book_details[-1]
                    
                    if genre != current_genre:
                        current_genre = genre
                    print("|".join(book_details))
=======
                print('Catalogue List:')
                longest_line = max(lines, key=len)
                length_of_longest_line = len(longest_line)
                print('=' * length_of_longest_line)

                # SORT BOOKS BY GENRE
                sorted_book = sorted(lines[1:], key = lambda x: x.strip().split(":")[-1].lower())
                current_genre = ""
                for line in sorted_book:
                    book_details = line.strip()
                    genre = book_details.split(':')[-1]
                    
                    if genre != current_genre:
                        current_genre = genre

                    print(f"{book_details}")
>>>>>>> origin/YongHeng

        except Exception as e:
            print("Error reading catalogue file:", e)
    
view_book_in_catalogue()





import os
# SEARCH BOOK FROM CATALOGUE
def search_book_from_catalogue():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue does not exist.')
<<<<<<< HEAD
        return None
=======
        return
>>>>>>> origin/YongHeng

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
<<<<<<< HEAD
        return None
    
    else:
        try:
            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt','r') as catalogue:
                lines = catalogue.readlines()
                headers = lines[0].strip().split(':')

                # GET SEARCH TERM FROM LIBRARIAN
                search_term = input('Enter the search term: ').strip().lower()
                search_words = search_term.split()
                print('Searching for results related to', search_term,'....')
                print('-'*50)

                # SEARCH FOR BOOKS MATCHING SEARCH TERM
                found_books = []
                for line in lines[1:]:
                    book_details = line.strip().split(':')
                    combined_details = ' '.join(book_details).lower()

                    for word in search_words:
                        if word not in combined_details:
                            break
                    else:
                        found_books.append(book_details)
                
                # DISPLAY SEARCH RESULTS
                if found_books:
                    print(f"Found {len(found_books)} result(s)")
                    print('|'.join(headers))
                    print('-'*50)
                    for book in found_books:
                        print('|'.join(book))
                else:
                    print("No results found for", search_term)
                
                return lines
=======
        return
    
    else:
        try:
            print("Welcome to search page:")
            search_term = input(("Please Enter Your Search Term:")).lower().strip()

            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt','r') as catalogue:
                lines = catalogue.readlines()
                header = lines[0].strip()

            found_books = []
            for line in lines[1:]:
                book_dtl = line.strip()
                book_details = line.strip().lower()
                for word in search_term:
                    if word not in book_details:
                        break
                else:
                    found_books.append(book_dtl)
                
            print(f"Found {len(found_books)} result(s)")
            print(header)
            print('=' * 50)

            for book in found_books:
                print(book)
                
>>>>>>> origin/YongHeng

        except FileNotFoundError:
            print("No catalogue found!")
        except Exception as e:
            print("Error reading catalogue file:", e)

search_book_from_catalogue()


<<<<<<< HEAD
=======



>>>>>>> origin/YongHeng
import os 
def edit_book_information(): 
    # CLEAR TERMINAL HSITORY  
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue does not exist.')
        return

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
        return

    else:
        try:
            # SEARCH THE BOOK THAT WANT TO EDIT (search_book_from_catalogue)
            lines = search_book_from_catalogue()

<<<<<<< HEAD
=======
            if not lines:
                return

>>>>>>> origin/YongHeng
            # DISPLAY THE BOOKS WITH IDs STARTING FROM 1
            print('Books in Catalogue')
            for index, line in enumerate(lines[1:], start = 1):
                print(f'{index}.{line.strip()}')

            while True:
                book_id_input = input("Based on your search term, please enter the book ID you want to edit: ")
                
                if not book_id_input.isdigit():
                    print("Invalid input. Please enter a valid book ID.")
                    continue
                
                book_id = int(book_id_input)-1

<<<<<<< HEAD
                if book_id < 1 or book_id >= len(lines)-1:
=======
                if book_id < 0 or book_id >= len(lines)-1:
>>>>>>> origin/YongHeng
                    print("Invalid book ID")
                else:
                    break

                book_details = lines[book_id + 1].strip().split()
                print('Current Details:')
                print('|'.join(book_details))

                new_title = input("Enter new title (leave blank to keep current): ").strip()
                new_author = input("Enter new author (leave blank to keep current): ").strip()
                new_publisher = input("Enter new publisher (leave blank to keep current): ").strip()
                new_publication_date = input("Enter new publication date (leave blank to keep current): ").strip()
                new_isbn = input("Enter new ISBN (leave blank to keep current): ").strip()
                new_genre = input("Enter new genre (leave blank to keep current): ").strip()

                if new_title:
                    book_details[0] = new_title
                if new_author:
                    book_details[1] = new_author
                if new_publisher:
                    book_details[2] = new_publisher
                if new_publication_date:
                    book_details[3] = new_publication_date
                if new_isbn:
                    book_details[4] = new_isbn
                if new_genre:
                    book_details[5] = new_genre

                lines[book_id + 1] = ':'.join(book_details)+ "\n"

                with open('catalogue.txt','w' ) as catalogue:
                    catalogue.writelines(lines)

                print('Book Information Update Successfully')

        except Exception as e:
            print("Error reading catalogue file:", e)

<<<<<<< HEAD
    pass

edit_book_information()


=======
edit_book_information()
















>>>>>>> origin/YongHeng
import os
def edit_book_information(): 
    # CLEAR TERMINAL HISTORY  
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IF THE FILE EXISTS
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue does not exist.')
        return

    # CHECK IF THE FILE IS EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
        return

    else:
        try:
            # READ THE BOOKS FROM THE CATALOGUE
            lines = search_book_from_catalogue()

            # DISPLAY BOOKS WITH IDs STARTING FROM 1
            print("Books in Catalogue:")
            for index, line in enumerate(lines[1:], start=1):  # Start from 1
                print(f"{index}. {line.strip()}")  # Display ID starting from 1

            while True:
                book_id_input = input("Based on your search term, please enter the book ID you want to edit: ")
                
                # Check if input is a digit
                if not book_id_input.isdigit():
                    print("Please enter a valid numeric book ID.")
                    continue
                
                book_id = int(book_id_input) - 1  # Adjust for 0-based indexing
                
                if book_id < 0 or book_id >= len(lines) - 1:  # -1 because of header
                    print("Invalid book ID. Please try again.")
                else:
                    break  # Exit the loop if the ID is valid

            book_details = lines[book_id + 1].strip().split(':')  # Get book details, +1 for header
            
            # Display current book details for editing
            print("Current details:")
            print("|".join(book_details))
            
            # Prompt for new details
            new_title = input("Enter new title (leave blank to keep current): ").strip()
            new_author = input("Enter new author (leave blank to keep current): ").strip()
            new_publisher = input("Enter new publisher (leave blank to keep current): ").strip()
            new_publication_date = input("Enter new publication date (leave blank to keep current): ").strip()
            new_isbn = input("Enter new ISBN (leave blank to keep current): ").strip()
            new_genre = input("Enter new genre (leave blank to keep current): ").strip()

            # Update the book details
            if new_title: book_details[0] = new_title
            if new_author: book_details[1] = new_author
            if new_publisher: book_details[2] = new_publisher
            if new_publication_date: book_details[3] = new_publication_date
            if new_isbn: book_details[4] = new_isbn
            if new_genre: book_details[5] = new_genre

            # Write the updated details back to the file
            lines[book_id + 1] = ":".join(book_details) + "\n"  # +1 for header

            with open('catalogue.txt', 'w') as catalogue:
                catalogue.writelines(lines)

            print("Book information updated successfully!")

        except Exception as e:
            print("Error reading catalogue file:", e)

edit_book_information()


            
    

import os
def clear_txt_file():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    with open('catalogue.txt','r') as catalogue:
        headers = catalogue.readline()

    with open('catalogue.txt', 'w') as catalogue:
        # Write the headers back to the file
        catalogue.write(headers)

    print("Catalogue cleared but headers retained!")

clear_txt_file()


book_details = "Kitchen Hell?Gordan Ransay?TheStar?2024/4/24?1234-5678?Cooking"
details_list = book_details.split('?')
print(details_list)
print(' '.join(details_list).lower())







