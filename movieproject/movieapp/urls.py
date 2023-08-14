from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('update/<int:update_id>/',views.update,name='update'),
    path('delete/<int:delete_id>/',views.delete,name='delete'),
]