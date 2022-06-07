from unicodedata import name
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.create, name='create'),
    path('today/', views.today_view, name="today"),
    path('viewall/', views.viewall , name='view_all'),
    path('completed/', views.completed, name="completed"),
    path('delete/<int:pk>', views.tdel, name="delete"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('viewone/<int:pk>', views.viewone, name="viewone")
]
