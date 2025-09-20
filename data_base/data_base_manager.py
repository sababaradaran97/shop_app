import sqlite3 
import datetime

def craete_table ():
    try:
        connection = sqlite3.connect( "data_base/data_base.db" )
        connection.cursor().execute(
                            """
                            CREATE TABLE "product" (
                                "id"	        INTEGER,
                                "title"	        TEXT NOT NULL,
                                "price"	        INTEGER NOT NULL,
                                "brand"	        TEXT NOT NULL,
                                "expire_date"	TEXT NOT NULL,
                                PRIMARY KEY("id" AUTOINCREMENT)
                            );
                            """ 
                            )
        connection.commit()
        connection.close()
    
    except:
        pass

def choose_title () :

    connection = sqlite3.connect( "data_base/data_base.db" )
    result = connection.cursor().execute( """ SELECT id, title FROM product """ ).fetchall()
    connection.commit()
    connection.close()

    result_as_list = []

    for row in result:
        result_as_list.append( str( row[ 0 ] ) + "-" + str( row[ 1 ] ) )

    return result_as_list

def count_bottom () :

    connection = sqlite3.connect( "data_base/data_base.db" )
    result = connection.cursor().execute( """ SELECT COUNT(id) AS count FROM product """ ).fetchall()
    connection.commit()
    connection.close()
    total_number = result[ 0 ][ 0 ]
    
    return ( total_number )

def check_date () :
     
    persent_time = str( datetime.datetime.now() )

    connection = sqlite3.connect( "data_base/data_base.db" )
    result = connection.cursor().execute( f""" SELECT title FROM product WHERE expire_date < "{ persent_time }" """ ).fetchall()
    connection.commit()
    connection.close()

    result_as_list = []

    for row in result:
        result_as_list.append( row[ 0 ] )

    return result_as_list
