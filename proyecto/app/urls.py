from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name ='app'
urlpatterns = [
    path('', views.home),
    path('acerca/',views.acercaDe,name='acerca'),
    path('agregarPost/', views.agregarPost),
    path('pages/<id>',views.verPost),
    path('imagen/<id>',views.stream_file,name='imagen')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
