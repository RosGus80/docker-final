from django.urls import path

from habits.views import HabitCreateAPIView, PublicHabitListAPIView, HabitRetrieveAPIView, HabitDestroyAPIView, \
    HabitUpdateAPIView, UserHabitListAPIView

app_name = 'habits'

urlpatterns = [
    path('habit_create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit_list/', PublicHabitListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/<int:pk>/delete/', HabitDestroyAPIView.as_view(), name='habit_destroy'),
    path('habit/<int:pk>/update/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit_user_list/', UserHabitListAPIView.as_view(), name='habit_user_list'),
]
