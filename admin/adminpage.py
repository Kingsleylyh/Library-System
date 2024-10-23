import os
import time
from admin.final_admin import *

# SYSTEM ADMIN PAGE
def system_admin_page():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.5)
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
    
    while True:
        try:
            admin_choice = int(input("Enter the index of your choice: "))
            if admin_choice == 1:
                add_member_to_database()
            elif admin_choice == 2:
                view_member_in_database()
            elif admin_choice == 3:
                search_display_members()
            elif admin_choice == 4:
                edit_member_information()
            elif admin_choice == 5:
                remove_member_from_database()
            elif admin_choice == 6:
                add_librarian_to_database()
            elif admin_choice == 7:
                view_librarian_in_database()
            elif admin_choice == 8:
                search_display_librarian()
            elif admin_choice == 9:
                edit_librarian_information()
            elif admin_choice == 10:
                remove_librarian_from_database()
            elif admin_choice == 11:
                from login import logout
                logout()
                break

            else:
                print("Please choose numbers within 1 ~ 11.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    system_admin_page()

if __name__ == "main":
    main()
