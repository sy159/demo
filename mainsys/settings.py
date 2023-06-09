import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_DIRNAME = BASE_DIR.split(os.sep)[-1]  # 项目名

STATIC_URL = "/static/"

# 不需要静态文件
# STATIC_ROOT = os.path.join(BASE_DIR, "/static/")
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# 不需要媒体文件
# MEDIA_URL = "media/"  # 媒体文件路径
#
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

CACHE_ROOT = os.path.join(BASE_DIR, "cache")

LOG_ROOT = os.path.join(BASE_DIR, 'logs')

ROOT_URLCONF = "mainsys.urls"

# 加入额外目录
APP_ROOT = os.path.join(BASE_DIR, "./apps/")
sys.path.insert(0, APP_ROOT)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
]

APPS_CANNOT_INTSALL = ["utils", ]  # 禁止作为app安装的目录

# 根据apps里的目录进行动态设置
for ap in os.listdir(APP_ROOT):
    if ap not in APPS_CANNOT_INTSALL and os.path.isdir(os.path.join(APP_ROOT, ap)) and \
            os.path.exists(os.path.join(os.path.join(APP_ROOT, ap), "__init__.py")):
        INSTALLED_APPS.append("apps." + ap)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'apps.middleware.RequestMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'apps.middleware.NotUseCsrfTokenMiddlewareMixin',  # 快速开发，直接使用的session登录认证
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainsys.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

USE_I18N = True  # 国际化(关闭可提高性能),设置为T，LANGUAGE_CODE才可以生效
TIME_ZONE = "Asia/Shanghai"
USE_TZ = False  # 不使用时区
DATETIME_FORMAT = 'Y-m-d H:i:s'  # 系统中显示datetime字段的默认格式
DATE_FORMAT = 'Y-m-d'
USE_L10N = True  # 用于决定是否开启数据本地化。如果此设置为True，例如Django将使用当前语言环境的格式显示数字和日期。
LANGUAGE_CODE = "zh-hans"  # 简体中文  zh-hant: 繁体中文
# X_FRAME_OPTIONS = 'SAMEORIGIN'  # 相同站点可嵌入iframe


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 缓存到内存
        'LOCATION': CACHE_ROOT,
        'TIMEOUT': 120,  # 缓存超时时间（默认300，None表示永不过期，0表示立即过期）
        'OPTIONS': {
            'MAX_ENTRIES': 500,  # 最大缓存个数（默认300）
            'CULL_FREQUENCY': 6,  # 缓存到达最大个数之后，剔除缓存个数的比例，即：1/CULL_FREQUENCY（默认3）
        },
    }
}

# 配置
try:
    from mainsys.config import *
except ImportError as e:
    if "config" not in e:
        raise e

# 数据库，es，缓存等配置
try:
    from mainsys.dbconfig import *
except ImportError as e:
    if "dbconfig" not in e:
        raise e

# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用logger
    # formatters(日志格式，可以自己根据需求配置)，提供给handler格式化日志输出使用(默认打印传入的消息体)
    'formatters': {
        # ================format参数中可能用到的格式化字符串=================
        # %(name)s  Logger的名字
        # %(levelno)s   数字形式的日志级别
        # %(levelname)s 文本形式的日志级别
        # %(pathname)s  调用日志输出函数的模块的完整路径名，可能没有
        # %(filename)s  调用日志输出函数的模块的文件名
        # %(module)s    调用日志输出函数的模块名
        # %(funcName)s  调用日志输出函数的函数名
        # %(lineno)d    调用日志输出函数的语句所在的代码行
        # %(created)f   当前时间，用UNIX标准的表示时间的浮 点数表示
        # %(relativeCreated)d   输出日志信息时的，自Logger创建以 来的毫秒数
        # %(asctime)s   字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        # %(thread)d    线程ID。可能没有
        # %(threadName)s    线程名。可能没有
        # %(process)d   进程ID。可能没有
        # %(message)s   用户输出的消息

        'simple': {'format': '%(asctime)s %(message)s'},  # 输出时间跟消息体（简单日志格式）
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
            # 标准日志输出
        },
    },

    # 过滤器，提供给handler使用(可以不使用)，也可以自定义过滤函数（https://docs.python.org/3/library/logging.html#filter-objects）
    'filters': {
        # 过滤debug为True
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        # 过滤debug为False
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # },
    },
    # 处理器，设置日志记录方式
    'handlers': {
        # =================class设置分类（根据需求设置）=================
        # 'logging.StreamHandler'  # 控制台打印
        # 'logging.FileHandler'  # 保存到文件
        # 'logging.handlers.RotatingFileHandler'  # 保存到文件，根据文件大小自动切
        # 'logging.handlers.TimedRotatingFileHandler'  # 保存到文件，根据时间自动切
        # 'django.utils.log.AdminEmailHandler'  # 管理员发送错误电子邮件（）

        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 设置过滤器，多个用逗号分割
            'class': 'logging.StreamHandler',  # 控制台打印
            'formatter': 'simple'  # 选用格式化样式
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
            'filename': 'mainsys/logs/error.log',  # 日志文件名
            'maxBytes': 1024 * 1024 * 20,  # 日志大小 20M
            'backupCount': 5,  # 保留的日志份数，默认为0表示都保存
            'formatter': 'simple',  # 选用格式化样式
            'encoding': 'utf-8'
        },
        'debug': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'mainsys/logs/debug.log',
            'formatter': 'simple',
            'encoding': 'utf-8'
        },
        'msg': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'mainsys/logs/msg.log',
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 10,
            'formatter': 'simple',
            'encoding': 'utf-8'
        },
        # 'push': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.TimedRotatingFileHandler',  # 按时间切割日志
        #     'filename':  'mainsys/logs/push.log',  # 日志输出文件
        #     'when': 'D',  # 按天分割(S/秒 M/分 H/小时 D/天 W0-W6/(周一到周天) midnight/如果没指定时间就默认在午夜)
        #     'backupCount': 7,
        #     'formatter': 'standard',
        # },
        # 'request': {
        #     'level': 'WARNING',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename':  'mainsys/logs/request_error.log',
        #     'maxBytes': 1024 * 1024 * 20,
        #     'backupCount': 5,
        #     'formatter': 'simple',
        #     'encoding': 'utf-8'
        # },
        # 给管理员发送邮件
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
            'filters': ['require_debug_false'],
            'include_html': True,
        }
    },

    # 日志记录器
    'loggers': {
        # 默认的logging应用
        '': {
            'handlers': ['console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),  # 只有设置DEBUG为True时，该配置才会打印sql信息
        },
        # 内置logger,与请求处理有关的日志消息(可用作监控使用)，5XX响应作为ERROR消息引发，出现4XX响应作为WARNING消息
        # 'django.request': {
        #     '''
        #     status_code：与请求关联的HTTP响应代码。
        #     request：生成日志消息的请求对象。
        #     '''
        #     'handlers': ['mail_admins'],  # 可配置为mail_admins
        #     'level': 'WARNING',
        #     'propagate': False,
        # },
        # 内置logger，数据库orm语句执行情况
        'django.db.backends': {
            '''
            duration：执行SQL语句所花费的时间。
            sql：执行的SQL语句。
            params：SQL调用中使用的参数
            '''
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        # 创建logger对象，logging.getLogger('my_logger')
        'error_logger': {
            'handlers': ['error'],
            'level': 'ERROR',  # 设置对象的最低等级，不能高于handlers设置的日志级别
            'propagate': False  # propagate是设定是否向父logger传播信息。必须设置为False，否则会打印两次
        },
        'msg_logger': {
            'handlers': ['msg'],
            'level': 'INFO',
            'propagate': False
        },
        'debug_logger': {
            'handlers': ['debug'],
            'level': 'INFO',
            'propagate': False
        },
    },
}
