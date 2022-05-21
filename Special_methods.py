#Special methods

#Creates book class
class Book(object):
    def __init__(self, title, autor, pages):
        print('A book was created')
        self.title = title
        self.autor = autor
        self.pages = pages
    
    def __str__(self):
        return "Title (a)".format(a = self.title)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('Book destroyed')

#Special methods brings special behaviors on methods
#We know we can create and print a list
l = [1,2,3]
print(l)

#Examples
book1 = Book('Python', 'Alex', 100)
#We can't --> print(book1) without def __str__(self)
print(book1)
#We can't --> len(book1) without def __len__(self)
print(len(book1))

#Destroy book1
del book1

#Now the book1 was destroyed, and we can't print
#print(book1)



