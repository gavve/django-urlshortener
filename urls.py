__author__ = 'jacob'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .import views

urlpatterns = patterns(
    '',
    # Front page
    url(r'^$', views.index, name="index"),

    # Url for form action, handling form
    url(r'^generate/$', views.generate_short_url, name="generate-short-url"),

    # Redirect to long_url
    url(r'^(?P<short_url>[a-z0-9]+)/$', views.redirect_to_long_url, name="redirect-to-long-url")
)
