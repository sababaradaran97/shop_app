from tkinter import *
from data_base.data_base_manager import *

def button_to_show () :
    resault = count()
    Message( "Number of items :" , resault )