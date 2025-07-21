Update Campaign Endpoint
==============

+--------------------------------------------------------------------+-------------------+------------------------------------------------+-----------------+
| URL                                                                | Required Values   | Other Values                                   | HTTP Methods    |
+====================================================================+===================+================================================+=================+
| https://api.tingting.io/api/v1/campaign/<campaign_id>/   | Campaign Id       | name, services, message, sms_message, schedule | POST            |
+--------------------------------------------------------------------+-------------------+------------------------------------------------+-----------------+

To update a campaign, you’ll need to provide the campaign ID in the URL of the API endpoint. 
In addition to the campaign ID, you’ll also need to provide the new values that will replace the existing values 
in the campaign.

https://api.tingting.io/api/v1/campaign/79/

Sample Input:

.. code-block:: json

    {
        "name" : "example test campaign example",
        "services" : "SMS & PHONE",
        "message" : "Hello, how are you hello?",
        "sms_message" : "SMS check is going on!!",
        "schedule" : "2025-07-09"
    }

Note that the <campaign_id> in the URL should be replaced with the ID of the campaign you want to update.

Sample Output:

.. code-block:: json

    {
        "id": 79,
        "name": "example test campaign example",
        "services": "SMS & PHONE",
        "status": "Not Started",
        "sms_message": "SMS check is going on!!",
        "message": "Hello, how are you hello?",
        "description": "Test message",
        "schedule": "2025-07-09T00:00:00+05:45",
        "audio_file": null,
        "category": "example category",
        "user_phone": [
            3
        ],
        "campaign_action_count": 1,
        "progress_percent": 0,
        "updated_at": "2025-07-07T14:01:50.508344+05:45",
        "credit_limit": 100,
        "voice": 3,
        "draft": false,
        "failover_target": [],
        "length_factor": "1.00"
    }