import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from courses import coursedet

def payment():
    print("This is payment file")
coursedet.course()