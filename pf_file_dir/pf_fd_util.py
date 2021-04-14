import os.path


def join_path(*args):
    return os.path.join(*args)


def is_exist(path):
    return os.path.exists(path)


def create_dir(path):
    if not is_exist(path):
        os.makedirs(path)
