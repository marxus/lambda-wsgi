from flask import Flask, request, jsonify
from lambda_wsgi import make_handler

lambda_handler = make_handler(app := Flask(__name__))


@app.route('/', methods=['GET'])
def get_index():
    return 'OK'


@app.route('/get/<path>', methods=['GET'])
def get_path(path):
    mv_qs = request.args
    mv_qs = {k: mv_qs.getlist(k) for k in mv_qs.keys()}
    return jsonify([path, mv_qs])
