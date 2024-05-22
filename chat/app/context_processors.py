import requests
from django.conf import settings


def global_settings(request):
    json_data = []
    response = requests.get(
        settings.QUOTE_URL,
        headers={"X-Api-Key": settings.QUOTE_API_KEY},
    )
    if response.status_code == 200:
        json_data = response.json()

        print(json_data[0])
    return {"daily_quote": json_data[0]}
