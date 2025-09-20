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

    def title_combo_eventhandler( event ) :

        title_str = title.get()
        title_str = str( title_str )
        title_str = title_str.split( "-" )
        id = title_str[ 0 ]

        connection = sqlite3.connect( "data_base/data_base.db" )
        result = connection.cursor().execute( f""" SELECT brand , price FROM product WHERE id = "{id}" """ ).fetchall()
        connection.commit()
        connection.close()

        brand.set( result[ 0 ][ 0 ] )
        price.set( result[ 0 ][ 1 ] )
        
        

    title = StringVar()
    Label( window , text = "product name" ).place( x = 25 , y = 30 )
    combobox = Combobox( window , textvariable = title, values = list_of_names , width = 17 , state = "readonly" )
    combobox.bind('<<ComboboxSelected>>', title_combo_eventhandler)
    combobox.place( x = 120 , y = 30 )    
    

   
    brand = StringVar()    
    Label( window , text = "product brand" ).place( x = 25 , y = 70 )
    Entry( window , textvariable = brand , state = "readonly" ).place( x = 120 , y = 70 )

    price = StringVar()
    Label( window , text = "product price" ).place( x = 25 , y = 110 )
    Entry( window , textvariable = price , width = 20 , state = "readonly" ).place( x = 120 , y = 110 )


    Label( window , text = "Expired date products" ).place( x = 360 , y = 30 )
    Combobox( window , values = list_of_expired_products , width = 17 , state = "readonly" ).place( x = 360 , y = 70 )


    Button( 
        window , 
        text = "show total number" , 
        width = 20 , 
        command = button_action 
    ).place( x = 25 , y = 200 ) 

    '''
    result_as_list = information( title )
    brand = result_as_list[ 0 ]
    price = result_as_list[ 1 ]

    print ( brand , price , result_as_list )
    '''

    window.mainloop()

