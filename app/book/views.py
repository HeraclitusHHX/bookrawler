from . import book
from .models import Book, BookExpectCondition
from app import db
from flask import request, jsonify


@book.route('/book', methods=['POST'])
def add_book():
    name = request.json.get('name')
    author = request.json.get('author')
    press = request.json.get('press')
    publication_date = request.json.get('publication_date')
    original_price = request.json.get('original_price')
    new_book = Book(name=name, author=author, press=press, publication_date=publication_date,
                    original_price=original_price)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'msg': '添加成功'}), 201


@book.route('/book', methods=['GET'])
def get_all():
    books = Book.query.all()
    return jsonify(json_list=[item.serialize for item in books]), 200


@book.route('/book_expect_condition', methods=['POST'])
def add_book_expect_condition():
    book_id = request.json.get('book_id')
    if_on_sell = request.json.get('if_on_sell', False)
    expect_price = request.json.get('expect_price')
    expect_quality = request.json.get('expect_quality')
    new_book_expect_condition = BookExpectCondition(book_id, if_on_sell=if_on_sell, expect_price=expect_price,
                                                    expect_quality=expect_quality)
    db.session.add(new_book_expect_condition)
    db.session.commit()
    return jsonify({'msg': '添加成功'}), 201
