import urlparse
import functools
from flask import request, redirect, Response
from werkzeug.contrib.cache import RedisCache, SimpleCache
#from config import REDIS_SERVER

#redis_cache_provider = RedisCache(**REDIS_SERVER)
memory_cache_provider = SimpleCache()


def require_ssl(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        parsed_url = urlparse.urlparse(request.url)
        if parsed_url.scheme != "https" and request.remote_addr != "127.0.0.1":
            secure_url = request.url.replace("http://", "https://")
            return redirect(secure_url)
        return f(*args, **kwargs)

    return decorator


def check_etag(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        etag = request.headers.get("If-None-Match")
        if etag == kwargs[kwargs.keys()[0]]:
            return Response(status=304)
        return f(*args, **kwargs)

    return decorator


# def redis_cached(f):
#     @functools.wraps(f)
#     def decorator(*args, **kwargs):
#         key = "{0}{1}".format(f.__name__, str(args[1:]))
#         result = redis_cache_provider.get(key)
#         if result is not None:
#             return result
#         result = f(*args, **kwargs)
#         redis_cache_provider.add(key, result)
#         return result
#
#     return decorator


def memory_cached(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        key = "{0}{1}".format(f.__name__, str(args[1:]))
        result = memory_cache_provider.get(key)
        if result is not None:
            return result
        result = f(*args, **kwargs)
        memory_cache_provider.add(key, result)
        return result

    return decorator


