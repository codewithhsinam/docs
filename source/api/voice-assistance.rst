Voice Assistance Endpoint
==============

+-------------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                           | Required Values   | HTTP Methods    |
+===============================================================================+===================+=================+
| https://api.tingting.io/api/v1/voice-models/                        |                   |      GET        |
+-------------------------------------------------------------------------------+-------------------+-----------------+

This endpoint is used to list the voice assistance available to use in the campaign.

Sample Output:

.. code-block:: json

    [
        {
            "id": 1,
            "voice_display_name": "Rija",
            "voice_internal_name": "np_rija",
            "is_premium": false
        },
        {
            "id": 2,
            "voice_display_name": "Rija premium",
            "voice_internal_name": "np_rija",
            "is_premium": true
        },
        {
            "id": 3,
            "voice_display_name": "Prashanna",
            "voice_internal_name": "np_prashanna",
            "is_premium": false
        },
        {
            "id": 4,
            "voice_display_name": "Binod",
            "voice_internal_name": "np_binod",
            "is_premium": false
        },
        {
            "id": 5,
            "voice_display_name": "Shreegya",
            "voice_internal_name": "np_shreegya",
            "is_premium": false
        }
    ]
