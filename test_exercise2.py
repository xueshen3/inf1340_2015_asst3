#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = "Bertha Chan & Philips Xue"
__copyright__ = "2015 INF 1340 Assignment 3"


# imports one per line
import pytest
import os
from exercise2 import decide

DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]


# def test_valid_visa():
#     assert decide("test_valid_visa.json", "countries.json") ==\
#         ["Accept"]