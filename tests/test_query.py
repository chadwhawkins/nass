# -*- coding: utf-8 -*-
"""Tests for Query object"""

from nass.query import Query
import pytest


@pytest.fixture
def query():
    return Query(None)


def test_value(query):
    query.filter('year', 2012)
    query.filter('state_alpha', 'VA')
    assert query.params == {
        'year': 2012,
        'state_alpha': 'VA',
    }


def test_chained_filters(query):
    query.filter('year', 2012).filter('state_alpha', 'VA')
    assert query.params == {
        'year': 2012,
        'state_alpha': 'VA',
    }


def test_multiple_ops(query):
    query.filter('year', 2012, 'ge').filter('year', 2014, 'le')
    query.filter('state_alpha', 'VA')
    assert query.params == {
        'year__GE': 2012,
        'year__LE': 2014,
        'state_alpha': 'VA',
    }


def test_invalid_op_raises(query):
    with pytest.raises(TypeError) as exc:
        query.filter('year', 2014, 'abc')
    assert 'Invalid operator' in str(exc.value)
