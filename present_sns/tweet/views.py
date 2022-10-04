
from django.shortcuts import render, redirect
from .models import UserModel
from .models import TweetModel
from .models import Comment
# from models import UserModel
from django.contrib.auth.decorators import login_required # need login module


# Create your views here.

def home(request):
    user = request.user.is_authenticated
    # user가 login 상태인지 아닌지 판별 할 수 있는 djanogo 기능
    if user:
        return redirect('/main')
    else:
        return redirect('/login')

def main(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # user가 login 상태인지 아닌지 판별 할 수 있는 djanogo 기능
        if user:
            return render(request, 'user/main_page.html')
        else:
            return redirect('/login')


def user_profile(request):
    if request.method == 'GET':
        user = request.user.is_authenticated

        if user:
            all_user = UserModel.objects.all()
            for i in all_user:
                if i == user:
                    return render(request, 'user/my_profile.html')
        else:
            redirect('/main')
            

# def defualt_comment(request):
#     pass