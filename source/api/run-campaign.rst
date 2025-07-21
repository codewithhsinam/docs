Run Campaign Endpoint
==============

+---------------------------------------------------------------------------------+-------------------+---------------+
| URL                                                                             | Required Values   | HTTP Methods  |
+=================================================================================+===================+===============+
| https://api.tingting.io/api/v1/run-campaign/<campaign_id>/            | Campaign ID       |     POST      |
+---------------------------------------------------------------------------------+-------------------+---------------+

Note that the <campaign_id> in the URL should be replaced with the ID of the campaign you want to begin.

Sample Output:

.. code-block:: json

    {
        "message": "Campaign Scheduled successfully for 2082-03-25 at 14:46:00"
    }

If the schedule time is not given, then the campaign is launched immediately after the endpoint is hit. And the
sample output is given below.

.. code-block:: json

    {
        "message": "Campaign Began Successfully!!"
    }