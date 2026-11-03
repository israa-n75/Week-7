from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('home/', views.home, name='home'),

    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('courses/', views.courses, name='courses'),
    path('add-course/', views.add_course, name='add_course'),
    path('edit-course/<int:id>/', views.edit_course, name='edit_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
]