#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('site_fotos.core.views',
  	url(r'^$', 'home_site', name='home_site'),
  
)