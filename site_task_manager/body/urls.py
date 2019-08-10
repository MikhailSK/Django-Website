from django.urls import path

from . import views

app_name = 'body'

urlpatterns = [
    path('', views.main_page),
    path('home/', views.home, name='home'),
    path('sing_in/', views.sing_in),
    path('sing_up/', views.sing_up),
    path('tasks/', views.tasks),
    path('settings/', views.settings),
    path('qestions/<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
