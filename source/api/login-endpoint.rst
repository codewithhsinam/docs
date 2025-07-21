Login Endpoint
==============


+------------------------------------------------------------+-------------------+---------------+
| URL                                                        | Required Values   | HTTP Methods  |
+============================================================+===================+===============+
| https://api.tingting.io/api/v1/auths/login/      | email, password   | POST          |
+------------------------------------------------------------+-------------------+---------------+

After successful authentication you will get an access token. This token needs to be provided for every further request.

Sample Input:

.. code-block:: json

    {
        "email": "test@gmail.com",
        "password": "test"
    }

The access token generated from the login endpoint must be provided to the bearer token. The 
refresh token, on the other hand needs to be used while refreshing the access token which will expire in 1 day.

Sample Output:

.. code-block:: json
    
    {
        "has_logged_in": true,
        "message": "Login Successful"
    }