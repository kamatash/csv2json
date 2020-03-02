import json
import sys

class Header:
    def __init__(self, lines):
        if not hasattr(lines, '__iter__'):
            self._header = []
            return
        self._header = [line.strip() for line in lines]


class Body:
    def __init__(self, lines, header):
        self._body = []

        if len(header) == 0:
            return

        for line in lines:
            if len(line.strip().split(',')) != len(header):
                continue
            csv_dict = {}
            for index, row in enumerate(line.strip().split(',')):
                csv_dict[header[index]] = row
            self._body.append(csv_dict)

    def to_json(self):
        if len(self._body) == 0:
            return ''
        return json.dumps(self._body)


def main():
    with open('header.txt', 'r') as f:
        header = Header(f.readlines())

    body = Body(sys.stdin, header._header)

    print(body.to_json())

if __name__ == "__main__":
    main()