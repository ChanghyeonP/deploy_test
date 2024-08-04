from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

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
