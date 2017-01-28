from app import db


class Book(db.Model):
    __tablename__ = 'Books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    author = db.Column(db.String(128))
    press = db.Column(db.String(128))
    publication_date = db.Column(db.Date)
    original_price = db.Column(db.Numeric(10, 2))

    def __init__(self, name=None, author=None, press=None, publication_date=None, original_price=None):
        self.name = name
        self.author = author
        self.press = press
        self.publication_date = publication_date
        self.original_price = original_price

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author': self.author,
            'press': self.press,
            'publication_date': self.publication_date,
            'original_price': self.original_price
        }

    def __str__(self):
        return '<"%s" by %s | %s | %s>' % (
            self.name, self.author, self.press, self.publication_date)


class BookExpectCondition(db.Model):
    __tablename__ = 'BookExpectConditions'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id), nullable=False)
    if_on_sell = db.Column(db.Boolean, default=False)
    expect_price = db.Column(db.Numeric(10, 2))
    expect_quality = db.Column(db.String(16))

    def __init__(self, book_id, if_on_sell=False, expect_price=None, expect_quality=None):
        self.book_id = book_id
        self.if_on_sell = if_on_sell
        self.expect_price = expect_price
        self.expect_quality = expect_quality


class BookSalesInfo(db.Model):
    __tablename__ = 'BookSalesInfos'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id), nullable=False)
    url = db.Column(db.Text)
    sale_price = db.Column(db.Numeric(10, 2))
    quality = db.Column(db.String(16))
    location = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, book_id, url, sale_price=None, quality=None, location=None):
        self.book_id = book_id
        self.url = url
        self.sale_price = sale_price
        self.quality = quality
        self.location = location
