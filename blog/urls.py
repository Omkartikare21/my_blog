from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='start_page'),
    path('post', views.AllPostsView.as_view(), name='posts_page'),
    # post/my-first-post... here the ny-first-post is a slug...it is generated dynamically
    #path('post/<slug:slug>', views.post_details, name='detail_posts')
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='detail_posts'),
    # slug (first one before colon) is is to identify the slug..and checks that it shouldn't contain special symbol
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]
