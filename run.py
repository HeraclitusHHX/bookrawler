#!flask/bin/python
from app import app

if __name__ == '__main__':
    app.run()
# from flask import Flask, request, jsonify
# import requests
#
# app = Flask(__name__)
#
# origin = 'http://book.163.com'
#
#
# @app.route('/music/<int:id>', methods=['GET'])
# def get_by(id):
#     response = requests.get('%s/api/song/detail?ids=%%5B%d%%5D' % (origin, id))
#     jsonified_response = response.json()
#     code = jsonified_response['code']
#     return response
#
#
# @app.route('/music/search', methods=['POST'])
# def search():
#     song_name = request.json['name']
#     data = {
#         's': song_name,
#         'limit': 10,
#         'type': 1,
#         'offset': 0
#     }
#     headers = {
#         'Origin': origin,
#         'Referer': origin,
#         'Content-Type': 'application/x-www-form-urlencoded'
#     }
#     response = requests.post(origin + '/api/search/suggest/web', headers=headers, data=data)
#     jsonified_response = response.json()
#     code = jsonified_response['code']
#     if code == 200:
#         result = jsonified_response['result']
#         songs = result['songs']
#         return jsonify({
#             'code': 200,
#             'result': songs
#         })
#     else:
#         return jsonify({
#             'code': 400,
#             'msg': '没这曲子：' % song_name
#         })
#
#
# @app.route('/music/search', methods=['GET'])
# def play():
#     pass
#
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
