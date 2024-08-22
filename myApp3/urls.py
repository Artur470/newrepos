
from django.urls import path


from .views import *
urlpatterns = [

    path('in3/', vun3, name='vun3'),
    path('blog/', blogList, name='blog'),

]
