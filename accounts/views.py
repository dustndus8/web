import json
import os
import requests

from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import ProfileFormImage
from accounts.models import User, ProfileImage
from config.settings import BASE_DIR

secret_files = os.path.join(BASE_DIR, 'secret.json')

def read(request):
    if request.method=="GET":
        user = User.objects.get(id=request.user.id)
        userimage = User.objects.prefetch_related('profileimage_set').all().order_by('-id')
        profileFormImage = ProfileFormImage()
        context = {'user':user, 'profileFormImage':profileFormImage}
        return render(request, 'account/read.html', context)

def create(request):
    if request.method == "GET":  # 작성하거나 수정할 페이지 띄워줌
        # postForm을 이용해 정보를 받아옴
        profileFormImage = ProfileFormImage()
        context = {'profileFormImage': profileFormImage}
        return render(request, 'account/create.html', context)
    elif request.method == "POST":
        if (ProfileImage.objects.first() is not None):
            profile = ProfileImage.objects.filter(user_id=request.user.id).delete()
            print('profile',profile)
        profileFormImage = ProfileFormImage(request.POST)
        print('post~~')
        if profileFormImage.is_valid():
            print('if문')
            #user = profileFormImage.save(commit=False)
            #user.user_id = request.user.id
            #user.save()
            for image in request.FILES.getlist('image',None):
                print('for문',image)
                profileImage = ProfileImage()
                print('프로필:',profileImage)

                profileImage.image = image
                profileImage.user_id = request.user.id
                print('프로필다음',profileImage)
                profileImage.save()
                print(profileImage)

        return redirect('/account/read')

def delete(request):
    if (ProfileImage.objects.first() is not None):
        profile = ProfileImage.objects.filter(user_id=request.user.id).delete()
        print('profile', profile)

    return redirect('/account/read')

def getcode(request):
    code = request.GET.get('code')

    with open(secret_files) as f:
        secrets = json.loads(f.read())
    # REST API를 이용해 토큰 발급 받아옴 (카카오에게)
    requests.post('https://kauth.kakao.com/oauth/token')
    data = {'grant_type': "authorization_code"
        , 'client_id': secrets['CLIENT_ID'],
            'redirect_uri': 'http://127.0.0.1:8000/oauth/redirect',
            'code': code}
    headers = {'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    res = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=headers)
    token_json = res.json()
    print(token_json)


    # REST API를 이용해 토큰으로 정보를 조회
    access_token = token_json['access_token']

    headers = {'Authorization': 'Bearer ' + access_token,
               'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'}
    res = requests.get("https://kapi.kakao.com//v2/user/me", headers=headers)
    profile_json = res.json()
    print(profile_json)
    print(profile_json['properties']['nickname'])
    kakaoid = profile_json['id']

    user = User.objects.filter(email=kakaoid)

    if user.first() is not None:
        login(request, user.first(), backend='django.contrib.auth.backends.ModelBackend')
        print('if문 login')
        return render(request, 'board/main.html')
    else:
        user = User()
        user.email = kakaoid
        user.username = profile_json['properties']['nickname']
        user.save()
        return render(request, 'login.html')


    return HttpResponse(code)