class Book:
    """Model a book"""

    def __init__(self, title, author, year_published):
        """Initialize the most basic information about a book"""
        self.title = title
        self.author = author
        self.year_published = year_published

    def get_description(self):
        """Return a formatted string with"""
        book_description = f"{self.title.title()}, by {self.author.title()}, {self.year_published}"
        return book_description


first_book = Book("ducky the duck", "fitzgerald", 1765)
print(first_book.get_description())
