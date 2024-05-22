import requests
import jwt
import time
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
    # json_data = []
    # response = requests.get(
    #    settings.QUOTE_URL,
    #    headers={"X-Api-Key": settings.QUOTE_API_KEY},
    # )
    # if response.status_code == 200:
    #    json_data = response.json()

    #    print(json_data[0])
    daily_quote = None
    return {"daily_quote": daily_quote, **get_centrifugo_data(request.user.id)}
