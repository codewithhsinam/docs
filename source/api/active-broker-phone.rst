Active Broker Phone Number Endpoint
==============

+-------------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                           | Required Values   | HTTP Methods    |
+===============================================================================+===================+=================+
| https://api.tingting.io/api/v1/active-broker-phone/                 |                   | GET             |
+-------------------------------------------------------------------------------+-------------------+-----------------+

This endpoint lists all the Broker phone number of the requested user.

Sample Output:

.. code-block:: json

    [
        {
            "id": 1,
            "phone_number": "+97715970425"
        }
    ]