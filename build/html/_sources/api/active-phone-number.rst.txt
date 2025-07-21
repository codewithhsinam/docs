Active Phone Number Endpoint
==============

+-------------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                           | Required Values   | HTTP Methods    |
+===============================================================================+===================+=================+
| https://api.tingting.io/api/v1/phone-number/active/                 |                   | GET             |
+-------------------------------------------------------------------------------+-------------------+-----------------+

This endpoint lists all active phone numbers for the authenticated user

Sample Output:

.. code-block:: json

    [
        {
            "id": 1,
            "phone_number": "+97715970425"
        }
    ]