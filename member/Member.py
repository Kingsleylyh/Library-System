import os
import datetime

def view_loaned_books(books, member):

    # Clear terminal history
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the file exists
    if not os.path.exists('librarian/catalogue.txt'):
        print('Catalogue does not exist.')
        return

    # Check if the file is empty
    elif os.path.getsize('librarian/catalogue.txt') == 0:
        print('Catalogue is empty.')
        return
    
    else:
        try:
            # View the member's loaned books with due dates and overdue fees
            with open('librarian/catalogue.txt', 'r') as catalogue:
                lines = catalogue.readlines()
                header = lines[0].strip()
        
                loaned_books = []
                for book in books:
                    if book['member_id'] == member['id']:
                        loaned_books.append(book)
                if loaned_books:
                    print("Your loaned books: ")
                    for book in loaned_books:
                        print(f"Tile: {book['title']}")
                        print(f"Author: {book['author']}")
                        print(f"Publisher: {book['publisher']}")
                        print(f"Publication Date: {book['publication date']}")
                        print(f"ISBN: {book['isbn']}")
                        print(f"Genre: {book['genre']}")
                        print(f"Due Date: {book['due date']}")
                        print(f"Availability: {'Available' if book['available'] else 'Not Available'}")
                        if book['due date'] < datetime.date.today():
                            print(f"Overdue Fees: {calculate_overdue_fees(book)}")
                else:
                    print("You have no loaned books.")

        except FileNotFoundError:
            print("No catalogue found!")
        except Exception as e:
            print("Error reading catalogue file:", e)

def calculate_overdue_fees(book):
    # Calculate overdue fees based on the number of days overdue
    days_overdue = (datetime.date.today() - book['due_date']).days
    if days_overdue <= 5:
        return days_overdue + 1
    else:
        return 10

# Update member information
def update_member_information():
    # Clear terminal history
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the file exists
    if not os.path.exists('admin/memberdatabase.txt'):
        print('Member is not registered.')
        return

    # Check if the file is empty
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record is empty.')
        return
    
    else:
        try:
            username = input("Enter Name: ")
            edited_profile = []
            with open("admin/memberdatabase.txt", "r") as memberfile:
                members = memberfile.readlines()
            
            for credentials in members:
                stored_username, stored_userage, stored_dob, stored_regdate, stored_ic = credentials.strip().split(":")
                if stored_username == username:
                    print(f"ID: {stored_username}\nName: {stored_userage}\nPassword: {stored_dob}\nRole: {stored_regdate}\nIC: {stored_ic}")
                    print("1. ID")
                    print("2. Name")
                    print("3. Password")
                    print("4. Role")
                    print("5. IC")
                    print("6. All")
                    choice = input("What would you like to edit?").strip()

                    new_username = stored_username
                    new_userage = stored_userage
                    new_dob = stored_dob
                    new_regdate = stored_regdate
                    new_ic = stored_ic

                    if choice == "1":
                        new_username = input("Enter new id: ")
                    elif choice == "2":
                        new_userage = input("Enter new name: ")
                    elif choice == "3":
                        new_dob = input("Enter new password: ")
                    elif choice == "4":
                        new_regdate = input("Enter new role: ")
                    elif choice == "5":
                        new_ic = input("Enter new ic: ")
                    elif choice == "6":
                        new_username = input("Enter new id: ")
                        new_userage = input("Enter new name: ")
                        new_dob = input("Enter new password: ")
                        new_regdate = input("Enter new role: ")
                        new_ic = input("Enter new ic: ")
                    else:
                        print("Invalid option.")
                        continue

                    edited_profile.append(f"{new_username}:{new_userage}:{new_dob}:{new_regdate}:{new_ic}\n")
                    print("Member information edited.")
                else:
                    edited_profile.append(credentials)

            with open("admin/memberdatabase.txt", "w") as memberfile:
                memberfile.writelines(edited_profile)

        except Exception as e:
            print("Error reading catalogue file:", e)


# Search member
def search_member_from_database():
    os.system('cls' if os.name == 'nt' else 'clear')
    if not os.path.exists('admin/memberdatabase.txt'): 
        print('Member Is Not Registered.')
        return
    elif os.path.getsize('admin/memberdatabase.txt') == 0:
        print('Record Is Empty.')
        return

    while True:
        with open('admin/memberdatabase.txt', 'r') as database:
            lines = database.readlines()
        keyword = input('Please Enter A Keyword:').lower().strip()

        found_member = []
        for line in lines[1:]:
            lower_member_details = line.strip().lower()
            normal_member_details = line.strip()
            if keyword in lower_member_details:
                found_member.append(normal_member_details)

        if len(found_member) == 0:
            print(f"\nFound 0 Result(s) for '{keyword}'")
            continue_search = input("Do you wish to continue searching? (yes/no): ").strip().lower()
            if continue_search == 'yes':
                continue
            else:
                return None

        else:
            print(f'\nFound {len(found_member)} Result(s):')
            headers = lines[0].strip()
            print(headers)
            print('=' * len(headers))

            # SET INDEX FOR MEMBER IN FOUND MEMBER []
            for index, member in enumerate(found_member, start=1):
                print(f"{index}. {member}")
            return found_member



# def main():
#     update_member_information()

# if __name__ == "__main__":
#     main()