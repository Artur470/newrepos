from django.shortcuts import render, redirect,  HttpResponse
from .models import Blog, Area
from .forms import CreateBlogForm, UpdateBlog
# Create your views h
def vun3(request):
    return render(request, "vun3.html")


def blogList(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render (request, 'blogs.html', context)


def createBlog(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        Blog.objects.create(

            title=title,
            body=body

        )
        return redirect('http://127.0.0.1:8000/home3/blog/')

    form = CreateBlogForm()
    context = {

        "form": form
    }
    return render(request, "blog_form.html", context)

def update_blog_view(request, id):

   blog = Blog.objects.get(pk=id)

   if request.method =="POST":
        blog = UpdateBlog(request.POST, instance=blog)
        if blog.is_valid():
            blog.save()
            return redirect("http://127.0.0.1:8000/home3/blog/")
        return HttpResponse('error')
   UpdateBlogForm = UpdateBlog(instance=blog)
   context = {

       'UpdateBlogForm': UpdateBlogForm

   }
   return render(request, "update_blog.html", context)


def deleteBlogview(request,  id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect("http://127.0.0.1:8000/home3/blog/")



def area_show(request):
    areas = Area.objects.all()
    context = {
        'areas': areas


    }
    return render(request, "area.html", context)