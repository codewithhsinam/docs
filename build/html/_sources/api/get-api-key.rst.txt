Get API Key Endpoint
=============================

+--------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                | Required Values   | HTTP Methods    |
+====================================================================+===================+=================+
| https://api.tingting.io/api/v1/auths/get-api-keys/       |                   | GET             |
+--------------------------------------------------------------------+-------------------+-----------------+

This endpoint returns the access_key and secret_key associated with the currently authenticated user. These keys can be used as an alternative to JWT login for authenticating API requests.

Sample Output (when API key exists):

.. code-block:: json

    {
        "access_key": "39106a38ac483eb4625308fe98411588",
        "secret_key": "4d97e63d3b59ff6a924acfbe21781187cb4f35ea7be478c033146eb4b4102464"
    }

Sample Output (when API key is not found):

.. code-block:: json

    {
        "message": "No API credentials found for this user."
    }

**How to Use API Keys**

Once you retrieve the API keys, you can authenticate without logging in again by passing them in the request headers for other endpoints.

Required Headers:

.. code-block:: http

    X-ACCESS-KEY: 39106a38ac483eb4625308fe98411588
    X-SECRET-KEY: 4d97e63d3b59ff6a924acfbe21781187cb4f35ea7be478c033146eb4b4102464

**Notes**

This endpoint is read-only and does not generate new keys.

Keys retrieved from this endpoint can be used to authorize requests to other API services.

Ensure you store the keys securely in your client environment.