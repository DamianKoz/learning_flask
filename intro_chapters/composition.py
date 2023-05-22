class Book:
    def __init__(self, name: str):
        self.name = name
        self.notes = []

    def __str__(self) -> str:
        return f"Book: {self.name!r} - Notes: {self.notes}"

    def add_note(self, note):
        self.notes.append(note)


class Note:
    def __init__(self, book: Book, content: str):
        self.book = book
        self.content = content

    def __str__(self) -> str:
        return f"{self.content!r}"

    def __repr__(self) -> str:
        return f"{self.content!r}"


book = Book("Beginning of Infinity")
book1 = Book("Harry Potter")
note = Note(book, "This is a good book")
book.add_note(note)
print(book)
print(book1)
