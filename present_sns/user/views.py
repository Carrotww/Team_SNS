from django.shortcuts import render,redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model  # 사용자가 데이터 베이스안에있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def testpage(request):
    return render(request, 'temp_test/nav.html') # 기본 test page

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

def login(request):
    return render(request, 'user/login.html')

def main_user(request):
    return render(request, 'user/main_user.html')

def signup(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        # me = UserModel.objects.get(username=username)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)
        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')
    return render(request, 'user/signup.html')

def main(request): # 로그인 후 main page 보여주기 형식
    if request.method == 'GET':
        return render(request, 'temp_test/main.html')

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        # me = UserModel.objects.get(username=username)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        bio = request.POST.get('bio', None)
        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return HttpResponse('로그인 성공!' + username + '님 반갑 습니다')
        else:
            return redirect('/sign-in')
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return  redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required()
def logout(request):
    auth.logout(request)
    return  redirect('/')
