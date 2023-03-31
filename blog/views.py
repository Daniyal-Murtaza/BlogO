from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogForm
from django.db.models import Q
from django.contrib.auth import logout

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            Blog = form.save(commit=False)
            Blog.author = request.user
            Blog.save()
            form.save_m2m()
            return redirect('blog_detail', pk=Blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blog/blog_create.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def index(request):
    blogs = Blog.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/index.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

def tag_filter(request, tag):
    blogs = Blog.objects.filter(tags__contains=tag)
    return render(request, 'blog/tag_filter.html', {'blogs': blogs})

def logout_view(request):
    logout(request)
    return redirect('index')

def about(request):
    return render(request, 'blog/about.html')
