from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('removepunc', views.removepunc, name='removepunc'),
    path('firstcapitilize', views.firstcap, name='firstcap'),
    path('newlineRemove', views.newlineRemove, name='newlineRemove'),
    path('spaceRemover', views.spaceRemover, name='spaceRemover'),
    path('charcount', views.charcount, name='charcount'),
]
