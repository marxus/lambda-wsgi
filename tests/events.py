api_v2_get = lambda path, qs='', stage='$default': {
    'version': '2.0',
    'rawQueryString': qs,
    'headers': {
        'host': 'r3pmxmplak.execute-api.us-east-2.amazonaws.com',
        'x-forwarded-for': '205.255.255.176',
        'x-forwarded-port': '443',
        'x-forwarded-proto': 'https'
    },
    'requestContext': {
        'http': {
            'method': 'GET',
            'path': path
        },
        'stage': stage
    },
    'isBase64Encoded': False
}

alb_mv_get = lambda path, qs={}: {
    'httpMethod': 'GET',
    'path': path,
    'multiValueQueryStringParameters': qs,
    'multiValueHeaders': {
        'host': ['test.wsgi.demo'],
        'x-forwarded-for': ['2.53.136.37'],
        'x-forwarded-port': ['443'],
        'x-forwarded-proto': ['https']
    },
    'isBase64Encoded': False
}
