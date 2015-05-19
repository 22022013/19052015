
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('site_fotos.core.urls', namespace='core')),
    url(r'', include('site_fotos.album.urls', namespace='album')),
    url(r'', include('site_fotos.evento.urls', namespace='evento')),
    url(r'', include('site_fotos.patrocinador.urls', namespace='patrocinador')),
]
