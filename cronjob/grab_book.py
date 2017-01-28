import requests
import re
from app.book.models import Book, db
from app.book.models import BookSalesInfo

fakeHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/55.0.2883.95 Safari/537.36 '
}


class KfzSaleBook:
    KFZ_URL = 'http://search.kongfz.com/'

    def __init__(self, book):
        self.__book = book

    def sync(self):
        BookSalesInfo.query.filter_by(book_id=self.__book['id']).delete()
        result = self.__pull_data()
        for on_sell_book in result:
            db.session.add(on_sell_book)
        db.session.commit()

    def __pull_data(self):
        return self.__pull_data_by_page(1)

    @property
    def encoding_book_name(self):
        return (self.__book['name'].encode('unicode_escape').decode('utf-8')).replace('\\u', 'k')

    def __pull_data_by_page(self, page):
        response = requests.get(
            '%sproduct/?type=1&params=z%sv1w%d' % (KfzSaleBook.KFZ_URL, self.encoding_book_name, page),
            headers=fakeHeaders)
        response.encoding = 'utf-8-sig'
        data = response.json()
        if self.__is_on_sell(data['positionStr']):
            on_sell_books = data['productList']
            result = []
            count = len(on_sell_books) - 3
            position = count - 1
            while position >= 0:
                on_sell_book = on_sell_books[str(position)]
                result.insert(0, BookSalesInfo(self.__book['id'], on_sell_book['url'], sale_price=on_sell_book['price'],
                                               quality=on_sell_book['quality'], location=on_sell_book['area']))
                position -= 1
            total_count = int(on_sell_books['total'])
            if count + (50 * (page - 1)) < total_count:
                return result + self.__pull_data_by_page(page + 1)
            return result
        return []

    @classmethod
    def __is_on_sell(cls, target):
        return True if re.findall(r'满足默认搜索条件的有<span class="red1">\s+\d+\s+', target) else False


def sync_data():
    books = Book.query.all()
    for book in books:
        KfzSaleBook({'id': book.id, 'name': book.name}).sync()


sync_data()
