import personalnames.names as names


def test_name_split():
    name = "John Smith"
    assert names.name_split(name) == ["John", "Smith"]


def test_name_split_comma():
    name = "Smith, John"
    assert names.name_split(name) == ["Smith", ",", "John"]


def test_name_split_multiple():
    name = "Chimamanda Ngozi Adichie"
    assert names.name_split(name) == ["Chimamanda", "Ngozi", "Adichie"]


def test_name_split_multiple_comma():
    name = "Rodríguez Zapatero, José Luis"
    assert names.name_split(name) == ["Rodríguez", "Zapatero", ",", "José", "Luis"]


def test_remove_whitespace():
    name = "John  Smi t h"
    assert names.removewhitespace(name) == "JohnSmith"


def test_normalise_whitespace():
    name = " John    Smith "
    assert names.normalise_whitespace(name) == "John Smith"


def test_whitespace_list():
    name_list = ["John ", "  Smith"]
    assert names.whitespace_list(name_list) == "John Smith"


def test_parse_titles():
    name_list = ["Dame", "Mary", "Ramirez"]
    assert names.parse_titles(name_list) == (["Dame"], ["Mary", "Ramirez"], [])


def test_parse_suffix():
    name_list = ["Martin", "Luther", "King", "Jr"]
    assert names.parse_titles(name_list) == ([], ["Martin", "Luther", "King"], ["Jr"])


def test_affixes():
    name_list = ["Dr", "Martin", "Luther", "King", "Jr."]
    assert names.parse_titles(name_list) == (
        ["Dr"],
        ["Martin", "Luther", "King"],
        ["Jr."],
    )


def test_split_parse():
    assert names.parse_titles(names.name_split("Dr Martin Luther  King")) == (
        ["Dr"],
        ["Martin", "Luther", "King"],
        [],
    )


def test_name_parts():
    name = "Dr Martin Luther King"
    assert names.name_parts(name) == ("Dr", "Martin Luther", "King", "")


def test_name_parts_comma():
    name = "King, Dr Martin Luther"
    assert names.name_parts(name) == ("Dr", "Martin Luther", "King", "")


def test_name_parts_separator():
    name = "King; Dr Martin Luther"
    assert names.name_parts(name, split_c=";") == ("Dr", "Martin Luther", "King", "")


def test_gen_initials_basic():
    assert sorted(
        names.gen_initials(
            lastname="King",
            firstname="Martin Luther",
            title="Dr",
            formats=["firstnamelastname"],
        )
    ) == sorted(
        [
            "Martin L. King",
            "Dr M. Luther King",
            "Dr Martin Luther King",
            "M. Luther King",
            "Dr M. L. King",
            "Martin Luther King",
            "Dr Martin L. King",
            "M. L. King",
        ]
    )


def test_gen_initials_lastname():
    assert sorted(
        names.gen_initials(
            lastname="King",
            firstname="Martin Luther",
            title="Dr",
            formats=["lastnamefirstname"],
        )
    ) == sorted(
        [
            "King, Martin L.",
            "King, Dr M. Luther",
            "King, Dr Martin Luther",
            "King, M. Luther",
            "King, Dr M. L.",
            "King, Martin Luther",
            "King, Dr Martin L.",
            "King, M. L.",
        ]
    )


def test_gen_initials_lastname_suffix():
    assert sorted(
        names.gen_initials(
            lastname="King",
            firstname="Martin Luther",
            title="Dr",
            post_nominal="Jr.",
            formats=["lastnamefirstname"],
        )
    ) == sorted(
        [
            "King, Dr M. L.",
            "King, Dr M. L., Jr.",
            "King, Dr M. Luther",
            "King, Dr M. Luther, Jr.",
            "King, Dr Martin L.",
            "King, Dr Martin L., Jr.",
            "King, Dr Martin Luther",
            "King, Dr Martin Luther, Jr.",
            "King, M. L.",
            "King, M. L., Jr.",
            "King, M. Luther",
            "King, M. Luther, Jr.",
            "King, Martin L.",
            "King, Martin L., Jr.",
            "King, Martin Luther",
            "King, Martin Luther, Jr.",
        ]
    )


def test_gen_initials_firstname_suffix():
    assert sorted(
        names.gen_initials(
            lastname="King",
            firstname="Martin Luther",
            title="Dr",
            post_nominal="Jr.",
            formats=["firstnamelastname"],
        )
    ) == sorted(
        [
            "Martin L. King",
            "Dr M. Luther King",
            "Dr Martin Luther King",
            "M. Luther King",
            "Dr M. L. King",
            "Martin Luther King",
            "Dr Martin L. King",
            "M. L. King",
            "Martin L. King, Jr.",
            "Dr M. Luther King, Jr.",
            "Dr Martin Luther King, Jr.",
            "M. Luther King, Jr.",
            "Dr M. L. King, Jr.",
            "Martin Luther King, Jr.",
            "Dr Martin L. King, Jr.",
            "M. L. King, Jr.",
        ]
    )


def test_name_initials():
    assert sorted(
        names.name_initials(
            name="Dr Martin Luther King", name_formats=["lastnamefirstname"]
        )
    ) == sorted(
        [
            "King, Martin L.",
            "King, Dr M. Luther",
            "King, Dr Martin Luther",
            "King, M. Luther",
            "King, Dr M. L.",
            "King, Martin Luther",
            "King, Dr Martin L.",
            "King, M. L.",
        ]
    )


def test_name_initials_defaults():
    assert sorted(names.name_initials(name="Dr Martin Luther King")) == sorted(
        [
            "Martin L. King",
            "Dr M. Luther King",
            "Dr Martin Luther King",
            "M. Luther King",
            "Dr M. L. King",
            "Martin Luther King",
            "Dr Martin L. King",
            "M. L. King",
            "King, Martin L.",
            "King, Dr M. Luther",
            "King, Dr Martin Luther",
            "King, M. Luther",
            "King, Dr M. L.",
            "King, Martin Luther",
            "King, Dr Martin L.",
            "King, M. L.",
        ]
    )


def test_pmc_example_parts():
    assert names.name_parts(name='Walter Thomas Monnington, R.A.') == ('', 'Walter Thomas', 'Monnington', 'R.A.')


def test_pmc_example_parts_commas():
    assert names.name_parts(name='Monnington, Walter T., R.A.') == ('', 'Walter T.', 'Monnington', 'R.A.')