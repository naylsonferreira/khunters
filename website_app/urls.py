from django.urls import path
from website_app import views

app_name = "website_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('jogadores/', views.Jogadores, name='Jogadores'),

    path(
        'jogadores/add/',
        views.JogadorCreate.as_view(),
        name='Add_Jogador'),

    path(
        'jogadores/up/<int:pk>/',
        views.JogadorUpdateView.as_view(),
        name='Update_Jogador'),

    path(
        'jogadores/del/<int:pk>/',
        views.JogadorDeleteView.as_view(),
        name='Delete_Jogador'),

    path(
        'objeto_ers/',
        views.Objeto_ers,
        name='Objeto_ers'),

    path(
        'objeto_ers/add/',
        views.Objeto_erCreate.as_view(),
        name='Add_Objeto_er'),

    path(
        'objeto_ers/up/<int:pk>/',
        views.Objeto_erUpdateView.as_view(),
        name='Update_Objeto_er'),

    path(
        'objeto_ers/del/<int:pk>/',
        views.Objeto_erDeleteView.as_view(),
        name='Delete_Objeto_er'),

    path(
        'objeto_er_maps/',
        views.Objeto_er_maps,
        name='Objeto_er_maps'),

    path(
        'objeto_er_maps/add/',
        views.Objeto_er_mapCreate.as_view(),
        name='Add_Objeto_er_map'),

    path(
        'objeto_er_maps/up/<int:pk>/',
        views.Objeto_er_mapUpdateView.as_view(),
        name='Update_Objeto_er_map'),

    path(
        'objeto_er_maps/del/<int:pk>/',
        views.Objeto_er_mapDeleteView.as_view(),
        name='Delete_Objeto_er_map'),
]
