#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. Kanadia

Computer-based immigration office for Kanadia

"""

__author__ = "Bertha Chan & Philips Xue"
__copyright__ = "2015 INF 1340 Assignment 3"

import re
import datetime
import json

######################
## global constants ##
######################
REQUIRED_FIELDS = ["passport", "first_name", "last_name",
                   "birth_date", "home", "entry_reason", "from"]

######################
## global variables ##
######################
'''
countries:
dictionary mapping country codes (lowercase strings) to dictionaries
containing the following keys:
"code","name","visitor_visa_required",
"transit_visa_required","medical_advisory"
'''
COUNTRIES = None


#####################
# HELPER FUNCTIONS ##
#####################
def is_more_than_x_years_ago(x, date_string):
    """
    Check if date is less than x years ago.

    :param x: int representing years
    :param date_string: a date string in format "YYYY-mm-dd"
    :return: True if date is less than x years ago; False otherwise.
    """

    now = datetime.datetime.now()
    x_years_ago = now.replace(year=now.year - x)
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d')

    return (date - x_years_ago).total_seconds() < 0


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param watchlist_file: The name of a JSON formatted file that
        contains names and passport numbers on a watchlist
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    # open the json file to read and store date then close right away
    with open(input_file) as json_file1:
        input_data = json.load(json_file1)
        json_file1.close()
    with open(countries_file) as json_file2:
        country_data = json.load(json_file2)
        json_file2.close()
    res_list = []
    for i in input_data:
        # create a temparary list to append temperary decision
        tem_list = []
        # check the traveller is coming from with a medical advisory
        if i['from']['country'] in country_data:
            if country_data[i['from']['country']]["medical_advisory"] is not '':
                tem_list.append("Quarantine")
        # check the traveller is through with a medical advisory
        if i['home']['country'] in country_data:
            if country_data[i['home']['country']]["medical_advisory"] is not '':
                tem_list.append("Quarantine")
        # check the information whether is complete
        if ('' in i.values()) and ('' == i['from']['country']) and ('' == i['home']['country']):
            tem_list.append("Rejected")
        if valid_date_format(i["birth_date"]) is False:
            tem_list.append("Rejected")
        if valid_passport_format(i["passport"]) is False:
            tem_list.append("Rejected")
        # check whether is from KAN
    return ["Reject"]


def valid_passport_format(passport_number):
    """
    Checks whether a pasport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    return False


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """

    return False