
from django.contrib import admin
from django.urls import path,include
from blogapp import views
from rest_framework import routers
from blogapp.serializers import blogserializer

from blogapp.views import blogViewSet

router= routers.DefaultRouter()
router.register(r'list' , blogViewSet)




urlpatterns = [
path("blog/" , views.blogs ,name="blog"),
 path("router/", include(router.urls)), 
path("news/", views.news , name="news"),
path("signup/", views.signup , name="signup"),
path("login/" , views.userlogin, name="login"),
path("new_page/", views.blog_create, name="new_page"),
path("feature/", views.featured_blogs, name="featured"),
path("api_data/", views.postdata , name="post"),
path("<int:id>/" , views.update_data , name="update"),
path("delete/<int:id>/" ,views.blog_delete , name="delete")
]