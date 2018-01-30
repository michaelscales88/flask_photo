import os


def make_dir(directory):
    os.makedirs(directory, exist_ok=True)
