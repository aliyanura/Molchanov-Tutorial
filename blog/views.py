from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import *
from .forms import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', locals())


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', locals())


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template =  'blog/post_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list'
    

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list'