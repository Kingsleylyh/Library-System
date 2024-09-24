import os
# ADD NEW MEMBER FUCNTION()
def add_new_member_to_database():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # PRINT SENTENCES  
    print('Please Enter the Member Details:')
    print('-'*40)

    # HEADER SETTINGS
    headers = ['Name', 'Age', 'Contact Number', 'Registration Date', 'ID', 'Date Of Birth'] # DEFINE COLUMN HEADERS
    header_line = ':'.join(headers) # JOIN HEADER WITH ":"

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('memberdatabase.txt') or os.path.getsize('memberdatabase.txt') == 0: 
        with open('memberdatabase.txt', 'w') as catalogue:
            catalogue.write(header_line + '\n')

    # GET MEMBER DETAILS FROM USERS
    Member_Name = input("Enter the member's name: ").strip()
    Member_Age = input("Enter the member's age: ").strip()
    Member_Contact_Number = input("Enter the member's contact number: ").strip()
    Registration_Date = input("Enter the member's registration date (YYYY-MM-DD): ").strip()
    Member_ID = input("Enter the member's ID: ").strip()
    Member_DOB = input("Enter the member's date of birth: ").strip()

    # JOIN MEMBER DETAILS WITH ":"
    member_line = ':'.join([Member_Name,
                          Member_Age,
                          Member_Contact_Number,
                          Registration_Date,
                          Member_ID,
                          Member_DOB])

    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('catalogue.txt','a') as catalogue:
        catalogue.write(member_line + "\n") 
    
    print("Member added to database successfully!")

add_new_member_to_database()



import os

# VIEW ALL EXISTING BOOK IN CATALOGUE
def view_book_in_catalogue():
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
            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()
                
                headers = lines[0].strip().split(':')
                print("|".join(headers))
                print("-"*50)

                # SORT BOOKS BY THE FIRST ALPHABET OF GENRE
                sorted_book = sorted(lines[1:], key=lambda x: x.strip().split(':')[-1][0].lower())
                current_genre = ""
                for line in sorted_book:
                    book_details = line.strip().split(':')
                    genre = book_details[-1]
                    
                    if genre[0].lower() != current_genre:
                        current_genre = genre[0].lower()
                    print("|".join(book_details))

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
        return None

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue is empty.')
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

        except FileNotFoundError:
            print("No catalogue found!")
        except Exception as e:
            print("Error reading catalogue file:", e)

search_book_from_catalogue()


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

                if book_id < 1 or book_id >= len(lines)-1:
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

    pass