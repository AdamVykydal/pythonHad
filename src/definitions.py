# pylint: disable=invalid-name
from os import path, pardir

ROOT_DIR = path.abspath(
    path.join(path.dirname(path.abspath(__file__)), pardir))
RESOURCES_DIR = path.join(ROOT_DIR, 'resources')
IMG_DIR = path.join(RESOURCES_DIR, 'img')
SOUNDS_DIR = path.join(RESOURCES_DIR, 'sounds')
