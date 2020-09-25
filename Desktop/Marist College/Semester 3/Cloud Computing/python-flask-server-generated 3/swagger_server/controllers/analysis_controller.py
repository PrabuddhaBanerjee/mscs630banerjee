# Kept the Server run code on terminal for self convinience:
# python3 -m swagger_server
# Copyright (c) Prabuddha Banerjee
# Class: MSCS 621
# Assignment - 3

import connexion
import six
import json
import re

from swagger_server.models.result import Result  # noqa: E501
from swagger_server import util

"""This method is used to return the specified JSON concordance based on an
    arbitrary English input text.
    param: 'body' is used to pass input for JSON message
    """

def get_concordance(body=None):  # noqa: E501
    """Calculate

    Post text to generate concordance # noqa: E501

    :param body: Text to be analyzed
    :type body: dict | bytes

    :rtype: Result
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        location = []

        # Convert String to bytes
        byte_body = body.decode('utf-8')

        # Remove all special charachters excluding space
        req_body = re.sub('[^A-Za-z ]+', "", byte_body)

        # Convert String to lowercase
        req_body = req_body.strip().lower().split(" ")

        dup_req_body= req_body.copy()

        # Sort the list alphabetically
        req_body.sort()

        # Fetch a list of no duplicate words
        res = []
        [res.append(x) for x in req_body if x not in res]

        # Get the length of list
        length = len(res)

        # Loop for getting word locations and forming new list
        for i in range (length):
            count = 0
            index = []
            for j in range (0 , len(dup_req_body), 1):
                if(res[i] == (dup_req_body[j])):
                    count+=1
                    index.append(j)
            result = {"token": res[i], "location": index}
            location.append(result)

        response, code = {
            "location": location,
            "input": byte_body
        }, 200

    except Exception as error:
        response, code = {
            "error": repr(error),
        }, 400

    return response, code
