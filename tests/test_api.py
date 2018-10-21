# -*- coding: utf-8 -*-
"""API integration tests"""

from nass.api import NassApi
import os
import requests
import requests_cache
from util import api


def test_key():
    api = NassApi('api key')
    assert api.key == 'api key'


def test_cache_setup():
    api = NassApi('api key')
    assert api.use_cache is False
    assert isinstance(api.http, requests.Session)

    api = NassApi('api key', use_cache=True, cache_name='nass_test', cache_expiration_minutes=10)
    assert api.use_cache
    assert isinstance(api.http, requests_cache.CachedSession)
    assert api.http._cache_name == 'nass_test'
    assert api.http._cache_expire_after.seconds / 60 == 10


def test_sources(api):
    data = api.param_values('source_desc')
    assert data


def test_api_count(api):
    query = api.query()
    query.filter('commodity_desc', 'CORN')
    query.filter('year', 2012, 'ge')
    query.filter('county_code', 187)
    count = query.count()
    assert count
    assert isinstance(count, int)


def test_api_query(api):
    query = api.query()
    query.filter('commodity_desc', 'CORN')
    query.filter('year', 2012, 'ge')
    query.filter('county_code', 187)
    data = query.execute()
    assert data


def test_api_query_cache():
    api = NassApi(os.environ.get('NASS_API_KEY'), use_cache=True)
    assert len(api.http.cache.keys_map) == 0

    api.param_values('source_desc')
    assert len(api.http.cache.keys_map) == 1
