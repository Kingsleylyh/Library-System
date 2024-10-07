import os
from datetime import datetime
# ADD NEW LIBRARIAN FUCNTION()
def add_librarian_to_database():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # PRINT SENTENCES  
    print('Please Enter the Librarian Details:')
    print('='*40)

    # HEADER SETTINGS
    headers = ("Name: Age: Date Of Birth: Registration Date: IC") # DEFINE COLUMN HEADERS

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('librariandatabase.txt') or os.path.getsize('librariandatabase.txt') == 0: 
        with open('librariandatabase.txt', 'w') as database:
            database.write(f"{headers}\n")


    # GET LIBRARIAN DETAILS FROM USERS
    while True:
        Librarian_Name = input("Enter the librarian's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in Librarian_Name):
            break
        else:
            print("Please enter a valid name.")

    while True:
        Librarian_Age = input("Enter the librarian's age: ").strip()
        if Librarian_Age.isdigit() and int(Librarian_Age) > 0:
            break
        else:
            print("Please enter a valid age.")

    while True:
        Librarian_DOB = input("Enter the librarian's date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(Librarian_DOB, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        Librarian_Register_Date = input("Enter the librarian's registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(Librarian_Register_Date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        Librarian_IC = input("Enter the librarian's IC: ").strip()
        if Librarian_IC.isdigit():
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    # ADD LIBRARIAN INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('librariandatabase.txt','a') as database:
        database.write(f"{Librarian_Name}:{Librarian_Age}:{Librarian_DOB}:{Librarian_Register_Date}:{Librarian_IC}\n")
    
    print("Member successfully registered!")

add_librarian_to_database()



import os

# VIEW ALL EXISTING LIBRARIAN IN CATALOGUE
def view_librarian_in_catalogue():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IF THE FILE EXISTS
    if not os.path.exists('librariandatabase.txt'):
        print('Catalogue does not exist.')
        return

    # CHECK IF THE FILE IS EMPTY
    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Catalogue is empty.')
        return
    
    else:
        try:
            # READ ALL LINES IN LIBRARIAN.TXT
            with open('librariandatabase.txt', 'r') as catalogue:
                lines = catalogue.readlines()
                
                headers = lines[0].strip().split(':')
                print("| ".join(headers))  
                print("-" * 50)  

                # SORT LIBRARIAN BY THE FIRST ALPHABET OF GENRE
                sorted_librarians = sorted(lines[1:], key=lambda x: x.split(':')[0].strip().lower())
                for line in sorted_librarians:
                    librarian_details = line.strip().split(':')
                    print("| ".join(librarian_details))
                    
        except Exception as e:
            print("Error reading catalogue file:", e)
    
view_librarian_in_catalogue()






import os
# SEARCH LIBRARIAN FROM CATALOGUE
def search_librarian_from_catalogue():
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('librariandatabase.txt'): 
        print('Catalogue does not exist.')
        return None

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Catalogue is empty.')
        return None
    
    else:
        try:
            # READ ALL LINES IN CATALOGUE.TXT
            with open('librariandatabase.txt','r') as catalogue:
                lines = catalogue.readlines()
                headers = lines[0].strip().split(':')

                # GET SEARCH TERM FROM LIBRARIAN
                search_term = input('Enter the search term: ').strip().lower()
                search_words = search_term.split()
                print('Searching for results related to', search_term,'....')
                print('-'*50)

                # SEARCH FOR BOOKS MATCHING SEARCH TERM
                found_librarian = []
                for line in lines[1:]:
                    librarian_details = line.strip().split(':')
                    combined_details = ' '.join(librarian_details).lower()

                    for word in search_words:
                        if word not in combined_details:
                            break
                    else:
                        found_librarian.append(librarian_details)
                
                # DISPLAY SEARCH RESULTS
                if found_librarian:
                    print(f"Found {len(found_librarian)} result(s)")
                    print('|'.join(headers))
                    print('-'*50)
                    for librarian in found_librarian:
                        print('|'.join(librarian))
                else:
                    print("No results found for", search_term)
                
                return lines

        except FileNotFoundError:
            print("No catalogue found!")
        except Exception as e:
            print("Error reading catalogue file:", e)

search_librarian_from_catalogue()


import os 
def edit_librarian_information(): 
    # CLEAR TERMINAL HSITORY  
    os.system('cls' if os.name == 'nt' else 'clear')

    # CHECK IS THE FILE EXISTS
    if not os.path.exists('librariandatabase.txt'): 
        print('Catalogue does not exist.')
        return

    # CHECK IS THE FILE EMPTY
    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Catalogue is empty.')
        return

    else:
        try:
            # SEARCH THE LIBRARIAN THAT WANT TO EDIT (search_librarian_from_catalogue)
            lines = search_librarian_from_catalogue()

            # DISPLAY THE BOOKS WITH IDs STARTING FROM 1
            print('Librarian in Catalogue')
            for index, line in enumerate(lines[1:], start = 1):
                print(f'{index}.{line.strip()}')

            while True:
                librarian_name_input = input("Based on your search term, please enter the librarian you want to edit: ")
                
                if not librarian_name.isalpha():
                    print("Invalid input. Please enter a valid librarian name.")
                    continue
                
                librarian_name = str(librarian_name_input)-1

                if librarian_name < 1 or librarian_name >= len(lines)-1:
                    print("Invalid librarian name")
                else:
                    break

                librarian_details = lines[librarian_name + 1].strip().split()
                print('Current Details:')
                print('|'.join(librarian_details))

                new_librarian = input("Enter new librarian (leave blank to keep current): ").strip()
                new_librarian_age = input("Enter librarian age (leave blank to keep current): ").strip()
                new_librarian_DOB = input("Enter new librarian DOB  (leave blank to keep current): ").strip()
                new_librarian_registration__date = input("Enter new librarian registration date (leave blank to keep current): ").strip()
                new_librarian_ic = input("Enter new librarian IC (leave blank to keep current): ").strip()
                
                if new_librarian:
                    librarian_details[0] = new_librarian
                if new_librarian_age:
                    librarian_details[1] = new_librarian_age
                if new_librarian_DOB:
                    librarian_details[2] = new_librarian_DOB
                if new_librarian_registration__date:
                    librarian_details[3] = new_librarian_registration__date
                if new_librarian_ic:
                    librarian_details[4] = new_librarian_ic

                lines[book_id + 1] = ':'.join(librarian_details)+ "\n"

                with open('catalogue.txt','w' ) as catalogue:
                    catalogue.writelines(lines)

                print('Book Information Update Successfully')

        except Exception as e:
            print("Error reading catalogue file:", e)

    pass