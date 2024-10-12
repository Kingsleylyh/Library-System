import os
from admin.AdminMIM import *
# SYSTEM ADMIN PAGE
def system_admin_page():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    admin_choice = int(input("Enter the index of your choice: "))
    if admin_choice == 1:
        add_member_to_database()
    elif admin_choice == 2:
        view_member_in_database()
    elif admin_choice == 3:
        search_member_from_database()
    elif admin_choice == 4:
        edit_member_information()
    elif admin_choice == 5:
        remove_member_from_database()
    elif admin_choice == 11:
        print("Thanks for visiting. Hope to see you again!")
        print("Loading...")
        import time
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        import Base
        Base.user_type()


def main():
    system_admin_page()
if __name__ == "main":
    main()
