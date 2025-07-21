Contact Information Endpoint
==============

+-------------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                           | Required Values   | HTTP Methods    |
+===============================================================================+===================+=================+
| https://api.tingting.io/api/v1/campaign/<contact_id>/attributes/    | Contact ID        | GET             |
+-------------------------------------------------------------------------------+-------------------+-----------------+

Note that the <contact_id> in the URL should be replaced with the ID of the contact you want to retrieve the information of.

The details of the contact will be retrieved with the following details:

Sample output:

.. code-block:: json

    {
        "age": 22,
        "name": "राहुल",
        "salary": "एक लाख "
    }