User Detail Endpoint
==============

+-------------------------------------------------------------------+-------------------+----------------+
| URL                                                               | Required Values   | HTTP Methods   |
+===================================================================+===================+================+
| https://newtingtingapi.prixa.live/api/v1/auths/user-profile/      |                   | GET            |
+-------------------------------------------------------------------+-------------------+----------------+

You can get all your details via a GET request.

Sample Output:

.. code-block:: json

    {
        "id": 35,
        "user": {
            "first_name": "Ram",
            "last_name": "Thapa",
            "username": "ramthapa",
            "email": "ram.thapa639@gmail.com"
        },
        "profile_picture": "https://newtingtingapi.prixa.live/media/account/1/202510200010/profile_image.jpg",
        "contact_no": "9808365218",
        "address": "Lalitpur",
        "is_verified_contact": true
    }