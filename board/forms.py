from django import forms

from board.models import Post, PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post # model은 Post 양식으로 쓰겠다.
        fields = ('title', 'sub_title', 'contents') # 어떤 필드를 입력 받을 지
        exclude = ('writer', ) # 폼에서 writer 입력받지 않게 함

class PostFormImage(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image',)