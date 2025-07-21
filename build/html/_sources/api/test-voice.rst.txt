Test Voice Endpoint
==============

To test a voice, a sample message needs to be provided.

+---------------------------------------------------------------------------------+-----------------------------------+---------------+
| URL                                                                             | Required Values                   | HTTP Methods  |
+=================================================================================+===================================+===============+
| https://api.tingting.io/api/v1/test-speak/riri/<campaign_id>/         | Message, Voice input, Campaign ID |     POST      |
+---------------------------------------------------------------------------------+-----------------------------------+---------------+

To test a voice, a sample message needs to be provided. You can also specify the voice to test your message. 
The options are: np_rija, np_rija(premium), np_prashanna, np_shreegya and np_binod. If nothing is provided, np_rija is used.

Sample Input:

.. code-block:: json

    {
        "voice_input" : 5,
        "message" : "yo test voice ko laagi ho"
    }

Sample Output:

    "https://riritwo.prixacdn.net/output/eccc8258894076a9dc9e00cf4ebf472a.mp3"