import os

initdir = os.path.dirname(os.path.realpath(__file__))
curdir = os.getcwd()

os.chdir(initdir)

from elipsoid import *

os.chdir(curdir)
