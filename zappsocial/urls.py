from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zappsocial.views.home', name='home'),
    # url(r'^zappsocial/', include('zappsocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quiz/$', 'quiz.views.index'),
    url(r'^quiz/generate/(?P<quiz_type>\w+)/(?P<id>\d+)$', 'quiz.views.generate'),
    #TODO:
    url(r'^quiz/(?P<quiz_id>\d+)/$', 'quiz.views.detail'),
    url(r'^quiz/(?P<quiz_id>\d+)/(?P<question_id>\d+)/$', 'quiz.views.question'),
    url(r'^quiz/(?P<quiz_id>\d+)/results/$', 'quiz.views.detail'),
)

urlpatterns += staticfiles_urlpatterns()