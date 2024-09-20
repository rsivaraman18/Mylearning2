# Magic methods also known as Dunder Method.

print("Hiiii")
class Author:

    def __init__(self,book,author) :
        self.book = book
        self.author = author
    
    # def __str__(self):
    #     return f"{self.book} written by {self.author}"

p = Author("Agni Siragu","APJ")
print(p)
print(str(p))