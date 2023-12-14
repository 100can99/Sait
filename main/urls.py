from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('news', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('', views.news, name='news'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('bros', views.bros, name='bros'),
    path('chashka', views.chashka, name='chashka'),
    path('panda', views.panda, name='panda'),
    path('prazd', views.prazd, name='prazd'),
    path('cena', views.cena, name='cena')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
