from datetime import datetime

class Author:

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])

class Book:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author needs to be type Author")
        else:
            self.author = author

        if not isinstance(book, Book):
            raise TypeError("Book needs to be type Book")
        else:
            self.book = book
        
        if not isinstance(date, str):
            raise TypeError("Date needs to be type str")
        else:
            self.date = date

        if not isinstance(royalties, int):
            raise TypeError("Royalties needs to be type int")
        else:
            self.royalties = royalties

        type(self).all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        # The test for this is badly written. The following passes
        #   the test even though it does not sort
        # return [contract for contract in cls.all if contract.date == date]
        return sorted([contract for contract in cls.all if contract.date == date], key=lambda contract: datetime.strptime(contract.date, "%m/%d/%Y"))
            