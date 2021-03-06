from pf_file_dir.pf_fd_util import is_exist


def get_file_content(path, encoding=None):
    if not is_exist(path):
        pass
    else:
        with open(path, encoding=encoding) as f:
            contents = f.read()
            f.close()
            return contents


def write_content_to_file(path: str, content: str):
    file = open(path, "w")
    file.write(content)
    file.close()
