import pytest

from csv2json import main

def test_body_success():
    lines = ['row1,1', 'row2,2']
    header = ['column1', 'column2']
    body = main.Body(lines, header)

    assert len(body._body) == 2
    assert body._body[0]['column1'] == 'row1'
    assert body._body[0]['column2'] == '1'
    assert body._body[1]['column1'] == 'row2'
    assert body._body[1]['column2'] == '2'


def test_body_success_lines_empty():
    lines = []
    header = ['column1', 'column2']
    body = main.Body(lines, header)

    assert len(body._body) == 0


def test_body_success_header_empty():
    lines = ['row1,1', 'row2,2']
    header = []
    body = main.Body(lines, header)

    assert len(body._body) == 0


def test_body_success_line_header_not_compatible():
    lines = ['row1,1,10', 'row2,2']
    header = ['column1', 'column2']
    body = main.Body(lines, header)

    assert len(body._body) == 1
    assert body._body[0]['column1'] == 'row2'
    assert body._body[0]['column2'] == '2'
