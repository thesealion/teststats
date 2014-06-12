# coding: utf-8
import datetime
from django.core.management.base import BaseCommand
from redis import Redis
from teststats.stats.models import Hit


class Command(BaseCommand):
    def handle(self, *args, **options):
        redis = Redis()
        count = redis.llen('hits') # Получаем текущее кол-во хитов
        hits = redis.lrange('hits', 0, count - 1) # Считываем первые count хитов

        to_create = []
        for hit in hits:
            user_id, page_id, timestamp = map(int, hit.split(':'))
            time = datetime.datetime.fromtimestamp(timestamp)
            to_create.append(Hit(user_id=user_id, page_id=page_id, time=time))

        Hit.objects.bulk_create(to_create)

        redis.ltrim('hits', count, -1) # Удаляем сохраненные в базу хиты.

        self.stdout.write('Processed %d hits.' % len(to_create))
