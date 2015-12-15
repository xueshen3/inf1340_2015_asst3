#!/usr/bin/env python3

""" Assignment 3, Exercise 2, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists. """

__author__ = 'Bertha Chan & Philips Xue'


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

#####################
# HELPER FUNCTIONS ##
#####################


def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class UnknownAttributeException(Exception):
    """
    Raised when attempting set operations on a table
    that does not contain the named attribute
    """
    pass


def selection(t, f):

    # new list created as a result
    result = []
    for t_list in t:
        # if rows are in the t_list after being run through the function, append to result
        if f(t_list):
            result.append(t_list)
    # if the result is none or the header only, return None
    if len(result) == 1 or len(result) == 0:
        return None
    # otherwise, return the result after removing any duplicates
    else:
        return remove_duplicates(result)


def projection(t, r):
    result = []
    matching_attributes_index = []
    # Enter the for loop to test if the attribute is in table 1
    for attribute in r:
        if attribute not in t[0]:
            raise UnknownAttributeException("Not in table1 attribute list")
    # Enter the for loop to append the attribute
    for attribute in t[0]:
        if attribute in r :
            matching_attributes_index.append(t[0].index(attribute))
    # Enter the for loop to append the attribute into the new row
    for row in t:
        filtered_row = []
        for index_to_append in matching_attributes_index:
            filtered_row.append(row[index_to_append])
        result.append(filtered_row)
    return result


def cross_product(t1, t2):
    # Create a empty result to store combined table
    result = []
    t1_counter = 0
    result.append(t1[0]+t2[0])
    # Enter the for loop to combine two table into and store them in result
    for t1_row in t1:
        t2_counter = 0
        for t2_row in t2:
            if t2_counter > 0:
                if t1_counter > 0:
                    result.append(t1_row + t2_row)
            t2_counter += 1
        t1_counter += 1
    return result
