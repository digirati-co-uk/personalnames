import personalnames.titles as titles
import bisect


# noinspection PyTypeChecker
def gen_initials(lastname, firstname, title, formats):
    """
    Generate the name formats with initials.

    :param lastname: person's lastname
    :param firstname: person's firstname
    :param title: person's title
    :param formats: list of formats ['firstnamelastname', 'lastnamefirstname']
    :return: de-duplicated list of names with initials.
    """
    # Normalise whitespace to single space
    lastname = normalise_whitespace(lastname)
    parts = normalise_whitespace(firstname).split()
    forms = []
    for x in range(1, len(parts) + 1):
        initials = [part[0:1] + "." for part in parts[0:x]]
        initials += parts[x:]
        if "firstnamelastname" in formats:
            forms.append(" ".join([" ".join(initials), lastname]))
            if title:
                forms.append(" ".join([title, " ".join(initials), lastname]))
        if "lastnamefirstname" in formats:
            forms.append(", ".join([lastname, " ".join(initials)]))
            if title:
                forms.append(", ".join([lastname, title + " " + " ".join(initials)]))
    for x in range(1, len(parts) + 1):
        initials = [part[0:1] + "." for part in parts[1:x]]
        initials += parts[x:]
        if "firstnamelastname" in formats:
            forms.append(" ".join([parts[0], " ".join(initials), lastname]))
            if title:
                forms.append(" ".join([title, parts[0], " ".join(initials), lastname]))
        if "lastnamefirstname" in formats:
            forms.append(lastname + ", " + " ".join([parts[0], " ".join(initials)]))
            if title:
                forms.append(lastname + ", " + " ".join([title, parts[0], " ".join(initials)]))
    return list(set(forms))


def parse_titles(parts):
    title_parts = []
    suffix_parts = []
    nominal_parts = []
    for part in parts:
        if part.lower() in titles.prefixes:
            title_parts.append(part)
        elif part.lower() in titles.suffixes:
            suffix_parts.append(part)
        else:
            nominal_parts.append(part)
    return title_parts, nominal_parts, suffix_parts


def name_split(name, split_char=","):
    """
    Split a name into a list of name parts (not categorised, just an ordered list).

    Retain commas for later use in splitting the list into surname and forename parts.

    :param name: string for personal name
    :param split_char: character to split on (default to comma)
    :return: list of strings, including commas.
    """
    name_list = []
    split_split = name.split(split_char)
    for split_item in split_split[:-1]:
        [name_list.append(normalise_whitespace(x)) for x in split_item.split()]
        name_list.append(split_char)
    [name_list.append(normalise_whitespace(x)) for x in split_split[-1].split()]
    return name_list


def name_parts(name, split_c=","):
    """
    TO DO: handle case with multiple commas (if this is a genuine case)

    :param name:
    :param split_c:
    :return:
    """

    n_parts = name_split(name, split_char=split_c)
    title, personal_name, suffix = parse_titles(n_parts)
    if split_c in personal_name:
        lastname = whitespace_list(personal_name[: bisect.bisect(personal_name, split_c) - 1])
        firstname = whitespace_list(personal_name[bisect.bisect(personal_name, split_c):])
    else:
        firstname = whitespace_list(personal_name[:-1])
        lastname = whitespace_list([personal_name[-1]])
    title = whitespace_list(title)
    suffix = whitespace_list(suffix)
    return (
        title,
        firstname,
        lastname,
        suffix
    )


def name_initials(name, name_formats=None):
    """
    Generate a set of initials from a name provided as a string.

    :param name: string, e.g. Dr. Martin Luther King
    :param name_formats: list of formats for the name.
    :return: list of formats including initials
    """
    if name_formats is None:
        name_formats = ['firstnamelastname', 'lastnamefirstname']
    honorific, forename, surname, suffix = name_parts(name)
    initials = gen_initials(lastname=surname, firstname=forename, title=honorific,formats=name_formats)
    return initials


def whitespace_list(text_list):
    return normalise_whitespace(' '.join(text_list))


def normalise_whitespace(text):
    """
    Normalise the whitespace in the string

    :param text: string
    :return: string with whitespace normalised to single space
    """
    return " ".join(text.strip().split())


def removewhitespace(text):
    """
    Remove the whitespace in the string

    :param text: string
    :return: string with no whitespace
    """
    return "".join(text.strip().split())

