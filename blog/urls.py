from django.urls import path
from .views import*

urlpatterns = [
    path('bloglist/',Bloglist.as_view()),
    path('bloglist/<int:id>/',GetBlog.as_view()),
    path('bloglist/<int:id>/like/',LikesApi.as_view()),
]