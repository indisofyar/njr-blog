from .base import *
import dj_database_url

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=1800),
}
