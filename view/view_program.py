from tkinter.ttk import Combobox
import datetime
from tkinter import *
from tools.mudals import button_to_show

product_list = []

window = Tk()
window.title( "shop" )
window.geometry ( "600x500" )

id = StringVar()
Label( window , text = "product id" ).place( x = 25 , y = 30 )
Combobox( window , values = [] , width = 17 , state = "readonly" ).place( x = 120 , y = 30 )

title = StringVar()
Label( window , text = "product name" ).place( x = 25 , y = 70 )
Entry( window , textvariable = title , state = "readonly" ).place( x = 120 , y = 70 )


brand = StringVar()
Label( window , text = "product brand" ).place( x = 25 , y = 110 )
Entry( window , textvariable = brand , width = 20 , state = "readonly" ).place( x = 120 , y = 110 )


price = StringVar()
Label( window , text = "product price" ).place( x = 25 , y = 150 )
Entry( window , textvariable = price , state = "readonly" ).place( x = 120 , y = 150 )

Label( window , text = "Expired date products" ).place( x = 400 , y = 30 )
Combobox( window , values = [] , width = 15 , state = "readonly" ).place( x = 400 , y = 70 )


Button( window , text = "show total number" , width = 20 , command = button_to_show() ).place( x = 25 , y = 200 )


window.mainloop()