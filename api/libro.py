libro = [
    {
        "ISBN": "2348734",
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "price": 8400,
        "published": "2019",
        "language": "EN",
        "number_pages": 539,
        "press": "no starch press",
        "ranking": 4.8
    }
    ]

class Books:
    def __init__(self, ISBN, title, author, price):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.price = price
    def __str__(self) -> str:
        return super().__str__()
    def serialize(self):
        return {
            'ISBN': self.ISBN,
            'Title': self.title,
            'Author': self.author,
            'Price': self.price,
        }