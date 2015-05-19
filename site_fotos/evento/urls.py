#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('site_fotos.evento.views',
  	url(r'^$', 'eventos', name='eventos'),
  
)