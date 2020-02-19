from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from profiles_api import views


router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'', include(router.urls))  
]
