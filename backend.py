import sqlite3, csv
#from IPython.display import display

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer, qtd text,path text)")   
    #("SELECT COUNT (*) FROM book")
    #with open (r"C:\Users\josepw\OneDrive\Python\The Python Mega Course - lessons\17 Object Oriented Programming\16 Application 5 Building a Desktop Database Application\csv.csv",'r') as fin:
        #dr=csv.DictReader(fin)
        #to_db=[(i['title'],i['author'],i['year'],i['ISBN'],i['qtd'])for i in dr]
    #cur.executemany ("INSERT INTO book VALUES (NULL,?,?,?,?,?)",to_db)
    conn.commit()
    conn.close()

def insert(title, author, year, isbn, qtd,path):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?,?)",(title,author,year,isbn,qtd,path))
    conn.commit()
    conn.close()

#def insert(title, author, year, isbn, qtd):
    #conn=sqlite3.connect("books.db")
    #cur=conn.cursor()
    #cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(title,author,year,isbn,qtd))
    #conn.commit()
    #conn.close()


def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()    
    return rows

def search(title="", author="", year="", isbn="", qtd="",path=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? OR qtd=? OR path=?",(title,author,year,isbn,qtd,path))
    rows=cur.fetchall()
    conn.close()    
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn,qtd,path):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, qtd=?, path=? WHERE id=?",(title,author,year,isbn,qtd,path,id))
    conn.commit()   
    conn.close()



connect()
#insert("O carro vermelho", "Afonso", 1910,981215)
#delete (4)
#update(3,"title","Song son",2021,123456)

#print (view())

#print(search(year=1920))#