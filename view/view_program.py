from tkinter.ttk import Combobox
import datetime
from tkinter import *

product_list = []

window = Tk()
window.title( "shop" )
window.geometry ( "600x500" )

id = StringVar()
Label( window , text = "product id" ).place( x = 25 , y = 30 )
Combobox( window , values = [ "White" , "Black" , "Red" ] , width = 17 , state = "readonly" ).place( x = 120 , y = 30 )

title = StringVar()
Label( window , text = "product name" ).place( x = 25 , y = 70 )
Combobox( window , values = product_list ).place( x = 120 , y = 70 )


brand = StringVar()
Label( window , text = "Car color" ).place( x = 25 , y = 110 )
Combobox( window , values = [ "White" , "Black" , "Red" ] , width = 17 , state = "readonly" ).place( x = 100 , y = 110 )


price = StringVar()
Label( window , text = "Car plate" ).place( x = 25 , y = 150 )
Entry( window , textvariable = price ).place( x = 100 , y = 150 )


Button( window , text = "show total number" , width = 15 , command = "" ).place( x = 25 , y = 200 )


window.mainloop()