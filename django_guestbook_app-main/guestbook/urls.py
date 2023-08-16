from django.urls import path, include

from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('pre-order/', views.pre_order_view, name='pre_order'),
    path('silver-bot/', views.silver_bot_view, name='silver_bot'),
    path('recommend/', views.recommend_view, name='recommend'),
]

from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign/', views.sign, name='sign')
]




"""
urlpatterns = [
    path('',views.index,name='index'),
    path('sign/',views.sign,name='sign')
]
"""