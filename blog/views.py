
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-date_published').all()
    return render(request, 'blog/index.html', {"posts": posts})


def about(request):
    return render(request, 'blog/about.html')


class ListPost(ListView):
    paginate_by = 10
    model = Post


class CreatePost(LoginRequiredMixin, CreateView, User):
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")


class DetailPost(DetailView):
    model=Post


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")


class DeletePost(LoginRequiredMixin, DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        post_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=post_title)


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'groups']
    success_url = reverse_lazy("blog-login")
