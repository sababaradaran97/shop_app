from tkinter.ttk import Combobox
import datetime
from tkinter import *
from tkinter import messagebox
import sqlite3 


def main_view( list_of_expired_products , total_number , list_of_names ) :

    window = Tk()
    window.title( "shop" )
    window.geometry ( "600x500" )

    def button_action():
        messagebox.showinfo( "", "Total Number of Products: " + str( total_number ) )
        # Message ( text = "Total : " + str( total_number ) )

    title = StringVar()
    Label( window , text = "product name" ).place( x = 25 , y = 30 )
    combobox = Combobox( window , textvariable = title, values = list_of_names , width = 17 , state = "readonly" ).place( x = 120 , y = 30 )
    title = title.get()

    def information( title ) :

        id , name = title.split( "-" )

        connection = sqlite3.connect( "data_base/data_base.db" )
        brand = connection.cursor().execute( f""" SELECT brand FROM product WHERE id = {id} """ ).fetchall()
        price = connection.cursor().execute( f""" SELECT price FROM product WHERE id = {id} """ ).fetchall()
        connection.close()

        brand = brand[ 0 ][ 0 ]
        price = price[ 0 ][ 0 ]

        return brand , price
    
    result = information( title )

    price = StringVar()
    brand = StringVar()
    
    brand = result[ 0 ]
    price = result[ 1 ]

    
    Label( window , text = "product brand" ).place( x = 25 , y = 70 )
    Entry( window , textvariable = brand , state = "readonly" ).place( x = 120 , y = 70 )


    Label( window , text = "product price" ).place( x = 25 , y = 110 )
    Entry( window , textvariable = price , width = 20 , state = "readonly" ).place( x = 120 , y = 110 )


    Label( window , text = "Expired date products" ).place( x = 360 , y = 30 )
    Combobox( window , values = list_of_expired_products , width = 23 , state = "readonly" ).place( x = 360 , y = 70 )


    Button( 
        window , 
        text = "show total number" , 
        width = 20 , 
        command = button_action 
    ).place( x = 25 , y = 200 ) 


    window.mainloop()
