import re


def underscore_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


def find_replace_into_text(content: str, key_value: dict):
    for key in key_value:
        value = key_value[key]
        if not value:
            value = ""
        content = content.replace(key, value)
    return content


def camelcase_to_lower(text: str, to: str = "_"):
    return camelcase_to(text, to).lower()


def camelcase_to(text: str, to: str = "_"):
    return re.sub(r'(?<!^)(?=[A-Z])', to, text)


def replace_space_with(text: str, to: str = "_"):
    return text.replace(" ", to)


def find_and_replace_with(text: str, find: any, replace: any):
    return text.replace(find, replace)
