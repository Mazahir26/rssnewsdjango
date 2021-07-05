"""Rss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    #Main Url
    path('admin/', admin.site.urls),
    path('api/feed', views.FeedList.as_view()),
    path('api/userfeed',views.UserFeedList.as_view()),
    path('api/feed/<int:pk>/subscribe',views.FeedSubscribe.as_view()),
    path('api/feed/<int:pk>/unsubscribe',views.FeedUnSubscribe.as_view()),
    path('api/saved', views.SaveURL.as_view()),
    path('api/saved/<int:pk>', views.SavedRemove.as_view()),
    path('api/category/<str:category>', views.CategoryFeedList.as_view()),


    #Auth
    path('api/signup', views.signup),
    path('api/login', views.login),
]