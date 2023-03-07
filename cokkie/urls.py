from django.urls import path
from . import views

urlpatterns = [
    path('set', views.set, name='set'),
    path('get', views.get, name='get'),
    path('delete', views.delete, name='delete'),
    path('session_set', views.session_set, name='session_set'),
    path('session_get', views.session_get, name='session_get'),
    path('session_delete', views.session_delete, name='session_delete')
]