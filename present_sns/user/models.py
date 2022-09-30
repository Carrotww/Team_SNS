from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "user_table"
        # 테이블 이름을 나타냄

    bio = models.CharField(max_length=256, default='')
    # user model을 가져왔고 bio 만 추가해서 사용
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    nickname = models.CharField(max_length=8, default='', primary_key =True, blank=False, unique=True)
    user_img = models.ImageField(upload_to='user', null=True, blank=True, default=None)
    following = models.ManyToManyField('self', null=True, blank=True)
    follow = models.ManyToManyField('self', null=True, blank=True)
