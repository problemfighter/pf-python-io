import os.path
import shutil


def join_path(*args):
    return os.path.join(*args)


def is_exist(path):
    return os.path.exists(path)


def create_dir(path):
    if not is_exist(path):
        os.makedirs(path)


def copy(source, destination):
    shutil.copytree(source, destination)


def delete(path):
    if is_exist(path):
        shutil.rmtree(path)


def delete_file(path):
    if is_exist(path):
        os.remove(path)


def rename(source, destination):
    os.rename(source, destination)
