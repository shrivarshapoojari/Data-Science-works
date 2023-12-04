import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0,abspath(join(dirname(__file__),'..')))
#from payments import paydetails

def course():
    print("My course")

#paydetails.payment()