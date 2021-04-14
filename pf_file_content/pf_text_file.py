from pf_file_dir.pf_fd_util import is_exist


def get_file_content(path, encoding=None):
    if not is_exist(path):
        pass
    else:
        with open(path, encoding=encoding) as f:
            contents = f.readlines()
            f.close()
            return contents
