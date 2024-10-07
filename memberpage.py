# LIBRARY MEMBER PAGE
import os
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
