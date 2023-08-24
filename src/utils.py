import os
from pathlib import Path


def create_dir(path: Path):
    if not os.path.exists(path):
        os.makedirs(path)
