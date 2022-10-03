from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views # user app의 views를 import 해옴

urlpatterns = [
    path('', views.testpage), # 테스트용 main 페이지 입니다.
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('test4/', views.test4),
    path('test5/', views.test5),
    path('login/',views.login), #login 페이지 접속
    path('signup/', views.signup), #signup 페이지 접속
    path('main/',views.main_page), #메인 페이지 접속
    path('logout/',views.logout,name='logout'),
    path('my_profile/', views.my_profile), #마이 프로필 접속
    path('read/', views.read), # 게시글 상세페이지 접속
]