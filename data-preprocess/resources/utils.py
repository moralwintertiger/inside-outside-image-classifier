import os
import shutil
import random
from .constants import DATA_DIRECTORY, FRAME_LIMIT

def update_file_location(dir_path: str, name: str, root: str,
                         item: str) -> None:
    """Copies file from first location to second"""
    original_loc = str(os.path.join(root, item))
    target_loc = str(os.path.join(DATA_DIRECTORY, dir_path, name))
    shutil.copy(original_loc, target_loc)


def train_test_split(directory: str, feature_class: str,
                     frame_limit: int = FRAME_LIMIT) -> None:
    """
    Parameters
    ----------
    directory: str, path to original file location
    feature_class: str, IN ['inside', 'outside']
    frame_limit: int, max number of frames to process
    """

    frame_cnt = 1
    for root, _, files in os.walk(directory, topdown=False):
        for item in files:
            _, ext = os.path.splitext(item)
            if ext == '.png':
                name = f"{frame_cnt}_{item}"
                t = random.random()
                if t <= .8:
                    update_file_location(f"train/{feature_class}", name, root,
                                         item)
                elif t >= .8 and t <= .9:
                    update_file_location(f"test/{feature_class}", name, root,
                                         item)
                elif t >= .9:
                    update_file_location(f"valid/{feature_class}", name, root,
                                         item)
                frame_cnt += 1
            if frame_cnt >= frame_limit:
                break