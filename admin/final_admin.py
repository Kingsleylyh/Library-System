import os
import time
from datetime import datetime

"""Function to add members"""
def add_member_to_database():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome To Add Member Page:")
 
    print('Please Enter the Member Details:')
    print('='*40)

    headers = ("Name: Age: Date Of Birth: Registration Date: IC") 
    if not os.path.exists('admin/memberdatabase.txt') or os.path.getsize('admin/memberdatabase.txt') == 0: 
        with open('admin/memberdatabase.txt', 'w') as database:
            database.write(f"{headers}\n")

    headers2 = ("Name: Username: Password: BookCount")
    if not os.path.exists('admin/member.txt') or os.path.getsize('admin/member.txt') == 0: 
        with open('admin/member.txt', 'w') as database:
            database.write(f"{headers2}\n")

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
            member_date_of_birth = datetime.strptime(member_DOB, "%Y-%m-%d") 
            if member_date_of_birth<= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
                            
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_Register_Date = input("Enter the member's registration date (YYYY-MM-DD): ").strip()
        try:
            member_Register_Date_strp = datetime.strptime(member_Register_Date, "%Y-%m-%d") 
            if member_Register_Date_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_IC = input("Enter the member's IC: ").strip()
        if member_IC.isdigit():
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    while True:
        member_username = input("Enter the member's username: ").strip()
        if member_username and not member_username.isspace():
            break
        else:
            print("Please enter a valid username without only spaces.")

    while True:
        member_password = input("Enter the member's password: ").strip()
        if member_password and not member_password.isspace():
            break
        else:
            print("Please enter a valid password without only spaces.")

    initial_book_count = 0

    with open('admin/memberdatabase.txt','a') as database:
        database.write(f"{member_Name}:{member_Age}:{member_DOB}:{member_Register_Date}:{member_IC}\n")

    with open('admin/member.txt','a') as database:
        database.write(f"{member_Name}:{member_username}:{member_password}:{initial_book_count}\n")
    
    print("Member successfully registered!")
    
    admin_end_choice()



"""Function to view members"""
def view_member_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('admin/memberdatabase.txt'):
        print('Member Is Not Registered.')
        admin_end_choice()

    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
    
    else:
        try:
            with open('admin/memberdatabase.txt', 'r') as database:
                lines = database.readlines()

            header = lines[0].strip()
            print('Member List:\n')
            print(header)

            longest_line = max(lines, key=len)
            length_of_longest_line = len(longest_line)
            print('=' * length_of_longest_line)

            sorted_by_name = sorted(lines[1:], key = lambda x: x.strip().split(":")[0].lower())
                
            current_name = ""
            for line in sorted_by_name:
                member_details = line.strip()
                name = member_details.split(':')[0]
                    
                if name != current_name:
                    current_name = name

                print(f"{member_details}")

        except Exception as e:
            print("Error Reading Database File:", e)
    
    admin_end_choice()



"""Function to search books"""
def search_member():

    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        admin_end_choice()
    
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()

    else:
        with open('admin/memberdatabase.txt', 'r') as database:
            lines = database.readlines()
            
        keyword = input('Please Enter A Keyword:').lower().strip()

        found_members = []
        for line in lines[1:]:
            lower_member_details = line.strip().lower()
            normal_member_details = line.strip()

            if keyword in lower_member_details:
                found_members.append(normal_member_details)
        
        return lines[0], found_members



"""Function to display search results"""
def search_display_members():
        
    os.system('cls' if os.name == 'nt' else 'clear')
   
    print("Welcome To Search Member Page:")

    header, found_members = search_member()

    if found_members:
        print(f'Found {len(found_members)} member(s):')

        print(header.strip())

        print('=' * len(header.strip()))

        for index, members in enumerate(found_members, start=1):
            print(f"{index}. {members}")

    else:
        print("No members found matching your search.")
        admin_end_choice()
            
    admin_end_choice()



"""Function to edit members information"""
def edit_member_information():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Member Page:")

    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        admin_end_choice()

    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
    
    else:
        header, found_members = search_member()

        if not found_members:
            print("No members to edit.")
            admin_end_choice()

        print(f'Found {len(found_members)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))
            
        for index, members in enumerate(found_members, start=1):
            print(f"{index}. {members}") 

        while True:
            try:
                edit_index = int(input('\nPlease Enter The Index Of Member To Edit:'))
                member_id = edit_index - 1

                if 0 <= member_id < len(found_members):
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")
  

        with open('admin/memberdatabase.txt', 'r') as database:
            lines = database.readlines()

        original_member = found_members[member_id]
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
                            # Ensure the input follows the correct date format
                            member_date = datetime.strptime(new_value2, "%Y-%m-%d") 

                            # Check if the date is today or in the past
                            if member_date <= datetime.now(): 
                                new_details.append(new_value2)
                                break
                            else:
                                print("The date cannot be in the future. Please enter a past or current date.")
                            
                        except ValueError:
                            print("Please enter the date according to the format YYYY-MM-DD.")
                    else:
                        new_details.append(member_details[i].strip())
                        break

        updated_member = ':'.join(new_details) + '\n'
        
        lines[line_index] = updated_member

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('admin/memberdatabase.txt', 'w') as database:
            database.writelines(lines)

        print('Member Information Updated Successfully!')

    admin_end_choice()



"""Function to remove book in catalogue"""
def remove_member_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Remove Member Page:")

    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        admin_end_choice()
    
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()

    else:
        header, found_members = search_member()
        
        if not found_members:
            admin_end_choice

        print(f'Found {len(found_members)} members(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        for index, members in enumerate(found_members, start=1):
            print(f"{index}. {members}")

        while True:
            try:
                remove_index = int(input('\nPlease Enter The Index Of Member To Remove: '))
                member_id = remove_index - 1

                if 0 <= member_id < len(found_members):
                    break

                else:
                    print("Invalid Index. Please Try Again.")

            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        member_to_remove = found_members[member_id]

        with open('admin/memberdatabase.txt', 'r') as database:
            lines = database.readlines()
                    
        # REMOVE THE SELECTED MEMBER
        lines = [line for line in lines if line.strip() != member_to_remove]

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('admin/memberdatabase.txt', 'w') as database:
            database.writelines(lines)

        print(f"Member '{member_to_remove.split(':')[0]}' has been removed from the database.")
        
    admin_end_choice()















"""Function to add librarian"""
def add_librarian_to_database():
    
    os.system('cls' if os.name == 'nt' else 'clear')
 
    print('Please Enter the Librarian Details:')
    print('='*40)

    headers = ("Name: Age: Date Of Birth: Registration Date: IC") # DEFINE COLUMN HEADERS
    if not os.path.exists('admin/librariandatabase.txt') or os.path.getsize('admin/librariandatabase.txt') == 0: 
        with open('admin/librariandatabase.txt', 'w') as database:
            database.write(f"{headers}\n")

    headers2 = ("LibrarianID: Name: Username: Password")
    if not os.path.exists('admin/librarian.txt') or os.path.getsize('admin/librarian.txt') == 0: 
        with open('admin/librarian.txt', 'w') as database:
            database.write(f"{headers2}\n")

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
            librarian_DOB_strp = datetime.strptime(librarian_DOB, "%Y-%m-%d") 
            if librarian_DOB_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        librarian_register_date = input("Enter the librarian's registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_register_date, "%Y-%m-%d")
            librarian_register_date_strp = datetime.strptime(librarian_register_date, "%Y-%m-%d") 
            if librarian_register_date_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
            break
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        librarian_IC = input("Enter the librarian's IC: ").strip()
        if librarian_IC.isdigit():
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    while True:
        librarian_username = input("Enter the librarian's username: ").strip()
        if librarian_username and not librarian_username.isspace():
            break
        else:
            print("Please enter a valid username without only spaces.")

    while True:
        librarian_password = input("Enter the librarian's password: ").strip()
        if librarian_password and not librarian_password.isspace():
            break
        else:
            print("Please enter a valid password without only spaces.")

    with open('admin/librariandatabase.txt','a') as database:
        database.write(f"{librarian_name}:{librarian_age}:{librarian_DOB}:{librarian_register_date}:{librarian_IC}\n")

    with open('admin/librarian.txt','r') as database:
        lines = database.readlines()
        if lines[1:]:
            last_line = lines[-1].strip()
            last_id = last_line.split(':')[0]
            numeric_id = int(last_id[1:]) + 1
            librarian_id = f'L{numeric_id:03d}'
        else:
            librarian_id = 'L001'

    with open('admin/librarian.txt','a') as database:
        database.write(f"{librarian_id}:{librarian_name}:{librarian_username}:{librarian_password}\n")
    
    print("Librarian successfully registered!")

    admin_end_choice()



"""Function to view librarians"""
def view_librarian_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('admin/librariandatabase.txt'):
        print('Librarian Is Not Registered.')
        admin_end_choice()

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
    
    else:
        try:
            with open('admin/librariandatabase.txt', 'r') as database:
                lines = database.readlines()
                
            header = lines[0].strip()
            print('Librarian List:\n')
            print(header)

            longest_line = max(lines, key=len)
            length_of_longest_line = len(longest_line)
            print('=' * length_of_longest_line)

            sorted_by_name = sorted(lines[1:], key = lambda x: x.strip().split(":")[0].lower())

            current_name = ""
            for line in sorted_by_name:
                librarian_detail = line.strip()
                name = librarian_detail.split(':')[0]
                    
                if name != current_name:
                    current_name = name

                print(f"{librarian_detail}")

        except Exception as e:
            print("Error Reading Database File:", e) 

    admin_end_choice()



"""Function to search librarians"""
def search_librarian():

    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Catalogue Does Not Exist.')
        admin_end_choice()

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Catalogue Is Empty.')
        admin_end_choice()
    
    else:
        with open('admin/librariandatabase.txt', 'r') as catalogue:
            lines = catalogue.readlines()

        search_term = input('Please Enter Your Search Term:').lower().strip()

        found_librarian = []
        
        for line in lines[1:]:
            librarian_detail = line.strip().lower()  

            if search_term in librarian_detail:
                found_librarian.append(librarian_detail) 
        
        return lines[0], found_librarian



"""Function to display search results"""
def search_display_librarian():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Search Librarian Page:")

    header, found_librarian = search_librarian()

    if found_librarian:
        print(f'Found {len(found_librarian)} librarian(s):')

        print(header.strip())

        print('=' * len(header.strip()))

        for index, librarian in enumerate(found_librarian, start=1):
            print(f"{index}. {librarian}")

    else:
        print("No librarians found matching your search.")
        admin_end_choice()
    
    admin_end_choice()



"""Function to edit librarian information"""
def edit_librarian_information():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Librarian Page:")

    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        admin_end_choice()

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
    
    else:
        header, found_librarian = search_librarian()
        
        if not found_librarian:
            print("No librarian to edit.")
            admin_end_choice()

        print(f'Found {len(found_librarian)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))
            
        for index, librarians in enumerate(found_librarian, start=1):
            print(f"{index}. {librarians}") 

        while True:
            try:
                edit_index = int(input('\nPlease Enter The Index Of Librarian To Edit:'))                
                librarian_id = edit_index - 1 # TO EXCLUDE HEADER AND TO LIMIT INPUTS ON INDEX SHOWN ONLY

                if 0 <= librarian_id < len(found_librarian):
                        break
                
                else:
                    print("Invalid Index. Please Try Again.")

            except ValueError:
                print("Invalid Input. Please Enter a Number.")


        with open('admin/librariandatabase.txt', 'r') as database:
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
                            # Ensure the input follows the correct date format
                            librarian_date = datetime.strptime(new_value2, "%Y-%m-%d") 

                            # Check if the date is today or in the past
                            if librarian_date <= datetime.now(): 
                                new_details.append(new_value2)
                                break
                            else:
                                print("The date cannot be in the future. Please enter a past or current date.")

                        except ValueError:
                            print("Please enter the date according to the format YYYY-MM-DD.")
                    else:
                        new_details.append(librarian_detail[i].strip())
                        break

        updated_librarian = ':'.join(new_details) + '\n'
        lines[line_index] = updated_librarian

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('admin/librariandatabase.txt', 'w') as database:
            database.writelines(lines)

        print('Librarian Information Updated Successfully!')
    
    admin_end_choice()



"""Function to remove book in catalogue"""
def remove_librarian_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        admin_end_choice()
    
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
    
    else:
        header, found_librarian = search_librarian()

        if not found_librarian:
            admin_end_choice()

        print(f'Found {len(found_librarian)} members(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        for index, members in enumerate(found_librarian, start=1):
            print(f"{index}. {members}")

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

        with open('admin/librariandatabase.txt', 'r') as database:
            lines = database.readlines()
                    
        # REMOVE THE SELECTED LIBRARIAN
        lines = [line for line in lines if line.strip() != librarian_to_remove]

        # WRITE BACK THE UPDATED LINES IN THE DATABASE
        with open('admin/librariandatabase.txt', 'w') as database:
            database.writelines(lines)

        print(f"Librarian '{librarian_to_remove.split(':')[0]}' has been removed from the database.")

    admin_end_choice()



"""Function to prompt admin for their choice to carry out additional functions or to log out""" 
def admin_end_choice():
    while True:
        end_choice = input("\nDo you want carry out other functions ? (y/n)")
        if end_choice.lower() == 'y':
            from admin.adminpage import system_admin_page
            system_admin_page()

        elif end_choice.lower() == 'n':
            admin_logout()

        else:
            print("Invalid choice. Please choose y or n.")



"""Function to handle the admin logout process."""
def admin_logout():
    from Base import user_type 
    print("Logging out...")
    time.sleep(2) 
    user_type()



def main():
    add_member_to_database()
    view_member_in_database()
    search_display_members()
    edit_member_information()
    remove_member_from_database()

    add_librarian_to_database()
    view_librarian_in_database()
    search_display_librarian()
    edit_librarian_information()
    remove_librarian_from_database()

if "__name__" == "__main__":
    main()








