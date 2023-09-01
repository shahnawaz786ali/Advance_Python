class Library:
    def __init__(self,bookname):
        self.books=bookname
        
    def availablebooks(self,listofbooks):
        print("The list of avilable books are: ", self.listofbooks)
        
    def displaybook(self):
        print("Books present in this library are: ")
        for books in self.books:
            print("\t " + books)
            
    def borrowbook(self, bookname):
        
        if bookname in self.books:
            print(f"You have issued {bookname} book.Please use carefully.")
            self.books.remove(bookname)
            return True
        else:
            print("This book is not available. Try after few days.")
            return False
            
    def returnbook(self, bookname):
        print(f"Thank you for returning {bookname}. Hope u enjoyed.")
        self.books.append(bookname)
    
class student:
    def requestbook(self):
        self.book=input("Enter the choice of ur book: ")
        return self.book
    def returnbook(self):
        self.book=input("Enter the name of book: ")
        return self.book


if __name__ =="__main__":
    central_library=Library(["python", "c", "c++", "java"])
    
    student_response=student()
    
    central_library.displaybook()
    
    while True:
        print("Welcome to the Central)library.")
        print('''Choose your choice option:
                1: List of all books
                2. Request a book
                3. Return a book
                4. Exit from the library''')
        
        choice=int(input("Enter your choice:"))
        
        if choice==1:
            central_library.displaybook()
        
        elif choice==2:
            central_library.borrowbook(student_response.requestbook())
            
        elif choice==3:
            central_library.returnbook(student_response.returnbook())
            
        elif choice==4:
            exit()
            
        else:
            print("Please enter valid choice.")
        
        
    
        
