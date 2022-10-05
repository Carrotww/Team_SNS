# tweet/models.py
from django.db import models
from user.models import UserModel
# user app 에서 usermodel 을 가져와서 사용
from taggit.managers import TaggableManager


# Create your models here.
class TweetModel(models.Model):
    class Meta:
        db_table = "tweet_table"

    write_no = models.AutoField(primary_key=True) # wirte number -> 기본키
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 외래키
    title = models.CharField(max_length=64, blank = False)
    content = models.CharField(max_length=256,blank = False)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tweet_img = models.ImageField(upload_to='tweet', null=True, blank=True, default=None) #업로드 이미지
    profile_img = models.TextField()


class Comment(models.Model):
    class Meta:
        db_table = "comment_table"
    write_no = models.ForeignKey(TweetModel, on_delete=models.CASCADE) # tweet 에서 가져온 외래키
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE) # user_table 에서 가져온 user username 외래키
    comment = models.CharField(max_length=100, null=False) # comment, 빈 값은 허용 X
    comment_write = models.DateTimeField(auto_now_add=True) # 작성 시간
    comment_update = models.DateTimeField(auto_now=True) # 수정 시간