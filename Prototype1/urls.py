from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:4
     url(r'^admin/', include(admin.site.urls)),

     url(r'^$', 'User.views.home', name='home'), 
     url(r'^about/', 'User.views.about', name='about'),
     url(r'^homepage/', 'User.views.homepage', name='about'),

     
    # url(r'^blog/', include('blog.urls')),

)