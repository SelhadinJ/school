from django.urls import path
from . import views

app_name = 'school_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list/', views.SchoolListView.as_view(), name='list'),
    path('list/<pk>/', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<pk>/', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<pk>/', views.SchoolDeleteView.as_view(), name='delete'),
    path('stu_update/<pk>/', views.StudentUpdateView.as_view(), name='stu_update'),
    path('stu_delete/<pk>/', views.StudentDeleteView.as_view(), name='stu_delete'),
]
