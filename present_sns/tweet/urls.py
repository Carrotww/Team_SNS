from django.urls import path
from . import views # user app의 views를 import 해옴
from tweet.views import UploadTweet
from present_sns.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .models import TweetModel
from django.db import models
from .views import search


# 1. main -> myprofile로 가는 경로
# 2. 게시물 보이는거, 작성하는 경로 + tag
# Beomki 회원정보수정 링크 연결

# 1. main page -> my_profile
# 2. tweet


urlpatterns = [
   path('', views.home, name='home'), # default path -> main 
   path('main/',views.main, name='main'), #메인 페이지 접속
   
   path('main/user_profile',views.user_profile, name='user_profile'), # 내 프로필 페이지
   path('main/user_profile_delete/<int:write_no>', views.user_profile_delete, name='user_profile_delete'), # 게시물 삭제
   path('main/tweet_edit/<str:write_no>', views.EditPeed, name='tweet_post'), #게시물 수정
   path('main/read/<int:write_no>', views.read_tweet, name='read_tweet'), # 게시글 상세페이지 접속
   path('main/comment/<int:id>', views.comment_write, name='comment_write'), # 해당 게시글의 댓글 작성
   path('main/read/comment/delete/<int:id>/<int:write_no_id>', views.comment_delete, name='comment_delete'), # 해당 게시글의 댓글 삭제 
   
   path('main/tweet_post', UploadTweet.as_view(), name='tweet_post'),
 
   
   path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
   path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

   # main page -> edit user profile
   path('main/<str:username>', views.user_profile, name='user_profile'),
#    path('main/user_profile')
   path('profileupdate/',views.profileupdate ,name='profileupdate'),
#    path('tweet/user_profile/<str:username>/')
   path('search', views.search, name='search'),
]

# 파일을 저장하는 미디어파일 확장하기 위해
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)