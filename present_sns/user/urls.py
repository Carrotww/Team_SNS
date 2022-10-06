
from django.urls import path, include # include 사용하기위함
from django.views.decorators.csrf import csrf_exempt
from . import views # user app의 views를 import 해옴
from django.contrib.auth import views as auth_views
app_name = "user"
urlpatterns = [
    path('signup/', views.signup), #signup 페이지 접속
    path('my_profile/', views.my_profile), #마이 프로필 접속
    
    # path('profileupdate/',views.profileupdate ,name='profileupdate'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 코드 추가하기
    path('login/',views.login, name='login'), #login 페이지 접속
    path('my_profile/', views.my_profile ,name='my_profile'),


]