
def underscore_to_camelcase(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))
