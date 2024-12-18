import requests
import jwt
import time
from django.core.cache import cache
from django.conf import settings


def get_centrifugo_data(user_id):
    ws_url = settings.CENTRIFUGO_WS_URL
    secret = settings.CENTRIFUGO_SECRET
    token = jwt.encode(
        {"sub": str(user_id), "exp": int(time.time()) + 10 * 60},
        secret,
        algorithm="HS256",
    )

    return {"centrifugo": {"token": token, "url": ws_url}}


def global_settings(request):
    daily_quote = cache.get("daily_quote")

    return {"daily_quote": daily_quote, **get_centrifugo_data(request.user.id)}
