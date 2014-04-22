# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from django.conf.urls import patterns, include, url
import views as views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.root_page),
    url(r'^html/hello', views.html_hello_page),
    url(r'^txt/hello', views.txt_hello_page),
    url(r'^redirect/simple', views.simple_redirect_page),
    url(r'^factorial/(\d+)$', views.factorial_page),
    url(r'^power/(\d+)/(\d+)$', views.power_page),
    url(r'^form$', views.form),
    url(r'^form/$', views.form),
    url(r'^contact$', views.contact),
    # Examples:
    # url(r'^$', 'django_project_1.views.home', name='home'),
    # url(r'^django_project_1/', include('django_project_1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
