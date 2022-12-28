from django.urls import path
from Portfolio import views

urlpatterns=[
    path('', views.Home, name="home"),
    path('mywork', views.work, name="work"),
]
