class Book:
    def __init__(self, author = "", title = ""):
        self.author = author
        self.title = title
    
    def display(self):
        print(self.title + ", written by " + self.author)

book1 = Book('J. K. Rowling', 'Harry Potter and the Goblet of Fire')
book2 = Book('Walter Scott', 'Ivanhoe: A Romance')

if __name__ == "__main__":
    book1.display()
    book2.display()