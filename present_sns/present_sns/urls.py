from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('user.urls')), # hyeong - user.urls 로 보내줌
    # path('', include('tweet.urls')),
]
