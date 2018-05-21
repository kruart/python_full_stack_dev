import ast
import os


def get_trees(_path):
    """Returns list of AST trees"""
    trees = []

    filenames = get_files(_path)

    print('total %s files' % len(filenames))

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()

        tree = parse_file(main_file_content)
        trees.append(tree)

    print('%s trees generated' % len(trees))
    return trees


def get_files(_path):
    """Returns list of python files"""
    filenames = []

    for dirname, dirs, files in os.walk(_path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
                if len(filenames) == 100:
                    break

    return filenames


def parse_file(file_content):
    """Parse the source into AST tree"""
    try:
        tree = ast.parse(file_content)
    except SyntaxError as e:
        print(e)
        tree = None
    return tree
