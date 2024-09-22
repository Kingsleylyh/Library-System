# PAGE TO CHOOSE USER TYPE
def user_type():
    print(
        "Welcome to Brickfields Kuala Lumpur Community Library:\n"
        "Please Select A User Type:\n"
        "   1. System Administrator\n"
        "   2. Librarian\n"
        "   3. Library Member"
    )
    while True:
        try:
            user_choice = int(input("Enter your user type (1/2/3):")) # REQUEST INPUT FROM USER
            if user_choice == 1:
                system_admin_page()
            elif user_choice == 2:
                librarian_page()
            elif user_choice == 3:
                library_member_page()
            else:
                print("Please choose 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


import os
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
    admin_choice = input("Enter your choice: ")


# LIBRARIAN PAGE
def librarian_page():
    os.system('cls' if os.name == 'nt' else 'clear') # CLEAR THE TERMINAL HISTORY
    print("Welcome to Brickfields Kuala Lumpur Community Library Librarian Page:\n"
          "-----------------------------------------------------------------------\n"
          "Book Catalogue Management:\n"
          " 1. Add New Book\n"
          " 2. View All Existing Book In Catalogue\n"
          " 3. Search Book From The Catalogue\n"
          " 4. Edit Book Information\n"
          " 5. Remove Book From Catalogue\n\n"
          " 6. Perform Book Loan Process\n"
          " 7. Logout\n"
          )
    librarian_choice = input("Enter your choice: ")


# LIBRARY MEMBER PAGE
def library_member_page():
    os.system('cls' if os.name == 'nt' else 'clear') # CLEAR THE TERMINAL HISTORY
    print("Welcome to Brickfields Kuala Lumpur Community Library Member Page:\n"
          "-----------------------------------------------------------------------\n"
          " 1. View Current Loaned Book\n"
          " 2. Update Profile Information\n"
          " 3. Search Book Catalogues\n\n"
          " 4. Logout\n"
          )
    librarian_member_choice = input("Enter your choice: ")
    

user_type()
