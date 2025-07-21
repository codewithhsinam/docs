Get Campaign Endpoint
==============

+------------------------------------------------------------+-------------------+---------------+
| URL                                                        | Required Values   | HTTP Methods  |
+============================================================+===================+===============+
| https://api.tingting.io/api/v1/campaign/         |                   |     GET       |
+------------------------------------------------------------+-------------------+---------------+

Information of all of your campaigns are retrieved at this endpoint. The information includes the campaign id, 
name, user phones, services, description, mesage,  status, category, voice, audio_file, bulk_file, etc. The id is to be used in the future to update, delete 
or begin the campaign.

Here is an example of the result: The campaign ID is used to edit, delete, run and perform other 
campaign activities.

.. code-block:: json

    {
    "count": 2,
    "total_pages": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 858,
            "name": "rockabye",
            "services": "PHONE",
            "status": "Completed",
            "sms_message": "",
            "message": "हेलो हेलो हेलो हेलो हेलो शिशिर् नसुत नसुत उठ उठ उठ, नसुत नसुत नसुत  महाराजअ महाराजअ महाराजअ महाराजअ",
            "description": "",
            "schedule": null,
            "audio_file": null,
            "bulk_file": null,
            "category": "Text",
            "user_phone": [
                12
            ],
            "campaign_action_count": 4,
            "progress_percent": 100,
            "updated_at": "2025-07-07T11:38:24.219065+05:45",
            "credit_limit": null,
            "voice": {
                "id": 5,
                "voice_display_name": "Shreegya",
                "voice_internal_name": "np_shreegya",
                "is_premium": false
            },
            "draft": false,
            "failover_target": [],
            "length_factor": "1.00"
        },
        {
            "id": 1208,
            "name": "test",
            "services": "PHONE",
            "status": "Terminated",
            "sms_message": "",
            "message": "हेल्लो हेल्लो हेल्लो हेल्लो हेल्लो हेल्लो हेल्लो स्तुति हेल्लो हील्लो हेल्लो हेल्लो हेल्लो हील्लूऊ",
            "description": "",
            "schedule": null,
            "audio_file": null,
            "bulk_file": null,
            "category": "Text",
            "user_phone": [
                12
            ],
            "campaign_action_count": 1,
            "progress_percent": 100,
            "updated_at": "2025-07-04T12:07:44.384374+05:45",
            "credit_limit": null,
            "voice": {
                "id": 3,
                "voice_display_name": "Prashanna",
                "voice_internal_name": "np_prasanna",
                "is_premium": false
            },
            "draft": false,
            "failover_target": [],
            "length_factor": "1.00"
        }
        ]
    }