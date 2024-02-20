
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('portfilo.html',views.portfolio_details,name='portfolio-details'),
    path('index.html',views.index,name='index'),
    #path('blog-single.html',views.blog,name='blog')
]
