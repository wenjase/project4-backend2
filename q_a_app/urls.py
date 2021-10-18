from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('questions/', views.QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(), name='question_detail'),
    path('answers/', views.AnswerList.as_view(), name='answer_list'),
    path('answers/<int:pk>', views.AnswerDetail.as_view(), name='answer_detail')
]