from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.utils import timezone
from .models import MyPost
from .forms import PostForm


def index(request):
    posts = MyPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def category(request, catid):
    return HttpResponse(f"<h1>Cats{catid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Странциа не найдена</h1>")


def post_info(request, pk):
    post = get_object_or_404(MyPost, pk=pk)
    return render(request, 'blog/post_info.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})
