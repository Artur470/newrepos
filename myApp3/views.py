from django.shortcuts import render
from .models import Blog

# Create your views h
def vun3(request):
    return render(request, "vun3.html")


def blogList(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render (request, 'blogs.html', context)