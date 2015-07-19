# -*- coding: utf-8 -*-
"""Utility pytest fixtures for testing"""

from nass.api import NassApi
import os
import pytest
import requests


@pytest.fixture
def api():
    """Construct a :class:`nass.api.NassApi` object

    Uses the environment variable NASS_API_KEY as the API key

    """

    key = os.environ.get('NASS_API_KEY')
    if not key:
        raise RuntimeError('No NASS_API_KEY environment variable set')
    return NassApi(key)


def resp_func(status):
    """Return a function that constructs a response with the given status code

    :param status: Status code

    """

    def func():
        resp = requests.Response()
        resp.status_code = status
        return resp
    return func

resp_ok = pytest.fixture(resp_func(200))
resp_bad = pytest.fixture(resp_func(400))
