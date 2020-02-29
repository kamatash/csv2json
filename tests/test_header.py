import pytest

from csv2json import main

def test_header_success_list():
    header = main.Header(['column1', 'column2', 'column3'])

    assert len(header._header) == 3
    assert header._header[0] == 'column1'
    assert header._header[1] == 'column2'
    assert header._header[2] == 'column3'


def test_header_success_tuple():
    header = main.Header(('column1', 'column2', 'column3'))

    assert len(header._header) == 3
    assert header._header[0] == 'column1'
    assert header._header[1] == 'column2'
    assert header._header[2] == 'column3'


def test_header_success_set():
    header = main.Header({'column1', 'column2', 'column3', 'column1'})

    assert len(header._header) == 3


def test_header_success_dict():
    header = main.Header({'key1': 'value1', 'key2': 'value2'})

    assert len(header._header) == 2
    assert header._header[0] == 'key1'
    assert header._header[1] == 'key2'


def test_header_success_string():
    header = main.Header('string1')

    assert len(header._header) == 7
    assert header._header[0] == 's'
    assert header._header[1] == 't'
    assert header._header[2] == 'r'
    assert header._header[3] == 'i'
    assert header._header[4] == 'n'
    assert header._header[5] == 'g'
    assert header._header[6] == '1'


def test_header_failed_not_iterable():
    header = main.Header(0)
    assert len(header._header) == 0
