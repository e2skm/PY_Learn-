## Classes Liabrary Management system- PY_learn_projectn
class Book:
    def __init__(self,title, author, gendre, available=True):
        self.title = title
        self.author = author
        self.gendre = gendre
        self.available = available
    def borrow(self):
        if self.available:
            print(f'You have successfully borrowed {self.title}, remeber to return it in 7 days time')
            self.available = False
        else:
            print(f"{self.title} is currently unavailable, check again in a week's time")   
    def return_book(self):
        self.available = True
        print(f'Thank you for returning {self.title} in good condition :)')
    def is_available(self):
        if self.available:
            print(f'The book {self.title} is available, Would you like to borrow it?\nEnter Yes/Y or No/N')
            wannaBorrow = input().upper()
            if wannaBorrow in ['YES','Y']:
                self.borrow()
        else:
            print(f"The book {self.title} is unavailable currently, check again in a week's time")  
## Instantiation
book1 = Book('The Holy Bible','Unknown','Religion')
book2 = Book('Life of PI','Yann Martel','Philosophical Novel' , False)  
book3 = Book('48 Laws of Power', 'Robert Green', 'Self-help',True)  
## Check which book is available
book1.is_available()
book2.is_available()
book3.is_available()   
## Borrow the available books
book1.borrow()
book2.borrow()
book3.borrow() 
## Return the borrowed book and borrow it
book2.return_book() 
book2.borrow() 
## Return all the books
book1.return_book()
book2.return_book()
book3.return_book()                      