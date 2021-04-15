
def underscore_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def find_replace_into_text(content: str, key_value: dict):
    for key in key_value:
        value = key_value[key]
        if not value:
            value = ""
        content = content.replace(key, value)
    return content
