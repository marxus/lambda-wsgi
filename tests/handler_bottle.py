from bottle import Bottle, request, response, json_dumps
from lambda_wsgi import make_handler

app = Bottle()
lambda_handler = make_handler(app)


@app.get('/')
def get_index():
    return 'OK'


@app.get('/get/<path>')
def get_path(path):
    response.content_type = 'application/json'
    mv_qs = request.query.decode()
    mv_qs = {k: mv_qs.getlist(k) for k in mv_qs.keys()}
    return json_dumps([path, mv_qs])
