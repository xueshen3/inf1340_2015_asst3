#!/usr/bin/env python

""" Assignment 3, Exercise 1, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Bertha Chan & Philips Xue'


from exercise1 import selection, projection, cross_product, UnknownAttributeException

###########
# TABLES ##
###########

EMPLOYEES = [["Surname", "FirstName", "Age", "Salary"],
             ["Smith", "Mary", 25, 2000],
             ["Black", "Lucy", 40, 3000],
             ["Verdi", "Nico", 36, 4500],
             ["Smith", "Mark", 40, 3900]]

EMPLOYEES_EMPTY = [["Surname", "FirstName," "Age", "Salary"]]

MANAGERS = [["Number", "Surname", "Age"],
        [2200, "Rob",35],
        ["Surname", "Katherine", 44],
        [3984, "Sara", 22]]

R1 = [["Employee", "Department"],
      ["Smith", "sales"],
      ["Black", "production"],
      ["White", "production"]]

R2 = [["Department", "Head"],
      ["production", "Mori"],
      ["sales", "Brown"]]

R3 = [["A", "B"]]

R4 = [["G", "H"]]

EMPTY = []


#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):

    t1.sort()
    t2.sort()

    return t1 == t2


#####################
# FILTER FUNCTIONS ##
#####################
def filter_employees(row):
    """
    Check if employee represented by row
    is AT LEAST 30 years old and makes
    MORE THAN 3500.
    :param row: A List in the format:
        [{Surname}, {FirstName}, {Age}, {Salary}]
    :return: True if the row satisfies the condition.
    """
    return row[-2] >= 30 and row[-1] > 3500


###################
# TEST FUNCTIONS ##
###################
def test_selection():
    """
    Test select operation.
    """

    result = [["Surname", "FirstName", "Age", "Salary"],
              ["Verdi", "Nico", 36, 4500],
              ["Smith", "Mark", 40, 3900]]

    assert is_equal(result, selection(EMPLOYEES, filter_employees))
    assert selection(MANAGERS, filter_employees) is None


def test_selection_empty_list():
    """
    Return None for an empty table
    """
    assert selection(EMPLOYEES_EMPTY, filter_employees) is None


def test_projection():
    """
    Test projection operation.
    """

    result = [["Surname", "FirstName"],
              ["Smith", "Mary"],
              ["Black", "Lucy"],
              ["Verdi", "Nico"],
              ["Smith", "Mark"]]
    result_2 = [["Surname"],
                ["Smith"],
                ["Black"],
                ["Verdi"],
                ["Smith"]]

    assert is_equal(result, projection(EMPLOYEES, ["Surname", "FirstName"]))
    assert is_equal(result_2, projection(EMPLOYEES, ["Surname"]))
    assert projection(R3, []) is None


def test_projection_error():
    try:
        projection(EMPLOYEES, ["No_Name"])
    except UnknownAttributeException:
        assert True


def test_cross_product():
    """
    Test cross product operation.
    """

    result = [["Employee", "Department", "Department", "Head"],
              ["Smith", "sales", "production", "Mori"],
              ["Smith", "sales", "sales", "Brown"],
              ["Black", "production", "production", "Mori"],
              ["Black", "production", "sales", "Brown"],
              ["White", "production", "production", "Mori"],
              ["White", "production", "sales", "Brown"]]

    assert is_equal(result, cross_product(R1, R2))
    assert cross_product(R3, R4) is None


def test_cross_product_error():
    try:
        projection(R1, EMPTY)
    except UnknownAttributeException:
        assert True

