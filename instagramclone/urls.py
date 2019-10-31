from django.urls import path
from instagramclone import views

urlpatterns = [
    path('hello-world/', views.hello_world),
    path('sorted/', views.sorted_integers),
    path('hi/<str:name>/<int:age>/', views.say_hi)
]