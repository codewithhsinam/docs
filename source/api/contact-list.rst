Contact List Endpoint
==============

+----------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                        | Required Values   | HTTP Methods    |
+============================================================================+===================+=================+
| https://api.tingting.io/api/v1/campaign-detail/<campaign_id>/    | Campaign ID       | GET             |
+----------------------------------------------------------------------------+-------------------+-----------------+

Note that the <campaign_id> in the URL should be replaced with the ID of the campaign you want to retrieve the contact of. 

Sample Output:

.. code-block:: json

    {
        "count": 3,
        "total_pages": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 125,
                "number": "9841349152",
                "status": "not started",
                "updated_at": "2025-07-08T16:52:53.054691+05:45",
                "call_duration": "0s",
                "playback": "",
                "credit_consumed": 0,
                "credit_consumed_SMS": 0,
                "carrier": "NTC"
            },
            {
                "id": 124,
                "number": "9865993245",
                "status": "not started",
                "updated_at": "2025-07-08T16:52:53.054691+05:45",
                "call_duration": "0s",
                "playback": "",
                "credit_consumed": 0,
                "credit_consumed_SMS": 0,
                "carrier": "NTC"
            },
            {
                "id": 123,
                "number": "9861566372",
                "status": "not started",
                "updated_at": "2025-07-08T16:52:53.054691+05:45",
                "call_duration": "10s",
                "playback": "91",
                "credit_consumed": 0,
                "credit_consumed_SMS": 0,
                "carrier": "NTC"
            }
        ],
        "total_credits_consumed": 0,
        "carrier_summary": {
            "NTC": 3
        }
    }