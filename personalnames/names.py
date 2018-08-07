# noinspection PyTypeChecker
def gen_initials(lastname, firstname, formats):
    """
    Generate the name formats with initials.

    :param lastname: person's lastname
    :param firstname: person's firstname
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
        if "lastnamefirstname" in formats:
            forms.append(", ".join([lastname, " ".join(initials)]))
    for x in range(1, len(parts) + 1):
        initials = [part[0:1] + "." for part in parts[1:x]]
        initials += parts[x:]
        if "firstnamelastname" in formats:
            forms.append(" ".join([parts[0], " ".join(initials), lastname]))
        if "lastnamefirstname" in formats:
            forms.append(lastname + ", " + " ".join([parts[0], " ".join(initials)]))
    return list(set(forms))


def normalise_whitespace(text):
    """
    Normalise the whitespace in the string

    :param text: string
    :return: string with whitespace normalised to single space
    """
    return " ".join(text.split())


def remove_whitespace(text):
    """
    Remove all whitespace from a string

    :param text: string
    :return: string with no whitespace
    """
    return "".join(text.split())





