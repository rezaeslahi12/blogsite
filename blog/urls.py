# from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"),
    path("blog_post/<int:category_id>/", views.index, name="index"),
    path("detail_post/<int:post_id>/", views.detail, name="detail"),
    path("<int:post_id>/results/", views.results, name="results"),
    path("like/<post_id>", views.post_like, name="like"),
    path("unlike/<post_id>", views.post_unlike, name="unlike"),
]