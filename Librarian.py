import os
# ADD BOOK FUCNTION()
def add_book_to_catalogue():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # PRINT SENTENCES  
    print('Please Enter the Book Details:')
    print('='*40)

    # HEADER SETTINGS
    headers = ("Title: Author: Publisher: Publication Date: ISBN: Genre") # DEFINE COLUMN HEADERS

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('catalogue.txt') or os.path.getsize('catalogue.txt') == 0: 
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.write(f"{headers}\n")


    # GET BOOK DETAILS FROM USERS
    book_title = input("Enter the book's title: ").strip()
    book_author = input("Enter the book's author: ").strip()
    book_publisher = input("Enter the book's publisher: ").strip()
    book_publication_date = input("Enter the book's publication date (YYYY-MM-DD): ").strip()
    book_isbn = input("Enter the book's ISBN: ").strip()
    book_genre = input("Enter the book's genre: ").strip()

    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('catalogue.txt','a') as catalogue:
        catalogue.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}\n")
    
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

        except Exception as e:
            print("Error reading catalogue file:", e)
    
view_book_in_catalogue()





import os
# SEARCH BOOK FROM CATALOGUE
def search_book_from_catalogue():
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
            print("Welcome to search page:")
            search_term = input("Please Enter Your Search Term: ").lower().strip()

            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()
                header = lines[0].strip()

            found_books = []
            for line in lines[1:]:
                book_dtl = line.strip()
                book_details = line.strip().lower()
                if search_term in book_details:
                    found_books.append(book_dtl)
                
            print(f"Found {len(found_books)} result(s)")
            print(header)
            print('=' * 50)

            for book in found_books:
                print(book)

            return [header] + found_books  # Return the header and found books

        except FileNotFoundError:
            print("No catalogue found!")
        except Exception as e:
            print("Error reading catalogue file:", e)

import os
# EDIT BOOK INFORMATION
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
            # SEARCH THE BOOK THAT WANTS TO BE EDITED
            lines = search_book_from_catalogue()

            if not lines:
                return

            # DISPLAY THE BOOKS WITH IDs
            print('='*40)
            print('Books in Catalogue')
            for index, line in enumerate(lines[1:], start=1):
                print(f'{index}. {line.strip()}')

            while True:
                # GET BOOK ID FROM USER
                book_id_input = input("Based on your search term, please enter the book ID you want to edit: ")

                if not book_id_input.isdigit():
                    print("Invalid input. Please enter a valid book ID.")
                    continue
                
                book_id = int(book_id_input) - 1

                if book_id < 0 or book_id >= len(lines) - 1:
                    print("Book ID doesn't exist.")
                else:
                    break

            # GET CURRENT DETAILS OF SELECTED BOOK
            book_details = lines[book_id + 1].strip().split(":")
            print('Current Details:')
            print('|'.join(book_details))
            print('='*40)

            valid_entities = ["title", "author", "publisher", "publication date", "isbn", "genre"]

            while True:
                # ASK WHICH ENTITY TO CHANGE
                Change = input("Which entity do you want to change (title, author, publisher, publication date, isbn, genre)? ").strip().lower()

                if Change not in valid_entities:
                    print("Invalid entity. Please enter a valid entity.")
                    continue
                else:
                    break

            # MAP THE ENTITY TO ITS CORRESPONDING INDEX
            entity_index = valid_entities.index(Change)

            # ASK FOR THE CHANGES
            edit = input(f"Enter the new {Change}: ").strip()

            # UPDATE
            book_details[entity_index] = edit

            # UPDATE TO ORIGINAL LIST
            lines[book_id + 1] = ':'.join(book_details) + "\n"

            # WRITE BACK TO THE FILE
            with open('catalogue.txt', 'w') as catalogue:
                catalogue.writelines(lines)

            print('Book Information Updated Successfully')

        except Exception as e:
            print("Error reading catalogue file:", e)

edit_book_information()



            
    

import os
def clear_txt_file():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clehar')

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







