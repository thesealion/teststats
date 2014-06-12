from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from teststats.stats.views import HitsView


urlpatterns = patterns('',
    url(r'^$', HitsView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
