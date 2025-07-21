Refresh Access Token Endpoint
=============================

+--------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                | Required Values   | HTTP Methods    |
+====================================================================+===================+=================+
| https://api.tingting.io/api/v1/auths/login/refresh/      |                   | POST            |
+--------------------------------------------------------------------+-------------------+-----------------+

Refreshes the access token using the refresh token stored in the HTTP cookie. This endpoint is used to 
keep the user logged in by issuing a new access token when the old one expires.

**Authentication:**

- Requires a **valid refresh token** stored in cookies.
- No need to include Authorization header or body content.

**Request:**

- No request body required.
- Include the `refresh` cookie in the request header:

.. code-block:: http

    Cookie: refresh=<your-refresh-token>

Sample Output:

.. code-block:: json

    {
        "message": "Session Refreshed Successfully"
    }

On success, a new `access` token will be set as an HttpOnly cookie in the response.

**Error Responses:**

**400 Bad Request**

- When no refresh token is found in cookies:

.. code-block:: json

    {
        "message": "No refresh token provided"
    }

- When the token payload is invalid or missing user_id:

.. code-block:: json

    {
        "detail": "Invalid token payload."
    }

**401 Unauthorized**

- When the user is inactive or does not exist:

.. code-block:: json

    {
        "detail": "Account is not activated."
    }

- When the token is expired or fails to refresh:

.. code-block:: json

    {
        "message": "Failed To Refresh The Session"
    }

**Notes:**

- This endpoint is typically called when the access token has expired.
- The client must rely on cookies (not JSON body) for the token exchange.
- The refreshed access token is returned via a secure HttpOnly cookie, not in the JSON response.
