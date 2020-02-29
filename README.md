# csv2json
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
docker run -v [host directory]:[container directory] python main.py
```

## Development
### Dependencies
* Docker

### Testing
