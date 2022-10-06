from telnetlib import STATUS
from unittest import result
from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터 베이스안에있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# csrf_exempt 는 보안관련
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
import logging
logger = logging.getLogger(__name__)
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username =request.POST.get('username', None)
        password =request.POST.get('userpw', None)

        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request, 'user/login.html', {'error':'이름 혹은 패스워드를 확인 해 주세요'}) 
        else:
            auth.login(request, user)
            return redirect('/main')

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/main')
        else:
            return render(request, 'user/login.html')



@csrf_exempt
def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/main')
        else:
            return render(request, 'user/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username','')
        userpw = request.POST.get('userpw','')
        userpw2 = request.POST.get('userpw2','')
        user = request.POST.get('user','')
        # userimg = request.POST.get('userimg','')
        useremail = request.POST.get('useremail','')
        phone = request.POST.get('phone','')
        bio = request.POST.get('bio','')


        if userpw != userpw2:
            return render(request, 'user/signup.html',{'error':'패스워드를 확인해주세요!'})
        else:
            if username == '' or userpw == '':
                return render(request, 'user/signup.html',{'error':'사용자 이름과 비밀번호는 필수입니다!'})
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html',{'error':'사용자가 이미 존재합니다!'})
            else:
                user_table = UserModel()
                user_table.username=username
                user_table.set_password(userpw2)
                user_table.user=user
                # user_table.user_img=userimg
                user_table.email=useremail
                user_table.phone=phone
                user_table.bio=bio
                user_table.save()
        
                return redirect('/login')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/login')


@csrf_exempt
def my_profile(request):
    return render(request, 'user/my_profile.html')

@csrf_exempt
def my_profile(request):
    return render(request, 'user/my_profile.html')
