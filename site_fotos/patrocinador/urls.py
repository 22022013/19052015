#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('site_fotos.patrocinador.views',
  	url(r'^$', 'patrocinador', name='patrocinador'),
  
)