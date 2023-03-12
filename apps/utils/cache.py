from __future__ import unicode_literals

from hashlib import md5

from django.core.cache import cache

from mainsys.settings import CACHE_MIDDLEWARE_SECONDS, CACHE_MIDDLEWARE_KEY_PREFIX


# error_log = logging.getLogger('error_logger')
# 示例文件


def _hashed_key(key: str) -> str:
    prefix = CACHE_MIDDLEWARE_KEY_PREFIX if CACHE_MIDDLEWARE_KEY_PREFIX else "zzq"
    key = f"{prefix}-{key}"
    return md5(key.encode("utf-8")).hexdigest()


def cache_set(key: str, value, timeout=-1):
    if timeout == -1:  # 默认采用系统设置缓存时间
        timeout = CACHE_MIDDLEWARE_SECONDS if CACHE_MIDDLEWARE_SECONDS else 1800
    return cache.set(_hashed_key(key), value, timeout)


def cache_get(key: str):
    return cache.get(_hashed_key(key))


def cache_del(key: str):
    return cache.delete(_hashed_key(key))
