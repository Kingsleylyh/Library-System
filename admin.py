def admin_login():
    with open("admin.txt", 'r') as info:
        lines = info.readlines()

        if len(lines) >= 4:
            name_line = lines[1].strip()
            username_line = lines[2].strip()
            password_line = lines[3].strip()
        else:
            return

        saved_username = username_line[16:]
        saved_password = password_line[10:]

    username = input("Please enter your username: ").strip()

    # Check if the entered credentials match the registered info
    if username == saved_username:
        count = 0
        while True:
            password = input("Please enter your password: ").strip()
            if password == saved_password and count < 3:
                print(f"Welcome!{name_line[11:]}.")
                system_admin_page()
                break
            elif count >= 3:
                print("Failed to login.")
                break
            else:
                count +=1
                print(f"Incorrect password! Please try again [{3 - count} attempt(s) left].")
    else:
        print("User doesn't exist.")

admin_login()



import os
from AdminMIM import *
from Logout import *
# SYSTEM ADMIN PAGE
def system_admin_page():
    os.system('cls' if os.name == 'nt' else 'clear') # CLEAR THE TERMINAL HISTORY
    print("Welcome to Brickfields Kuala Lumpur Community Library Admin Page:\n"
          "-------------------------------------------------------------------\n"
          "Member Information Management:\n"
          " 1. Add New Member Information\n"
          " 2. View All Member Information\n"
          " 3. Search Member Information\n"
          " 4. Edit Member Information\n"
          " 5. Remove Member Information\n\n"   
          "Librarian Information Management:\n"
          " 6. Add New Librarian\n"
          " 7. View All Librarian Information\n"
          " 8. Search Librarian Information\n"
          " 9. Edit Librarian Information\n"
          " 10. Remove Librarian\n"
          " 11. Logout"
          )
    librarian_choice = input("Enter the index of your choice: ")
    if librarian_choice == 1:
        add_member_to_database()
    elif librarian_choice == 2:
        view_member_in_database()
    elif librarian_choice == 3:
        search_member_from_database()
    elif librarian_choice == 4:
        edit_member_information()
    elif librarian_choice == 5:
        remove_member_from_database()
    elif librarian_choice == 11:
        logout()
        
system_admin_page()
