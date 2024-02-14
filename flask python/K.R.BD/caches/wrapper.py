from functools import wraps
from caches.connection import RedisCache


def fetch_from_cache(cache_name: str, cache_config: dict):
    cache = RedisCache(cache_config['redis'])
    ttl = cache_config['ttl']

    def wrapper_func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            cached_value = cache.get_value(cache_name)
            if cached_value:
                return cached_value
            response = f(*args, **kwargs)
            cache.set_value(cache_name, response, ttl=ttl)
            return response

        return wrapper

    return wrapper_func
