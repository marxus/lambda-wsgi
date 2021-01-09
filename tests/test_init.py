from base64 import b64decode
from json import loads
from .handler_bottle import lambda_handler as bottle
from .handler_flask import lambda_handler as flask
from . import events

test_bottle__api_v2_get_index = lambda: api_v2_get_index(bottle)
test__flask__api_v2_get_index = lambda: api_v2_get_index(flask)


def api_v2_get_index(lambda_handler):
    rsp = lambda_handler(events.api_v2_get('/'), None)
    body = b64decode(rsp['body'])
    assert body == b'OK'
    assert 'text/html' in rsp['headers']['content-type']


test_bottle__api_v2_get_index_stage = lambda: api_v2_get_index_stage(bottle)
test__flask__api_v2_get_index_stage = lambda: api_v2_get_index_stage(flask)


def api_v2_get_index_stage(lambda_handler):
    rsp = lambda_handler(events.api_v2_get('/test/', stage='test'), None)
    body = b64decode(rsp['body'])
    assert body == b'OK'
    assert 'text/html' in rsp['headers']['content-type']


test_bottle__api_v2_get_path = lambda: api_v2_get_path(bottle)
test__flask__api_v2_get_path = lambda: api_v2_get_path(flask)


def api_v2_get_path(lambda_handler):
    rsp = lambda_handler(events.api_v2_get(
        '/get/נתיב',
        '%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A1&%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A2&key=value',
    ), None)
    path, args = loads(b64decode(rsp['body']))
    assert path == 'נתיב'
    assert args['מפתח'] == ['ערך1', 'ערך2']
    assert rsp['headers']['content-type'] == 'application/json'


test_bottle__api_v2_get_path_stage = lambda: api_v2_get_path_stage(bottle)
test__flask__api_v2_get_path_stage = lambda: api_v2_get_path_stage(flask)


def api_v2_get_path_stage(lambda_handler):
    rsp = lambda_handler(events.api_v2_get(
        '/test/get/נתיב',
        '%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A1&%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A2&key=value',
        'test'
    ), None)
    path, args = loads(b64decode(rsp['body']))
    assert path == 'נתיב'
    assert args['מפתח'] == ['ערך1', 'ערך2']
    assert rsp['headers']['content-type'] == 'application/json'


test_bottle__alb_mv_get_path = lambda: alb_mv_get_path(bottle)
test__flask__alb_mv_get_path = lambda: alb_mv_get_path(flask)


def alb_mv_get_path(lambda_handler):
    rsp = lambda_handler(events.alb_mv_get(
        '/get/%D7%A0%D7%AA%D7%99%D7%91',  # '/get/נתיב'
        {'%D7%9E%D7%A4%D7%AA%D7%97': ['%D7%A2%D7%A8%D7%9A1', '%D7%A2%D7%A8%D7%9A2'], 'key': ['value']}
        # '%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A1&%D7%9E%D7%A4%D7%AA%D7%97=%D7%A2%D7%A8%D7%9A2&key=value'
    ), None)
    path, args = loads(b64decode(rsp['body']))
    assert path == 'נתיב'
    assert args['מפתח'] == ['ערך1', 'ערך2']
    assert rsp['multiValueHeaders']['content-type'][0] == 'application/json'
