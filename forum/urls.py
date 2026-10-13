from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topic, name='board_topics'),
    path('signup/', views.signup, name='signup'),
]