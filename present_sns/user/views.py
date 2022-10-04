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

# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('리퀘스트 로그 '+ str(request.body))
        username =request.POST.get('username',None)
        password =request.POST.get('userpw',None)
        print ("name =" +username +"PW="+password)

        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request,'user/login.html', {'error':'이름 혹은 패스워드를 확인 해 주세요'}) 
        django_login(request, user) 
        return redirect('/main')

    elif request.method == 'GET':
        return render(request, 'user/login.html')



@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request, 'user/signup.html')
    elif request.method == "POST":
        username = request.POST.get('username','')
        userpw = request.POST.get('userpw','')
        userpw2 = request.POST.get('userpw2','')
        usernickname = request.POST.get('usernickname','')
        userimg = request.POST.get('userimg','')
        useremail = request.POST.get('useremail','')
        phone = request.POST.get('phone','')
        bio = request.POST.get('bio','')

        if userpw != userpw2:
            return render(request, 'user/signup.html',{})
        else:
            exist_user = UserModel.objects.filter(username=username)
            
            if exist_user:
                return render(request, 'user/signup.html')  #사용자가 이미 존재하는 경우 회원가입 다시
            else:
                user_table = UserModel()
                user_table.username=username
                user_table.set_password(userpw2)
                user_table.nickname=usernickname
                user_table.user_img=userimg
                user_table.email=useremail
                user_table.phone=phone
                user_table.bio=bio
                user_table.save()
        
                return redirect('/login', {'error':'이름 혹은 패스워드를 확인 해 주세요'})

@csrf_exempt
def my_profile(request):
    return render(request, 'user/my_profile.html')
@csrf_exempt
def read(request):
    return render(request, 'tweet/read.html')

@csrf_exempt
def profileupdate(request):
    return render(request, 'user/profileupdate.html')

@csrf_exempt
def my_profile(request):
    return render(request, 'user/my_profile.html')