import os
from typing import List
from resources.constants import (INSIDE_DIRECTORY, OUTSIDE_DIRECTORY,
                                 DATA_DIRECTORY)
from resources.utils import train_test_split


class Bunchify(object):
    def __init__(self, inside_path: str, outside_path: str):
        self.inside_path = inside_path
        self.outside_path = outside_path

    def create_train_test_directories(self):
        category_folders: List[str] = ['inside', 'outside']
        split_folders: List[str] = ['train', 'test', 'valid']
        for split in split_folders:
            for category in category_folders:
                new_path = os.path.join(DATA_DIRECTORY, split, category)
                try:
                    os.makedirs(new_path)
                except FileExistsError:
                    pass

    def run_split(self) -> None:
        path_dict = {'inside': self.inside_path, 'outside': self.outside_path}
        for cat_type, cat_path in path_dict.items():
            train_test_split(directory=cat_path, feature_class=cat_type)


if __name__ == '__main__':
    bunch = Bunchify(inside_path=INSIDE_DIRECTORY,
                     outside_path=OUTSIDE_DIRECTORY)
    bunch.create_train_test_directories()
    bunch.run_split()
