"""
Gets ALL of the files inside a directory including full paths
"""
import os

def get_tree(root_dir):
    def add_files(directory, tree):
        for file in os.listdir(directory):
            file = os.path.join(directory, file)
            if os.path.isdir(file):
                add_files(file, tree)
            else:
                tree.append(file)

    tree = []
    add_files(root_dir, tree)

    return tree
