# PAGE TO CHOOSE USER TYPE
def user_type():
    print(
        "Welcome to Brickfields Kuala Lumpur Community Library:\n"
        "Please Select A User Type:\n "
        "   1. System Administrator\n"
        "   2. Librarian\n"
        "   3. Library Member"
    )
    user_type = input("Enter your user type (1/2/3): ")

user_type()


# PAGE FOR SYSTEM ADMIN
def system_admin_page():
    print("Welcome to Brickfields Kuala Lumpur Community Library Admin Page:\n"
          
          "Member Information Management:\n"
          " 1. Add New Member\n"
          " 2. View All Member Information\n"
          " 3. Search Member Information\n"
          " 4. Edit Member Information\n"
          " 5. Remove Member Information\n"

          "Librarian Information Management\n"
          " 6. Add New Librarian\n"
          " 7. View All Librarian Information\n"
          " 8. Search Librarian Information\n"
          " 9. Edit Librarian Information\n"
          " 10. Remove Librarian\n"

          " 11. Logout"
          )
    admin_choice = input("Enter your choice: ")

system_admin_page()






