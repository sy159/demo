""""
本文件记录数据库相关配置
"""

# elasticsearch连接配置
es_conf = {
    "host": "http://127.0.0.1:9200/",
    "user": "xxx",
    "pwd": "123456",
}

# mq连接配置
mq_conf = {
    "host": "127.0.0.1",
    "port": 5672,
    "vhost": "test",  # 虚拟主机名
    "user": "xxx",
    "pwd": "xxx",
}

# redis连接配置
redis_conf = {
    "host": "127.0.0.1",
    "port": 6379,
    "db": "0",
    "pwd": "xxx",
}

# 缓存设置
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://%s:%d/%s" % (redis_conf.get("host"), redis_conf.get("port"), redis_conf.get("db")),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {"max_connections": 100},  # 连接池（最大连接数）
#             "PASSWORD": redis_conf.get("pwd")
#         }
#     }
# }

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 如果想要postgresql改一下引擎，本地是mysql所以直接用的mysql
        'NAME': "demo",
        'USER': "root",
        'PASSWORD': "zx.123",
        'HOST': "127.0.0.1",
        'PORT': 3306,
        # 持久化(每个数据库连接的最大存活时间，以秒为单位。0表示在每个请求结束时关闭数据库连接，None表示无限的持久连接),小于数据库的maxWait
        'CONN_MAX_AGE': 20,
    }
}

# todo 多数据库联用配置

# todo 配置多数据库路由规则，实现读写分离等操作

