from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'Frontend'

urlpatterns = [
    path('', views.listView, name = 'list_view'), ]