from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<drug>', views.form, name='drug')
]
