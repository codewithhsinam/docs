Test Voice Endpoint
==============

To test a voice, a sample message needs to be provided.

+---------------------------------------------------------------------------------+-----------------------------------+---------------+
| URL                                                                             | Required Values                   | HTTP Methods  |
+=================================================================================+===================================+===============+
| https://newtingtingapi.prixa.live/api/v1/test-speak/riri/<campaign_id>/         | Message, Voice input, Campaign ID |     POST      |
+---------------------------------------------------------------------------------+-----------------------------------+---------------+

To test a voice, a sample message needs to be provided. You can also specify the voice to test your message. 
The options are: np_rija, np_prasanna, np_shreegya and np_binod. If nothing is provided, np_rija is used.