from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            return member.borrow_book(book)
        return False

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)
        if member and book:
            return member.return_book(book)
        return False

    def search_book(self, title):
        return [book for book in self.books.values() if title.lower() in book.title.lower()]