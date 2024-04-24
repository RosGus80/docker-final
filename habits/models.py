import datetime

from django.db import models

from users.models import User


# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='Место')
    action = models.CharField(max_length=255, verbose_name='Задача')
    time = models.CharField(max_length=255, verbose_name='Время')
    pleasant_habit = models.ForeignKey("self", on_delete=models.CASCADE, related_name='pleasant',
                                       verbose_name='Приятная привычка', **NULLABLE)
    tied_habit = models.ForeignKey("self", on_delete=models.CASCADE,
                                   verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(verbose_name='Периодичность в днях', default=1)
    reward = models.CharField(max_length=255, verbose_name='Награда')
    time_to_complete = models.TimeField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Публичность привычки')
    last_reminder = models.DateField(verbose_name='Время последнего напоминания',
                                     default=datetime.date(2000, 1, 1), **NULLABLE)
