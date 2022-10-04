from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static # djaongo 이미지 불러오기
from django.conf import settings #django 이미지 불러오기

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user.urls')), # hyeong - user.urls 로 보내줌
    path('', include('tweet.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Beomki static 불러오는 코드