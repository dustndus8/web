from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    sub_title = models.CharField(max_length=40)
    # writer은 다른 모델을 참조하겠다.(User) 외래키 추가
    writer = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete : User가 delete 될 때 게시글을 어떻게 설정한 것인지에 대해 설정 1. 게시글 같이 지우기(CASCADE) 2. 없는 값으로 해서 게시글은 남겨두기
    # 다대다 관계는 ManyToManyField, 아무도 누르지 않을 수 있으니 blank가 True, 참조할 때 이름을 지어줌(위에서랑 겹치지않게)
    like = models.ManyToManyField(User, related_name='likes' ,blank=True)
    def __str__(self):
        return 'id : {}, title : {}'.format(self.id, self.title, self.contents)