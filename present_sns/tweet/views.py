from pyclbr import readmodule
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import UserModel
from .models import TweetModel
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from uuid import uuid4
import os
# BEOki 추가

from django.contrib import messages
from django.db.models import Q
# BEOki 추가
from present_sns.settings import MEDIA_ROOT
# from models import UserModel
from django.contrib.auth.decorators import login_required # need login module
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


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
            all_comment = Comment.objects.all().order_by('comment_write')
            temp_comment = []
            for i in all_tweet:
                pass
            if all_comment:
                if len(all_comment) >= 2:
                    for i in range(2):
                        temp_comment.append(all_comment[i])
                else:
                    for i in all_comment:
                        temp_comment.append(i)
                return render(request, 'user/main_page.html', {'tweet': all_tweet}) 
                #{'comment': temp_comment})
            
            return render(request, 'user/main_page.html', {'tweet': all_tweet})
        else:  # 로그인이 되어 있지 않다면
            return redirect('/signin')
            
    elif request.method == 'POST':  # main_profile 에서 dict 형태로 가져옴
        username = request.user.username  # 현재 로그인 한 사용자를 불러오기
        my_tweet = TweetModel()  # 글쓰기 모델 가져오기
        my_tweet.username = request.POST.get('')
        my_tweet.content = request.POST.get('my-content', '')  # 모델에 글 저장
        my_tweet.tweet_img = request.POST.get('tweet_img','') # 트윗에 길
        my_tweet.save()
        return redirect('/main')

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
class UploadTweet(APIView):
    def post(self, request):
        #파일 불러오기
        file = request.FILES['file']
        # 고유아이디 값을 주기 위해 uuid를 사용함(파이슨에서 사용하는 문법)
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:  #파일을 저장,open이 저장 경로
            for chunk in file.chunks():
                destination.write(chunk)
        
        tweet_img = uuid_name #업로드 이미지
        content = request.data.get('content')
        username = request.user
        # user_img = request.data.get('user_img')
        tags = request.data.get('tag', '').split()
        write_no = request.data.get('write_no')
        
        current_tweet = TweetModel.objects.create(tweet_img=tweet_img, content=content,
        username=username, write_no=write_no)
        # user_img=user_img, # like_count=0,
        if tags:
            for tag in tags:
                tag = tag.strip()
                if tag != '':
                    current_tweet.tags.add(tag)
        current_tweet.save()
        
        return Response(status=200), redirect('/main')

@login_required
def user_profile_delete(request, write_no):
    # current_user_tweet = TweetModel.objects.filter(username=username)
    current_user_tweet = TweetModel.objects.get(write_no=write_no)
    # for i in current_user_tweet:
    #     if i['write_no'] == write_no:
    #         i.delete()
    #         continue
    current_user_tweet.delete()
    return redirect('/main')

@login_required
def EditPeed(request, write_no):
    
    if request.method == "POST":
        editpeed = TweetModel.objects.get(write_no=write_no)
        editpeed.content = request.POST.get('content', '')
        editpeed.tags = request.POST.get('tags')
        editpeed.save()
        print(request.POST) #수정할 부분 보여줌
        return redirect('/main')

def read_tweet(request, write_no):
    if request.method == 'GET':
        click_tweet = TweetModel.objects.get(write_no=write_no)
        comments = click_tweet.comment_set.all()
            
        return render(request, 'tweet/read.html', {'tweet': click_tweet, 'comments': comments})
        # return render(request, 'tweet/read.html', {'tweet': click_tweet})

@login_required
@csrf_exempt
def comment_write(request, id):
    print('testestestesttest')
    print('testestestesttest')
    print('testestestesttest')
    print('testestestesttest')
    if request.method == 'POST':
        username = request.user.username
        comment = request.POST.get('my-comment',"")
        if comment == '':
            messages.warning(request, '댓글을 입력해 주세요!')
            return redirect('/main/read/'+str(id))
            # return redirect('/main/read/'+str(id), {'error': '댓글을 입력해 주세요!'})
        
        WC = Comment()
        WC.write_no_id = id
        WC.comment = comment
        WC.username_id = username
        WC.save()
        return redirect('/main/read/'+str(id))

@login_required
def comment_delete(request, id, write_no_id):
    current_comment = Comment.objects.get(id=id)
    # temp_write_no = current_comment.write_no
    current_comment.delete()
    
    return redirect('/main/read/'+str(write_no_id))

@login_required
def write_main_comment(request, id, username): # id값은 write_no의 id값
    if request.method == "POST":
        comment = request.POST.get('my-comment',"")
        current_tweet_id = TweetModel.objects.get(write_no=id) # 작성 post의 id
        write_username = UserModel.objects.get(username=username)

        WC = Comment()
        WC.write_no = current_tweet_id
        WC.comment = comment
        WC.username = write_username
        WC.save()

        return redirect('/main/' + str(id))
        # return redirect(f'/main/{str(c)urrent_tweet_id}/read/')

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html' # tag_cloud_view.html 아직 없음!

class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html' # tag_with_post.html 아직 없음!
    model = TweetModel
    
    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

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

@login_required
def search(request):
    if request.method == "POST":
        search_keyword = request.POST['search']
        print(search_keyword)
        if not search_keyword:
            return redirect('/main')
        else:
            if len(search_keyword) >= 2 :
                searched = TweetModel.objects.filter(Q(content__icontains=search_keyword))
                # | Q(tags__icontains=search_keyword) 컬럼tags 추가요망                
                for i in searched:
                    print(searched)
                return render(request, 'tweet/searhed.html',{'searched': searched})
            if len(search_keyword) <= 1:
                return redirect('/main')

class TagCloudTV(TemplateView):
    template_name = 'tweet/searhed.html'

class TaggedObjectLV(ListView):
    template_name = 'tweet/searhed.html'
    model = TweetModel
    
    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context