#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = "Bertha Chan & Philips Xue"
__copyright__ = "2015 INF 1340 Assignment 3"


# imports one per line
import pytest
import os
from exercise2 import *

DIR = os.getcwd()
DIR += "/test_jsons"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide('test_returning_citizen.json', 'countries.json') ==\
        ['Accept', 'Accept', 'Quarantine']


def test_medical_advisory():

    # Check if traveller is coming from or travelling via a country with a medical advisory
    assert decide('test_medical_advisory.json', 'countries.json') ==\
       ['Quarantine', 'Accept', 'Quarantine']


def test_lowercase():

    # Country code and passport in lowercase should not be rejected
    assert decide('test_returning_citizen_2.json', 'countries.json') ==\
        ['Accept', 'Accept', 'Quarantine']


def test_location_check():

    # If country does not exist, reject entry
    assert decide("test_location_check.json", "countries.json") ==\
        ["Reject", "Accept", "Reject"]


def test_valid_date_format():

    # Checks date, must be in format yyyy-mm-dd & in numbers
    assert valid_date_format('') == False
    assert valid_date_format('March 06,1999') == False
    assert valid_date_format('2011.02.02') == False
    assert valid_date_format('Mar.16, 2035') == False
    assert valid_date_format('11-11-11') == False
    assert valid_date_format('2016-January-16') == False
    assert valid_date_format('9768e-ab1de-8bc14-a3c4e-b12de') == False
    assert valid_date_format('Sep 2015/15') == False
    assert valid_date_format('2016 Sep 15') == False


def test_passport_format():
    # Valid passport format
    # Test passport consisted of all upper cases
    assert valid_passport_format('JMZ0S-89IA9-OTCLY-MQILJ-P7CTY') == True
    # Test passport consisted of all number
    assert valid_passport_format('12345-12345-67890-00000-00000') == True
    # Test passport consisted of all lower cases
    assert valid_passport_format('abced-76hfg-26bjh-angel-ffabc') == True
    # Test passport consisted of mixture of upper and lower cases
    assert valid_passport_format('Abced-HHhfg-BBbjh-Angel-FFabc') == True
    # Test passport consisted of mixture of number and upper cases
    assert valid_passport_format('Ab123-HHh78-BBb34-Ang77-FFa12') == True


    # Invalid passport format
    assert valid_passport_format("JMZ0S-89IA9-OTCLY-MQILJ-") == False
    # Test the incomplete passport
    assert valid_passport_format('') == False
    # Test the passport without dashes
    assert valid_passport_format('JMZ0S89IA9OTCLYMQILJfhdsf') == False
    # Test the passport with space in between instead of dashes
    assert valid_passport_format('JMZ0S 89IA9 OTCLY MQILJ 278dd') == False

def test_visa_format():
    # Valid visa format
    assert valid_visa_format("CfR6x-XSMVA") == True

    # Invalid visa format
    # Test the visa format with incomplete visa
    assert valid_visa_format("xsmvA") == False
    # Test the visa with the invalid character
    assert valid_visa_format("&*&%f-fid92") == False
    # Test the empty visa
    assert valid_visa_format("") == False
    # Test the visa that is over length
    assert valid_visa_format("93624768726") == False


def test_record_completeness():
    # If required fields are not in entry record, reject entry
    assert decide("test_record_completeness.json", "countries.json") ==\
        ["Reject", "Accept", "Reject"]


def test_visa_validation():
    # Visa must be less than 2 years old and in valid visa format
    assert decide("test_visa_validation.json", "countries.json") ==\
        ["Reject", "Accept", "Reject"]
