from django.shortcuts import render

# Create your views here.
def testpage(request):
    return render(request, 'temp_test/main_test.html') # 기본 test page

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

def signup(request):
    return render(request, 'user/signup.html')