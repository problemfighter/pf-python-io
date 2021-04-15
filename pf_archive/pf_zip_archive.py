import os
import zipfile


def create_zip_archive(source, destination_with_zip):
    zip_file = zipfile.ZipFile(destination_with_zip, "w")
    source_abspath = os.path.abspath(source)
    for dirname, sub_dirs, files in os.walk(source):
        for filename in files:
            abs_name = os.path.abspath(os.path.join(dirname, filename))
            arcname = abs_name[len(source_abspath) + 1:]
            zip_file.write(abs_name, arcname)
    zip_file.close()
