.. _api:

API Reference
=============

.. module:: nass

NassApi class
-------------

.. autoclass:: nass.api.NassApi
   :inherited-members:

Query class
-----------

.. autoclass:: nass.query.Query
   :inherited-members:

Exceptions
----------

Since all custom exceptions subclass :class:`NassException
<nass.exceptions.NassException>`, you can use it to catch all exceptions raised
by this package.

.. autoexception:: nass.exceptions.NassException
.. autoexception:: nass.exceptions.NetworkException
.. autoexception:: nass.exceptions.InvalidJson
.. autoexception:: nass.exceptions.UnexpectedResponseData
.. autoexception:: nass.exceptions.ApiException
.. autoexception:: nass.exceptions.ExceptionList
.. autoexception:: nass.exceptions.ExceedsRowLimit
.. autoexception:: nass.exceptions.Unauthorized
.. autoexception:: nass.exceptions.InvalidQuery
.. autoexception:: nass.exceptions.BadMediaType
