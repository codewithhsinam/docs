Send OTP Endpoint
==============

+---------------------------------------------------------------------+-----------------------------------+---------------+
| URL                                                                 | Required Values                   | HTTP Methods  |
+=====================================================================+===================================+===============+
| https://app.tingting.io/api/system/send/otp/                        | number, message, sms_send_options |     POST      |
+---------------------------------------------------------------------+-----------------------------------+---------------+

By utilizing this endpoint, you can send OTPs to users by specifying the recipient’s phone number as a string, along with the message containing the OTP 
and the desired delivery method - either through voice or text through the sms_send_option attribute. The OTP can be integrated in the message by passing 
it inside curly braces of the messages attribute.

For Example,

.. code-block:: json

    {
        "message" : "Hi Your OTP is {otp}"
    }


In addition, you have the flexibility to choose between sending your own OTP or generating it automatically through the OTP options attribute. The available options 
are personnel and generated. If you choose personnel, you’ll need to provide the OTP yourself. On the other hand, if you select generated, the OTP will be auto-generated. 
In the generated scenario, you can specify the length via the otp_length for the auto-generated OTP. If nothing is provided, by default a generated OTP will be provided.

Sample Input For Customized OTP

.. code-block:: json

    {
        "number": "9851023212",
        "message": "Hi your OTP is {otp}",
        "sms_send_options": "text",
        "otp_options": "personnel",
        "otp": "12345"
    }

Sample Input For Auto-Generated OTP

.. code-block:: json

    {
        "number": "9851023212",
        "message": "Hi your OTP is {otp}",
        "sms_send_options": "voice",
        "otp_options": "generated",
        "otp_length": "4"
    }

The details of the sent OTP is shown.

Sample Output:

.. code-block:: json

    {
        "status": 200,
            "success": true,
            "message": "OTP Sent Successfully.",
            "errors": [],
            "data": {
                "details" : {
                        "number": "9843818700",
                        "otp_options": "personnel",
                        "message": "Hi your OTP is 1 2 3 4 5",
                        "otp": "12345",
                        "sms_send_options": "text"
                }
                }
    }