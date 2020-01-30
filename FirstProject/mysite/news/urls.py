from django.urls import path
from . import views




urlpatterns = [
    #path('index', views.index.as_view(), name='index'),
    path('home', views.Home.as_view(), name='home'),
    path('news-submit-action', views.news_submit_action, name='news-submit-action'),
    path('aboutme', views.about_me.as_view(), name='aboutme'),
    path('artical-list', views.artical_list.as_view(), name='artical-list'),
    path('employee_insert', views.employee_form, name='employee_insert'),
    path('employee_list', views.employee_list, name='employee_list'),
    path('employee_update/<int:id>/', views.employee_form,name='employee_update'),
    path('employee_delete/<int:id>/',views.employee_delete,name='employee_delete'),



]