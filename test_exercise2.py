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
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def test_medical_advisory():

    # Check if traveller is coming from or travelling via a country with a medical advisory
    assert decide("test_medical_advisory.json", "countries.json") ==\
       ["Quarantine", "Accept", "Quarantine"]


def test_lowercase():

    # Country code and passport in lowercase should not be rejected
    assert decide("test_returning_citizen_2.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


def test_location_check():

    # If country does not exist, reject entry
    assert decide("test_location_check.json", "countries.json") ==\
        ["Reject", "Accept", "Reject"]


def test_valid_date_format():

    # Checks date, must be in format yyyy-mm-dd & in numbers
    assert (valid_date_format('')) == False
    assert (valid_date_format('March 06,1999')) == False
    assert (valid_date_format('2011.02.02')) == False
    assert (valid_date_format('Mar.16, 2035')) == False
    assert (valid_date_format('11-11-11')) == False
    assert (valid_date_format('2016-January-16')) == False
    assert valid_date_format('9768e-ab1de-8bc14-a3c4e-b12de') == False


def test_passport_format():
    # Valid passport format
    assert valid_passport_format('JMZ0S-89IA9-OTCLY-MQILJ-P7CTY') == True
    assert valid_passport_format("12345-12345-67890-00000-00000") == True

    # Invalid passport format
    assert valid_passport_format("JMZ0S-89IA9-OTCLY-MQILJ-") == False
    assert valid_date_format('') == False


def test_visa_format():
    # Valid visa format
    assert valid_visa_format("CfR6x-XSMVA") == True

    # Invalid visa format
    assert valid_visa_format("xsmvA") == False
    assert valid_visa_format("&*&%f-fid92") == False
    assert valid_visa_format("") == False
    assert valid_visa_format("93624768726") == False
