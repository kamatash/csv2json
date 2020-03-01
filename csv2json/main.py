import json

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
        return json.dumps(self._body)


def main():
    with open('header.txt', 'r') as f:
        header = Header(f.readlines())

    with open('input.csv', 'r') as f:
        body = Body(f.readlines(), header._header)

    with open('output.json', 'w') as fw:
        fw.write(body.to_json())

if __name__ == "__main__":
    main()