# personalnames
Lightweight Python functions for generating different formats for personal names

## Usage

```python
from personalnames import names

name = "Dr. Martin Luther King, Jr."

formats = names.name_initials(
    name=name, name_formats=["firstnamelastname", "lastnamefirstname"]
)

assert sorted(formats) == sorted(
    [
        "King, Dr. M. L., Jr.",
        "Dr. Martin Luther King",
        "Dr. M. Luther King, Jr.",
        "King, M. L.",
        "King, M. L., Jr.",
        "Dr. Martin L. King",
        "Martin Luther King",
        "King, Dr. Martin L.",
        "M. Luther King, Jr.",
        "Dr. Martin Luther King, Jr.",
        "King, Dr. Martin L., Jr.",
        "Dr. M. L. King, Jr.",
        "King, Martin Luther",
        "King, Dr. M. L.",
        "King, M. Luther, Jr.",
        "King, Martin Luther, Jr.",
        "Dr. M. Luther King",
        "Dr. M. L. King",
        "Martin Luther King, Jr.",
        "King, Dr. M. Luther",
        "Martin L. King, Jr.",
        "M. Luther King",
        "King, Dr. Martin Luther",
        "M. L. King, Jr.",
        "Dr. Martin L. King, Jr.",
        "Martin L. King",
        "King, Martin L., Jr.",
        "King, Dr. Martin Luther, Jr.",
        "M. L. King",
        "King, M. Luther",
        "King, Dr. M. Luther, Jr.",
        "King, Martin L.",
    ]
)
```

There are two possible formats for name order: `firstnamelastname` and `lastnamefirstname`.

Additional Options:

`non_ws=True`

will return the same list but with additional versions that have no whitespace.

```python
from personalnames import names

name = "Dr. Martin Luther King, Jr."

formats = names.name_initials(
    name=name, name_formats=["firstnamelastname"], non_ws=True
)


assert sorted(formats) == sorted(
    [
        "Dr. M. L. King, Jr.",
        "Martin L. King",
        "M.LutherKing,Jr.",
        "Dr.MartinL.King",
        "M. Luther King",
        "Dr.MartinL.King,Jr.",
        "Dr. Martin Luther King, Jr.",
        "Dr.M.L.King,Jr.",
        "Martin Luther King, Jr.",
        "Dr.M.LutherKing",
        "Dr. Martin Luther King",
        "MartinL.King",
        "Dr. M. Luther King, Jr.",
        "Dr. M. L. King",
        "MartinLutherKing,Jr.",
        "M. L. King, Jr.",
        "M. Luther King, Jr.",
        "M.L.King",
        "Dr.M.LutherKing,Jr.",
        "Martin Luther King",
        "MartinLutherKing",
        "Dr.M.L.King",
        "MartinL.King,Jr.",
        "M. L. King",
        "Dr. Martin L. King, Jr.",
        "Martin L. King, Jr.",
        "Dr.MartinLutherKing,Jr.",
        "Dr. M. Luther King",
        "Dr.MartinLutherKing",
        "Dr. Martin L. King",
        "M.L.King,Jr.",
        "M.LutherKing",
    ]
)
```
