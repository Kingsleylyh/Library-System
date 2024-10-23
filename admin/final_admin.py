import os
from datetime import datetime

"""Function to add members"""
def add_member_to_database():
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome To Add Member Page:")
 
    print('Please Enter the Member Details:')
    print('='*40)

    member_database_header = ("Name: Age: Date Of Birth: Registration Date: IC") 
    if not os.path.exists('admin/memberdatabase.txt') or os.path.getsize('admin/memberdatabase.txt') == 0: 
        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.write(f"{member_database_header}\n")

    member_header = ("Name: Username: Password: BookCount")
    if not os.path.exists('admin/member.txt') or os.path.getsize('admin/member.txt') == 0: 
        with open('admin/member.txt', 'w') as member_file:
            member_file.write(f"{member_header}\n")

    while True:
        member_name = input("Enter the member's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in member_name):
            break
        else:
            print("Please enter a valid name.")

    while True:
        member_age = input("Enter the member's age: ").strip()
        if member_age.isdigit() and int(member_age) > 0:
            break
        else:
            print("Please enter a valid age.")

    while True:
        member_dob = input("Enter the member's date of birth (YYYY-MM-DD): ").strip()
        try:      
            member_dob_strp = datetime.strptime(member_dob, "%Y-%m-%d") 
            if member_dob_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
                            
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_register_date = input("Enter the member's registration date (YYYY-MM-DD): ").strip()
        try:
            member_register_date_strp = datetime.strptime(member_register_date, "%Y-%m-%d") 
            if member_register_date_strp<= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        member_ic = input("Enter the member's IC: ").strip()
        if member_ic.isdigit() and len(member_ic) == 12:
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    while True:
        member_username = input("Enter the member's username: ").strip()
        if member_username:
            break
        else:
            print("Please enter a valid username without only spaces.")

    while True:
        member_password = input("Enter the member's password: ").strip()
        if member_password and len(member_password) <= 12:
            break
        else:
            print("Please enter a valid password without only spaces.")

    initial_book_count = 0

    with open('admin/memberdatabase.txt','a') as member_database_file:
        member_database_file.write(f"{member_name}:{member_age}:{member_dob}:{member_register_date}:{member_ic}\n")

    with open('admin/member.txt','a') as member_file:
        member_file.write(f"{member_name}:{member_username}:{member_password}:{initial_book_count}\n")
    
    print("Member successfully registered!")
    
    admin_end_choice()
    return



"""Function to view members"""
def view_member_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('admin/memberdatabase.txt'):
        print('Member Is Not Registered.')
        admin_end_choice()
        return

    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return
    
    else:
        try:
            with open('admin/memberdatabase.txt', 'r') as member_database_file:
                lines = member_database_file.readlines()

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
    return



"""Function to search books"""
def search_member():

    if not os.path.exists('admin/memberdatabase.txt'): 
        return None, [],[]
    
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        return None, [],[]

    else:
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            lines = member_database_file.readlines()
            
        keyword = input('Please Enter A Keyword:').lower().strip()

        found_members = []
        index_list = []
        for index, line in enumerate(lines[1:]):
            member_details = line.strip()

            if keyword in member_details.lower():
                found_members.append(member_details)
                index_list.append(index+1)
        
        if not found_members:
            return None, [], []
   
    return lines[0], found_members, index_list



"""Function to display search results"""
def search_display_members():
        
    os.system('cls' if os.name == 'nt' else 'clear')
   
    print("Welcome To Search Member Page:")

    header, found_members, _ = search_member()

    if found_members:
        print(f'\nFound {len(found_members)} member(s):')
        print(header.strip())
        print('=' * len(header.strip()))

        for index, members in enumerate(found_members, start=1):
            print(f"{index}. {members}")
    else:
        print("No members found matching your search.")
        admin_end_choice()
        return
            
    admin_end_choice()
    return



"""Function to edit members information"""
def edit_member_information():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Member Page:")

    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        admin_end_choice()
        return

    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
        return
    
    else:
        header, found_members, found_members_index = search_member()

        if not found_members:
            print("No members to edit.")
            admin_end_choice()
            return

        print(f'Found {len(found_members)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))

        for choice, members in enumerate(found_members, start=1):
            print(f"{choice}. {members}") 

        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Member To Edit:')) - 1
                if 0 <= choice_selected < len(found_members):
                    remove_index = found_members_index[choice_selected]
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")
  
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            member_database_lines = member_database_file.readlines()

        with open('admin/member.txt', 'r') as member_file:
            member_lines = member_file.readlines()

        original_member_database = member_database_lines[remove_index].strip().split(':')
        original_member = member_lines[remove_index].strip().split(':')

        while True:
            new_name = input(f'Enter New Name (Press Enter To Keep Current Value):').strip()
            if new_name == "":  
                break
            elif all(element.isalpha() or element.isspace() for element in new_name):
                original_member_database[0] = new_name
                original_member[0] = new_name
                break
            else:
                print("Invalid Name. Please Try Again.")
                
        while True:
            new_age = input(f'Enter New Age (Press Enter To Keep Current Age): ').strip()
            if new_age == "": 
                break
            if new_age.isdigit() and int(new_age) > 0:
                original_member_database[1] = new_age
                break
            else:
                print("No valid age entered, keeping current value.")

        while True:
            new_dob = input(f'Enter New Date Of Birth (YYYY-MM-DD) (Press Enter To Keep Current DOB): ').strip()
            if new_dob == "": 
                break
            try:
                dob_date = datetime.strptime(new_dob, "%Y-%m-%d")
                if dob_date <= datetime.now(): 
                    original_member_database[2] = new_dob
                    break                          
                else:
                    print("The date cannot be in the future.")        
            except ValueError:
                print("Invalid date format. Please enter date as YYYY-MM-DD.")

        while True:
            new_reg_date = input(f'Enter New Register Date (YYYY-MM-DD) (Press Enter To Keep Current Register Date): ').strip()
            if new_reg_date == "":  
                break
            try:
                reg_date = datetime.strptime(new_reg_date, "%Y-%m-%d")
                if reg_date <= datetime.now(): 
                    original_member_database[3] = new_reg_date
                    break                          
                else:
                    print("The date cannot be in the future.")        
            except ValueError:
                    print("Invalid date format. Please enter date as YYYY-MM-DD.")

        while True:
            new_ic = input(f'Enter New IC (Press Enter To Keep Current IC): ').strip()
            if new_ic == "":
                break
            elif new_ic.isdigit() and len(new_ic) == 12:
                original_member_database[4] = new_ic
                break
            else:
                print("Invalid IC. Please enter a valid numeric value.")

        while True:
            new_username = input(f'Enter New Member username (Press Enter To Keep Current Username): ').strip()
            if new_username == "":
                break
            elif new_username:
                original_member[1] = new_username
                break
            else:
                print("Invalid username. Please enter a valid username.")

        while True:
            new_password = input(f'Enter New Member Password (Press Enter To Keep Current Password): ').strip()
            if new_password == "":
                break
            elif new_password and len(new_password) <= 12:
                original_member[2] = new_password
                break
            else:
                print("Invalid username. Please enter a valid password.")

        updated_original_member_database = ':'.join(original_member_database) + '\n'
        updated_original_member = ':'.join(original_member) + '\n'

        member_database_lines[remove_index] = updated_original_member_database
        member_lines[remove_index] = updated_original_member

        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.writelines(member_database_lines)

        with open('admin/member.txt', 'w') as member_file:
            member_file.writelines(member_lines)
        
        print('Member Information Updated Successfully!')
    
    admin_end_choice()
    return



"""Function to remove book in catalogue"""
def remove_member_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Remove Member Page:")

    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member is not registered.')
        admin_end_choice()
        return
    
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return

    else:
        # Search
        header, found_members, found_members_index = search_member()
        
        if not found_members:
            admin_end_choice()
            return

        print(f'Found {len(found_members)} members(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        # Select 
        for choice, members in enumerate(found_members, start=1):
            print(f"{choice}. {members}")

        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Member To Remove: ')) - 1
                if 0 <= choice_selected < len(found_members):
                    remove_index = found_members_index[choice_selected]
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Delete
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            lines = member_database_file.readlines()
     
        # Pop remove line at selected index
        lines.pop(remove_index)

        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.writelines(lines)

        with open('admin/member.txt', 'r') as member_file:
            lines = member_file.readlines()
     
        # Pop remove line at selected index
        lines.pop(remove_index)

        with open('admin/member.txt', 'w') as member_file:
            member_file.writelines(lines)
        
    admin_end_choice()
    return











"""Function to add librarian"""
def add_librarian_to_database():
    
    os.system('cls' if os.name == 'nt' else 'clear')
 
    print('Please Enter the Librarian Details:')
    print('='*40)

    header = ("Name: Age: Date Of Birth: Registration Date: IC") # DEFINE COLUMN HEADERS
    if not os.path.exists('admin/librariandatabase.txt') or os.path.getsize('admin/librariandatabase.txt') == 0: 
        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.write(f"{header}\n")

    header2 = ("LibrarianID: Name: Username: Password")
    if not os.path.exists('admin/librarian.txt') or os.path.getsize('admin/librarian.txt') == 0: 
        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.write(f"{header2}\n")

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
        librarian_dob = input("Enter the librarian's date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_dob, "%Y-%m-%d")
            librarian_dob_strp = datetime.strptime(librarian_dob, "%Y-%m-%d") 
            if librarian_dob_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
            
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
            
        except ValueError:
            print("Please enter the date according to the format.")

    while True:
        librarian_ic = input("Enter the librarian's IC: ").strip()
        if librarian_ic.isdigit() and len(librarian_ic) == 12:
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    while True:
        librarian_username = input("Enter the librarian's username: ").strip()
        if librarian_username:
            break
        else:
            print("Please enter a valid username without only spaces.")

    while True:
        librarian_password = input("Enter the librarian's password: ").strip()
        if librarian_password and len(librarian_password) <= 12:
            break
        else:
            print("Please enter a valid password without only spaces.")

    with open('admin/librariandatabase.txt','a') as librarian_database_file:
        librarian_database_file.write(f"{librarian_name}:{librarian_age}:{librarian_dob}:{librarian_register_date}:{librarian_ic}\n")

    with open('admin/librarian.txt','r') as librarian_file:
        lines = librarian_file.readlines()
        if lines[1:]:
            last_line = lines[-1].strip()
            last_id = last_line.split(':')[0]
            numeric_id = int(last_id[1:]) + 1
            librarian_id = f'L{numeric_id:03d}'
        else:
            librarian_id = 'L001'

    with open('admin/librarian.txt','a') as librarian_file:
        librarian_file.write(f"{librarian_id}:{librarian_name}:{librarian_username}:{librarian_password}\n")
    
    print("Librarian successfully registered!")

    admin_end_choice()
    return



"""Function to view librarians"""
def view_librarian_in_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    if not os.path.exists('admin/librariandatabase.txt'):
        print('Librarian Is Not Registered.')
        admin_end_choice()
        return

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return
    
    else:
        try:
            with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
                lines = librarian_database_file.readlines()
                
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
    return



"""Function to search librarians"""
def search_librarian():

    if not os.path.exists('admin/librariandatabase.txt'): 
        return None, [],[]
        
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        return None, [],[]
    
    else:
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            lines = librarian_database_file.readlines()

        keyword = input('Please Enter Your Search Term:').lower().strip()

        found_librarian = []
        index_list = []
        for index, line in enumerate(lines[1:]):
            member_details = line.strip()

            if keyword in member_details.lower():
                found_librarian.append(member_details)
                index_list.append(index + 1)
        
        if not found_librarian:
            return None, [], []
   
    return lines[0], found_librarian, index_list



"""Function to display search results"""
def search_display_librarian():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Search Librarian Page:")

    header, found_librarian, _ = search_librarian()

    if found_librarian:
        print(f'\nFound {len(found_librarian)} librarian(s):')
        print(header.strip())
        print('=' * len(header.strip()))

        for index, librarian in enumerate(found_librarian, start=1):
            print(f"{index}. {librarian}")
    else:
        print("No librarians found matching your search.")
        admin_end_choice()
        return
    
    admin_end_choice()
    return



"""Function to edit librarian information"""
def edit_librarian_information():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Librarian Page:")

    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        admin_end_choice()
        return

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
        return

    else:
        header, found_librarian, found_librarian_index = search_librarian()
        
        if not found_librarian:
            print("No librarian to edit.")
            admin_end_choice()
            return

        print(f'Found {len(found_librarian)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))
            
        for choice, librarians in enumerate(found_librarian, start=1):
            print(f"{choice}. {librarians}") 

        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Librarian To Edit:')) - 1
                if 0 <= choice_selected < len(found_librarian):
                    remove_index = found_librarian_index[choice_selected]
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")
  
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            librarian_database_lines = librarian_database_file.readlines()

        with open('admin/librarian.txt', 'r') as librarian_file:
            librarian_lines = librarian_file.readlines()

        original_librarian_database = librarian_database_lines[remove_index].strip().split(':')
        original_librarian = librarian_lines[remove_index].strip().split(':')

        while True:
            new_name = input(f'Enter New Name (Press Enter To Keep Current Value):').strip()
            if new_name == "":  
                break
            elif all(element.isalpha() or element.isspace() for element in new_name):
                original_librarian_database[0] = new_name
                original_librarian[1] = new_name
                break
            else:
                print("Invalid Name. Please Try Again.")

        while True:
            new_age = input(f'Enter New Age (Press Enter To Keep Current Age): ').strip()
            if new_age == "": 
                break
            if new_age.isdigit() and int(new_age) > 0:
                original_librarian_database[1] = new_age
                break
            else:
                print("No valid age entered, keeping current value.")

        while True:
            new_dob = input(f'Enter New Date Of Birth (YYYY-MM-DD) (Press Enter To Keep Current DOB): ').strip()
            if new_dob == "": 
                break
            try:
                dob_date = datetime.strptime(new_dob, "%Y-%m-%d")
                if dob_date <= datetime.now(): 
                    original_librarian_database[2] = new_dob
                    break                          
                else:
                    print("The date cannot be in the future.")        
            except ValueError:
                print("Invalid date format. Please enter date as YYYY-MM-DD.")

        while True:
            new_reg_date = input(f'Enter New Register Date (YYYY-MM-DD) (Press Enter To Keep Current Register Date): ').strip()
            if new_reg_date == "":  
                break
            try:
                reg_date = datetime.strptime(new_reg_date, "%Y-%m-%d")
                if reg_date <= datetime.now(): 
                    original_librarian_database[3] = new_reg_date
                    break                          
                else:
                    print("The date cannot be in the future.")        
            except ValueError:
                    print("Invalid date format. Please enter date as YYYY-MM-DD.")

        while True:
            new_ic = input(f'Enter New IC (Press Enter To Keep Current IC): ').strip()
            if new_ic == "":
                break
            elif new_ic.isdigit() and len(new_ic) == 12:
                original_librarian_database[4] = new_ic
                break
            else:
                print("Invalid IC. Please enter a valid numeric value.")

        while True:
            new_username = input(f'Enter New Librarian username (Press Enter To Keep Current Username): ').strip()
            if new_username == "":
                break
            elif new_username:
                original_librarian[2] = new_username
                break
            else:
                print("Invalid username. Please enter a valid username.")

        while True:
            new_password = input(f'Enter New Librarian Password (Press Enter To Keep Current Password): ').strip()
            if new_password == "":
                break
            elif new_password and len(new_password) <= 12:
                original_librarian[3] = new_password
                break
            else:
                print("Invalid username. Please enter a valid password.")

        updated_original_librarian_database = ':'.join(original_librarian_database) + '\n'
        updated_original_librarian = ':'.join(original_librarian) + '\n'

        librarian_database_lines[remove_index] = updated_original_librarian_database
        librarian_lines[remove_index] = updated_original_librarian

        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.writelines(librarian_database_lines)

        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.writelines(librarian_lines)
        
        print('Member Information Updated Successfully!')
    
    admin_end_choice()
    return



"""Function to remove book in catalogue"""
def remove_librarian_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Remove Librarian Page:")

    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian is not registered.')
        admin_end_choice()
        return
    
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return

    else:
        # Search
        header, found_librarian, found_librarian_index = search_librarian()
        
        if not found_librarian:
            admin_end_choice()
            return

        print(f'Found {len(found_librarian)} members(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        # Select 
        for choice, librarian in enumerate(found_librarian, start=1):
            print(f"{choice}. {librarian}")

        while True:
            try:
                choice_selected = int(input('\nPlease Enter The Index Of Librarian To Remove: ')) - 1
                if 0 <= choice_selected < len(found_librarian):
                    remove_index = found_librarian_index[choice_selected]
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Delete
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            librarian_database_lines = librarian_database_file.readlines()
     
        # Pop remove line at selected index
        librarian_database_lines.pop(remove_index)

        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.writelines(librarian_database_lines)

        with open('admin/librarian.txt', 'r') as librarian_file:
            librarian_file_lines = librarian_file.readlines()
     
        # Pop remove line at selected index
        librarian_file_lines.pop(remove_index)

        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.writelines(librarian_file_lines)
        
    admin_end_choice()
    return




"""Function to prompt admin for their choice to carry out additional functions or to log out""" 
def admin_end_choice():
    from admin.adminpage import system_admin_page
    from login import logout
    while True:
        end_choice = input("\nDo you want carry out other functions ? (y/n)")
        if end_choice.lower() == 'y':
            system_admin_page()
            break
        elif end_choice.lower() == 'n':
            logout()
            break
        else:
            print("Invalid choice. Please choose y or n.")



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








