from tkinter.ttk import Combobox
import datetime
from tkinter import *

def main_view( list_of_expired_products , total_number , list_of_names ) :

    window = Tk()
    window.title( "shop" )
    window.geometry ( "600x500" )

    title = StringVar()
    Label( window , text = "product name" ).place( x = 25 , y = 30 )
    Combobox( window , values = list_of_names , width = 17 , state = "readonly" ).place( x = 120 , y = 30 )
    

    brand = StringVar()
    Label( window , text = "product brand" ).place( x = 25 , y = 70 )
    Entry( window , textvariable = brand , state = "readonly" ).place( x = 120 , y = 70 )


    price = StringVar()
    Label( window , text = "product price" ).place( x = 25 , y = 110 )
    Entry( window , textvariable = price , width = 20 , state = "readonly" ).place( x = 120 , y = 110 )


    Label( window , text = "Expired date products" ).place( x = 400 , y = 30 )
    Combobox( window , values = list_of_expired_products , width = 15 , state = "readonly" ).place( x = 400 , y = 70 )


    Button( window , text = "show total number" , width = 20 , command = Message( "Total :" , total_number ) ).place( x = 25 , y = 200 )


    window.mainloop()