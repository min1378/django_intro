from django.urls import path
from . import views


# 이후의 url들이 여기로 온다!
urlpatterns = [
    path('index/', views.index),

]