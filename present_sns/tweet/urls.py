from django.urls import path
from . import views # user app의 views를 import 해옴

# 1. main -> myprofile로 가는 경로
# 2. 게시물 보이는거, 작성하는 경로 + tag
# Beomki 회원정보수정 링크 연결

# 1. main page -> my_profile
# 2. tweet


urlpatterns = [
   path('', views.home, name='home'), # default path -> main 
   path('main/',views.main, name='main'), #메인 페이지 접속
   path('main/user_profile',views.user_profile, name='user_profile'),
   path('main/user_profile_delete/<int:write_no>', views.user_profile_delete, name='user_profile_delete'),
   path('main/user_profile_edit/<int:write_no>', views.user_profile_edit, name='user_profile_edit'),

   # main page -> edit user profile

   path('main/<str:username>', views.user_profile, name='user_profile'),
#    path('main/user_profile')
   path('profileupdate/',views.profileupdate ,name='profileupdate'),
#    path('tweet/user_profile/<str:nickname>/')
]