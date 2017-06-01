from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Tag
from .forms import BlogPostCreateModelForm, LoginForm, BlogPostRegistrationForm
from . import services
from .decorators import anonymous_required


def index(request):
    if not request.session.get('counter'):
        request.session['counter'] = 0

    request.session['counter'] += 1
    if request.user.is_authenticated:
        posts = services.get_all_blogs()
    else:
        posts = services.get_private_posts()
        
    tags = Tag.objects.all()

    return render(request, 'blog/index.html', locals())

@login_required(login_url=reverse_lazy('blog:index'))
def create_blog_post(request):
    form = BlogPostCreateModelForm()

    if request.method == 'POST':
        form = BlogPostCreateModelForm(data=request.POST)

        if form.is_valid():
            services.create_blog_post(**form.cleaned_data)
            return redirect(reverse('blog:index'))

    return render(request, 'blog/create.html', locals())


@anonymous_required(profile_url=reverse_lazy('blog:profile'))
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is None:
                form.add_error(field='', error='No such user')
            else:
                login(request, user)

    return render(request, 'blog/login.html', locals())

@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('blog:index'))

@login_required(login_url=reverse_lazy('blog:index'))
def profile_view(request):

    return render(request, 'blog/profile.html', locals())

def single_post(request, id):
    post = BlogPost.objects.filter(id=id).first()
    # BlogPost.objects.filter(is_private=True)

    return render(request, 'blog/single_post.html', locals())

def register_new_account(request):
    tags = Tag.objects.all()
    form = BlogPostRegistrationForm()
    if request.method == "POST":
        form = BlogPostRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)

            return redirect(reverse('index'))
        else:
            alert = form.errors
            return render(request, 'blog/register.html', {'alert': alert})
    return render(request, 'blog/register.html', locals())
