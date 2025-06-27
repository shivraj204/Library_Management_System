class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"