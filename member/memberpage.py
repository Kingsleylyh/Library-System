# LIBRARY MEMBER PAGE
import os
import time
from member.Member import *


def library_member_page():
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Welcome to Brickfields Kuala Lumpur Community Library Member Page:\n"
          "-----------------------------------------------------------------------\n"
          " 1. View Current Loaned Book\n"
          " 2. Update Profile Information\n"
          " 3. Search in Book Catalogues\n"
          " 4. Logout\n"
          )
      while True:
            try:
                  member_choice = int(input("Enter your choice: "))
                  if member_choice == 1:
                        view_loaned_book()
                  elif member_choice == 2:
                        update_member_information()
                  elif member_choice == 3:
                        search_display_catalogue_books()
                  elif member_choice == 4:
                        member_logout()
                  else:
                        print("Please choose numbers within 1 ~ 4.")

            except ValueError:
                  print("Invalid input. Please enter a number.")
    
def main():
      library_member_page()

if "__name__" == "__main__":
      main()
