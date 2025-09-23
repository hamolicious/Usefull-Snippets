"""
Gets ALL of the files inside a directory including full paths
"""
import os
from pathlib import Path


def get_tree(root_dir: Path):
    def add_files(directory: Path, tree: list[Path]):
        for file in os.listdir(directory):
            file = os.path.join(directory, file)
            if os.path.isdir(file):
                add_files(Path(file), tree)
            else:
                tree.append(Path(file))

    tree: list[Path] = []
    add_files(root_dir, tree)

    return tree
