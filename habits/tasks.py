import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import TGBot


@shared_task
def send_all_messages():
    """Celery задача на каждый день для отправки всех уведомлений о привычках всем пользователям в случае, если
    эта привычка была выполнена достаточно давно"""
    mybot = TGBot()
    queryset = Habit.objects.all()
    for habit in queryset:
        text = f'Привычка: {habit.action}\nВремя на выполнение: {habit.time_to_complete}'
        if habit.last_reminder + datetime.timedelta(days=habit.periodicity) <= datetime.date.today():
            habit.last_reminder = datetime.date.today()
            habit.save()
            mybot.send_message(text=text)


