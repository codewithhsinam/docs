Delete Action Endpoint
==============

+-------------------------------------------------------------------------------+-------------------+-----------------+
| URL                                                                           | Required Values   | HTTP Methods    |
+===============================================================================+===================+=================+
| https://api.tingting.io/api/v1/phone-number/delete/<contact_id>/    | Contact ID        | DEL             |
+-------------------------------------------------------------------------------+-------------------+-----------------+

Note that the <number_id> in the URL should be replaced with the ID of the number you want to delete from the campaign.

Sample Output:

.. code-block:: json

    {
        "message": "Successfully Deleted."
    }