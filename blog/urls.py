from django.urls import path
from .views import viewposts,singlepost,addPost,editPost


app_name = 'blog'
urlpatterns = [
    path('',viewposts,name='allPosts' ),
    path('<int:id>',singlepost,name='singlePost'),
    path('addPost',addPost,name='addPost'),
    path('<int:id>/editPost',editPost,name="editPost")
]