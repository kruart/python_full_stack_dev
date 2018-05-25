import os
from config import TEMPLATES_DIR


def get_content(file_name):
    file_path = construct_html_path(file_name)
    print(file_path)
    with open(file_path, 'rb') as f:
        return f.read()


def construct_html_path(file_name, templates_dir=TEMPLATES_DIR, extension='.html'):
    return os.path.join(templates_dir, file_name) + extension
