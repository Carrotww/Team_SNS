from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class UserModel(AbstractUser): # 적용하기 위해서 admin.py에서 적용 시켜주어야 함
    class Meta:
        db_table = "user_table"
        # 테이블 이름을 나타냄

    username = models.CharField(max_length=20,null=False,unique=True)
    # unique -> False 로 나중에 변경 해야함 동명이인 가입 불가능
    password = models.CharField(max_length=256,null=False)
    bio = models.CharField(max_length=256, default='')
    # user model을 가져왔고 bio 만 추가해서 사용
    nickname = models.CharField(max_length=8, default='', blank=False, unique=True)
    user_img = models.ImageField(upload_to='user', null=True, blank=True, default=None)
    phone = models.CharField(max_length=256,null=True,unique=True)


    bio = models.CharField(max_length=256, default='') # user model을 가져왔고 bio 만 추가해서 사용
    # follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
    nickname = models.CharField(max_length=8, default='', primary_key =True, blank=False, unique=True)
    # user_img = models.ImageField(upload_to='images/',blank=True, null=True) 아래 photo클래스에 이관
    # following = models.ManyToManyField('self', null=True, blank=True) # manytomany 오류 해결불가능으로 일시적으로 주석처리
    # follow = models.ManyToManyField('self', null=True, blank=True)
    # def __str__(self):
    #     return self.title # 정확한의미를 모르겠음..
class Photo(models.Model):
    userModel = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    user_img = models.ImageField(upload_to='images/', blank=True, null=True)
