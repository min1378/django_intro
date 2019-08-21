from django.urls import path
from . import views



urlpatterns = [
    path('introduce/', views.introduce),
    path('dinner/<str:name>', views.dinner),
    path('image/', views.image),
    path('greeting/<str:name>', views.greeting),
    path('times/<int:num1>:<int:num2>', views.times),
    path('template_language/', views.template_language),
    path('info/', views.info),
    path('student/<str:name>:<int:age>', views.student),
    path('isbirthday/', views.isbirthday),
    path('lotto/', views.lotto),
    path('search/', views.search),
    path('result/', views.result),
    path('lotto_pick/', views.lotto_pick),
    path('lotto_result/', views.lotto_result),
    path('static_example/', views.static_example),
    path('push/', views.push),
    path('pull/', views.pull),
    path('index/', views.index),

]