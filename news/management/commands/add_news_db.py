import os
from datetime import datetime

from django.core.management.base import BaseCommand
from news.models import News
import csv


class Command(BaseCommand):
    help = 'Load news from Fake.csv into the News model'

    def handle(self, *args, **kwargs):
        csv_path = 'news/management/commands/Fake.csv'

        with open(csv_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            count = 0
            for row in csv_reader:
                if count >= 5:
                    break

                try:
                    date_value = datetime.strptime(
                        row['date'],
                        '%B %d, %Y'
                    ).date()
                except (ValueError, KeyError):
                    continue

                News.objects.create(
                    headline=row['title'],
                    body=row['text'],
                    date=date_value
                )

                count += 1

        self.stdout.write(self.style.SUCCESS(f'{count} noticias agregadas correctamente.'))