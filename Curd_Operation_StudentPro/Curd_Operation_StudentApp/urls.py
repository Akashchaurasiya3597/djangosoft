from django.urls import path
from Curd_Operation_StudentApp import views

urlpatterns = [
    path('', views.Homepage_view, name='Homepage'),
    path('student_create/',views.Student_create_view, name='student_create'),
    path('insert/',views.Insert_data,name='insert'),
    path('update/<pk>',views.update_view,name='update'),
    path('replace/<pk>',views.replace_view,name='replace'),
    path('delete/<pk>',views.delete_view,name='delete')
]
