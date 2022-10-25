#program to ko wthe no of books in the shelf
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return (f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}")

#assingn thr argument for the class
book1 = Book('Book 1', 85, 'Author 1', 160)
book2 = Book('Book 2', 64, 'Author 2', 300)
book3 = Book('Book 3', 98, 'Author 3', 200)

#printing
print(book1)
print(book2)
print(book3)

#book1 .__class__.attr   using class attribute to access your class
