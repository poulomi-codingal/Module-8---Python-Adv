class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We have the follwing books in our library .. {self.bookname}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book DB has been updated, U can take the book now ..")

        else:
            print(f"book is already being used by {self.lendDict[book]}")
    
    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the booklist ..")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    books = Library(['Python', 'C by Kanethkar', 'Java by Balaguruswamy', 'The art of public speaking', 'How to think and grow rich', 'the art of talking with children'], "Central Library")

    while (True):
        print(f"Welcome to the library, {books.name}, enter your choice to continue..")
        print("1. Dispaly books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input()
        if user_choice not in ["1","2", "3","4"]:
            print("enter valid option..")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.displayBook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name ")
            books.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the book name you want to add")
            books.addBook(book)

        elif user_choice == 4:
            book = input("Enter the book name you want to return :")

        else:
            print("Not avlid option ..")
        
        print("press q for quit and c for continue")

        user_choice2 = ""
        if user_choice2 == "Q" or "q":
            exit()
        
        elif user_choice2 == "C" or "c":
            continue



