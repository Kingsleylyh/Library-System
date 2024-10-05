import os
# ADD BOOK FUCNTION()
def add_book_to_catalogue():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # PRINT SENTENCES  
    print('Please Enter The Book Details:')
    print('='*40)

    # HEADER SETTINGS
    headers = ("Title: Author: Publisher: Publication Date: ISBN: Genre") # DEFINE COLUMN HEADERS

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('catalogue.txt') or os.path.getsize('catalogue.txt') == 0: 
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.write(f"{headers}\n")

    # GET BOOK DETAILS FROM USERS
    book_title = input("Enter The Book's title: ").strip()
    book_author = input("Enter The Book's author: ").strip()
    book_publisher = input("Enter The Book's publisher: ").strip()
    book_publication_date = input("Enter The Book's publication date (YYYY-MM-DD): ").strip()
    book_isbn = input("Enter The Book's ISBN: ").strip()
    book_genre = input("Enter The Book's genre: ").strip()

    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('catalogue.txt','a') as catalogue:
        catalogue.write(f"{book_title}:{book_author}:{book_publisher}:{book_publication_date}:{book_isbn}:{book_genre}\n")
    
    print("Book Added To Catalogue Successfully!")

add_book_to_catalogue()





import os
# VIEW ALL EXISTING BOOK IN CATALOGUE
def view_book_in_catalogue():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('catalogue.txt'):
        print('Catalogue Does Not Exist.')
        return

    #CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        try:
            # READ ALL LINES IN CATALOGUE.TXT
            with open('catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()

                header = lines[0].strip()
                
                print('Catalogue List:\n')

                print(header)

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
            print("Error Reading Catalogue File:", e)
    
view_book_in_catalogue()





import os
# SEARCH BOOK FROM CATALOGUE
def search_book_from_catalogue():
    # CLEAR TERMIANL HSITORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXIST
    if not os.path.exists('catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        return

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        with open('catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()
        
        search_term = input('Please Enter Your Search Term:')
        search_term = search_term.lower().strip()

        found_book = []
        for line in lines[1:]:
            lower_book_details = line.strip().lower()
            normal_book_details = line.strip()
            if search_term in lower_book_details:
                found_book.append(normal_book_details)
        

        print(f'\nFound {len(found_book)} Result(s):')

        headers = lines[0].strip()
        print(headers)

        print('=' * len(headers))

        for index,book in enumerate (found_book,start = 1):  # SET INDEX FOR BOOKS IN FOUND BOOK []
            print(f"{index}. {book}")

        return found_book
    
search_book_from_catalogue()
    




def edit_book_information():

    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('catalogue.txt'): 
        print('Catalogue Does Not Exist.')
        return

    elif os.path.getsize('catalogue.txt') == 0:
        print('Catalogue Is Empty.')
        return
    
    else:
        found_book = search_book_from_catalogue() 

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


        with open('catalogue.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        original_book = found_book[book_id]
        book_details = original_book.split(':')
        line_index = lines.index(original_book + '\n')

        fields = ['title', 'author', 'publisher', 'publication date', 'ISBN', 'genre']
        new_details = []

        for i, field in enumerate(fields):
            new_value = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
            if new_value:
                new_details.append(new_value)
            else:
                new_details.append(book_details[i].strip())

        updated_book = ':'.join(new_details) + '\n'
        lines[line_index] = updated_book

        # Write back the updated lines to the catalogue
        with open('catalogue.txt', 'w') as catalogue:
            catalogue.writelines(lines)

        print('Book Information Updated Successfully.')

edit_book_information()

