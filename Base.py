# PAGE TO CHOOSE USER TYPE
from admin import *
def user_type():
    print(
        "Welcome to Brickfields Kuala Lumpur Community Library login page:\n"
        "Please Select A User Type:\n"
        "   1. System Administrator\n"
        "   2. Librarian\n"
        "   3. Library Member"
    )
    while True:
        try:
            user_choice = int(input("Enter your user type (1/2/3):")) # REQUEST INPUT FROM USER
            if user_choice == 1:
                admin_login()
            elif user_choice == 2:
                librarian_page()
            elif user_choice == 3:
                library_member_page()
            else:
                print("Please choose 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

user_type()


from Librarian import *
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
    if librarian_choice == 1:
        add_book_to_catalogue()
    elif librarian_choice == 2:
        view_book_in_catalogue()
    elif librarian_choice == 3:
        search_book_from_catalogue()
    elif librarian_choice == 4:
        edit_book_information()

librarian_page()


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

library_member_page()