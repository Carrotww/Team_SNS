from django.urls import path
from . import views # user app의 views를 import 해옴

urlpatterns = [
   path('', views.home, name='home'), # default path -> main 
   path('main/',views.main, name='main'), #메인 페이지 접속
   path('tweet/user_profile/', views.user_profile, name='user_profile'),
#    path('tweet/user_profile/<str:nickname>/')
]