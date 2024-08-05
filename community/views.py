from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def community_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community')
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, 'community.html', {'form': form, 'posts': posts})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author or request.user.is_staff:  # 자기 자신 또는 관리자인 경우만 삭제할 수 있습니다.
        if request.method == 'POST':
            post.delete()
            return redirect('community')
        return render(request, 'delete_post.html', {'post': post})
    else:
        return redirect('community')