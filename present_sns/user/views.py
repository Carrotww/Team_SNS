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

# Create your views here.
def testpage(request):
    return render(request, 'user/login.html') # 기본 test page

def test1(request):
    return render(request, 'temp_test/testpage1.html')

def test2(request):
    return render(request, 'temp_test/testpage2.html')

def test3(request):
    return render(request, 'temp_test/testpage3.html')

def test4(request):
    return render(request, 'temp_test/testpage4.html')

def test5(request):
    return render(request, 'temp_test/testpage5.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        print('리퀘스트 로그 '+ str(request.body))
        username =request.POST.get('username',None)
        password =request.POST.get('userpw',None)
        print ("name =" +username +"PW="+password)

        user = authenticate(request, username=username, password=password)
        if not user:
            return render(request,'user/login.html') 
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

        if userpw !=userpw2:
            return render(request, 'user/signup.html',{})
        else:
            user_table = UserModel()
            user_table.username=username
            user_table.set_password(userpw2)
            user_table.nickname=usernickname
            user_table.user_img=userimg
            user_table.email=useremail
            user_table.phone=phone
            user_table.save()
        
        return redirect('/login')


@login_required()
def logout(request):
    auth.logout(request)
    return  redirect('/')


@csrf_exempt
def main_page(request):
    return render(request, 'user/main_page.html') 

def my_profile(request):
    return render(request, 'user/my_profile.html')

def read(request):
    return render(request, 'tweet/read.html')