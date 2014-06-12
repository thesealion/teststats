from redis import Redis
import time
from urlparse import parse_qs


redis = Redis()
GIF = 'GIF89a\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\xff\xff\xff!\xf9\x04\x01\n\x00\x01\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02L\x01\x00;'


def app(environ, start_response):
    query = parse_qs(environ['QUERY_STRING'])
    try:
        redis.rpush('hits', '%d:%d:%d' % (
            int(query['user_id'][0]),
            int(query['page_id'][0]),
            time.time(),
        ))
    except (KeyError, ValueError):
        pass

    start_response('200 OK', [
        ('Content-Type', 'image/gif'),
        ('Content-Length', len(GIF)),
    ])
    return GIF
