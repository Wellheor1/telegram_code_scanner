# Адрес и порт сервера
ADDRESS = "127.0.0.1"
PORT = 8000


try:
    from app.local_settings import *  # noqa: F403
except ImportError:
    pass
