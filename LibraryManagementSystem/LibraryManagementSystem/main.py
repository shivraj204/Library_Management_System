from book import Book
from member import Member
from library import Library

def main():
    library = Library()

    # Sample books
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "Brave New World", "Aldous Huxley")
    library.add_book(book1)
    library.add_book(book2)

    # Sample member
    member = Member(101, "Alice")
    library.register_member(member)

    # Borrowing a book
    if library.borrow_book(101, 1):
        print(f"{member.name} borrowed '{book1.title}'")
    else:
        print(f"{member.name} could not borrow '{book1.title}'")

    # Searching for a book
    results = library.search_book("Brave")
    for b in results:
        print(f"Found: {b}")

    # Returning a book
    if library.return_book(101, 1):
        print(f"{member.name} returned '{book1.title}'")

if __name__ == "__main__":
    main()