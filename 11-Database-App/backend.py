import sqlite3

def connect():
    conn=sqlite2.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER) ")
    conn.commit()
    conn.close()

    connect()

def insert():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("")
    conn.commit()
    conn.close()
