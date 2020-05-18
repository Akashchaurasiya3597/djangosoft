
from django.urls import path
from personalDiaryApp import views
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('diary/', views.Dairy_view, name='diary'),
    path('insert/', views.insert_view, name='insert'),
    path('update/<pk>', views.Update_view, name='update'),
    path('delete/<pk>', views.delete_view, name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
