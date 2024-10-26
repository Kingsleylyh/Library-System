import os
from datetime import datetime

"""Function to add members"""
def add_member_to_database():
    # Clear the console for a better user experience
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome To Add Member Page:")
    print('Please Enter the Member Details:')
    print('=' * 40)

    # Define the header for the member database file
    member_database_header = "Name: Age: Date Of Birth: Registration Date: IC" 
    
    # Create the member database file if it doesn't exist or is empty
    if not os.path.exists('admin/memberdatabase.txt') or os.path.getsize('admin/memberdatabase.txt') == 0: 
        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.write(f"{member_database_header}\n")

    # Define the header for the member file
    member_header = "Name: Username: Password: BookCount"
    
    # Create the member file if it doesn't exist or is empty
    if not os.path.exists('admin/member.txt') or os.path.getsize('admin/member.txt') == 0: 
        with open('admin/member.txt', 'w') as member_file:
            member_file.write(f"{member_header}\n")

    # Get member's name with validation
    while True:
        member_name = input("Enter the member's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in member_name):
            break
        else:
            print("Please enter a valid name.")

    # Get member's age with validation
    while True:
        member_age = input("Enter the member's age: ").strip()
        if member_age.isdigit() and int(member_age) > 0:
            break
        else:
            print("Please enter a valid age.")

    # Get member's date of birth with validation
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

    # Get member's registration date with validation
    while True:
        member_register_date = input("Enter the member's registration date (YYYY-MM-DD): ").strip()
        try:
            member_register_date_strp = datetime.strptime(member_register_date, "%Y-%m-%d") 
            if member_register_date_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
        except ValueError:
            print("Please enter the date according to the format.")

    # Get member's IC with validation
    while True:
        member_ic = input("Enter the member's IC: ").strip()
        if member_ic.isdigit() and len(member_ic) == 12:
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    # Get member's username with validation
    while True:
        member_username = input("Enter the member's username: ").strip()
        if member_username:
            break
        else:
            print("Please enter a valid username without only spaces.")

    # Get member's password with validation
    while True:
        member_password = input("Enter the member's password: ").strip()
        if member_password and len(member_password) <= 12:
            break
        else:
            print("Please enter a valid password without only spaces.")

    initial_book_count = 0  # Set initial book count to 0

    # Append member data to the member database file
    with open('admin/memberdatabase.txt', 'a') as member_database_file:
        member_database_file.write(f"{member_name}:{member_age}:{member_dob}:{member_register_date}:{member_ic}\n")

    # Append member data to the member file
    with open('admin/member.txt', 'a') as member_file:
        member_file.write(f"{member_name}:{member_username}:{member_password}:{initial_book_count}\n")
    
    print("Member successfully registered!")
    
    admin_end_choice()  # Call function to handle admin's end choice
    return



"""Function to view members"""
def view_member_in_database():
    # Clear the console for a better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the member database file exists
    if not os.path.exists('admin/memberdatabase.txt'):
        print('Member Is Not Registered.')
        admin_end_choice()  # Redirect to the admin choice function
        return

    # Check if the member database file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()  # Redirect to the admin choice function
        return
    
    else:
        try:
            # Open and read the member database file
            with open('admin/memberdatabase.txt', 'r') as member_database_file:
                lines = member_database_file.readlines()

            # Print the header of the database
            header = lines[0].strip()
            print('Member List:\n')
            print(header)

            # Determine the length of the longest line for formatting
            longest_line = max(lines, key=len)
            length_of_longest_line = len(longest_line)
            print('=' * length_of_longest_line)

            # Sort the member records by name (case insensitive)
            sorted_by_name = sorted(lines[1:], key=lambda x: x.strip().split(":")[0].lower())
                
            current_name = ""
            # Print each member's details
            for line in sorted_by_name:
                member_details = line.strip()
                name = member_details.split(':')[0]
                    
                # Track the current name to avoid duplication in output
                if name != current_name:
                    current_name = name

                print(f"{member_details}")  # Print member details

        except Exception as e:
            print("Error Reading Database File:", e)
    
    admin_end_choice()  # Redirect to the admin choice function
    return



"""Function to search books"""
def search_member():
    # Check if the member database file exists
    if not os.path.exists('admin/memberdatabase.txt'):
        return None, [], []
    
    # Check if the member database file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        return None, [], []

    else:
        # Open and read the member database file
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            lines = member_database_file.readlines()
            
        # Prompt the user for a keyword to search
        keyword = input('Please Enter A Keyword: ').lower().strip()

        found_members = []  # List to store found member details
        index_list = []     # List to store the index of found members

        # Search through each line for the keyword
        for index, line in enumerate(lines[1:]):  # Skip the header line
            member_details = line.strip()

            # If the keyword is found in member details (case insensitive)
            if keyword in member_details.lower():
                found_members.append(member_details)  # Store the found member details
                index_list.append(index + 1)          # Store the corresponding index (1-based)

        # If no members are found, return empty lists
        if not found_members:
            return None, [], []

    return lines[0], found_members, index_list  # Return the header, found members, and their indices



"""Function to display search results"""
def search_display_members():
    # Clear the console for a clean display
    os.system('cls' if os.name == 'nt' else 'clear')
   
    # Welcome message for the search member page
    print("Welcome To Search Member Page:")

    # Call the search_member function to retrieve header and found members
    header, found_members, _ = search_member()

    # Check if any members were found
    if found_members:
        # Display the number of found members
        print(f'\nFound {len(found_members)} member(s):')
        # Print the header for the member list
        print(header.strip())
        print('=' * len(header.strip()))

        # Enumerate and display each found member with an index
        for index, members in enumerate(found_members, start=1):
            print(f"{index}. {members}")
    else:
        # Message when no members are found
        print("No members found matching your search.")
        # Call to return to the admin choice menu
        admin_end_choice()
        return
            
    # Call to return to the admin choice menu after displaying members
    admin_end_choice()
    return



"""Function to edit members information"""
def edit_member_information():
    # Clear the console for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Member Page:")

    # Check if the member database file exists
    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        admin_end_choice()
        return

    # Check if the member database file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
        return
    
    else:
        # Search for the member to edit and get relevant data
        header, found_members, found_members_index = search_member()

        if not found_members:
            print("No members to edit.")
            admin_end_choice()
            return

        print(f'Found {len(found_members)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))

        # Display the found members for selection
        for choice, members in enumerate(found_members, start=1):
            print(f"{choice}. {members}") 

        while True:
            try:
                # Get the index of the member to edit
                choice_selected = int(input('\nPlease Enter The Index Of Member To Edit:')) - 1
                if 0 <= choice_selected < len(found_members):
                    remove_index = found_members_index[choice_selected]
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")
  
        # Read the member database and member files
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            member_database_lines = member_database_file.readlines()

        with open('admin/member.txt', 'r') as member_file:
            member_lines = member_file.readlines()

        # Split the original member information into components for editing
        original_member_database = member_database_lines[remove_index].strip().split(':')
        original_member = member_lines[remove_index].strip().split(':')

        # Prompt for new name and validate input
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
                
        # Prompt for new age and validate input
        while True:
            new_age = input(f'Enter New Age (Press Enter To Keep Current Age): ').strip()
            if new_age == "": 
                break
            if new_age.isdigit() and int(new_age) > 0:
                original_member_database[1] = new_age
                break
            else:
                print("No valid age entered, keeping current value.")

        # Prompt for new date of birth and validate input
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

        # Prompt for new registration date and validate input
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

        # Prompt for new IC and validate input
        while True:
            new_ic = input(f'Enter New IC (Press Enter To Keep Current IC): ').strip()
            if new_ic == "":
                break
            elif new_ic.isdigit() and len(new_ic) == 12:
                original_member_database[4] = new_ic
                break
            else:
                print("Invalid IC. Please enter a valid numeric value.")

        # Prompt for new username and validate input
        while True:
            new_username = input(f'Enter New Member username (Press Enter To Keep Current Username): ').strip()
            if new_username == "":
                break
            elif new_username:
                original_member[1] = new_username
                break
            else:
                print("Invalid username. Please enter a valid username.")

        # Prompt for new password and validate input
        while True:
            new_password = input(f'Enter New Member Password (Press Enter To Keep Current Password): ').strip()
            if new_password == "":
                break
            elif new_password and len(new_password) <= 12:
                original_member[2] = new_password
                break
            else:
                print("Invalid username. Please enter a valid password.")

        # Update the member information in the respective lists
        updated_original_member_database = ':'.join(original_member_database) + '\n'
        updated_original_member = ':'.join(original_member) + '\n'

        # Write the updated member information back to the files
        member_database_lines[remove_index] = updated_original_member_database
        member_lines[remove_index] = updated_original_member

        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.writelines(member_database_lines)

        with open('admin/member.txt', 'w') as member_file:
            member_file.writelines(member_lines)
        
        print('Member Information Updated Successfully!')
    
    # End the admin session and return
    admin_end_choice()
    return



"""Function to remove book in catalogue"""
def remove_member_from_database():
    # Clear the console for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Remove Member Page:")

    # Check if the member database file exists
    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member is not registered.')
        admin_end_choice()
        return
    
    # Check if the member database file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return

    else:
        # Search for the member to remove and get relevant data
        header, found_members, found_members_index = search_member()
        
        if not found_members:
            admin_end_choice()
            return

        print(f'Found {len(found_members)} members(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        # Display the found members for selection
        for choice, members in enumerate(found_members, start=1):
            print(f"{choice}. {members}")

        while True:
            try:
                # Get the index of the member to remove
                choice_selected = int(input('\nPlease Enter The Index Of Member To Remove: ')) - 1
                if 0 <= choice_selected < len(found_members):
                    remove_index = found_members_index[choice_selected]
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Read the member database file
        with open('admin/memberdatabase.txt', 'r') as member_database_file:
            lines = member_database_file.readlines()
     
        # Remove the selected member from the list
        lines.pop(remove_index)

        # Write the updated member list back to the database file
        with open('admin/memberdatabase.txt', 'w') as member_database_file:
            member_database_file.writelines(lines)

        # Read the member file to remove the member entry
        with open('admin/member.txt', 'r') as member_file:
            lines = member_file.readlines()
     
        # Remove the selected member from the list
        lines.pop(remove_index)

        # Write the updated member list back to the member file
        with open('admin/member.txt', 'w') as member_file:
            member_file.writelines(lines)
        
    # End the admin session and return
    admin_end_choice()
    return








"""Function to add librarian"""
def add_librarian_to_database():
    # Clear the console for a better user experience
    os.system('cls' if os.name == 'nt' else 'clear')
 
    print('Please Enter the Librarian Details:')
    print('='*40)

    # Define column headers for the librarian database
    header = ("Name: Age: Date Of Birth: Registration Date: IC") 
    # Create librarian database file if it doesn't exist or is empty
    if not os.path.exists('admin/librariandatabase.txt') or os.path.getsize('admin/librariandatabase.txt') == 0: 
        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.write(f"{header}\n")

    # Define column headers for the librarian login file
    header2 = ("LibrarianID: Name: Username: Password")
    # Create librarian login file if it doesn't exist or is empty
    if not os.path.exists('admin/librarian.txt') or os.path.getsize('admin/librarian.txt') == 0: 
        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.write(f"{header2}\n")

    # Input validation for librarian's name
    while True:
        librarian_name = input("Enter the librarian's name: ").strip()
        if all(x.isalpha() or x.isspace() for x in librarian_name):
            break
        else:
            print("Please enter a valid name.")

    # Input validation for librarian's age
    while True:
        librarian_age = input("Enter the librarian's age: ").strip()
        if librarian_age.isdigit() and int(librarian_age) > 0:
            break
        else:
            print("Please enter a valid age.")

    # Input validation for librarian's date of birth
    while True:
        librarian_dob = input("Enter the librarian's date of birth (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_dob, "%Y-%m-%d")  # Validate date format
            librarian_dob_strp = datetime.strptime(librarian_dob, "%Y-%m-%d") 
            if librarian_dob_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
        except ValueError:
            print("Please enter the date according to the format.")

    # Input validation for librarian's registration date
    while True:
        librarian_register_date = input("Enter the librarian's registration date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(librarian_register_date, "%Y-%m-%d")  # Validate date format
            librarian_register_date_strp = datetime.strptime(librarian_register_date, "%Y-%m-%d") 
            if librarian_register_date_strp <= datetime.now(): 
                break
            else:
                print("The date cannot be in the future. Please enter a past or current date.")
        except ValueError:
            print("Please enter the date according to the format.")

    # Input validation for librarian's IC
    while True:
        librarian_ic = input("Enter the librarian's IC: ").strip()
        if librarian_ic.isdigit() and len(librarian_ic) == 12:
            break
        else:
            print("Please enter a valid 12 digit IC number.")

    # Input validation for librarian's username
    while True:
        librarian_username = input("Enter the librarian's username: ").strip()
        if librarian_username:
            break
        else:
            print("Please enter a valid username without only spaces.")

    # Input validation for librarian's password
    while True:
        librarian_password = input("Enter the librarian's password: ").strip()
        if librarian_password and len(librarian_password) <= 12:
            break
        else:
            print("Please enter a valid password without only spaces.")

    # Append librarian details to the librarian database file
    with open('admin/librariandatabase.txt','a') as librarian_database_file:
        librarian_database_file.write(f"{librarian_name}:{librarian_age}:{librarian_dob}:{librarian_register_date}:{librarian_ic}\n")

    # Read the librarian file to determine the next available Librarian ID
    with open('admin/librarian.txt','r') as librarian_file:
        lines = librarian_file.readlines()
        if lines[1:]:
            last_line = lines[-1].strip()
            last_id = last_line.split(':')[0]
            numeric_id = int(last_id[1:]) + 1  # Increment the numeric part of the last ID
            librarian_id = f'L{numeric_id:03d}'  # Format new ID with leading zeros
        else:
            librarian_id = 'L001'  # Start with the first ID if file is empty

    # Append librarian login details to the librarian file
    with open('admin/librarian.txt','a') as librarian_file:
        librarian_file.write(f"{librarian_id}:{librarian_name}:{librarian_username}:{librarian_password}\n")
    
    print("Librarian successfully registered!")  # Confirmation message

    admin_end_choice()  # End the admin session and return
    return



"""Function to view librarians"""
def view_librarian_in_database():
    # Clear the console for a better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the librarian database file exists
    if not os.path.exists('admin/librariandatabase.txt'):
        print('Librarian Is Not Registered.')
        admin_end_choice()  # End admin session
        return

    # Check if the librarian database file is empty
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()  # End admin session
        return
    
    else:
        try:
            # Read lines from the librarian database file
            with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
                lines = librarian_database_file.readlines()
                
            header = lines[0].strip()  # Get header line
            print('Librarian List:\n')
            print(header)  # Print the header

            # Determine the length of the longest line for formatting
            longest_line = max(lines, key=len)
            length_of_longest_line = len(longest_line)
            print('=' * length_of_longest_line)  # Print separator

            # Sort librarian records by name (case insensitive)
            sorted_by_name = sorted(lines[1:], key=lambda x: x.strip().split(":")[0].lower())

            current_name = ""  # Variable to keep track of the current name
            for line in sorted_by_name:
                librarian_detail = line.strip()
                name = librarian_detail.split(':')[0]  # Extract the librarian's name
                    
                if name != current_name:  # Update current name for grouping
                    current_name = name

                print(f"{librarian_detail}")  # Print librarian details

        except Exception as e:
            print("Error Reading Database File:", e)  # Handle file reading errors

    admin_end_choice()  # End the admin session
    return



"""Function to search librarians"""
def search_librarian():
    # Check if the librarian database file exists
    if not os.path.exists('admin/librariandatabase.txt'): 
        return None, [],[]  # Return empty results

    # Check if the librarian database file is empty
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        return None, [],[]  # Return empty results
    
    else:
        # Read lines from the librarian database file
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            lines = librarian_database_file.readlines()

        # Prompt user for a search term
        keyword = input('Please Enter Your Search Term:').lower().strip()

        found_librarian = []  # List to store found librarian details
        index_list = []  # List to store indexes of found librarians
        for index, line in enumerate(lines[1:]):  # Start from the second line
            member_details = line.strip()

            # Check if the keyword is in the librarian details
            if keyword in member_details.lower():
                found_librarian.append(member_details)  # Add found details to the list
                index_list.append(index + 1)  # Add the index (adjusted for header)

        if not found_librarian:
            return None, [], []  # Return empty results if no matches found
   
    return lines[0], found_librarian, index_list  # Return header, found details, and indexes



"""Function to display search results"""
def search_display_librarian():
    # Clear the console for a better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Search Librarian Page:")

    # Call the search_librarian function to find matching librarians
    header, found_librarian, _ = search_librarian()

    # Check if any librarians were found
    if found_librarian:
        print(f'\nFound {len(found_librarian)} librarian(s):')  # Display number of found librarians
        print(header.strip())  # Print the header
        print('=' * len(header.strip()))  # Print separator

        # Enumerate through the found librarians and print their details
        for index, librarian in enumerate(found_librarian, start=1):
            print(f"{index}. {librarian}")  # Print each librarian's details with an index
    else:
        print("No librarians found matching your search.")  # Inform user if no matches found
        admin_end_choice()  # End admin session if no matches
        return
    
    admin_end_choice()  # End the admin session after displaying results
    return



"""Function to edit librarian information"""
def edit_librarian_information():
    # Clear the console for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome To Edit Librarian Page:")

    # Check if the librarian database file exists and is not empty
    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian Is Not Registered.')
        admin_end_choice()
        return

    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record Is Empty.')
        admin_end_choice()
        return

    else:
        # Search for librarians in the database
        header, found_librarian, found_librarian_index = search_librarian()
        
        # Check if any librarian was found
        if not found_librarian:
            print("No librarian to edit.")
            admin_end_choice()
            return

        print(f'Found {len(found_librarian)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip()))
            
        # Display found librarians and prompt for selection
        for choice, librarians in enumerate(found_librarian, start=1):
            print(f"{choice}. {librarians}") 

        while True:
            try:
                # User selects librarian to edit
                choice_selected = int(input('\nPlease Enter The Index Of Librarian To Edit:')) - 1
                if 0 <= choice_selected < len(found_librarian):
                    remove_index = found_librarian_index[choice_selected]
                    break                   
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")
  
        # Read current librarian details from the database files
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            librarian_database_lines = librarian_database_file.readlines()

        with open('admin/librarian.txt', 'r') as librarian_file:
            librarian_lines = librarian_file.readlines()

        # Store original librarian details for editing
        original_librarian_database = librarian_database_lines[remove_index].strip().split(':')
        original_librarian = librarian_lines[remove_index].strip().split(':')

        # Prompt for new librarian details with validation
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

        # Create updated entries for the librarian
        updated_original_librarian_database = ':'.join(original_librarian_database) + '\n'
        updated_original_librarian = ':'.join(original_librarian) + '\n'

        # Update the database files with the new information
        librarian_database_lines[remove_index] = updated_original_librarian_database
        librarian_lines[remove_index] = updated_original_librarian

        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.writelines(librarian_database_lines)

        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.writelines(librarian_lines)
        
        print('Member Information Updated Successfully!')  # Confirm successful update
    
    admin_end_choice()  # End the admin session
    return



"""Function to remove book in catalogue"""
def remove_librarian_from_database():
    # Clear the console for better user experience
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to Remove Librarian Page:")

    # Check if the librarian database file exists and is not empty
    if not os.path.exists('admin/librariandatabase.txt'): 
        print('Librarian is not registered.')
        admin_end_choice()
        return
    
    elif os.path.getsize('admin/librariandatabase.txt') == 0:
        print('Record is empty.')
        admin_end_choice()
        return

    else:
        # Search for librarians in the database
        header, found_librarian, found_librarian_index = search_librarian()
        
        # Check if any librarian was found
        if not found_librarian:
            admin_end_choice()
            return

        print(f'Found {len(found_librarian)} member(s):\n')
        print(header.strip()) 
        print('=' * len(header.strip())) 

        # Display found librarians and prompt for selection
        for choice, librarian in enumerate(found_librarian, start=1):
            print(f"{choice}. {librarian}")

        while True:
            try:
                # User selects librarian to remove
                choice_selected = int(input('\nPlease Enter The Index Of Librarian To Remove: ')) - 1
                if 0 <= choice_selected < len(found_librarian):
                    remove_index = found_librarian_index[choice_selected]
                    break
                else:
                    print("Invalid Index. Please Try Again.")
            except ValueError:
                print("Invalid Input. Please Enter a Number.")

        # Read current librarian details from the database files
        with open('admin/librariandatabase.txt', 'r') as librarian_database_file:
            librarian_database_lines = librarian_database_file.readlines()
     
        # Remove the selected librarian from the database
        librarian_database_lines.pop(remove_index)

        # Write the updated lines back to the database file
        with open('admin/librariandatabase.txt', 'w') as librarian_database_file:
            librarian_database_file.writelines(librarian_database_lines)

        # Read the librarian file to remove the corresponding line
        with open('admin/librarian.txt', 'r') as librarian_file:
            librarian_file_lines = librarian_file.readlines()
     
        # Remove the selected librarian from the file
        librarian_file_lines.pop(remove_index)

        # Write the updated lines back to the librarian file
        with open('admin/librarian.txt', 'w') as librarian_file:
            librarian_file.writelines(librarian_file_lines)
        
    admin_end_choice()  # End the admin session
    return



"""Function to prompt admin for their choice to carry out additional functions or to log out""" 
def admin_end_choice():
    # Import necessary functions for navigating the admin system and logging out
    from admin.adminpage import system_admin_page
    from login import logout
    
    while True:
        # Prompt the admin for whether they want to perform more actions
        end_choice = input("\nDo you want to carry out other functions? (y/n): ")
        
        if end_choice.lower() == 'y':
            # If yes, redirect to the admin system page
            system_admin_page()
            break
        elif end_choice.lower() == 'n':
            # If no, log out and end the session
            logout()
            break
        else:
            # Handle invalid input
            print("Invalid choice. Please choose y or n.")




"""def main():
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
    main()"""








