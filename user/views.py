from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout # login함수이름과 겹쳐서 auth_login으로 해줌


# 회원가입
def singup(request):
    if request.method == "GET":
        signupForm = UserCreationForm() # 장고에서 제공하는 유저 Form
        return render(request,'user/signup.html', {'signupForm':signupForm})
    elif request.method == "POST":
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save(commit=False)
            user.save()

        return redirect('/board/listGet') # 회원가입 하면 게시글 목록으로 가도록 이동시켜줌
# 회원탈퇴

def signout(request, uid):
    user = User.objects.get(id=uid)  # Q 안쓰고도 가능, Q는 쿼리 들어갈 때 여러 기능
    # writer와 현재 user가 같을 때만 삭제 시켜줘야 함
    user.delete()
    return redirect('/main')  # board의 list url로 redirect 되게 함

# 로그인 입력 양식이 주어져야함
def login(request):
    if request.method == "GET":
        loginForm = AuthenticationForm() # 로그인 시 사용하는 Form
        print(loginForm)
        return render(request,'user/login.html', {'loginForm' : loginForm})
    elif request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST) # request와 request.POST를 둘 다 넣어주어야 함
        print(loginForm.request.POST)
        print("으응??")
        if loginForm.is_valid():
            print('loginForm error')
            auth_login(request, loginForm.get_user()) # request, 유저정보를 뽑아 넣어줌 id, pw를 직접 뽑아내서 아이디 비번 맞는지 할 필요 없이 이렇게 하면됨
            return redirect('/main')
        else:
            print('loginform no valid')
            return redirect('/user/login')
def logout(request):
    # 세션 정보를 지우는 것
    auth_logout(request)
    return redirect('/board/listGet')