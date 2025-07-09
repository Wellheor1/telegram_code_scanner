BOT_TOKEN = "your-telegram-bot-token"
WEB_APP_URL = "http://127.0.0.1:9000"


try:
    from local_settings import *  # noqa: F403
except ImportError:
    pass
