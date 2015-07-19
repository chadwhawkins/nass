# -*- coding: utf-8 -*-
"""Tests for exceptions"""

from nass import exceptions
from nass.api import NassApi
from util import api, resp_ok, resp_bad
import pytest


def test_404(api):
    with pytest.raises(exceptions.ApiException):
        api._api_request('/asdf', {}, '')


def test_network_error(api):
    with pytest.raises(exceptions.NetworkException):
        api.BASE_URL = 'http://somefakedomainname'
        api.param_values('source_desc')


def test_bad_media_type(api):
    with pytest.raises(exceptions.BadMediaType):
        query = api.query()
        query.filter('commodity_desc', 'CORN')
        query.filter('year', 2012, 'ge')
        query.filter('county_code', 187)
        query.params.update({'format': 'fax'})
        query.execute()


def test_invalid_json(api):
    with pytest.raises(exceptions.InvalidJson):
        query = api.query()
        query.filter('commodity_desc', 'CORN')
        query.filter('year', 2012, 'ge')
        query.filter('county_code', 187)
        query.params.update({'format': 'csv'})
        query.execute()


def test_unauthorized():
    with pytest.raises(exceptions.Unauthorized):
        api = NassApi('')
        api.param_values('source_desc')


def test_invalid_query(api):
    with pytest.raises(exceptions.InvalidQuery):
        api.query().filter('source_desc', '').execute()


def test_exceeds_row_limit(api):
    with pytest.raises(exceptions.ExceedsRowLimit):
        api.query().execute()


def test_exceeds_row_limit_weird_format_1(api, resp_bad):
    with pytest.raises(exceptions.ExceedsRowLimit):
        api._handle_response_data({'error': ['exceeds limit']}, resp_bad, '')


def test_exceeds_row_limit_weird_format_2(api, resp_bad):
    with pytest.raises(exceptions.ExceedsRowLimit):
        api._handle_response_data({'error': ['exceeds limit=a']}, resp_bad, '')


def test_response_not_dict(api, resp_ok):
    with pytest.raises(exceptions.UnexpectedResponseData):
        api._handle_response_data(123, resp_ok, 'field')


def test_bad_response(api, resp_bad):
    with pytest.raises(exceptions.NassException):
        api._handle_response_data({}, resp_bad, 'field')


def test_unexpected_response(api, resp_ok):
    with pytest.raises(exceptions.UnexpectedResponseData):
        api._handle_response_data({}, resp_ok, 'field')


def test_generic_error(api, resp_bad):
    with pytest.raises(exceptions.ApiException) as exc:
        api._handle_response_data({'error': ['blah']}, resp_bad, '')
    assert 'Server returned error message ' in str(exc)


def test_exception_list(api, resp_bad):
    with pytest.raises(exceptions.ExceptionList) as exc:
        api._handle_response_data({'error': ['a', 'b']}, resp_bad, '')
    assert 'Server returned error messages ' in str(exc)


def test_network_400(api, resp_bad):
    """Should get a NassException without explicit error message"""
    with pytest.raises(exceptions.NassException):
        api._handle_response_data({}, resp_bad, '')
