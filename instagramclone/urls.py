from django.urls import path
from instagramclone import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('hi/', views.hi)
]
