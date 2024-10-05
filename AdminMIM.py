import os
from datetime import datetime
# ADD NEW MEMBER FUNCTION()
def add_member_to_database():
    
    # CLEAR TERMINAL HISTORY
    os.system('cls' if os.name == 'nt' else 'clear')
 
    print('Please Enter the Member Details:')
    print('='*40)

    # HEADER SETTINGS
    headers = ("Name: Age: Date Of Birth: Registration Date: IC") # DEFINE COLUMN HEADERS

    # CHECK IF THE FILE EXISTS OR IT IS EMPTY
    if not os.path.exists('memberdatabase.txt') or os.path.getsize('memberdatabase.txt') == 0: 
        with open('memberdatabase.txt', 'w') as database:
            database.write(f"{headers}\n")


    # GET MEMBER DETAILS FROM USERS
    while True:
        member_Name = input("Enter the member's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in member_Name):
            break
        else:
            print("Please enter a valid name.")

    while True:
        member_Age = input("Enter the member's age: ").strip()
        if member_Age.isdigit() and int(member_Age) > 0:
            break
        else:
            print("Please enter a valid age.")

    while True:
        member_DOB = input("Enter the member's date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(member_DOB, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_Register_Date = input("Enter the member's registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(member_Register_Date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_IC = input("Enter the member's IC: ").strip()
        if member_IC.isdigit():
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    # ADD BOOK INFORMATIONS GIVEN BY LIBRARIAN INTO FILE
    with open('memberdatabase.txt','a') as database:
        database.write(f"{member_Name}:{member_Age}:{member_DOB}:{member_Register_Date}:{member_IC}\n")
    
    print("Member successfully registered!")

add_member_to_database()



import os
# VIEW ALL EXISTING MEMBER IN database
def view_member_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('memberdatabase.txt'):
        print('Member Is Not Registered.')
        return

    elif os.path.getsize('memberdatabase.txt') == 0:
        print('Record is empty.')
        return
    
    else:
        try:
            # READ ALL LINES IN DATABASE.TXT
            with open('memberdatabase.txt', 'r') as database:
                lines = database.readlines()
                header = lines[0].strip()
                print('Member List:\n')
                print(header)
                #PRINT DIVIDER '=' ACCORDING TO LENGTH
                longest_line = max(lines, key=len)
                length_of_longest_line = len(longest_line)
                print('=' * length_of_longest_line)

                # SORT MEMBER BY NAME
                sorted_by_name = sorted(lines[1:], key = lambda x: x.strip().split(":")[-1].lower())
                current_name = ""
                for line in sorted_by_name:
                    member_details = line.strip()
                    name = member_details.split(':')[-1]
                    
                    if name != current_name:
                        current_name = name

                    print(f"{member_details}")

        except Exception as e:
            print("Error Reading Database File:", e)
    
view_member_in_database()



import os
# SEARCH MEMBER
def search_member_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('memberdatabase.txt'): 
        print('Member Is Not Registered.')
        return
    elif os.path.getsize('memberdatabase.txt') == 0:
        print('Record Is Empty.')
        return

    while True:
        with open('memberdatabase.txt', 'r') as database:
            lines = database.readlines()
        keyword = input('Please Enter A Keyword:').lower().strip()

        found_member = []
        for line in lines[1:]:
            lower_member_details = line.strip().lower()
            normal_member_details = line.strip()
            if keyword in lower_member_details:
                found_member.append(normal_member_details)

        if len(found_member) == 0:
            print(f"\nFound 0 Result(s) for '{keyword}'")
            continue_search = input("Do you wish to continue searching? (yes/no): ").strip().lower()
            if continue_search == 'yes':
                continue
            else:
                return None

        else:
            print(f'\nFound {len(found_member)} Result(s):')
            headers = lines[0].strip()
            print(headers)
            print('=' * len(headers))

            # SET INDEX FOR MEMBER IN FOUND MEMBER []
            for index, member in enumerate(found_member, start=1):
                print(f"{index}. {member}")
            return found_member

search_member_from_database()



import os
from datetime import datetime
# EDIT INFORMATION
def edit_member_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('memberdatabase.txt'): 
        print('Member Is Not Registered.')
        return

    elif os.path.getsize('memberdatabase.txt') == 0:
        print('Record Is Empty.')
        return
    
    else:
        found_member = search_member_from_database()
        if found_member is None:
            return

        while True:
            try:
                edit_index = int(input('\nPlease Enter The Index Of Member To Edit:'))
                #TO EXCLUDE HEADER AND TO LIMIT INPUTS ON INDEX SHOWN ONLY
                member_id = edit_index - 1
                if 0 <= member_id < len(found_member):
                        break
                
                else:
                    print("Please choose a valid index as shown.")

            except ValueError:
                print("Invalid input. Please enter numerical index only.")


        with open('memberdatabase.txt', 'r') as database:
            lines = database.readlines()

        original_member = found_member[member_id]
        member_details = original_member.split(':')
        line_index = lines.index(original_member + '\n')

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
                        new_details.append(member_details[i].strip())
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
                        new_details.append(member_details[i].strip())
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
                        new_details.append(member_details[i].strip())
                        break

        updated_member = ':'.join(new_details) + '\n'
        lines[line_index] = updated_member

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('memberdatabase.txt', 'w') as database:
            database.writelines(lines)

        print('Member Information Updated Successfully!')

edit_member_information()



import os
# REMOVE
def remove_member_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('memberdatabase.txt'): 
        print('Member Is Not Registered.')
        return
    elif os.path.getsize('memberdatabase.txt') == 0:
        print('Record Is Empty.')
        return
    else:
        found_member = search_member_from_database()
        if found_member is None:
            return


        while True:
            try:
                remove_index = int(input('\nPlease Enter The Index Of Member To Remove: '))
                member_id = remove_index - 1
                if 0 <= member_id < len(found_member):
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        member_to_remove = found_member[member_id]

        with open('memberdatabase.txt', 'r') as database:
            lines = database.readlines()
                    
        # REMOVE THE SELECTED MEMBER
        lines = [line for line in lines if line.strip() != member_to_remove]

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('memberdatabase.txt', 'w') as database:
            database.writelines(lines)

        print(f"Member '{member_to_remove.split(':')[0]}' has been removed from the database.")

remove_member_from_database()