#from django.conf.urls import url
from . import views
from django.urls import path
app_name = 'Music'


urlpatterns = [

    #/music/
    path('', views.index, name='index'),

    #/music/<album_id>/
    path('<int:album_id>/', views.detail, name='detail'),

    #/music/<album_id>/favorite/
    path('<int:album_id>/favorite/', views.favorite, name='favorite'),
]