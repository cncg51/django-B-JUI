# encoding:utf-8

#import os

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                    url(r'^$', 'bui_app.views.index', name='index'),
                    url(r'^index_tree$', 'bui_app.views.index_tree', name='index_tree'),
                    url(r'^index_layout.html$','bui_app.views.index_layout', name="index_layout"),
                      )
