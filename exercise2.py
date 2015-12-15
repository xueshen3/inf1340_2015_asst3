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


def decide_helper(res_list, tem_list):
    """
    Decides whether a traveller's entry into Kanadia

    :param res_list: The result list pass for storing the final decision of each traveller
    :param tem_list: The decision(s) for each traveller base on the rules
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    for j in tem_list:
        # if first element is "Quarantine" then return and store "Quarantine"
        if j is "Quarantine":
            return res_list.append("Quarantine")
        # if first element is "Rejected" then return and store "Rejected"
        elif j is "Rejected":
            return res_list.append("Rejected")
        # if first element is "Accepted" then return and store "Accepted"
        else:
            return res_list.append("Accepted")


def valid_visa_format(visa_code):
    """
    Checks whether a visa code is two groups of five alphanumeric characters
    :param visa_code: alphanumeric string
    :return: Boolean; True if the format is valid, False otherwise

    """
    # counter for valid substring
    substring_counter = 0
    # Check each substring separated by "-"
    for substring in visa_code.split('-'):
        substring.strip()
        # if substring is alphanumereic and have five characters increase the substring_counter
        if substring.isalnum() and len(substring) == 5:
            substring_counter += 1
    if substring_counter == 2:
        return True
    else:
        return False


def valid_passport_format(passport_number):
    """
    Checks whether a passport number is five sets of five alpha-number characters separated by dashes
    :param passport_number: alpha-numeric string
    :return: Boolean; True if the format is valid, False otherwise
    """
    rex = re.match(r'^[a-zA-Z0-9]+(-[a-zA-Z0-9]+)+(-[a-zA-Z0-9]+)+(-[a-zA-Z0-9]+)+(-[a-zA-Z0-9]+)$',passport_number)
    # valid length must be 29
    if len(passport_number) == 29:
        # if rex is not None, means there find a match
        if rex is not None:
            return True
    # it is None then return False
        else:
            return False
    else:
        return False


def valid_date_format(date_string):
    """
    Checks whether a date has the format YYYY-mm-dd in numbers
    :param date_string: date to be checked
    :return: Boolean True if the format is valid, False otherwise
    """
    substring_counter = 0
    for substring in date_string.split('-'):
        substring.strip()
        if substring.isdigit():
            if substring_counter == 0 and len(substring) == 4:
                substring_counter += 1
            elif substring_counter > 0 and len(substring) == 2:
                substring_counter += 1
            else:
                break
    if substring_counter == 3:
        return True
    else:
        return False

#####################
# MAIN FUNCTION ##
#####################


def decide(input_file, countries_file):
    """
    Decides whether a traveller's entry into Kanadia should be accepted

    :param input_file: The name of a JSON formatted file that contains
        cases to decide
    :param countries_file: The name of a JSON formatted file that contains
        country data, such as whether an entry or transit visa is required,
        and whether there is currently a medical advisory
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    with open(input_file) as data_file:
        cases = json.load(data_file)
    with open(countries_file) as data_file:
        countries = json.load(data_file)
    decisions = ['Reject', 'Accept', 'Quarantine']
    result = []
    for case in cases:
        print case

    return result


