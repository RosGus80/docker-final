import datetime

from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        exclude = ('user',)

    def validate(self, attrs):
        """Функционал валидирования для создания привычки"""

        # Находим связанную и полезные привычки и, если их не задали, назначаем их как None,
        # чтобы не возникало KeyError во время проверки на совместное существование связанной и полезной привычек
        try:
            tied_habit = attrs['tied_habit']
        except KeyError:
            tied_habit = None
        try:
            pleasant_habit = attrs['pleasant_habit']
        except KeyError:
            pleasant_habit = None

        with open('/Users/rostislavgusev/PycharmProjects/py_project/drf-final/log.log', 'w') as file:
            file.write(str(attrs))

        if attrs['time_to_complete'] > datetime.time(0, 2):
            raise serializers.ValidationError('Слишком большое время на выполнение. '
                                              'Оно не должно превышать 120 секунд')

        if pleasant_habit is not None and tied_habit is not None:
            raise serializers.ValidationError('Приятная и связанная привычки не могут быть заданы одновременно')

        if tied_habit is not None:
            if tied_habit.pleasant_habit is not None:
                raise serializers.ValidationError('Связанная привычка не может иметь приятную привычку')

        if pleasant_habit is not None:
            if pleasant_habit.reward is not None or pleasant_habit.tied_habit is not None:
                raise serializers.ValidationError('Приятная привычка не может иметь связанную привычку и/или награду')

        if attrs['periodicity'] > 7:
            raise serializers.ValidationError('Нужно выполнять привычку хотя бы раз в неделю')

        return super(HabitSerializer, self).validate(attrs)
