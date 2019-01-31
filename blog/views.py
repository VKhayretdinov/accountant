from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from . import info_db
from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_add_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})


def inn(request):
    inn = request.GET.get('INN', '')
    org_name = request.GET.get('orgName', '')
    org_name = org_name.upper()
    if inn:
        res = info_db.search_by_inn(inn)
        print(res)
        return render(request, 'blog/INN.html', res)
    if org_name:
        res = info_db.search_by_org_name(org_name)
        return render(request, 'blog/INN.html', res)

    return render(request, 'blog/INN.html')
