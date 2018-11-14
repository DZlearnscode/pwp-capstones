import operator 

class User(object):

    def __init__(self, name, email):

        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):

        return "User {user} registered with {email} email address, read {n_books} books".format(
            user = self.name, email = self.email, n_books = str(len(self.books)))

    def __eq__(self, other_user):
        
        if self.name == other_user.name and self.email == other_user.email:
            return True
        elif self.name != other_user.name or self.email != other_user.email: 
            return False
        else:
            print("User isn't registered")

    def __hash__(self):

        return hash((self.name, self.email))        

    def get_email(self):

        return self.email

    def change_email(self, address):

        self.email = address

        return self.name + "your email had been changed to /n" + self.email

    def read_book(self, book, rating = None):

        if rating in range(0,5) or rating == None:
            self.books[book] = rating
        else:
            print("Please choose a rating between 0 and 4")

    def get_average_rating(self):

        total_rating = 0        
        for value in self.books.values():
            if value:
                total_rating += value 
        return total_rating / len(self.books)

    def num_of_books_read(self):

        return len(self.books)

class Book():

    def __init__(self, title, isbn, price):

        self.title = title
        self.isbn = isbn
        self.rating = []
        self.price = price
    #dictionary that maps books to reviews - books as keys
        self.reviews = {}

    def __eq__(self, other_book):

        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        elif self.title != other_book.title or self.isbn != other_book.isbn:
            return False
        else:
            print("Book isn't registered")

    def __hash__(self):

        return hash((self.title, self.isbn))        

    def __repr__(self):

        return "'{}'".format(self.title)

    def get_title(self):
        
        return self.title

    def get_isbn(self):
        
        return self.isbn

    def set_isbn(self, new_isbn):

        self.isbn = new_isbn
        return "The ISBN for {} had been changed to {}".format(self.title, new_isbn)

    def add_rating(self, rating):

        if rating in range(0,5):
            self.rating.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):

        total_rating = 0        
        for value in self.rating:
            total_rating += value 
        return total_rating / len(self.rating)

    def add_a_review(self, book, review):

        if book not in self.reviews.keys():
            self.reviews[book] = [review]

        self.reviews[book].append(review)   

    def get_review(self, book):

        return self.reviews[book]

    def set_price(self, new_price):

        self.price = new_price
        return "A new price of {} was set to {}".format(new_price, self.title)

   
class Fiction(Book):
    
    def __init__(self, title, author, isbn, price):

        super().__init__(title, isbn, price)
        self.author = author

    def __repr__(self):

        return "'{}' by {}".format(self.title, self.author)

    def get_author(self):

        return self.author


class Non_Fiction(Book):
    
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def __repr__(self):

        return "'{}', a {} manual on {}".format(self.title, self.level, self.subject)

    def get_level(self):

        return self.level

    def get_subject(self):

        return self.subject
        
        
class TomeRater():

    def __init__(self):

        self.users = {}
        self.books = {}

    def __repr__(self):

        return """Registered users: {self.users} 
        Available books and number of time they were read {self.book}""".format(self.users, self.books)

    def __eq__(self, other):

        if self.users == other.users and self.books == other.books:
            return True
        else:
            return False

    def create_book(self, title, isbn, price):

        for book in self.books.keys():
            if book.get_isbn == isbn:
                return "A book with such ISBN is already registered"
        
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price):

        for book in self.books.keys():
            if book.get_isbn == isbn:
                return "A book with such ISBN is already registered"
        
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price):

        for book in self.books.keys():
            if book.get_isbn == isbn:
                return "A book with such ISBN is already registered"
            
        return Non_Fiction(title, subject, level, isbn, price)

    def add_book_to_user(self, book, email, rating = None):

        if self.users.get(email, None):
            user_name = self.users.get(email)
            user_name.read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            elif book in self.books:
                self.books[book] += 1
        else:

            return "Cannot find user with email {}".format(email)

    def add_user(self, name, email, user_books = None):

        if email in self.users.keys():
            print("User with this email already exists")
        else:
            self.users[email] = User(name, email)
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):

        amount_read = 0
        most_read_book = None

        for book, read in self.books.items():
            if read > amount_read:
                amount_read = read
                most_read_book = book

        return "The most read book is {}, it was read by {} people".format(most_read_book, amount_read)
             
    def highest_rated_book(self):
        
        highest_rated_book = None
        higest_average = 0

        for book in self.books.keys():
            average = book.get_average_rating()

            if average > higest_average:
                higest_average = average
                highest_rated_book = book

        return "The most rated book is {} with average rating {}".format(highest_rated_book, higest_average)

    def most_positive_user(self):
        
        average_rating = 0
        positive_user = None

        for user in self.users.values():
            average = user.get_average_rating()

            if average > average_rating:
                average_rating = average
                positive_user = user

        return "The most positive uesr is {} with average rating {}".format(
            positive_user, average_rating)

    def add_a_review(self, book, review):

        book.add_a_review(book, review)

    def get_review(self, book):

        return book.get_review(book)

    def get_n_most_read_books(self, n):

        books_sorted = sorted(self.books.items(), key = operator.itemgetter(1), reverse = True)

        for x in range(0, n):

            print(books_sorted[x])

    def get_n_most_prolific_readers(self, n):

        users = []
        read = []

        for user in self.users.values():

            users.append(user)
            read.append(user.num_of_books_read())

        users_read = {user:read for user, read in zip(users, read)}

        users_read_sorted = sorted(users_read.items(), key = operator.itemgetter(1), reverse = True)

        for x in range(0, n):

            print(users_read_sorted[x])

    def get_n_most_expensive_books(self, n):

        books = []
        price = []

        for book in self.books.keys():

            books.append(book)
            price.append(book.price)

        books_prices = {book:price for book, price in zip(books, price)}

        books_prices_sorted = sorted(books_prices.items(), key = operator.itemgetter(1), reverse = True)

        for x in range(0, n):

            print(books_prices_sorted[x])

    def get_worth_of_user(self, user_email):

        user = self.users[user_email]
        wroth = 0
        for book in user.books.keys():
            wroth += book.price
        return "{} worth £{}".format(self.users[user_email], wroth)


            















        































