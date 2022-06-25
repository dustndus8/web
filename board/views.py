from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from board.forms import PostForm
from board.models import Post
from reply.forms import ReplyForm

@login_required(login_url='/accounts/login')
def like(request,bid):
    # 어떤 게시물에, 어떤 사람이 like를 했는 지
    post = Post.objects.get(id=bid) # 게시물 번호 몇번인지 정보 가져옴
    user = request.user
    if post.like.filter(id=request.user.id).exists(): # 유저면 알아서 유저의 id로 검색해줌
        post.like.remove(user)
        return JsonResponse({'message': 'deleted', 'like_cnt' : post.like.count() })
    else:
        post.like.add(user) # post의 like에 현재유저의 정보를 넘김
        return JsonResponse({'message': 'added', 'like_cnt' : post.like.count()})



def mainPage(request):
    posts = Post.objects.all().order_by('-id')  # id 순으로 정렬하는데 - 니까 오름차순으로 정렬
    context = {'posts': posts}
    return render(request, 'board/main.html', context)

@login_required(login_url='/accounts/login')
def create(request):
    if request.method == "GET": # 작성하거나 수정할 페이지 띄워줌
        # postForm을 이용해 정보를 받아옴
        postForm = PostForm()
        context = {'postForm' : postForm}
        return render(request, 'board/update.html',context)
    elif request.method == "POST": # 실제 그 내용이 DB에 저장되도록
        # postForm을 받아와 유효성 확인이 되면, save 해줌
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.writer = request.user  # 현재 로그인한 사용자를 writer로 고정시켜줘야함
            post.save()
            print(post.id)
        return redirect('/board/readGet/'+str(post.id)) # 자기가 쓴 게시물 조회로 가도록 함

def listGet(request):
    posts = Post.objects.all().order_by('-id') # id 순으로 정렬하는데 - 니까 오름차순으로 정렬
    context = {'posts' : posts}
    return render(request, 'board/list.html',context)

def readGet(request, bid):
    # post = Post.objects.filter(id=bid)

    # select_related : 댓글을 뽑으려하는데 댓글과 관련된 게시물을 뽑으려할 때 (Reply모델에 post가 있으면 정방향)
    # prefetch_related : 게시글에 대한 모델  (post로 갔는데 댓글이 없는데, 댓글 조회하고 싶으면 역방향이라고 함)

    post = Post.objects.prefetch_related('reply_set').get(id=bid) # Q (장고에 있는 모델) 이용해서 하나만 조회 가능 (filter은 for문 해야하는데 이 경우 하나만 가능)
    replyForm = ReplyForm()
    context = {
        'post' : post,
        'replyForm': replyForm
    }

    return render(request, 'board/read.html',context)

@login_required(login_url='/accounts/login')
def deleteGet(request,bid):
    post = Post.objects.get(id=bid) # Q 안쓰고도 가능, Q는 쿼리 들어갈 때 여러 기능
    # writer와 현재 user가 같을 때만 삭제 시켜줘야 함
    if request.user != post.writer:
        return redirect('/board/listGet')
    post.delete()
    return redirect('/board/listGet') # board의 list url로 redirect 되게 함

@login_required(login_url='/accounts/login')
def update(request,bid):
    # 해당 게시글이 한번 조회가 되어야 함
    post = Post.objects.get(id=bid)
    if request.method == "GET" : # 작성하거나 수정할 페이지 띄워줌
        context = {'post' : post}
        return render(request,'board/update.html',context) # 수정할 페이지를 띄워줌

    elif request.method == "POST" : # 실제 그 내용이 DB에 저장되도록
        postForm = PostForm(request.POST, instance=post) # 위에서 받아온 게시물의 내용을 Form으로 받아옴
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()

        return redirect('/board/readGet/'+str(post.id))# 수정 후 조회하는 곳으로 이동
