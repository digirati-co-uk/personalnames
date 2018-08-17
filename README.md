# personalnames

[https://github.com/digirati-co-uk/personalnames](https://github.com/digirati-co-uk/personalnames)

Lightweight Python functions for generating different formats for personal names

For example, when parsing text (from OCR or manual transcription) for named individuals, it can be useful to know all of the forms in which a name might appear.

"Dr Martin Luther King, Jr."

for example, might appear as "Dr. M. L. King, Jr." or as "King, Dr. Martin L., Jr.".

This code will generate name variants by parsing a name (as a string), identifying prexifes and suffixes, and returning possible variants.

## Requirements

Python 3.x

Required python packages are listed in `requirements.txt`.

## Installation

`pip install personalnames`

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

# License

MIT License

Copyright Digirati Ltd. (c) 2018 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Contribution Guidelines

Personalnames uses Python 3.x. 

Feel free to raise Github issues. 

If you find an issue you are interested in fixing you can:


* Fork the repository
* Clone the repository to your local machine
* Create a new branch for your fix using `git checkout -b branch-name-here`.
* Fix the issue.
* Commit and push the code to your remote repository.
* Submit a pull request to the `personalnames` repository, with a description of your fix and the issue number.
* The PR will be reviewed by the maintainer [https://github.com/mattmcgrattan](https://github.com/mattmcgrattan) and either merge the PR or response with comments.

Thanks!
