from . import book


@book.route('/book', methods=['POST'])
def add():
    pass


@book.route('/book/<int:id>', methods=['GET'])
def get_by_id(id):
    pass

