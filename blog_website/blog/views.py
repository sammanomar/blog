from django.shortcuts import render

from .models import (
    Blog,
    Tag
)
# Create your views here.


def home(request):
    blogs = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    context = {
        "blogs": blogs,
        "tags": tags
    }
    return render(request, 'home.html', context)


def blogs(request):
    return render(request, 'blogs.html')
