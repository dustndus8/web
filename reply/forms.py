from django import forms

from reply.models import Reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply # model은 Post 양식으로 쓰겠다.
        fields = ('contents',) # 어떤 필드를 입력 받을 지
        exclude = ('writer',)




