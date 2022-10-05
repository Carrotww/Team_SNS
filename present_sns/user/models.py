from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "user_table"
        # 테이블 이름을 나타냄

    username = models.CharField(max_length=20,null=False, primary_key=True)
    # user_id
    # unique -> False 로 나중에 변경 해야함 동명이인 가입 불가능
    password = models.CharField(max_length=256,null=False)
    bio = models.CharField(max_length=256, default='')
    # user model을 가져왔고 bio 만 추가해서 사용
    user = models.CharField(max_length=8, blank=False) # 사람 이름
    # user_img = models.ImageField(upload_to='user', null=True, blank=True, default=None)
    phone = models.CharField(max_length=256,null=True,unique=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    # followers = models.ManyToManyField('self', related_name='follower',blank=True)
    # following = models.ManyToManyField('self', related_name='following',blank=True)

# class UserFollowing(models.Model):
#     user_id = models.ForeignKey(UserModel, related_name="following", on_delete=models.CASCADE)
#     following_user_id = models.ForeignKey(UserModel, related_name="followers", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

