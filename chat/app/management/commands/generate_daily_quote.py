import requests
from django.core.cache import cache
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        json_data = []
        response = requests.get(
            settings.QUOTE_URL,
            headers={"X-Api-Key": settings.QUOTE_API_KEY},
        )
        if response.status_code == 200:
            json_data = response.json()
            daily_quote = json_data[0]
            cache.set("daily_quote", daily_quote, 10)
