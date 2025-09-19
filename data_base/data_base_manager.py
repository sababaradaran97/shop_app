import sqlite3 

def craete_table ():
    try:
        connection = sqlite3.connect( "data_base.db" )
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

# def choose_id () :
    # connection = sqlite3.connect( "data_base.db" )
    # connection.cursor().execute( """ SELECT id FROM products """ )
    # connection.commit()
    # connection.close()

def count () :
        resualt = 0
        connection = sqlite3.connect( "data_base.db" )
        connection.cursor().execute ( f""" SELECT MAX(id) FROM product AND {resualt} = MAX(id) """ ) 
        connection.commit()
        connection.close()
        return resualt

