Add Campaign Endpoint
==============

+--------------------------------------------------------------------+--------------------------------------------------------------------------------+----------------+
| URL                                                                | Required Values                                                                | HTTP Methods   |
+====================================================================+================================================================================+================+
| https://api.tingting.io/api/v1/campaign/create/          | name, services, user_phone, message, sms_message, description, schedule, voice |     POST       |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------+----------------+

To add a campaign, you’ll need to access the campaign endpoint using the HTTP POST method. The required inputs for 
creating a campaign include the name of the campaign, the services offered by the campaign, phone number through
which the campaign will be executed, the message to be sent, the SMS message is needed for SMS service and 
PHONE & SMS service only, the description of the campaign, schedule of the campaign and voice assistance for the campaign.

Furthermore, you can also add available tags to your message using variables and passing it inside curly braces.

Sample Tags:

Message: “नमस्कार, {tags_name}, हजुर {tags_age} वर्षको हुनुहुन्छ र हजुरको सालारी {tags_salary} छ |”



Sample Input:

.. code-block:: json

    {
        "name" : "example test campaign",
        "services" : "PHONE",
        "credit_limit" : 100,
        "user_phone" : [3],                   # Here, 3 is the id of the phone number
        "message" : "Hello, how are you?",
        "sms_message" : "SMS check!!",
        "description" : "Test message",
        "schedule" : "2025-07-08",         
    }

Sample Output:

.. code-block:: json

    {
        "id": 79,
        "name": "example test campaign",
        "services": "PHONE",
        "status": "Not Started",
        "sms_message": "SMS check!!",
        "message": "Hello, how are you?",
        "description": "Test message",
        "schedule": "2025-07-08T00:00:00+05:45",
        "audio_file": null,
        "bulk_file": null,
        "category": "",
        "user_phone": [
            3
        ],
        "progress_percent": 0,
        "updated_at": "2025-07-07T13:13:16.286224+05:45",
        "credit_limit": 100,
        "voice": null,
        "draft": false,
        "failover_target": [],
        "length_factor": "1.00",
        "main_audit": "4770",
        "voice" : 3
    }



**Add Voice Assistance Endpoint**

+------------------------------------------------------------------------------------+-------------------------------------------------------------------+----------------+
| URL                                                                                | Required Values                                                   | HTTP Methods   |
+====================================================================================+===================================================================+================+
| https://api.tingting.io/api/v1/campaign/create/<campaign_id>/message/    | Campaign ID, voice, category, length_factor, message, sms_message |     PATCH      |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------+----------------+

Note that the <contact_id> in the URL should be replaced with the ID of the contact you want to add the details of.

Sample Input:

..  code-block:: json

    {
        "voice" : 3,
        "category" : "example category"
    }

As message, sms_message is already provided above so no need to provide here. length_factor default value is 1 and draft value is false.

Sample Output:

.. code-block:: json

    {
        "voice": 3,
        "sms_message": "SMS check!!",
        "message": "Hello, how are you?",
        "category": "example category",
        "draft": false,
        "length_factor": "1.00"
    }


**Add Individual Contact in Campaign Endpoint**

+---------------------------------------------------------------------------------+--------------------+----------------+
| URL                                                                             | Required Values    | HTTP Methods   |
+=================================================================================+====================+================+
| https://api.tingting.io/api/v1/campaign/<campaign_id>/add-contact/    | Campaign ID        |     POST       |
+---------------------------------------------------------------------------------+--------------------+----------------+

Sample Input To Add Individual Contact:

.. code-block:: json

    {
        "number" : 9823561098
    }

Sample Output for Individual Contact:

.. code-block:: json

    {
        "message": "New Contact added"
    }

**Add Bulk Contact in Campaign Endpoint**

+-----------------------------------------------------------------------------------+--------------------+----------------+
| URL                                                                               | Required Values    | HTTP Methods   |
+===================================================================================+====================+================+
| https://api.tingting.io/api/v1/campaign/create/<campaign_id>/detail/    | Campaign ID        |     POST       |
+-----------------------------------------------------------------------------------+--------------------+----------------+

Sample Input To Add Bulk Contact:

.. code-block:: json

    {
        "bulk_file" : "numbers.xlsx"
    }

Sample Output for Bulk Contact:

.. code-block:: json

    {
        "error_list": [],
        "samples": [
            {
                "column": "numbers",
                "sample": [
                    "9801356897",
                    "9812345698",
                    "9745610235"
                ]
            },
            {
                "column": "name",
                "sample": [
                    "अद्वैत",
                    "आशिष",
                    "शिखर"
                ]
            },
            {
                "column": "age",
                "sample": [
                    20,
                    21,
                    21
                ]
            },
            {
                "column": "salary",
                "sample": [
                    "एक लाख",
                    "दुइ लाख",
                    "तिन लाख"
                ]
            }
        ],
        "total_validated_rows": 3
    }