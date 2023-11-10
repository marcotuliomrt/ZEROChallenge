from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solved/', views.solved, name='solved'),
    path('unsolved/', views.unsolved, name='unsolved'),
    path('all/',views.all, name='all' )
]

# path('update_state/', views.update_state, name='update_state'),
