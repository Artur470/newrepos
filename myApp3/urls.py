
from django.urls import path


from .views import *
urlpatterns = [

    path('in3/', vun3, name='vun3'),
    path('blog/', blogList, name='blog'),
    path('create/', createBlog),
    path('update/<int:id>/',update_blog_view),
    path('delete/<int:id>', deleteBlogview),
    path('area/', area_show)
]
