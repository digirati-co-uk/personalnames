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


