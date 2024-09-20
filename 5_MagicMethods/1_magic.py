# Magic methods also known as Dunder Method.

from typing import Any


print("Hiiii")
class Author:

    def __init__(self,book,author,page) :
        self.book = book
        self.author = author
        self.page = page
    
    def __str__(self):
        return f"{self.book} written by {self.author}"
    
    def __len__(self):
        return self.page
    
    def __call__(self) :
        return "Now I am Callable"
    
    

p = Author("Agni Siragu","APJ",120)
print(p)
print(str(p))
print(len(p))
print(p())
