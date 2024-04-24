import requests
from django.test import TestCase
from rest_framework.test import force_authenticate

from habits.models import Habit
from habits.permissions import IsOwnerOrReadOnly
from users.models import User


# Create your tests here.

#
# class HabitTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(email='test@mail.com', password='PassOne1')
#
#     def test_create(self):
#         data = {
#             'place': 'some place',
#             'action': 'some action',
#             'time': 'some time',
#             'periodicity': 1,
#             'reward': 'some reward',
#             'is_public': True
#         }
#         force_authenticate(self, user=self.user)
#         response = requests.post('/habit_create/', data=data)
#         self.assertEqual(response.status_code, 201)
#         if Habit.objects.filter(user=self.user).exists():
#             self.assertTrue(True)
#         else:
#             self.assertEqual(response.status_code, 400)


