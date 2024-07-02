
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('community/', views.community, name='community'),
    path('mypage/', views.mypage, name='mypage'),
    path('search_results/', views.search_results, name='search_results'),
    path('record_detail/<int:record_id>/', views.record_detail, name='record_detail'),
    path('admin/', admin.site.urls),
]