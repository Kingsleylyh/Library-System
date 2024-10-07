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