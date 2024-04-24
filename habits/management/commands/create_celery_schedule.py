from django.core.management import BaseCommand
from django_celery_beat.models import IntervalSchedule, PeriodicTask


class Command(BaseCommand):
    """Команда для подготовки базы данных к запуску celery задач"""

    def handle(self, *args, **options):

        # Чистим базу данных от ненужнфх интервалов
        IntervalSchedule.objects.filter(period=IntervalSchedule.DAYS, every=1).delete()

        schedule = IntervalSchedule.objects.create(
            every=1,
            period=IntervalSchedule.DAYS,
        )

        # Чистим базу данных от прошлых созданных задач отправки сообщений
        PeriodicTask.objects.filter(name='Send_messages').delete()

        PeriodicTask.objects.create(
            interval=schedule,
            name='Send_messages',
            task='habits.tasks.send_all_messages',
        )

