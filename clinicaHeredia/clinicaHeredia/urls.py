from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clinicaHeredia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/(?P<nombre_per>[\w\-]+)/', 'personas.views.persona_view', name='persona_view'),

)

urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


