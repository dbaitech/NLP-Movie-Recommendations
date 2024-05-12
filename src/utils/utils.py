def int_list_to_str(elements: list, attribute: str=None):
    if attribute:
        return '|'.join([str(element[attribute]) for element in elements])
    return '|'.join([str(element) for element in elements])


def flatten_dict(dictionary, parent_key=''):
    items = []
    for key, value in dictionary.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key).items())
        else:
            items.append((new_key, value))
    return dict(items)