def int_list_to_str(elements: list, attribute: str=None):
    if attribute:
        return '|'.join([str(element[attribute]) for element in elements])
    return '|'.join([str(element) for element in elements])