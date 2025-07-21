Campaign Details Endpoint
==============

+------------------------------------------------------------------+-------------------+-----------------+
| URL                                                              | Required Values   | HTTP Methods    |
+==================================================================+===================+=================+
| https://api.tingting.io/api/v1/campaign/<campaign_id>/ | Campaign ID       | GET             |
+------------------------------------------------------------------+-------------------+-----------------+

Note that the <campaign_id> in the URL should be replaced with the ID of the campaign you want to delete.

Sample Output:

.. code-block:: json

    {
        "id": 79,
        "name": "example test campaign example",
        "services": "SMS & PHONE",
        "status": "Not Started",
        "sms_message": "SMS check is going on!!",
        "message": "Hello, how are hello?",
        "description": "Test message",
        "schedule": "2025-07-09T00:00:00+05:45",
        "audio_file": null,
        "bulk_file": null,
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