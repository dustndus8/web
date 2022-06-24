from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from board.models import Post
from reply.forms import ReplyForm
from reply.models import Reply


@login_required(login_url='/accounts/login')
def create(request,bid):
    if request.method == "POST":
        replyForm = ReplyForm(request.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False) # 저장 전 확인
            post= Post()
            post.id = bid
            reply.post = post
            reply.writer = request.user
            reply.save()
        return redirect('/board/readGet/'+str(post.id))

def read(request,rid):
    reply = Reply.objects.get(id=rid)
    context = {
        'reply' : reply
    }
    return render(request,'reply/read.html',context)

def list(request):
    replys = Reply.objects.all().order_by('-id')
    context = {
        'replys' : replys
    }
    return render(request, 'reply/list.html',context)

@login_required(login_url='/accounts/login')
def delete(request,rid):
    reply = Reply.objects.get(id=rid)
    post_id = reply.post_id
    reply.delete()
    return redirect('/board/readGet/'+str(post_id))

@login_required(login_url='/accounts/login')
def update(request,rid):
    reply = Reply.objects.get(id=rid)
    if request.method == "GET":
        replyForm = ReplyForm(instance=reply)
        context = {'replyForm':replyForm}
        return render(request, 'reply/create.html', context)
    elif request.method == "POST":
        replyForm = ReplyForm(request.POST, instance=reply)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False) # 저장 전 확인
            reply.save()
        return redirect('/reply/read/'+str(reply.id)) # 자신이 쓴 댓글로 가도록함