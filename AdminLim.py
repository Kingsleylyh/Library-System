import os
from datetime import datetime
# ADD NEW LIBRARIAN FUNCTION()
def add_librarian_to_database():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')
 
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
        librarian_name = input("Enter the librarian's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in librarian_name):
            break
        else:
            print("Please enter a valid name.")

    while True:
        librarian_age = input("Enter the librarian's age: ").strip()
        if librarian_age.isdigit() and int(librarian_age) > 0:
            break
        else:
            print("Please enter a valid age.")

    while True:
        librarian_DOB = input("Enter the librarian's date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_DOB, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        librarian_register_date = input("Enter the librarian's registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_register_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        librarian_IC = input("Enter the librarian's IC: ").strip()
        if librarian_IC.isdigit():
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    # ADD LIBRARIAN INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('librariandatabase.txt','a') as database:
        database.write(f"{librarian_name}:{librarian_age}:{librarian_DOB}:{librarian_register_date}:{librarian_IC}\n")
    
    print("Librarian successfully registered!")



import os
# VIEW ALL EXISTING LIBRARIAN IN database
def view_librarian_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('librariandatabase.txt'):
        print('Librarian Is Not Registered.')
        return

    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Record is empty.')
        return
    
    else:
        try:
            # READ ALL LINES IN DATABASE.TXT
            with open('librariandatabase.txt', 'r') as database:
                lines = database.readlines()
                header = lines[0].strip()
                print('Librarian List:\n')
                print(header)
                #PRINT DIVIDER '=' ACCORDING TO LENGTH
                longest_line = max(lines, key=len)
                length_of_longest_line = len(longest_line)
                print('=' * length_of_longest_line)

                # SORT LIBRARIAN BY NAME
                sorted_by_name = sorted(lines[1:], key = lambda x: x.strip().split(":")[-1].lower())
                current_name = ""
                for line in sorted_by_name:
                    librarian_detail = line.strip()
                    name = librarian_detail.split(':')[-1]
                    
                    if name != current_name:
                        current_name = name

                    print(f"{librarian_detail}")

        except Exception as e:
            print("Error Reading Database File:", e)
    



import os
# SEARCH LIBRARIAN
def search_librarian_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        return
    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Record Is Empty.')
        return

    while True:
        with open('librariandatabase.txt', 'r') as database:
            lines = database.readlines()
        keyword = input('Please Enter A Keyword:').lower().strip()

        found_librarian = []
        for line in lines[1:]:
            lower_librarian_detail = line.strip().lower()
            normal_librarian_detail = line.strip()
            if keyword in lower_librarian_detail:
                found_librarian.append(normal_librarian_detail)

        if len(found_librarian) == 0:
            print(f"\nFound 0 Result(s) for '{keyword}'")
            continue_search = input("Do you wish to continue searching? (yes/no): ").strip().lower()
            if continue_search == 'yes':
                continue
            else:
                return None

        else:
            print(f'\nFound {len(found_librarian)} Result(s):')
            headers = lines[0].strip()
            print(headers)
            print('=' * len(headers))

            # SET INDEX FOR LIBRARIAN IN FOUND MEMBER []
            for index, member in enumerate(found_librarian, start=1):
                print(f"{index}. {member}")
            return found_librarian





import os
from datetime import datetime
# EDIT INFORMATION
def edit_librarian_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        return

    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Record Is Empty.')
        return
    
    else:
        found_librarian = search_librarian_from_database()
        if found_librarian is None:
            return

        while True:
            try:
                edit_index = int(input('\nPlease Enter The Index Of Librarian To Edit:'))
                #TO EXCLUDE HEADER AND TO LIMIT INPUTS ON INDEX SHOWN ONLY
                librarian_id = edit_index - 1
                if 0 <= librarian_id < len(found_librarian):
                        break
                
                else:
                    print("Please choose a valid index as shown.")

            except ValueError:
                print("Invalid input. Please enter numerical index only.")


        with open('librariandatabase.txt', 'r') as database:
            lines = database.readlines()

        original_librarian = found_librarian[librarian_id]
        librarian_detail = original_librarian.split(':')
        line_index = lines.index(original_librarian + '\n')

        fields = ['Name', 'Age', 'Date Of Birth', 'Registration date', 'IC']
        new_details = []

        for i, field in enumerate(fields):
            if field == 'Name':
                while True:
                    new_value = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_value:
                        if all(x.isalpha() or x.isspace() for x in new_value):
                            new_details.append(new_value)
                            break
                        else:
                            print("Please enter a valid name.")
                    else:
                        new_details.append(librarian_detail[i].strip())
                        break
            elif field == 'Age' or field == 'IC':
                while True:
                    new_value1 = input(f'Enter New {field} (Press Enter To Keep Current Value): ').strip()
                    if new_value1:
                        if new_value1.isdigit() and int(new_value1) > 0:
                            new_details.append(new_value1)
                            break
                        else:
                            print("Please enter numerical values only.")
                    else:
                        new_details.append(librarian_detail[i].strip())
                        break
            else:
                while True:
                    new_value2 = input(f'Enter New {field} in YYYY-MM-DD (Press Enter To Keep Current Value): ').strip()
                    if new_value2:
                        try:
                            datetime.strptime(new_value2, "%Y-%m-%d")
                            new_details.append(new_value2)
                            break
                        except ValueError:
                            print("Please enter the date according to the format YYYY-MM-DD.")
                    else:
                        new_details.append(librarian_detail[i].strip())
                        break

        updated_librarian = ':'.join(new_details) + '\n'
        lines[line_index] = updated_librarian

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('librariandatabase.txt', 'w') as database:
            database.writelines(lines)

        print('Librarian Information Updated Successfully!')



import os
# REMOVE
def remove_librarian_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        return
    elif os.path.getsize('librariandatabase.txt') == 0:
        print('Record Is Empty.')
        return
    else:
        found_librarian = search_librarian_from_database()
        if found_librarian is None:
            return


        while True:
            try:
                remove_index = int(input('\nPlease Enter The Index Of Librarian To Remove: '))
                librarian_id = remove_index - 1
                if 0 <= librarian_id < len(found_librarian):
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        librarian_to_remove = found_librarian[librarian_id]

        with open('librariandatabase.txt', 'r') as database:
            lines = database.readlines()
                    
        # REMOVE THE SELECTED LIBRARIAN
        lines = [line for line in lines if line.strip() != librarian_to_remove]

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('librariandatabase.txt', 'w') as database:
            database.writelines(lines)

        print(f"Member '{librarian_to_remove.split(':')[0]}' has been removed from the database.")
