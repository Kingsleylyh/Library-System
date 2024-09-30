import os
import datetime

def view_loaned_books(member, books):

    # Clear terminal history
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # View the member's loaned books with due dates and overdue fees
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
            print(f"Publication date: {book['publication date']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Genre: {book['genre']}")
            print(f"Due date: {book['due date']}")
            if book['due date'] < datetime.date.today():
                print(f"Overdue Fees: {calculate_overdue_fees(book)}")
    else:
        print("You have no loaned books.")

def calculate_overdue_fees(book):
    # Calculate overdue fees based on the number of days overdue
    days_overdue = (datetime.date.today() - book['due_date']).days
    return days_overdue * 0.5

def 