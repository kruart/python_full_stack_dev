﻿import ast
import os
import collections
import sys
from utils import flatten_list, is_verb
from file_utils import get_trees


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]
    function_names = [f for f in flatten_list([get_all_names(t) for t in trees]) if not (f.startswith('__') and f.endswith('__'))]

    def split_snake_case_name_to_words(name):
        return [n for n in name.split('_') if n]
    return flatten_list([split_snake_case_name_to_words(function_name) for function_name in function_names])


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    list_of_nodes = get_nodes(trees)
    fncs = get_function_names(list_of_nodes)
    print('%s functions extracted' % len(fncs))

    verbs = flatten_list([get_verbs_from_function_name(function_name) for function_name in fncs])
    return collections.Counter(verbs).most_common(top_size)


def get_nodes(trees):
    list_of_nodes = []
    for t in trees:
        nodes = [node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)]

        if nodes:
            list_of_nodes.append(nodes)
    return list_of_nodes


def get_function_names(list_of_nodes):
    return [f for f in flatten_list(list_of_nodes) if not (f.startswith('__') and f.endswith('__'))]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def main(dir_path='.'):
    wds = []
    projects = ['django', 'flask', 'pyramid', 'reddit', 'requests', 'sqlalchemy']

    for project in projects:
        path = os.path.join(dir_path, project)
        print('+++scanning in %s+++' % path)
        wds += get_top_verbs_in_path(path)

    top_size = 200
    print('total %s words, %s unique' % (len(wds), len(set(wds))))
    for word, occurence in collections.Counter(wds).most_common(top_size):
        print(word, occurence)


if __name__ == '__main__':
    print('The program is running with arguments: ', str(sys.argv))
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main()
    print('The program is over')
