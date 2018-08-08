import personalnames.names as names


def test_name_split():
    name = 'John Smith'
    assert names.name_split(name) == ['John', 'Smith']


def test_name_split_comma():
    name = 'Smith, John'
    assert names.name_split(name) == ['Smith', ',', 'John']


def test_name_split_multiple():
    name = 'Chimamanda Ngozi Adichie'
    assert names.name_split(name) == ['Chimamanda', 'Ngozi', 'Adichie']


def test_name_split_multiple_comma():
    name = 'Rodríguez Zapatero, José Luis'
    assert names.name_split(name) == ['Rodríguez', 'Zapatero', ',', 'José', 'Luis']


def test_remove_whitespace():
    name = 'John  Smi t h'
    assert names.removewhitespace(name) == 'JohnSmith'


def test_normalise_whitespace():
    name = ' John    Smith '
    assert names.normalise_whitespace(name) == 'John Smith'
