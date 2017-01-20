from app import db


class Book(db.Model):
    __tablename__ = 'Books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    author = db.Column(db.String(128))
    press = db.Column(db.String(128))
    publication_date = db.Column(db.Date)
    original_price = db.Column(db.Numeric(10, 2))

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


class BookSalesInfo(db.Model):
    __tablename__ = 'BookSalesInfos'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id), nullable=False)
    url = db.Column(db.Text)
    sale_price = db.Column(db.Numeric(10, 2))
    quality = db.Column(db.String(16))
    location = db.Column(db.String(128))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
