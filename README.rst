``nass``
========

.. image:: https://img.shields.io/travis/nickfrostatx/nass.svg
        :target: https://travis-ci.org/nickfrostatx/nass

.. image:: https://img.shields.io/pypi/v/nass.svg
    :target: https://pypi.python.org/pypi/nass

``nass`` is a wrapper around the public API for the USDA National Agricultural
Statistics Service.

Installation
------------

::

    $ pip install nass

Usage
-----

::

    >>> import nass
    >>> api = nass.NassApi('your api key')
    >>> api.param_values('source_desc')
    ['CENSUS', 'SURVEY']
    >>> q = api.query()
    >>> q.filter('commodity_desc', 'CORN').filter('year', 1990)
    >>> q.count()
    25259
    >>> q.execute()
    [{'sector_desc': 'CROPS', ...}, ...]

See http://quickstats.nass.usda.gov/ for the full list of fields.

Exceptions
----------

If something goes wrong communicating with NASS, an exception will be raised.
This includes connection problems (e.g. timeout, DNS failure), as well as
specific error messages.

All exceptions subclass :class:`nass.exceptions.NassException`, so you can use
it to catch all exceptions.

Documentation
-------------

You can find full documentation of the ``nass`` package at
https://nass.readthedocs.org.
