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
    Decides whether a traveller has entry into Kanadia
    :param res_list: The result list pass for storing the final decision of each traveller
    :param tem_list: The decision(s) for each traveller base on the rules
    :return: List of strings. Possible values of strings are:
        "Accept", "Reject", and "Quarantine"
    """
    for element in tem_list:
        # if first element is "Quarantine" then return and store "Quarantine"
        if element is "Quarantine":
            return res_list.append("Quarantine")
        # if first element is "Rejected" then return and store "Rejected"
        elif element is "Rejected":
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
    # Create an empty counter
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
    # valid length of passport number must be 29
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
### MAIN FUNCTION ###
#####################

# The valid passport must contain all of the following information
def valid_record(record):
    """
    Checks whether a passport number contains all necessary information
    :param record
    :return: Result if the passport is valid, Return False otherwise
    """
    if not record['first_name']:
        return False
    elif not record['last_name']:
        return False
    elif not record['home']:
        return False
    elif not record['entry_reason']:
        return False
    elif not record['birth_date']:
        return False
    elif not record['from']:
        return False
    elif not record['passport']:
        return False
    elif record.has_key('visa') is True:
        if valid_visa_format(record['visa']['code']) is False or valid_date_format(record['visa']['date']) is False:
            return False
    else:
    # Once the passport is confirmed valid, save it in result
        result = valid_passport_format(record['passport'])and valid_date_format(record['birth_date'])
        return result

def decide(input_file, countries_file):
    with open(input_file) as data_file:
       cases = json.load(data_file)
    with open(countries_file) as data_file:
       countries = json.load(data_file)
    decisions = ['Quarantine','Reject', 'Accept']
    result = []
    for case in cases:
        via_medical_advisory= ""
        #Check if record is completed if not REJECT
        if valid_record(case) is False:
            result.append(decisions[1])
            continue

        #Check which country coming back from
        departure_country = case['from']['country'].upper()
        #The country is not in the dictionary, REJECT traveller
        if countries.has_key(departure_country) is False:
            result.append(decisions[1])
            continue

        #via country is unknow REJECT
        if case.has_key('via') is True:
            via_country = case['via']['country'].upper()
            if countries.has_key(via_country) is True:
                #Check is there is medical advisory in via country
                via_medical_advisory = countries[via_country]['medical_advisory']
            else:
                #print 'Reject via'
                result.append(decisions[1])
                continue

        #fetch requirements of entry
        visitor_visa_required = countries[departure_country]['visitor_visa_required']
        transit_visa_required = countries[departure_country]['transit_visa_required']
        medical_advisory = countries[departure_country]['medical_advisory']

        #check if home country
        if case['home']['country'].upper() == "KAN" and case['entry_reason'].lower() == "returning":
            if medical_advisory or via_medical_advisory:
                result.append(decisions[0])
                continue
            else:
                result.append(decisions[2])
                continue

        #check is medical advisory is needed
        if medical_advisory or via_medical_advisory:
            #print "Quarantine"
            result.append(decisions[0])
            continue

        #Check if visa is required
        if visitor_visa_required == '1' or transit_visa_required == '1':
            #check visa formatting if wrong REJECT
            if case.has_key('visa') is True:
                    if is_more_than_x_years_ago(2,case['visa']['date']) is True:
                        #print 'visa outdated'
                        result.append(decisions[1])
                        continue

        #print "accept"
        result.append(decisions[2])

    return result
