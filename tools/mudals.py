from tkinter import *
from data_base.data_base_manager import *

def button_to_show () :
    total_number = count()
    Message( "Number of items :" , total_number )