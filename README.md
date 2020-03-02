# csv2json [![codecov](https://codecov.io/gh/kamatash/csv2json/branch/master/graph/badge.svg)](https://codecov.io/gh/kamatash/csv2json)
## Overview
* CSV file convert to JSON file.
* Convert one line of CSV to one object of JSON.
* JSON key name is column name written in txt.
### Example
header.txt
```
column1
column2
```

input.csv
```
row1,1
row2,2
```

output.json
```
[
    {
        "column1": "row1",
        "column2": "1"
    },
    {
        "column1": "row2",
        "column2": "2"
    }
]
```


## Usage
```
docker build -t kamatash/csv2json .
docker run -v $PWD:/usr/src/app -w /usr/src/app kamatash/csv2json python csv2json/main.py
```

## Development
### Dependencies
* Docker

### Testing
