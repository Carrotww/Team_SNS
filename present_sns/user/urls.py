from django.urls import path,include # include 사용하기위함
from django.views.decorators.csrf import csrf_exempt
from . import views # user app의 views를 import 해옴
from django.contrib.auth import views as auth_views

app_name = "user"
urlpatterns = [
    path('', views.testpage), # 테스트용 main 페이지 입니다.
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('test4/', views.test4),
    path('test5/', views.test5),
    path('login/',views.login, name='login'), #login 페이지 접속
    path('signup/', views.signup), #signup 페이지 접속
    path('main_user/',views.main_user),
    # path('logout/',views.logout,name='logout'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 코드 추가하기
    path('profileupdate/',views.profileupdate ,name='profileupdate'),
]