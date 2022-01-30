class library:
    def __init__(self, list ,name):
        self.booklist = list
        self.name = name
        self.lenDict = {}

    def displayBooks(self):
        print(f"We Have Following in our library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendBooks(self,user,book):
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print(" Lender-Book database has been updated. You can take book now")

        else:
            print(f" Book is already being used by {self.lendDict[book]}")




    def addBooks(self,book):
        self.booklist.append(book)
        print("Book has been added to book list ")

    def returnBook(self,book):
        self.lenDict.pop(book)

if __name__ == '__main__':

    ajay = library(['Python','Rich Dad and Poor Dad','Harry Potter','C++ Basic'], "Ajay Library")
    while(True):
        print(f"Welcome to the {ajay.name} library.Enter to your choice to continue")

        print("1. Display Books")
        print("2. Lend a book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice==1:
            ajay.displayBooks()


        elif user_choice ==2:
            book = input("Enter the name you want to lend:")
            user = input("Enter your name")
            ajay.lendBooks(user,book)

        elif user_choice==3:
            book = input("Enter the name of book you want to add")
            ajay.addBooks(book)

        elif user_choice==4:
            book = input("Enter the name of book you want to return")
            ajay.returnBook(book)
        else:
            print("Not valid option")

        print(" Press q to quit and c to continue")
        user_choice2 = ""

        user_choice2 = input()
        if user_choice2 == "q":
            exit()

        elif user_choice2 =="c":
            continue




