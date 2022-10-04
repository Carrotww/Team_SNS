
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
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'user/main_page.html', {'tweet': all_tweet})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/signin')
            
    elif request.method == 'POST':  # main_profile 에서 dict 형태로 가져옴
        username = request.username  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.write_no = username  # 모델에 사용자 저장
        my_tweet.nickname = request.POST.get('')
        my_tweet.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_tweet.tweet_img = request.POST.get('tweet_img','') # 트윗에 길
        my_tweet.save()
        return redirect('/main')

"""
    write_no = models.AutoField(primary_key=True) # wirte number -> 기본키
    nickname = models.ForeignKey(UserModel, on_delete=models.CASCADE) # 외래키
    title = models.CharField(max_length=64, blank = False)
    content = models.CharField(max_length=256,blank = False)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tweet_img = models.ImageField(upload_to='tweet', null=True, blank=True, default=None) #업로드 이미지
    profile_img = models.TextField()
"""


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

# @login_required
# def delete_tweet(request, id):
#     my_tweet = TweetModel.objects.get(id=id)
#     my_tweet.delete()
#     return redirect('/tweet')

@login_required
def user_profile_delete(request, write_no):
    # current_user_tweet = TweetModel.objects.filter(nickname=nickname)
    current_user_tweet = TweetModel.objects.get(write_no=write_no)
    # for i in current_user_tweet:
    #     if i['write_no'] == write_no:
    #         i.delete()
    #         continue
    current_user_tweet.delete()
    return redirect('/main')

def defualt_comment(request):
    pass

def profileupdate(request):
    if request.method == "POST":
        
        user_table = request.user
        user_table.phone=request.POST.get('phone'," ")
        user_table.password=request.POST.get('userpw'," ")
        user_table.user_id=request.POST.get('user_id'," ")
        user_table.email=request.POST.get('useremail'," ")
        # user_table.user_img=request.POST.get('userimg'," ")
        user_table.bio=request.POST.get('bio'," ")

        user_table.set_password(user_table.password)
        user_table.user_id=user_table.user_id
        # user_table.user_img=user_table.user_img
        user_table.email=user_table.email
        user_table.phone=user_table.phone
        user_table.bio=user_table.bio
        user_table.save()
        return redirect('/')
    return render(request, 'user/profileupdate.html')