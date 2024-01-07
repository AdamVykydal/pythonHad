from os import path, getcwd, pardir

ROOT_DIR = path.abspath(path.join(getcwd(), pardir))
RESOURCES_DIR = path.join(ROOT_DIR, 'resources')
IMG_DIR = path.join(RESOURCES_DIR, 'img')
