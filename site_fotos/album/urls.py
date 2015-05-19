#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('site_fotos.album.views',
  	url(r'^$', 'albuns', name='albuns'),
  
)