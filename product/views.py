from django.shortcuts import render

# Create your views here.
from product.models import Fruits


def createFruitGet(request): # 입력 페이지 띄워주는 함수
    return render(request, 'product/create.html')

def createFruitPost(request): # db에 과일 정보 데이터 저장
    fruit = Fruits()
    fruit.name = request.POST.get('fname',None)
    fruit.descript = request.POST.get('fdescript',None)
    fruit.price = request.POST.get('fprice',None)
    fruit.quantity = request.POST.get('fquantity',None)

    fruit.save() # DB에 저장시켜줌

    return render(request, 'product/createResult.html')

def readFruitGet(request): # 읽기
    fruits = Fruits.objects.all() # Fruits 모델의 모든 객체들 불러옴
    fruit_one = Fruits.objects.filter(id=1) # filter를 이용해 원하는 데이터 불러옴

    context = {
        'fruits' : fruits,
        'fruit_one' : fruit_one,
    }
    return render(request, 'product/read.html', context)